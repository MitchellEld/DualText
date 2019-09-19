import bpy

word1 = "Samuel"
word2 = "Wonfor"

#-------------begin of script---------------
word1 = word1.upper()
word2 = word2.upper()

for i in range(0,len(word1)):
    letter1 = word1[i]
    letter2 = word2[i]
    

    bpy.ops.object.text_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0),)
    txt = bpy.data.objects['Text']

    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    #bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.editmode_toggle()
    for j in range(4):
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text=letter1)
    bpy.ops.object.editmode_toggle()
    fnt = bpy.data.fonts.load('C:\\Windows\\Fonts\\FRAHV.TTF')
    txt.data.font = fnt

    bpy.context.object.data.extrude = 1.5
    bpy.ops.object.convert(target='MESH')

    bpy.ops.object.text_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, .01),)
    txt2 = bpy.data.objects[('Text.00'+str(i+1))]
    

    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.editmode_toggle()
    #REVERSE HERE^^ -------------------------
    
    for j in range(4):
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text=letter2)
    bpy.ops.object.editmode_toggle()
    fnt = bpy.data.fonts.load('C:\\Windows\\Fonts\\FRAHV.TTF')
    txt2.data.font = fnt
    
    bpy.context.object.data.extrude = 1.5
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].solver = 'CARVE'

    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
    bpy.context.object.location[0] = i/1.8
    bpy.context.object.location[1] = i/1.8
    #REVERS HERE ^^^ ---------------------

    objs = bpy.data.objects
    objs.remove(objs["Text"], True)
    

bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(1.47556, 0.825532, 0.0500103), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
platform = len(word1)/1.6
bpy.context.object.location[0] = (platform-1)/2
bpy.context.object.location[1] = (platform-1)/2
bpy.context.object.location[2] = -0.05
bpy.context.object.rotation_euler[2] = 0.785398
bpy.context.object.scale[1] = 0.5
bpy.context.object.scale[2] = 0.05
bpy.context.object.scale[0] = (platform*3)/4

