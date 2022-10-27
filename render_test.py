#!/usr/bin/python
# run script in command prompt with command:
#"C:\Program Files\Blender Foundation\Blender 3.1\blender.exe" --background studio_start_up_file.blend --python render_test.py

import bpy
import os
from math import radians
import sys, getopt
import argparse

pdb_id = '4ccz'

folder_path = r"C:\Users\davida\Documents\outreach\blender\scripts\\"
render_folder = r"renders\\"
render_file = "%s_render" % pdb_id
render_path = folder_path+render_folder+render_file
model_folder = r"models\\"
model_file = "%s.obj" % pdb_id
model_path = folder_path+model_folder+model_file

bpy.ops.import_scene.obj(filepath=model_path, filter_glob="*.obj;*.mtl")
bpy.data.objects[pdb_id].select_set(True)
current_x, current_y, current_z = bpy.data.objects[pdb_id].dimensions
new_x = 0.7*(current_x/current_y)
new_y = 0.7
new_z = 0.7*(current_z/current_y)
bpy.data.objects[pdb_id].dimensions = [new_x, new_y, new_z]

#bpy.ops.transform.resize(value=(0.002, 0.002, 0.002))
bpy.ops.transform.translate(value=(0, 0, 0.35), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)

bpy.context.scene.render.resolution_percentage = 20
bpy.context.scene.render.filepath = render_path
bpy.ops.render.render(write_still=True)
   
