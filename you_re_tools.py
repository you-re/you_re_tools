bl_info = {
    "name" : "Youre Tools",
    "author" : "You Re <j.sulic@gmail.com>",
    "version" : (0, 0, 1),
    "blender" : (3, 1, 0),
    "category" : "Object",
    "location" : "Operator Search",
    "description" : "A bunch of tools I find useful.",
    "warning" : "",
    "doc_url" : "",
    "tracker_url" : "",
    }

import bpy

# class material_assigner_properties(bpy.types.PropertyGroup):
#     separator: bpy.props.StringProperty(
#         name = "Separator",
#         description = "String separator",
#         default = ".",
#         maxlen = 255
#         )

class OBJECT_OT_material_assigner(bpy.types.Operator):
    """Takes the name of the object and assigns a material with the same name to it"""
    bl_idname = "object.mat_ass"
    bl_label = "Material Assigner"
    bl_options = {'REGISTER', 'UNDO'}

    separator: bpy.props.StringProperty(
        name = "Separator",
        description = "String separator",
        default = ".",
        maxlen = 255
        )

    def execute(self, context):        
        # ----------- Function start -----------

        # Set view layer
        view_layer = bpy.context.view_layer

        # Set active object
        obj_active = view_layer.objects.active

        # Get the selected objects
        selected_objects = bpy.context.selected_objects

        # Deselect all
        bpy.ops.object.select_all(action="DESELECT")

        def add_material(object, separator):
            
            obj.select_set(True)
            
            view_layer.objects.active = obj
            
            # Remove all material slots
            for mat in obj.data.materials:
                bpy.ops.object.material_slot_remove()
            
            # Create a new material with the name of the object
            material_name = str(obj.name).split(separator)[0]

            mat = bpy.data.materials.get(material_name)
            
            # If material does not exist create one
            if not mat:
                mat = bpy.data.materials.new(material_name)
            
            # Assign the material to the object
            obj.data.materials.append(mat)
            
            # Deselect the object
            obj.select_set(False)

        # Assign material for each mesh in selection
        sep = self.separator

        for obj in selected_objects:
            if (obj.type == "MESH"):
                add_material(obj, sep)

        # Set object back to active
        view_layer.objects.active = obj_active

        # Set the initial selection to selected
        for obj in selected_objects:
            obj.select_set(True)

        # ----------- Function end -----------

        return {"FINISHED"}

class VIEW3D_PT_material_assigner(bpy.types.Panel):
    bl_label = "Youre Tools"
    bl_idname = "VIEW3D_PT_youre_tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Youre Tools"    

    def draw(self, context):
        column = self.layout.column()

        column.operator("object.mat_ass",
            text = "Assign Materials",
            icon = "SHADING_RENDERED")

        scene = context.scene
        
        column = self.layout.column(align = True)
        row = column.row(align = True)
        row.operator("scene.material_assigner_properties.separator",
            text = "String Separator")
        # row.prop(context.scene.material_assigner_properties, "separator", text = ".")        

        # layout = self.layout
        # layout.label(text = " Simple Row:")
        # row = layout.row()
        # row.prop(self.separator, "default")
        # column = self.layout.label(align = True)
        # self.layout.label(text = "Separator string: ")

def mesh_add_menu_draw(self, contex):
    pass

def register():
    bpy.utils.register_class(OBJECT_OT_material_assigner)
    bpy.utils.register_class(VIEW3D_PT_material_assigner)
    bpy.types.VIEW3D_MT_object.append(mesh_add_menu_draw)
    
def unregister():
    bpy.utils.unregister_class(OBJECT_OT_material_assigner)
    bpy.utils.unregister_class(VIEW3D_PT_material_assigner)
    bpy.types.VIEW3D_MT_object.remove(mesh_add_menu_draw)