import bpy
import os

i = 0
for mat in bpy.data.materials:
    i = i + 1
    
print("There are " + str(i) + " materials in the scenes.")