from typing import NamedTuple, Optional, Dict

class SongMeta(NamedTuple):
    """Contains difficulty information, Use None for unsupported intsruments"""

    songname: str
    artistname: str
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

#Key Format XXYYZZ
#XX
#44 represents GH (Guitar Hero) in T9 Notation
#YY
#01 represents first entry (Guitar Hero 1)
#ZZ represents unique song identifier (incremental)

Songs: Dict[int, SongMeta] = {
#Guitar Hero 1
#4401
    440101: SongMeta("Hey You", "The Exies (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440102: SongMeta("Infected", "Bad Religion (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440103: SongMeta("Godzilla", "Blue Oyster Cult (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440104: SongMeta("Fly On The Wall", "Din", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440105: SongMeta("More Than A Feeling", "Boston (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440106: SongMeta("Cochise", "Audioslave (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440107: SongMeta("Decontrol", "Drist", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440108: SongMeta("Crossroads", "Cream (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440109: SongMeta("Behind The Mask", "Anarchy Club", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440110: SongMeta("The Breaking Wheel", "Artillery", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440111: SongMeta("Heart Full of Black", "Burning Brides (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440112: SongMeta("Sail Your Ship By", "Count Zero", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440113: SongMeta("Smoke On The Water", "Deep Purple (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440114: SongMeta("Fire It Up", "Black Label Society", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440115: SongMeta("Ziggy Stardust", "David Bowie (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440116: SongMeta("Iron Man", "Black Sabbath (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440117: SongMeta("Take Me Out", "Franz Ferdinand (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440118: SongMeta("Hey", "Honest Bob and the Factory-to-Dealer Incentives", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440119: SongMeta("Bark at the Moon", "Ozzy Osbourne (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440120: SongMeta("Symphony Of Destruction", "Megadeth (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440121: SongMeta("Ace Of Spades", "Motorhead (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440122: SongMeta("You Got Another Thing Comin'", "Judas Priest (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440123: SongMeta("Frankenstein", "The Edgar Winter Group (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440124: SongMeta("Unsung", "Helmet (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440125: SongMeta("No One Knows", "Queens of the Stone Age (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440126: SongMeta("Killer Queen", "Queen (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440127: SongMeta("Get Ready 2 Rokk", "Freezepop", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440128: SongMeta("Cheat on the Church", "Graveyard BBQ", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440129: SongMeta("Guitar Hero", "Monkey Steals The Peach", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440130: SongMeta("Cowboys from Hell", "Pantera (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440131: SongMeta("Stellar", "Incubus (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440132: SongMeta("I Love Rock & Roll", "Joan Jett & the Blackhearts (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440133: SongMeta("Farewell Myth", "Made In Mexico", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440134: SongMeta("Texas Flood", "Stevie Ray Vaughan (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440135: SongMeta("I Wanna Be Sedated", "The Ramones (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440136: SongMeta("Fat Lip", "Sum41 (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440137: SongMeta("Higher Ground", "Red Hot Chili Peppers (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440138: SongMeta("All of This", "Shaimus", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440139: SongMeta("Callout", "The Acro-Brats", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440140: SongMeta("Spanish Castle Magic", "Jimi Hendrix (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440141: SongMeta("Eureka, I've Found Love", "The Upper Crust", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440142: SongMeta("Thunder Kiss 65", "White Zombie (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440143: SongMeta("Sharp Dressed Man", "ZZ Top (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440144: SongMeta("Story of My Love", "The Model Sons", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440145: SongMeta("Caveman Rejoice", "The Bags", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440146: SongMeta("Even Rats", "The Slip", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    440147: SongMeta("Take It Off", "The Donnas (WaveGroup)", "Guitar Hero 1", "gh1", 0, None, None, None, None, None, None, None, None, None,),
#GH1 Hidden Songs
#Hidden on disc. Usually only accessible in-game with cheating. Made optional for purity.
    1440148: SongMeta("Trippolette", "Andraleia Buch", "GH1 Hidden Songs", "gh1", 0, None, None, None, None, None, None, None, None, None,),
    1440149: SongMeta("Graveyard Shift", "Gurney", "GH1 Hidden Songs", "gh1", 0, None, None, None, None, None, None, None, None, None,),
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
    
    