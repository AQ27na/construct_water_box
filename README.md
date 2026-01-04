# construct_water_box

A python script using **Packmol** (installed by Julia) to generate a water box (1g/cm3) on Windows system.

**1**. Install Julia (Julia.appinstaller)
**2**. Install Packmol by Julia. (https://m3g.github.io/packmol/download.shtml).

       a. Open Julia

       b. Input: import Pkg; Pkg.add("Packmol")

**3**. cmd: **python cal-water.py --x 30 --y 30 --z 30**
 
       a. **30 Å * 30 Å * 30 Å** is the box's dimension, water count is based on this.

       b. what we get is a box with a dimension of **28 Å * 28 Å * 26 Å**, which is useful for merging the box with other structures.

       c. If the real box's dimension is needed to change, it is on the **python file line 49**

          (  inside box 1.0 1.0 22.5 {Lx-1.0:.6f} {Ly-1.0:.6f} {Lz + 22.5 - 4.0:.6f})

       d. --water **spce** (default), --d **1.0** (defalut 1.0 g/cm3), these options have deafult settings and are not required to input.

       e. --no-run, generate a packmol input file without using Packmol to generate the water box.

**4**. water models

       tip3p.pdb is TIP3P model

       spec.pdb is SPC/E model

       opc.pdb is four point OPC model

       opc3.pdb is three point OPC model.

**5**. example:

       a. **python cal-water.py --x 30 --y 30 --z 30**

          a water box (x:1-29, y:1-29, z:22.5-48.5), spce water model, 1 g/cm3.

       a. **python cal-water.py --x 30 --y 30 --z 30 --water tip3p.pdb --d 0.8**

          a water box (x:1-29, y:1-29, z:22.5-48.5), tip3p water model, 0.8 g/cm3.
