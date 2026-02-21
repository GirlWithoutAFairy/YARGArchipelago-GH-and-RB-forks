from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import YARGRockBand3World


def create_and_connect_regions(world: YARGRockBand3World) -> None:
    create_all_regions(world)
    

def create_all_regions(world: YARGRockBand3World) -> None:
    #We only have one region still had too many headaches
    #regarding regions somehow
    menu = Region("Menu", world.player, world.multiworld)

    regions = [menu,]

    world.multiworld.regions += regions
