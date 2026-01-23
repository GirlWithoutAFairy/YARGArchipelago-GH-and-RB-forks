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
        self.selectedsonglist = []
        self.yarggemamount = 0
        self.songinstruments = {}


    
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
        shuffletoggle = False
        shuffledinstruments = 0
        instrumentlist = []
        if self.options.shuffle_guitar:
            shuffledinstruments += 1
            instrumentlist.append("guitar5F")
        if self.options.shuffle_bass:
            shuffledinstruments += 1
            instrumentlist.append("bass5F")
        if self.options.shuffle_rhythm:
            shuffledinstruments += 1
            instrumentlist.append("rhythm5F")
        if self.options.shuffle_drums:
            shuffledinstruments += 1
            instrumentlist.append("drums")
        if self.options.shuffle_keys:
            shuffledinstruments += 1
            instrumentlist.append("keys5F")
        if self.options.shuffle_pro_keys:
            shuffledinstruments += 1
            instrumentlist.append("keysPro")
        if self.options.shuffle_vocals:
            shuffledinstruments += 1
            instrumentlist.append("vocals")
        if self.options.shuffle_2_part_harmony:
            shuffledinstruments += 1
            instrumentlist.append("harmony2")
        if self.options.shuffle_3_part_harmony:
            shuffledinstruments += 1
            instrumentlist.append("harmony3")

        #Enable Instrument Shuffle only if 2 or more instruments were selected
        if shuffledinstruments >= 2:
            if self.options.instrument_shuffle:
                shuffletoggle = True

        print("~~~~~~~~~~PRE SHUFFLE CHECK LIST~~~~~~~~~~")
        print(f"Length = {len(fullsonglist)}")
        print(fullsonglist)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        #Remove all songs from fullsonglist that don't have any shuffle selected instruments
        if shuffletoggle:
            for song in fullsonglist.copy():
                compatableinstruments = 0
                if self.options.shuffle_guitar:
                    if (Songs.get(song)).guitar5F:
                        compatableinstruments += 1
                        print(f"{song} Has Guitar")
                if self.options.shuffle_bass:
                    if (Songs.get(song)).bass5F:
                        compatableinstruments += 1
                        print(f"{song} Has Bass")
                if self.options.shuffle_rhythm:
                    if (Songs.get(song)).rhythm5F:
                        compatableinstruments += 1
                        print(f"{song} Has Rhythm")
                if self.options.shuffle_drums:
                    if (Songs.get(song)).drums:
                        compatableinstruments += 1
                        print(f"{song} Has Drums")
                if self.options.shuffle_keys:
                    if (Songs.get(song)).keys5F:
                        compatableinstruments += 1
                        print(f"{song} Has Keys")
                if self.options.shuffle_pro_keys:
                    if (Songs.get(song)).keysPro:
                        compatableinstruments += 1
                        print(f"{song} Has Pro Keys")
                if self.options.shuffle_vocals:
                    if (Songs.get(song)).vocals:
                        compatableinstruments += 1
                        print(f"{song} Has Vocals")
                if self.options.shuffle_2_part_harmony:
                    if (Songs.get(song)).harmony2:
                        compatableinstruments += 1
                        print(f"{song} Has 2 Part Harmony")
                if self.options.shuffle_3_part_harmony:
                    if (Songs.get(song)).harmony3:
                        compatableinstruments += 1
                        print(f"{song} Has 3 Part Harmony")
                
                if compatableinstruments == 0:
                    fullsonglist.remove(song)
                    print(f"{song} has no compatible instruments, removing {song}.")

            if len(fullsonglist) == 0:
                raise OptionError("Instrument Shuffle failed: Add setlist with compatible instruments")


        print("~~~~~~~~~~POST SHUFFLE SONG LIST~~~~~~~~~~")
        print(f"Length = {len(fullsonglist)}")
        print(fullsonglist)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")            

        #Check that every instrument is in at least 1 song
        if shuffletoggle:
            for x in instrumentlist:
                compatiblesong = False
                for song in fullsonglist:
                    if x == "guitar5F":
                        if (Songs.get(song)).guitar5F:
                            compatiblesong = True
                    if x == "bass5F":
                        if (Songs.get(song)).bass5F:
                            compatiblesong = True
                    if x == "rhythm5F":
                        if (Songs.get(song)).rhythm5F:
                            compatiblesong = True
                    if x == "drums":
                        if (Songs.get(song)).drums:
                            compatiblesong = True
                    if x == "keys5F":
                        if (Songs.get(song)).keys5F:
                            compatiblesong = True
                    if x == "keysPro":
                        if (Songs.get(song)).keysPro:
                            compatiblesong = True
                    if x == "vocals":
                        if (Songs.get(song)).vocals:
                            compatiblesong = True
                    if x == "harmony2":
                        if (Songs.get(song)).harmony2:
                            compatiblesong = True
                    if x == "harmony3":
                        if (Songs.get(song)).harmony3:
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
        tempsonglist = self.selectedsonglist
        if shuffletoggle:
            #Make sure every instrument has at least 1 song
            for x in instrumentlist:
                tempindex = self.random.randint(0,(len(tempsonglist) - 1))
                combosuccess = False
                while combosuccess == False:
                    #Cycle through the temp song list
                    if tempindex == (len(tempsonglist) -1):
                        tempindex = 0
                    else:
                        tempindex += 1
                    
                    #Check for instrument compatibility and add combo to dictionary
                    if x == "guitar5F":
                        if (Songs.get(tempsonglist[tempindex])).guitar5F:
                            print(f"{tempsonglist[tempindex]} assigned guitar")
                            self.songinstruments[tempsonglist[tempindex]] = "guitar5F"
                            tempsonglist.remove(tempsonglist[tempindex])
                            combosuccess = True

                    if x == "bass5F":
                        if (Songs.get(tempsonglist[tempindex])).bass5F:
                            print(f"{tempsonglist[tempindex]} assigned bass")
                            self.songinstruments[tempsonglist[tempindex]] = "bass5F"
                            tempsonglist.remove(tempsonglist[tempindex])
                            combosuccess = True
                    if x == "rhythm5F":
                        if (Songs.get(tempsonglist[tempindex])).rhythm5F:
                            print(f"{tempsonglist[tempindex]} assigned rhythm")
                            self.songinstruments[tempsonglist[tempindex]] = "rhythm5F"
                            tempsonglist.remove(tempsonglist[tempindex])
                            combosuccess = True
                    if x == "drums":
                        if (Songs.get(tempsonglist[tempindex])).drums:
                            print(f"{tempsonglist[tempindex]} assigned drums")
                            self.songinstruments[tempsonglist[tempindex]] = "drums"
                            tempsonglist.remove(tempsonglist[tempindex])
                            combosuccess = True
                    if x == "keys5F":
                        if (Songs.get(tempsonglist[tempindex])).keys5F:
                            print(f"{tempsonglist[tempindex]} assigned keys")
                            self.songinstruments[tempsonglist[tempindex]] = "keys5F"
                            tempsonglist.remove(tempsonglist[tempindex])
                            combosuccess = True
                    if x == "keysPro":
                        if (Songs.get(tempsonglist[tempindex])).keysPro:
                            print(f"{tempsonglist[tempindex]} assigned pro keys")
                            self.songinstruments[tempsonglist[tempindex]] = "keysPro"
                            tempsonglist.remove(tempsonglist[tempindex])
                            combosuccess = True
                    if x == "vocals":
                        if (Songs.get(tempsonglist[tempindex])).vocals:
                            print(f"{tempsonglist[tempindex]} assigned vocals")
                            self.songinstruments[tempsonglist[tempindex]] = "vocals"
                            tempsonglist.remove(tempsonglist[tempindex])
                            combosuccess = True
                    if x == "harmony2":
                        if (Songs.get(tempsonglist[tempindex])).harmony2:
                            print(f"{tempsonglist[tempindex]} assigned 2 part harmony")
                            self.songinstruments[tempsonglist[tempindex]] = "harmony2"
                            tempsonglist.remove(tempsonglist[tempindex])
                            combosuccess = True
                    if x == "harmony3":
                        if (Songs.get(tempsonglist[tempindex])).harmony3:
                            print(f"{tempsonglist[tempindex]} assigned 3 part harmony")
                            self.songinstruments[tempsonglist[tempindex]] = "harmony3"
                            tempsonglist.remove(tempsonglist[tempindex])
                            combosuccess = True
                    if combosuccess == False:
                        print(f"{tempsonglist[tempindex]} failed all assignments")
                    
            #Apply a random instrument to each song
            for song in tempsonglist:
                
                tempindex = self.random.randint(0,(len(instrumentlist)) - 1)
                combosuccess = False
            
                while combosuccess == False:
                    #Cycle instrument list
                    if tempindex == (len(instrumentlist) -1):
                        tempindex = 0
                    else:
                        tempindex += 1
                    
                    #Check for instrument compatibility and add combo to dictionary
                    if instrumentlist[tempindex] == "guitar5F":
                        if (Songs.get(song)).guitar5F:
                            self.songinstruments[song] = "guitar5F"
                            combosuccess = True
                    if instrumentlist[tempindex] == "bass5F":
                        if (Songs.get(song)).bass5F:
                            self.songinstruments[song] = "bass5F"
                            combosuccess = True
                    if instrumentlist[tempindex] == "rhythm5F":
                        if (Songs.get(song)).rhythm5F:
                            self.songinstruments[song] = "rhythm5F"
                            combosuccess = True
                    if instrumentlist[tempindex] == "drums":
                        if (Songs.get(song)).drums:
                            self.songinstruments[song] = "drums"
                            combosuccess = True
                    if instrumentlist[tempindex] == "keys5F":
                        if (Songs.get(song)).keys5F:
                            self.songinstruments[song] = "keys5F"
                            combosuccess = True
                    if instrumentlist[tempindex] == "keysPro":
                        if (Songs.get(song)).keysPro:
                            self.songinstruments[song] = "keysPro"
                            combosuccess = True
                    if instrumentlist[tempindex] == "vocals":
                        if (Songs.get(song)).vocals:
                            self.songinstruments[song] = "vocals"
                            combosuccess = True
                    if instrumentlist[tempindex] == "harmony2":
                        if (Songs.get(song)).harmony2:
                            self.songinstruments[song] = "harmony2"
                            combosuccess = True
                    if instrumentlist[tempindex] == "harmony3":
                        if (Songs.get(song)).harmony3:
                            self.songinstruments[song] = "harmony3"
                            combosuccess = True
            
            print("~~~~~~~~~~SONG INSTRUMENT COMBOS~~~~~~~~~~")
            print(self.songinstruments)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    





        #Determine starting song and goal song
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

        #Create Item for starting song early and push it into collected inventory
        startingsong = self.create_item(str(self.selectedsonglist[starting_song_index]))
        #push_precollected does create a duplicate of the song unlock item
        #This shouldn't be a problem for now but should be looked into if
        #we run into too many items in the future somehow
        self.push_precollected(startingsong)
        
        #Get starting songs instrument if using instrument shuffle
        if shuffletoggle:
            startinginstrument = ""
            print("~~~~~~~~~~~~self.songinstruments~~~~~~~~~~~~")
            print(self.songinstruments)
            print(f"getting value for ({startingsong})")
            print(f"self.starting_song = {self.starting_song}")
            if self.songinstruments[self.starting_song] == "guitar5F":
                startinginstrument = "Guitar"
            if self.songinstruments[self.starting_song] == "bass5F":
                startinginstrument = "Bass"
            if self.songinstruments[self.starting_song] == "rhythm5F":
                startinginstrument = "Rhythm"
            if self.songinstruments[self.starting_song] == "drums":
                startinginstrument = "Drums"
            if self.songinstruments[self.starting_song] == "keys5F":
                startinginstrument = "Keys"
            if self.songinstruments[self.starting_song] == "keysPro":
                startinginstrument = "Pro Keys"
            if self.songinstruments[self.starting_song] == "vocals":
                startinginstrument = "Vocals"
            if self.songinstruments[self.starting_song] == "harmony2":
                startinginstrument = "2 Part Harmony"
            if self.songinstruments[self.starting_song] == "harmony3":
                startinginstrument = "3 Part Harmony"
            pushedinstrument = self.create_item(startinginstrument)
            self.push_precollected(pushedinstrument)


        self.goal_song = str(self.selectedsonglist[goal_song_index])
        
        #Calculate required YARG gem count based on song list and yaml option (thanks kev :) 
        optionpercent = self.options.percent_of_gems_generated
        setlistlength = (len(self.selectedsonglist) - 3)
        self.yarggemamount = (int(math.floor((optionpercent / 100) * setlistlength)))
        
        #Set completion condition for the world based on fianl song and gem amount
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