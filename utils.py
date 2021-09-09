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
import itertools

def build_combo_list() -> list[list[bpy.types.Object]]:
    mutProps = bpy.context.scene.MutProps
    collections = mutProps.collections

    combos = []

    for col in collections:
        objects = get_collection_objects(col.collection)
        combos.append(objects)

    return list(itertools.product(*combos))


def calc_combinations() -> int:
    mutProps = bpy.context.scene.MutProps
    collections = mutProps.collections

    combos = 1
    for col in collections:
        if not col.collection:
            continue
        length = len(col.collection.all_objects)
        if length > 0:
            combos *= max(calc_collection(col.collection), 1)

    return combos


def calc_collection(collection: bpy.types.Collection) -> int:
    if not collection:
        return 0

    count = 0
    for obj in collection.all_objects:
        if not obj.parent:
            count += 1
    return count


def get_collection_objects(collection: bpy.types.Collection) -> list[bpy.types.Object]:
    objects = []

    for obj in collection.all_objects:
        if not obj.parent:
            objects.append(obj)

    return objects


def clear_all_keyframes():
    mutProps = bpy.context.scene.MutProps
    collections = mutProps.collections

    for col in collections:
        for obj in col.collection.all_objects:
            obj.animation_data_clear()


def insert_frames(obj: bpy.types.Object, visible: bool):
    f = bpy.context.scene.frame_current
    obj.hide_render = visible
    obj.hide_viewport = visible
    obj.keyframe_insert(data_path="hide_render", frame=f)
    obj.keyframe_insert(data_path="hide_viewport", frame=f)
    obj.keyframe_insert(data_path="location", frame=f)
    obj.keyframe_insert(data_path="rotation_euler", frame=f)
    obj.keyframe_insert(data_path="scale", frame=f)


def disable_all():
    mutProps = bpy.context.scene.MutProps
    collections = mutProps.collections

    for col in collections:
        for obj in col.collection.objects:
            insert_frames(obj, True)


