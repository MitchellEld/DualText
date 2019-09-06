import bpy

word1 = "TEXAS"
word2 = "HOWDY"

for i in range(0,len(word1)):
    letter1 = word1[i]
    letter2 = word2[i]
    

    bpy.ops.object.text_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0),)

    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    #bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.editmode_toggle()
    for j in range(4):
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text=letter1)
    bpy.ops.object.editmode_toggle()

    bpy.context.object.data.extrude = 1.5
    bpy.ops.object.convert(target='MESH')




    bpy.ops.object.text_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, .01),)

    bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.object.editmode_toggle()
    for j in range(4):
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.text_insert(text=letter2)
    bpy.ops.object.editmode_toggle()
    
    bpy.context.object.data.extrude = 1.5
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].solver = 'CARVE'

    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Text"]
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
    bpy.context.object.location[0] = i
    bpy.context.object.location[1] = i

    objs = bpy.data.objects
    objs.remove(objs["Text"], True)

