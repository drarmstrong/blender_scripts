import bpy
import os
from math import radians

context = bpy.context

folder_path = r"C:\Users\davida\Documents\outreach\blender\scripts\"
models_path = "//models/"
render_path = "//renders/"
scene_file = "studio_start_up_file"
scene_path = folder_path+scene_file

model = "5IRE.obj"
model_path = folder_path+models_path+model

#import a scene
scene = bpy.ops.wm.open_mainfile(filepath=scene_path)

for model_path in models:
    scene.camera = camera
    path = os.path.join(models_path, model_path)
    # make a new scene with cam and lights linked
    context.screen.scene = scene
    bpy.ops.scene.new(type='LINK_OBJECTS')
    context.scene.name = model_path
    cams = [c for c in context.scene.objects if c.type == 'CAMERA']
    #import model
    bpy.ops.import_scene.obj(filepath=path, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl")
    for c in cams:
        context.scene.camera = c                                    
        print("Render ", model_path, context.scene.name, c.name)
        context.scene.render.filepath = "somepathmadeupfrommodelname"
        bpy.ops.render.render(write_still=True)

folder_path = r"C:\Users\davida\Documents\outreach\blender\scripts\"
scene_path = r"C:\Users\davida\Documents\outreach\blender\scripts\studio_5ire_zika.blend"
#model_path = r"C:\Users\davida\Documents\outreach\blender\scripts\"

#import a scene
scene_path = r"C:\Users\davida\Documents\outreach\blender\scripts\studio_5ire_zika.blend"
bpy.ops.wm.open_mainfile(filepath=scene_path)
#import an object
bpy.ops.import_scene.obj(filepath=path, axis_forward='-Z', axis_up='Y', filter_glob="*.obj;*.mtl")
#render image
context.scene.render.filepath = "somepathmadeupfrommodelname"
bpy.ops.render.render(write_still=True)
