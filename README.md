# construct_water_box
Using packmol to construct water box

## Description

This repository contains a Python script that generates water boxes for molecular dynamics simulations using [packmol](http://leandro.iqm.unicamp.br/m3g/packmol/home.shtml). The script creates a packmol input file and can optionally run packmol to generate a PDB file containing the water box.

## Requirements

- Python 3.6 or higher
- Packmol (optional, for actually generating the water box)

To install packmol:
- **Ubuntu/Debian**: `sudo apt-get install packmol`
- **macOS**: `brew install packmol`
- **From source**: Download from [packmol website](http://leandro.iqm.unicamp.br/m3g/packmol/home.shtml)

## Files

- `construct_water_box.py` - Main Python script for generating water boxes
- `water.pdb` - Template PDB file containing a single water molecule (TIP3P geometry)

## Usage

### Basic usage

Generate a water box with default parameters (1000 molecules in a 30 Å cubic box):

```bash
python3 construct_water_box.py
```

### Custom parameters

```bash
python3 construct_water_box.py -n 500 -b 25.0 -t 2.0 -o my_water_box.pdb
```

### Generate input file only (without running packmol)

```bash
python3 construct_water_box.py --no-run
```

Then run packmol manually:

```bash
packmol < packmol_input.inp
```

### Command-line options

- `-o, --output` - Output PDB file for the water box (default: `water_box.pdb`)
- `-w, --water` - Input PDB file containing a single water molecule (default: `water.pdb`)
- `-n, --nmol` - Number of water molecules (default: 1000)
- `-b, --box` - Size of the cubic box in Angstroms (default: 30.0)
- `-t, --tolerance` - Minimum distance between atoms in Angstroms (default: 2.0)
- `-s, --seed` - Random seed for packmol, -1 for random (default: -1)
- `-i, --input` - Packmol input file name (default: `packmol_input.inp`)
- `--no-run` - Only generate input file, do not run packmol
- `--packmol-exe` - Path to packmol executable (default: `packmol`)

### Examples

1. Generate a small water box with 100 molecules:
   ```bash
   python3 construct_water_box.py -n 100 -b 15.0
   ```

2. Generate a large water box with reproducible results:
   ```bash
   python3 construct_water_box.py -n 5000 -b 50.0 -s 12345
   ```

3. Generate input for manual packmol execution:
   ```bash
   python3 construct_water_box.py --no-run -i my_input.inp
   packmol < my_input.inp
   ```

## How it works

1. The script reads a water molecule template from `water.pdb`
2. It generates a packmol input file with the specified parameters
3. If packmol is available and `--no-run` is not specified, it runs packmol to generate the water box
4. The output is a PDB file containing the specified number of water molecules randomly positioned within the box

## Water molecule geometry

The included `water.pdb` file uses TIP3P water geometry:
- O-H bond length: 0.9572 Å
- H-O-H angle: 104.52°

You can replace this file with your own water model if needed.

## License

This project is provided as-is for generating water boxes for molecular dynamics simulations.
