# construct_water_box

A python script to using the Packmol (installed by Julia) to generate a water box (1g/cm3) on Windows system.

1. Install Julia (Julia.appinstaller)
2. Install Packmol by Julia. (https://m3g.github.io/packmol/download.shtml).

   a. Open Julia

   b. Input: import Pkg; Pkg.add("Packmol")

4. cmd: **python cal-water.py --x 30 --y 30 --z 30**
 
   a. 30 Å * 30 Å * 30 Å is the box's dimension, water count is based on this.

   b. what we get is a box with a dimension of 28 Å * 28 Å * 26 Å, which is useful for merging the box with other structures.

   c. --water **spce** (default), --d **1.0** (defalut 1.0 g/cm3), these options have deafult settings and are not required to input.

   d. If the real box's dimension is needed to change, it is on the **python file line 49**

       (  inside box 1.0 1.0 22.5 {Lx-1.0:.6f} {Ly-1.0:.6f} 53.5)

6. water models

   tip3p.pdb is TIP3P model

   spec.pdb is SPC/E model

   opc.pdb is four point OPC model

   opc3.pdb is three point OPC model.
   
