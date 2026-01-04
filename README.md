# construct_water_box

A python script to using the Packmol (installed by Julia) to generate a water box (1g/cm3) on Windows system.

1. Install Julia (Julia.appinstaller)
2. Install Packmol by Julia. (https://m3g.github.io/packmol/download.shtml).

   a. Open Julia
   b. Input: import Pkg; Pkg.add("Packmol")

3. cmd: python cal-water.py --x 30 --y 30 --z 30
 
   30 Å * 30 Å * 30 Å is the box's dimension, water count is based on this.

   what we get is a box with a dimension of 28 Å * 28 Å * 26 Å, which is useful for merging the box with other structures.

   If the real box's dimension is needed to change, it is on the **line 50** (  inside box 1.0 1.0 22.5 {Lx-1.0:.6f} {Ly-1.0:.6f} 53.5) 
   
