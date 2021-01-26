# Script by ComboDev. Tested in Blender 2.91.2
# This script creates VMTs based on the existing materials of the entire Blender project.
# Converted VTFs have to have the same names as the used textures in Blender. Ex: tex1.png -> tex1.vtf
# MMD Shaders (and maybe normal maps) are not yet supported. You will have to convert MMD shaders to cycles.
# You have to have your .blend project saved in a folder. The materials will convert there!
#==========================
#VARIABLES TO CHANGE!!!
shadertype = "VertexLitGeneric"
vmtparameters = ["$alphatest 1"] #List of $ to add. Ex: "$alphatest" 1
materialcd = 'models/combodev/angelisland' #Path to textures
#==========================
import bpy
import os

materials = []

for mat in bpy.data.materials:
    if mat.node_tree:
        #print(mat.node_tree)
        for x in mat.node_tree.nodes:
            #print(x)
            pass
        try:
            tex = None
            for x in mat.node_tree.nodes:
                #print(x)
                if type(x) is bpy.types.ShaderNodeTexImage: #does not work well... 
                    #print(x)                               #probably a problem with the type and mmd nodes
                    tex = x
            texname = tex.image.filepath
            texname = texname.replace('\\', '/')
            texname = os.path.splitext(texname)[0]+'.vtf'
            #print(texname)
            #Okay, so you have the $basetexture right here.
            #Now for the converstion.
            path = bpy.path.abspath("//materials/") + materialcd
            #print(path)
            try:
                os.makedirs(path)
            except:
                pass #The directorties already exist.
            try:
                f = open(path+'/'+mat.name+".vmt", "r")
                if f.read() != '':
                    print ("File already exists... ("+mat.name+".vmt)") #File already exists and isn't empty.
            except: # if file doesn't exist
                f = open(path+'/'+mat.name+".vmt", "a")
                f.write('"' + shadertype + '"')
                f.write('\n{')
                f.write('\n\t"$basetexture" "' + materialcd+'/'+texname[2:]+ '"')
                for x in vmtparameters:
                    f.write('\n\t' + x)
                f.write('\n}')
                f.close()
            
        except Exception as e:
            print(e)
            pass

    

