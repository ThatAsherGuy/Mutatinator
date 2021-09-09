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

class CUSTOM_UL_collection_list(bpy.types.UIList):
    EMPTY = 1 << 0

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        row = layout.row(align=True)
        
        row.prop(item, "collection", text="")
        row.label(text="", icon='RADIOBUT_ON' if data.active == index else 'RADIOBUT_OFF')

    def draw_filter(self, context, layout):
        row = layout.row()

class VIEW3D_PT_mutatinator_main(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Item"
    bl_label = "Mutatinator"

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        layout = self.layout
        root = layout.column(align=True)

        root.label(text="Total Combinations:  " + str(utils.calc_combinations()))

        root.template_list(
            "CUSTOM_UL_collection_list", "",
            context.scene.MutProps, "collections",
            context.scene.MutProps, "active",
            rows=1, maxrows=4)

        row = root.row(align=True)

        op = row.operator(
            "mut.add_or_remove_collection",
            text="+"
        )
        op.add = True

        op = row.operator(
            "mut.add_or_remove_collection",
            text="-"
        )
        op.add = False

        root.separator()

        row = root.row(align=True)
        row.scale_y = 2
        op = row.operator(
            "mut.setup_mutations",
            text="Generate!"
        )

