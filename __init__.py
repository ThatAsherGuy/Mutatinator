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

import bpy

from .properties import MutinatorCollectionWraper
from .properties import MutatinatorProps

from .ui import CUSTOM_UL_collection_list
from .ui import VIEW3D_PT_mutatinator_main

from .operators import Mut_AddRemoveCollection
from .operators import Mut_SetupMutations
from .operators import Mut_ClearFrames
from .operators import Mut_ConfigureSettings

bl_info = {
    "name" : "Mutatinator",
    "author" : "ThatAsherGuy",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Rendering"
}

classes = [
    MutinatorCollectionWraper,
    MutatinatorProps,

    CUSTOM_UL_collection_list,
    VIEW3D_PT_mutatinator_main,

    Mut_AddRemoveCollection,
    Mut_SetupMutations,
    Mut_ClearFrames,
    Mut_ConfigureSettings,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
   
    bpy.types.Scene.MutProps = bpy.props.PointerProperty(type=MutatinatorProps)


def unregister():
    del  bpy.types.Scene.MutProps
