# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Hell is other people's code

import bpy
from . import utils

class Mut_AddRemoveCollection(bpy.types.Operator):
    """Edit Mode Context menu for out-of-mode objects"""
    bl_idname = "mut.add_or_remove_collection"
    bl_label = "Mutatinator Add/Remove Collection"
    bl_description = "I heard you like context menus, so I put some context in your context menu"

    add: bpy.props.BoolProperty(
        name="Add",
        description="",
        default=True
    )

    def execute(self, context):
        if self.add:
            new_collection = context.scene.MutProps.collections.add()
            new_collection.collection = context.collection
        else:
            context.scene.MutProps.collections.remove(context.scene.MutProps.active)
        return {'FINISHED'}


class Mut_SetupMutations(bpy.types.Operator):
    bl_idname="mut.setup_mutations"
    bl_label="Mutatinator Setup Mutations"

    def execute(self, context):
        combos = utils.build_combo_list()
        context.scene.frame_current = 0
        utils.clear_all_keyframes()
        utils.disable_all()

        mutProps = bpy.context.scene.MutProps
        collections = mutProps.collections

        for combo in combos:
            context.scene.frame_current += 1
            for col in collections:
                for obj in col.collection.objects:
                    result = False if obj in combo else True
                    if not result == obj.hide_render:
                        utils.insert_frames(obj, result)

        context.scene.frame_current = 0

        return {'FINISHED'}


class Mut_ClearFrames(bpy.types.Operator):
    bl_idname="mut.clear_frames"
    bl_label="Mutatinator Clear Keyframes"

    def execute(self, context):
        utils.clear_all_keyframes()
        return {'FINISHED'}


class Mut_ConfigureSettings(bpy.types.Operator):
    bl_idname="mut.configure_settings"
    bl_label="Mutatinator Configure Settings"

    def execute(self, context):
        context.scene.fps = 2
        context.scene.frame_end = utils.calc_combinations()
        context.scene.render.image_settings.file_format = 'PNG'

        return {'FINISHED'}