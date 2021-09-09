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

# class MutinatorCollectionList(bpy.)

import bpy

class MutinatorCollectionWraper(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
        name="Collection Name",
        default=""
    )
    collection: bpy.props.PointerProperty(
        type=bpy.types.Collection
    )

class MutatinatorProps(bpy.types.PropertyGroup):
    active: bpy.props.IntProperty(
        name="Active Collection"
    )

    collections: bpy.props.CollectionProperty(
        type=MutinatorCollectionWraper,
        name="Collections",
        description=""
    )