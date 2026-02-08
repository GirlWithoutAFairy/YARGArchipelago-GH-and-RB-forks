from typing import NamedTuple, Optional, Dict

class SongMeta(NamedTuple):
    """Contains difficulty information, Use None for unsupported intsruments"""

    group: str
    source: str
    guitar5F: Optional[int]
    bass5F: Optional[int]
    drums: Optional[int]
    drumsElite: Optional[int]
    keys5F: Optional[int]
    keysPro: Optional[int]
    vocals: Optional[int]
    harmony2: Optional[int]
    harmony3: Optional[int]
    rhythm5F: Optional[int]

Songs: Dict[str, SongMeta] = {
    "Trippolette": SongMeta("Guitar Hero 1 Hidden Songs", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Infected": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Godzilla": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Fly On The Wall": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "More Than A Feeling": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Cochise": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Decontrol": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Crossroads": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Behind The Mask": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "The Breaking Wheel": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Heart Full of Black": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Sail Your Ship By": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Smoke On The Water": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Fire It Up": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Ziggy Stardust": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Iron Man": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Take Me Out": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Hey": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Bark at the Moon": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Symphony Of Destruction": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Ace Of Spades": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "You Got Another Thing Comin'": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Graveyard Shift": SongMeta("Guitar Hero 1 Hidden Songs", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Unsung": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "No One Knows": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Killer Queen": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Get Ready 2 Rokk": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Cheat on the Church": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Guitar Hero": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Cowboys from Hell": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Stellar": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "I Love Rock & Roll": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Farewell Myth": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Texas Flood": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "I Wanna Be Sedated": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Fat Lip": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Higher Ground": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "All of This": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Callout": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Spanish Castle Magic": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Eureka, I've Found Love": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Thunder Kiss 65": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Sharp Dressed Man": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Story of My Love": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Caveman Rejoice": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Even Rats": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Take It Off": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Hey You": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
    "Frankenstein": SongMeta("Guitar Hero 1", "gh1",  None, None, None, None, None, None, None, None, None, None,),
}

#Example on using the Songs Dictionary
#
#for name, data in Songs.items():
#    print("Song Name: " + name)
#    print("5 Fret Guitar Diff: " + str(data.guitar5F))
#    print("5 Fret Bass Diff: " + str(data.bass5F))
#
#If you want to use the Songs Dict in other file add to top of file
#
#from .songinfo import Songs
    
    