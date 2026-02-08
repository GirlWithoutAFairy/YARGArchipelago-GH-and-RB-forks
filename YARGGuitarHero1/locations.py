from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location, Region

from . import items

from .songinfo import Songs

if TYPE_CHECKING:
    from .world import YARGGuitarHero1World

LOCATION_NAME_TO_ID = {}

#Putting quotes around the location names does look nicer, unless
#the song has quotes in it's name.. considering removing the quotes
locationID = 1
for name in Songs.keys():
    LOCATION_NAME_TO_ID["\"" + str(name) + "\" Item 1"] = (locationID)
    locationID = locationID + 1
    LOCATION_NAME_TO_ID["\"" + str(name) + "\" Item 2"] = (locationID)
    locationID = locationID + 1
    LOCATION_NAME_TO_ID["\"" + str(name) + "\" Item 3"] = (locationID)
    locationID = locationID + 1


class YARGGuitarHero1Location(Location):
    game = "YARG Guitar Hero 1"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: YARGGuitarHero1World) -> None:
    create_regular_locations(world)


def create_regular_locations(world: YARGGuitarHero1World) -> None:
    menu = world.get_region("Menu")

    for name in world.selectedsonglist:
        if name != world.goal_song:
            location1 = YARGGuitarHero1Location(
                world.player, (str("\"" + str(name) + "\" Item 1")), world.location_name_to_id[str("\"" + str(name) + "\" Item 1")], menu
            )
            location2 = YARGGuitarHero1Location(
                world.player, (str("\"" + str(name) + "\" Item 2")), world.location_name_to_id[str("\"" + str(name) + "\" Item 2")], menu
            )
            location3 = YARGGuitarHero1Location(
                world.player, (str("\"" + str(name) + "\" Item 3")), world.location_name_to_id[str("\"" + str(name) + "\" Item 3")], menu
            )

            menu.locations.append(location1)
            menu.locations.append(location2)
            menu.locations.append(location3)