# coding: utf-8
# This is an example of pyvista, you can modify it freely. Pyvista can also output gif, mp4 and html. If you are interested in 3D visualization, you can also find more examples on https://docs.pyvista.org/version/stable/
import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv

f = open("../Boxes/xHII_LoneRs_z06.923_xef6.673586e-01_110_3300Mpc","rb")

data = f.read()
f.close()
#if your box is in single precision, like output from 21cmFAST, use float32. If in double precision, then float64
data = np.frombuffer(data,np.float32)
dim = round(data.size**0.3333333)
data3d = data.reshape(dim,dim,dim)
print("Read in");
# Create the spatial reference
grid = pv.UniformGrid()
print("Create the spatial reference");
# Set the grid dimensions: shape + 1 because we want to inject our values on
#   the CELL data
grid.dimensions = np.array(data3d.shape) + 1
print("Set the grid dimensions");
# Edit the spatial reference
grid.origin = (100, 33, 55.6)  # The bottom left corner of the data set
grid.spacing = (2, 2, 2)  # These are the cell sizes along each axis
print("Edit the spatial reference");
# Add the data values to the cell data
grid.cell_data["x_HII"] = data3d.flatten(order="F");  # Flatten the array
#grid.save("imgdata.vtk");
print("Add the data values to the cell data");


p=pv.Plotter(off_screen=True,window_size=[800,800]);
# you can modify parameters of plots here

#p.add_axes(color="white")

p.add_volume(grid,opacity="linear",cmap="jet",clim=[0,1]);
_=p.set_background("black");
#p.export_html("img.html",backend='panel');
p.show(screenshot='img.png')
p.screenshot('img.png',transparent_background=True,return_img=False);
# your output file name.

