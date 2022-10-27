#!/usr/bin/python

import bpy
import os
from math import radians
import sys, getopt
import argparse

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('Input file is "', inputfile)
   print('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])

   model_path = inputfile
   render_path = outputfile
   
   #folder_path = r"C:\Users\davida\Documents\outreach\blender\scripts\\"
   #render_folder = r"renders\\"
   #render_file = "5ire_render"
   #render_path = folder_path+render_folder+render_file
   #model_folder = r"models\\"
   #model_file = "5ire.obj"
   #model_path = folder_path+model_folder+model_file
   
   bpy.ops.import_scene.obj(filepath=model_path, filter_glob="*.obj;*.mtl")
   bpy.data.objects["5ire"].select_set(True)
   bpy.ops.transform.resize(value=(0.002, 0.002, 0.002))
   bpy.ops.transform.translate(value=(0, 0, 0.5), orient_axis_ortho='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, release_confirm=True)
   
   bpy.context.scene.render.resolution_percentage = 5
   bpy.context.scene.render.filepath = render_path
   bpy.ops.render.render(write_still=True)
   
   