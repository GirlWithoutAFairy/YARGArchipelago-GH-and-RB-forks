from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from .songinfo import Songs

if TYPE_CHECKING:
    from .world import YARGWorld


def set_all_rules(world: YARGWorld) -> None:
    set_all_location_rules(world)

def set_all_location_rules(world: YARGWorld) -> None:
    #Loop the songs dictionary and add location rules for both song locations
    #on every song to the relative song unlock item
    for name in world.selectedsonglist:
        location1 = world.get_location("\"" + str(name) + "\" Item 1")
        location2 = world.get_location("\"" + str(name) + "\" Item 2")
        item = str(name)
        set_rule(location1, lambda state, x=item: state.has(x, world.player))
        
        set_rule(location2, lambda state, x=item: state.has(x, world.player))