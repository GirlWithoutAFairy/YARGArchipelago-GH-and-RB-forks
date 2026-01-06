from collections.abc import Mapping
from typing import Any
from BaseClasses import Region, MultiWorld

from worlds.AutoWorld import World

from . import items, locations, options, regions, rules, web_world
from . import options as YARG_options

from .songinfo import Songs
from .locations import LOCATION_NAME_TO_ID
from .items import ITEM_NAME_TO_ID

import math

class YARG(World):
    """
    YARG is an Open-Source plastic band rhythm game! 
    Play through the YARG Official Setlist for the crowd,
    and maybe get some free items from your fans!
    """

    game = "YARG"

    web = web_world.YARGWebWorld()

    options_dataclass = YARG_options.YARGOptions
    options: YARG_options.YARGOptions

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.goal_song = ""
        self.starting_song = ""
        self.selectedsonglist = []
        self.yarggemamount = 0


    
    def generate_early(self) -> None:
        
        #fullsonglist = list(Songs.keys())
        fullsonglist = list()

        
        for test, data in Songs.items():
            for x in set(self.options.enabled_setlists.value):
                if str(data.group) == str(x):
                    fullsonglist.append(test)

        if len(fullsonglist) < self.options.total_songs:
            finalsongcount = len(fullsonglist)
        else:
            finalsongcount = self.options.total_songs


        for i in range(finalsongcount):
            selectedsongindex = self.random.randint(0,(len(fullsonglist) - 1))
            self.selectedsonglist.append(fullsonglist[selectedsongindex])
            fullsonglist.pop(selectedsongindex)

        starting_song_index = self.random.randint(0,(len(self.selectedsonglist) - 1))
        tempindex = self.random.randint(0,(len(self.selectedsonglist) - 1))
        #If the starting song and goal song end up the same (really low odds),
        #bump the index by 1 to avoid go mode in sphere 0 
        if tempindex == starting_song_index:
            if tempindex == 0:
                tempindex = tempindex + 1
            else:
                tempindex = tempindex - 1
        goal_song_index = tempindex
        self.starting_song = str(self.selectedsonglist[starting_song_index])
        startingsong = self.create_item(str(self.selectedsonglist[starting_song_index]))
        #push_precollected does create a duplicate of the song unlock item
        #This shouldn't be a problem for now but should be looked into if
        #we run into too many items in the future somehow
        self.push_precollected(startingsong)
        self.goal_song = str(self.selectedsonglist[goal_song_index])
        
        #Calculate required YARG gem count based on song list and yaml option (thanks kev :) 
        optionpercent = self.options.percent_of_gems_generated
        setlistlength = (len(self.selectedsonglist) - 3)
        self.yarggemamount = (int(math.floor((optionpercent / 100) * setlistlength)))
        
        
        self.multiworld.completion_condition[self.player] = lambda state: (
            state.has((self.selectedsonglist[goal_song_index]), self.player) and state.has("YARG Gem", self.player, self.yarggemamount)
        )
    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = {}
        slotdatasongdict = {}
        for name in self.selectedsonglist:
            metadatalist = []
            loc1id = LOCATION_NAME_TO_ID["\"" + str(name) + "\" Item 1"]
            loc2id = LOCATION_NAME_TO_ID["\"" + str(name) + "\" Item 2"]
            itemid = ITEM_NAME_TO_ID[str(name)]
            source = str((Songs.get(str(name))).source)
            metadatalist.append(loc1id)
            metadatalist.append(loc2id)
            metadatalist.append(itemid)
            metadatalist.append(source)
            slotdatasongdict[str(name)] = (metadatalist)
        #Add goal song to slot data for use in the client
        
        slot_data["Goal Song"] = self.goal_song
        slot_data["Goal Song Source"] = str((Songs.get(str(self.goal_song))).source)
        slot_data["songlist"] = slotdatasongdict
        slot_data["Gems Required"] = self.yarggemamount
        slot_data["Goal Song Visibility"] = self.options.goal_song_visibility.value
        slot_data["Death Link"] = self.options.deathlink.value
        slot_data["Energy Link"] = self.options.energylink.value

        return slot_data

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    def create_regions(self):
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.YARGItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)