#!/usr/bin/env python3
"""
Example usage of construct_water_box module.

This script demonstrates how to use the water box generation functions
programmatically without command-line arguments.
"""

from construct_water_box import generate_packmol_input, write_packmol_input


def main():
    """Example: Generate a water box with custom parameters."""
    
    # Example 1: Small water box
    print("Example 1: Generating small water box (100 molecules, 15 Å)")
    input_content = generate_packmol_input(
        output_pdb="small_water_box.pdb",
        water_pdb="water.pdb",
        n_molecules=100,
        box_size=15.0,
        tolerance=2.0,
        seed=42
    )
    write_packmol_input(input_content, "small_box_input.inp")
    print()
    
    # Example 2: Medium water box
    print("Example 2: Generating medium water box (1000 molecules, 30 Å)")
    input_content = generate_packmol_input(
        output_pdb="medium_water_box.pdb",
        water_pdb="water.pdb",
        n_molecules=1000,
        box_size=30.0,
        tolerance=2.0
    )
    write_packmol_input(input_content, "medium_box_input.inp")
    print()
    
    # Example 3: Large water box
    print("Example 3: Generating large water box (5000 molecules, 50 Å)")
    input_content = generate_packmol_input(
        output_pdb="large_water_box.pdb",
        water_pdb="water.pdb",
        n_molecules=5000,
        box_size=50.0,
        tolerance=2.0,
        seed=12345
    )
    write_packmol_input(input_content, "large_box_input.inp")
    print()
    
    print("Input files generated. Run packmol manually:")
    print("  packmol < small_box_input.inp")
    print("  packmol < medium_box_input.inp")
    print("  packmol < large_box_input.inp")


if __name__ == "__main__":
    main()
