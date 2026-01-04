#!/usr/bin/env python3
import argparse
import math
import subprocess
from pathlib import Path
import cmd

AVOGADRO = 6.02214076e23  # 1/mol
MOLAR_MASS_WATER = 18.015  # g/mol
DENSITY_WATER = 1.0  # g/cm^3
ANGSTROM_TO_CM = 1e-8

def compute_n(x, y, z):
    """
    Given box edges x, y, z in Å, compute number of water molecules at 1.0 g/cm^3
    for the (x-1, y-1, z-1) Å box.
    """
    Lx = max(x, 0.0)
    Ly = max(y, 0.0)
    Lz = max(z, 0.0)

    # Convert to cm and compute volume
    Lx_cm = Lx * ANGSTROM_TO_CM
    Ly_cm = Ly * ANGSTROM_TO_CM
    Lz_cm = Lz * ANGSTROM_TO_CM
    V_cm3 = Lx_cm * Ly_cm * Lz_cm

    # mass = density * volume
    mass_g = DENSITY_WATER * V_cm3
    # moles = mass / molar mass
    moles = mass_g / MOLAR_MASS_WATER
    # molecules = moles * Avogadro
    molecules = moles * AVOGADRO

    # Round to nearest integer, minimum 0
    n = max(int(round(molecules)), 0)
    return n, (Lx, Ly, Lz)

def write_packmol_input(n, box_dims, water_pdb, output_pdb, inp_path):
    """
    Create a Packmol input file to place n water molecules inside the given box.
    """
    Lx, Ly, Lz = box_dims
    content = f"""tolerance 2.0
filetype pdb
output {output_pdb}

structure {water_pdb}
  number {n}
  inside box 1.0 1.0 22.5 {Lx-1.0:.6f} {Ly-1.0:.6f} 53.5
end structure
"""
    Path(inp_path).write_text(content)
    return content


def main():
    parser = argparse.ArgumentParser(description="Fill a box with water at 1.0 g/cm^3 using Packmol.")
    parser.add_argument("--x", type=float, required=True, help="Box length in Å")
    parser.add_argument("--y", type=float, required=True, help="Box width in Å")
    parser.add_argument("--z", type=float, required=True, help="Box height in Å")
    parser.add_argument("--water", type=str, default="water.pdb", help="Path to a single water molecule pdb file")
    parser.add_argument("--out", type=str, default=f"water_box.pdb", help="Output pdb file from Packmol")
    parser.add_argument("--inp", type=str, default="packmol.inp", help="Generated Packmol input file")
    parser.add_argument("--no-run", action="store_true", help="Generate input but do not call Packmol")
    args = parser.parse_args()

    n, box = compute_n(args.x, args.y, args.z)
    args.out = f"water_box_{n}.pdb"
    Lx, Ly, Lz = box
    print(f"Box (Å): ({Lx:.6f}, {Ly:.6f}, {Lz:.6f})")
    print(f"Water molecules (n): {n}")

    if n == 0:
        print("Computed n=0. Box volume too small after subtracting 1 Å from each edge.")
        return

    write_packmol_input(n, box, args.water, args.out, args.inp)
    print(f"Packmol input written to: {args.inp}")

    # If not --no-run, attempt to call Packmol via Julia
    if not args.no_run:
        julia_cmd = [
            "julia",
            "-e",
            f'using Packmol; run_packmol("{args.inp}")'
        ]
        print(f"Running: {' '.join(julia_cmd)}")
        subprocess.run(julia_cmd, check=True)
    
    

if __name__ == "__main__":
    main()
