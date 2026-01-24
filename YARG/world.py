from collections.abc import Mapping
from typing import Any
from BaseClasses import Region, MultiWorld
from Options import OptionError

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
        self.starting_song2 = ""
        self.selectedsonglist = []
        self.yarggemamount = 0
        self.songinstruments = {}
        self.shuffletoggle = False
        self.instrumentlist = []
        self.startinginstrument = ""


    
    def generate_early(self) -> None:
        
        fullsonglist = list()

        #force enable default setlist if no setlists are enabled in the yaml (stops a gen crash)
        enabledsets = set(self.options.enabled_setlists.value)
        if set(enabledsets) == set():
            enabledsets.add("YARG Official Setlist")

        #Build up song list out of songs in selected setlists
        for test, data in Songs.items():
            for x in set(enabledsets):
                if str(data.group) == str(x):
                    fullsonglist.append(test)


        #Default instrument shuffle off and count selected shuffled instruments
        self.shuffletoggle = False
        shuffledinstruments = 0
        self.instrumentlist = []
        if self.options.shuffle_guitar:
            shuffledinstruments += 1
            self.instrumentlist.append("guitar5F")
        if self.options.shuffle_bass:
            shuffledinstruments += 1
            self.instrumentlist.append("bass5F")
        if self.options.shuffle_rhythm:
            shuffledinstruments += 1
            self.instrumentlist.append("rhythm5F")
        if self.options.shuffle_drums:
            shuffledinstruments += 1
            self.instrumentlist.append("drums")
        if self.options.shuffle_keys:
            shuffledinstruments += 1
            self.instrumentlist.append("keys5F")
        if self.options.shuffle_pro_keys:
            shuffledinstruments += 1
            self.instrumentlist.append("keysPro")
        if self.options.shuffle_vocals:
            shuffledinstruments += 1
            self.instrumentlist.append("vocals")
        if self.options.shuffle_2_part_harmony:
            shuffledinstruments += 1
            self.instrumentlist.append("harmony2")
        if self.options.shuffle_3_part_harmony:
            shuffledinstruments += 1
            self.instrumentlist.append("harmony3")

        #Enable Instrument Shuffle only if 2 or more instruments were selected
        if shuffledinstruments >= 2:
            if self.options.instrument_shuffle:
                self.shuffletoggle = True


        #Remove all songs from fullsonglist that don't have any shuffle selected instruments
        if self.shuffletoggle:
            for song in fullsonglist.copy():
                compatableinstruments = 0
                if self.options.shuffle_guitar:
                    if type((Songs.get(song)).guitar5F) == int:
                        compatableinstruments += 1
                if self.options.shuffle_bass:
                    if type((Songs.get(song)).bass5F) == int:
                        compatableinstruments += 1
                if self.options.shuffle_rhythm:
                    if type((Songs.get(song)).rhythm5F) == int:
                        compatableinstruments += 1
                if self.options.shuffle_drums:
                    if type((Songs.get(song)).drums) == int:
                        compatableinstruments += 1
                if self.options.shuffle_keys:
                    if type((Songs.get(song)).keys5F) == int:
                        compatableinstruments += 1
                if self.options.shuffle_pro_keys:
                    if type((Songs.get(song)).keysPro) == int:
                        compatableinstruments += 1
                if self.options.shuffle_vocals:
                    if type((Songs.get(song)).vocals) == int:
                        compatableinstruments += 1
                if self.options.shuffle_2_part_harmony:
                    if type((Songs.get(song)).harmony2) == int:
                        compatableinstruments += 1
                if self.options.shuffle_3_part_harmony:
                    if type((Songs.get(song)).harmony3) == int:
                        compatableinstruments += 1
                
                if compatableinstruments == 0:
                    fullsonglist.remove(song)

            if len(fullsonglist) == 0:
                raise OptionError("Instrument Shuffle failed: Add setlist with compatible instruments")



        #Check that every instrument is in at least 1 song
        if self.shuffletoggle:
            for x in self.instrumentlist:
                compatiblesong = False
                for song in fullsonglist:
                    if x == "guitar5F":
                        if type((Songs.get(song)).guitar5F) == int:
                            compatiblesong = True
                    if x == "bass5F":
                        if type((Songs.get(song)).bass5F) == int:
                            compatiblesong = True
                    if x == "rhythm5F":
                        if type((Songs.get(song)).rhythm5F) == int:
                            compatiblesong = True
                    if x == "drums":
                        if type((Songs.get(song)).drums) == int:
                            compatiblesong = True
                    if x == "keys5F":
                        if type((Songs.get(song)).keys5F) == int:
                            compatiblesong = True
                    if x == "keysPro":
                        if type((Songs.get(song)).keysPro) == int:
                            compatiblesong = True
                    if x == "vocals":
                        if type((Songs.get(song)).vocals) == int:
                            compatiblesong = True
                    if x == "harmony2":
                        if type((Songs.get(song)).harmony2) == int:
                            compatiblesong = True
                    if x == "harmony3":
                        if type((Songs.get(song)).harmony3) == int:
                            compatiblesong = True
                if compatiblesong == False:
                    raise OptionError(f"Instrument Shuffle failed: Remove incompatible instrument: {x} ")
                        



        #Check if yaml asks for too many songs, if so, clamp song count to length of selected setlists
        if len(fullsonglist) < self.options.total_songs:
            finalsongcount = len(fullsonglist)
        else:
            finalsongcount = self.options.total_songs

        #Fill selected song list with random songs from the full song list, removing from full list along the way
        for i in range(finalsongcount):
            selectedsongindex = self.random.randint(0,(len(fullsonglist) - 1))
            self.selectedsonglist.append(fullsonglist[selectedsongindex])
            fullsonglist.pop(selectedsongindex)

        #If shuffle is on, apply compatible instruments to every song
        tempsonglist = self.selectedsonglist.copy()
        if self.shuffletoggle:
            #Make sure every instrument has at least 2 song
            for i in range(2):
                for x in self.instrumentlist:
                    if len(tempsonglist) == 0:
                        raise OptionError(f"Currently unkown edge case in YARG AP world. Please send the YAML used and this error to the maintainer. Try adding more setlists that have instrument {x}")
                    tempindex = self.random.randint(0,(len(tempsonglist) - 1))
                    combosuccess = False
                    print(f"~~~~~~~~~~CHECKING INSTRUMENT {x}~~~~~~~~~~")
                    loopnumber = 0
                    while combosuccess == False:
                        if loopnumber == (len(tempsonglist) + 1):
                            raise OptionError(f"Not enough songs have instrument {x}. Please add another setlist with more songs with the instrument or remove the instrument from shuffle.")
                        print("#Cycle through the temp song list")
                        print(f"Temp song list is this long: {len(tempsonglist)}")
                        if tempindex == (len(tempsonglist) -1):
                            tempindex = 0
                        else:
                            tempindex += 1
                        

                        print("#Check for instrument compatibility and add combo to dictionary")
                        print(f"Checking song: {tempsonglist[tempindex]}")
                        if x == "guitar5F":
                            if type((Songs.get(tempsonglist[tempindex])).guitar5F) == int:
                                self.songinstruments[tempsonglist[tempindex]] = "guitar5F"
                                tempsonglist.remove(tempsonglist[tempindex])
                                combosuccess = True
                        if x == "bass5F":
                            if type((Songs.get(tempsonglist[tempindex])).bass5F) == int:
                                self.songinstruments[tempsonglist[tempindex]] = "bass5F"
                                tempsonglist.remove(tempsonglist[tempindex])
                                combosuccess = True
                        if x == "rhythm5F":
                            if type((Songs.get(tempsonglist[tempindex])).rhythm5F) == int:
                                self.songinstruments[tempsonglist[tempindex]] = "rhythm5F"
                                tempsonglist.remove(tempsonglist[tempindex])
                                combosuccess = True
                        if x == "drums":
                            if type((Songs.get(tempsonglist[tempindex])).drums) == int:
                                self.songinstruments[tempsonglist[tempindex]] = "drums"
                                tempsonglist.remove(tempsonglist[tempindex])
                                combosuccess = True
                        if x == "keys5F":
                            if type((Songs.get(tempsonglist[tempindex])).keys5F) == int:
                                self.songinstruments[tempsonglist[tempindex]] = "keys5F"
                                tempsonglist.remove(tempsonglist[tempindex])
                                combosuccess = True
                        if x == "keysPro":
                            if type((Songs.get(tempsonglist[tempindex])).keysPro) == int:
                                self.songinstruments[tempsonglist[tempindex]] = "keysPro"
                                tempsonglist.remove(tempsonglist[tempindex])
                                combosuccess = True
                        if x == "vocals":
                            if type((Songs.get(tempsonglist[tempindex])).vocals) == int:
                                self.songinstruments[tempsonglist[tempindex]] = "vocals"
                                tempsonglist.remove(tempsonglist[tempindex])
                                combosuccess = True
                        if x == "harmony2":
                            if type((Songs.get(tempsonglist[tempindex])).harmony2) == int:
                                self.songinstruments[tempsonglist[tempindex]] = "harmony2"
                                tempsonglist.remove(tempsonglist[tempindex])
                                combosuccess = True
                        if x == "harmony3":
                            if type((Songs.get(tempsonglist[tempindex])).harmony3) == int:
                                self.songinstruments[tempsonglist[tempindex]] = "harmony3"
                                tempsonglist.remove(tempsonglist[tempindex])
                                combosuccess = True
                        loopnumber += 1
        
            print("#Apply a random instrument to each song")
            for song in tempsonglist:
                
                tempindex = self.random.randint(0,(len(self.instrumentlist)) - 1)
                combosuccess = False
                print(f"~~~~~~~~~CHECKING SONG {song}~~~~~~~~~~~")
            
                while combosuccess == False:
                    print("#Cycle instrument list")
                    if tempindex == (len(self.instrumentlist) -1):
                        tempindex = 0
                    else:
                        tempindex += 1
                    
                    print(f"~~~~~~~~~~~~CHECKING INSTRUMENT {self.instrumentlist[tempindex]}")
                    print("#Check for instrument compatibility and add combo to dictionary")
                    if self.instrumentlist[tempindex] == "guitar5F":
                        if type((Songs.get(song)).guitar5F) == int:
                            self.songinstruments[song] = "guitar5F"
                            combosuccess = True
                    if self.instrumentlist[tempindex] == "bass5F":
                        if type((Songs.get(song)).bass5F) == int:
                            self.songinstruments[song] = "bass5F"
                            combosuccess = True
                    if self.instrumentlist[tempindex] == "rhythm5F":
                        if type((Songs.get(song)).rhythm5F) == int:
                            self.songinstruments[song] = "rhythm5F"
                            combosuccess = True
                    if self.instrumentlist[tempindex] == "drums":
                        if type((Songs.get(song)).drums) == int:
                            self.songinstruments[song] = "drums"
                            combosuccess = True
                    if self.instrumentlist[tempindex] == "keys5F":
                        if type((Songs.get(song)).keys5F) == int:
                            self.songinstruments[song] = "keys5F"
                            combosuccess = True
                    if self.instrumentlist[tempindex] == "keysPro":
                        if type((Songs.get(song)).keysPro) == int:
                            self.songinstruments[song] = "keysPro"
                            combosuccess = True
                    if self.instrumentlist[tempindex] == "vocals":
                        if type((Songs.get(song)).vocals) == int:
                            self.songinstruments[song] = "vocals"
                            combosuccess = True
                    if self.instrumentlist[tempindex] == "harmony2":
                        if type((Songs.get(song)).harmony2) == int:
                            self.songinstruments[song] = "harmony2"
                            combosuccess = True
                    if self.instrumentlist[tempindex] == "harmony3":
                        if type((Songs.get(song)).harmony3) == int:
                            self.songinstruments[song] = "harmony3"
                            combosuccess = True
            
                    




        print("#Determine starting song and goal song")
        starting_song_index = self.random.randint(0,(len(self.selectedsonglist) - 1))
        tempindex = self.random.randint(0,(len(self.selectedsonglist) - 1))
        print("#If the starting song and goal song end up the same (really low odds),")
        print("#bump the index by 1 to avoid go mode in sphere 0 ")
        if tempindex == starting_song_index:
            if tempindex == 0:
                tempindex = tempindex + 1
            else:
                tempindex = tempindex - 1
        goal_song_index = tempindex
        self.starting_song = str(self.selectedsonglist[starting_song_index])

        print("#Create Item for starting song early and push it into collected inventory")
        startingsong = self.create_item(str(self.selectedsonglist[starting_song_index]))
        print("#push_precollected does create a duplicate of the song unlock item")
        print("#This shouldn't be a problem for now but should be looked into if")
        print("#we run into too many items in the future somehow")
        self.push_precollected(startingsong)
        
        print("#Get starting songs instrument if using instrument shuffle")
        if self.shuffletoggle:
            self.startinginstrument = ""
            if self.songinstruments[self.starting_song] == "guitar5F":
                self.startinginstrument = "Guitar"
            if self.songinstruments[self.starting_song] == "bass5F":
                self.startinginstrument = "Bass"
            if self.songinstruments[self.starting_song] == "rhythm5F":
                self.startinginstrument = "Rhythm"
            if self.songinstruments[self.starting_song] == "drums":
                self.startinginstrument = "Drums"
            if self.songinstruments[self.starting_song] == "keys5F":
                self.startinginstrument = "Keys"
            if self.songinstruments[self.starting_song] == "keysPro":
                self.startinginstrument = "Pro Keys"
            if self.songinstruments[self.starting_song] == "vocals":
                self.startinginstrument = "Vocals"
            if self.songinstruments[self.starting_song] == "harmony2":
                self.startinginstrument = "2 Part Harmony"
            if self.songinstruments[self.starting_song] == "harmony3":
                self.startinginstrument = "3 Part Harmony"
            pushedinstrument = self.create_item(self.startinginstrument)
            self.push_precollected(pushedinstrument)

            print("#Add second starting song with compatible instrument")
            self.starting_song2 = ""
            for song in self.songinstruments.keys():
                if song != self.starting_song:
                    if self.startinginstrument == self.songinstruments[song]:
                        pushedsong2 = self.create_item(song)
                        self.starting_song2 = song

            


        self.goal_song = str(self.selectedsonglist[goal_song_index])
        
        print("#Calculate required YARG gem count based on song list and yaml option (thanks kev :) ")
        optionpercent = self.options.percent_of_gems_generated
        setlistlength = (len(self.selectedsonglist) - 3)
        self.yarggemamount = (int(math.floor((optionpercent / 100) * setlistlength)))
        
        print("#Set completion condition for the world based on final song and gem amount")
        if self.shuffletoggle:
            inst = self.songinstruments[self.selectedsonglist[goal_song_index]]
            if inst == "guitar5F":
                instname = "Guitar"
            if inst == "bass5F":
                instname = "Bass"
            if inst == "rhythm5F":
                instname = "Rhythm"
            if inst == "drums":
                instname = "Drums"
            if inst == "keys5F":
                instname = "Keys"
            if inst == "keysPro":
                instname = "Pro Keys"
            if inst == "vocals":
                instname = "Vocals"
            if inst == "harmony2":
                instname = "2 Part Harmony"
            if inst == "harmony3":
                instname = "3 Part Harmony"
            self.multiworld.completion_condition[self.player] = lambda state: (
                state.has_all(((self.selectedsonglist[goal_song_index]), instname), self.player) and state.has("YARG Gem", self.player, self.yarggemamount)
            )
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
        print("#Add goal song to slot data for use in the client")
        
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