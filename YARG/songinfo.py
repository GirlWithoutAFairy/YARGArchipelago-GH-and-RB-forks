from typing import NamedTuple, Optional, Dict

class SongMeta(NamedTuple):
    """Contains difficulty information, Use None for unsupported intsruments"""

    guitar5F: Optional[int]
    bass5F: Optional[int]
    drums: Optional[int]
    drumsElite: Optional[int]
    keys5F: Optional[int]
    keysPro: Optional[int]
    vocals: Optional[int]
    harmony2: Optional[int]
    harmony3: Optional[int]

Songs: Dict[str, SongMeta] = {
    "106": SongMeta(5, 4, 4, 4, None, None, 2, 2, 2),
    "1nput This 2 Y0ur Spine": SongMeta(6, 4, 6, 6, 6, 6, 0, None, None),
    "322": SongMeta(4, 4, 5, None, 3, 3, 0, None, None),
    "A Visitant (feat. Victor Borba)": SongMeta(3, 1, 5, None, 6, 6, 4, 4, None),
    "About the Author": SongMeta(3, 2, 2, None, 1, 1, 5, 5, 5),
    "The Afterparty": SongMeta(3, 1, 2, None, 2, 3, 3, 3, 3),
    "Al Gore Rhythm": SongMeta(5, 4, 5, None, None, None, 5, 5, 5),
    "Alibi": SongMeta(3, 3, 6, None, 0, 0, 4, 4, 4),
    "All of a Sudden": SongMeta(3, 3, 4, None, 2, 3, 1, 1, None),
    "Allure": SongMeta(5, 5, 6, None, 0, 0, 2, 2, 2),
    "Avatar the Last Cakebender": SongMeta(4, 3, 5, None, 4, 4, 4, 4, 4),
    "Avatara": SongMeta(2, 2, 4, 4, 2, 2, 0, 0, None),
    "Bathe in Blood": SongMeta(6, 2, 6, None, None, None, 0, None, None),
    "Bedroom Community": SongMeta(3, 3, 3, 3, 5, 5, 3, 3, 3),
    "Beverly": SongMeta(2, 2, 2, None, None, None, 2, 2, 2),
    "Blue (feat. Miori Celesta)": SongMeta(3, 5, 4, None, 5, 5, 5, 5, 5),
    "Boom Slayer (feat. Scott Foster Harris)": SongMeta(3, 3, 4, None, 2, 2, 3, 3, None),
    "Bottleneck": SongMeta(5, 5, 5, None, None, None, 3, 3, None),
    "Buds": SongMeta(2, 1, 2, None, None, None, 2, 2, 2),
    "Butterflies": SongMeta(3, 3, 4, 4, None, None, 1, 1, 1),
    "Choked Up": SongMeta(3, 1, 2, 2, 3, 4, 4, 4, 4),
    "Circles": SongMeta(3, 3, 3, None, 0, 0, 3, 3, 3),
    "Cowboy Tanaka": SongMeta(4, 3, 5, None, 5, 5, 4, 4, 4),
    "Cruisin'": SongMeta(5, 3, 4, None, 3, 3, None, None, None),
    "Discipline": SongMeta(3, 2, 2, 2, 2, 2, 3, 3, 3),
    "Do": SongMeta(3, 4, 5, None, 4, 4, 6, 6, None),
    "Don't Look!": SongMeta(2, 3, 4, None, 6, 6, 1, 1, 1),
    "Don't Spook the Owl": SongMeta(3, 3, 4, None, None, None, 4, 4, 4),
    "Dreamweaver": SongMeta(3, 3, 4, 4, None, None, 0, 0, 0),
    "Duvet Thief": SongMeta(2, 2, 4, None, 1, 2, 3, 3, 3),
    "Eleven": SongMeta(2, 2, 3, None, 0, 0, 2, 2, 2),
    "Emperor Rising": SongMeta(5, 5, 6, None, None, None, 4, 4, 4),
    "Empires": SongMeta(2, 1, 4, None, 4, 4, 4, 4, 4),
    "Everybody Do the Flop": SongMeta(4, 3, 5, None, 4, 4, 5, 5, 5),
    "Exeter": SongMeta(3, 4, 4, None, 0, 0, 2, 2, 2),
    "Fine": SongMeta(4, 2, 4, 4, 2, 2, 4, 4, 4),
    "Flight of the Bumblebee": SongMeta(6, 3, 6, None, None, None, None, None, None),
    "Formless Collective": SongMeta(6, 5, 8, None, None, None, 0, 0, 0),
    "Frank Scored a Video Game": SongMeta(6, 5, 5, None, None, None, None, None, None),
    "Front Row Seats (To Watching Your World Burn)": SongMeta(2, 2, 5, None, 1, 1, 3, 3, 3),
    "The Game": SongMeta(4, 2, 4, 4, 2, 2, 3, 3, 3),
    "God Only Knows (feat. Kasane Teto)": SongMeta(5, 5, 5, None, 4, 4, 3, 3, 3),
    "Guess I'll Never Know": SongMeta(1, 0, 3, None, 0, 0, 2, 2, 2),
    "Half Measures": SongMeta(0, 0, 1, None, 0, 1, 6, 6, 6),
    "I Don't Wanna Talk": SongMeta(3, 3, 3, None, 2, 2, 2, 2, 2),
    "I Wish That I Could Fall (feat. GUMI)": SongMeta(3, 5, 1, None, 5, 5, 5, 5, 5),
    "I'm a Bug": SongMeta(1, 1, 3, None, 5, 5, 2, 2, 2),
    "Igowallah": SongMeta(0, 2, 5, None, 0, 0, 4, 4, 4),
    "In My Head": SongMeta(1, 1, 2, None, None, None, 2, 2, 2),
    "Is This What You Wanted": SongMeta(4, 1, 2, None, 2, 2, 5, 5, 5),
    "It Kills Me": SongMeta(2, 2, 4, None, 1, 2, 3, 3, 3),
    "Jenny B": SongMeta(7, 4, 2, 2, None, None, 5, None, None),
    "John, Take Me with You": SongMeta(2, 2, 2, None, None, None, 2, 2, 2),
    "Join the Club": SongMeta(3, 2, 2, None, 3, 3, 3, 3, 3),
    "Languish": SongMeta(4, 3, 5, 5, 2, 2, 0, 0, 0),
    "Long in the Tooth": SongMeta(5, 3, 5, 5, 3, 3, 2, 2, 2),
    "Luminaire": SongMeta(3, 3, 7, None, 5, 5, None, None, None),
    "Marlboro Mountain": SongMeta(3, 3, 3, None, 0, 0, 3, 3, 3),
    "The Masquerade": SongMeta(4, 4, 4, None, 5, 5, 2, 2, 2),
    "Mass Gap": SongMeta(6, 6, 6, None, 6, 7, None, None, None),
    "Moonlight Sonata 3rd Mvt (Big Band Version)": SongMeta(3, 5, 7, None, 6, 6, None, None, None),
    "Need 2": SongMeta(3, 0, 0, None, 2, 2, 1, 1, 1),
    "The New World Disorder": SongMeta(7, 7, 6, 6, None, None, 3, 3, 3),
    "No Nations": SongMeta(0, 1, 0, None, 0, 0, 1, 1, 1),
    "No Remedy": SongMeta(1, 1, 3, None, 3, 3, 2, 2, 2),
    "Nomu": SongMeta(3, 2, 3, None, None, None, 5, 5, 5),
    "Numb the Mind": SongMeta(1, 0, 2, None, 0, 0, 2, None, None),
    "Oh, Krissy Baby!": SongMeta(3, 2, 2, None, 3, 3, 4, 4, 4),
    "Oopsie Daisy": SongMeta(1, 3, 2, None, 2, 2, 3, 3, 3),
    "Over Again": SongMeta(2, 1, 2, None, 1, 1, 5, 5, 5),
    "Overdrive": SongMeta(3, 2, 3, None, None, None, 3, None, None),
    "Oxygen": SongMeta(2, 1, 2, None, 2, 2, 2, 2, 2),
    "Participation Trophy Wife": SongMeta(4, 3, 3, None, None, None, 3, 3, None),
    "Pixel Galaxy": SongMeta(6, 2, 4, None, 3, 3, None, None, None),
    "Pizza Rolls": SongMeta(5, 1, 2, 2, None, None, 2, 2, 2),
    "Plastic Boogie": SongMeta(3, 3, 1, None, 1, 1, 2, 2, 2),
    "Poser": SongMeta(4, 3, 3, None, None, None, 4, 4, 4),
    "Positively Clark Street": SongMeta(4, 2, 2, None, 2, 2, 4, 4, 4),
    "Queen of the Night": SongMeta(3, 4, 3, None, 3, 3, 4, 4, 4),
    "Runnin Man": SongMeta(3, 3, 5, 5, None, None, 0, 0, 0),
    "Sadness (feat. Sapphire Noel)": SongMeta(2, 2, 5, None, 2, 2, 2, 2, None),
    "Seasons (feat. Shiki Miyoshino)": SongMeta(2, 1, 0, None, 1, 2, 3, 3, None),
    "Show Ya": SongMeta(2, 0, 2, None, 2, 2, 3, 3, 3),
    "Smile for Me": SongMeta(4, 2, 4, None, None, None, 3, 3, 3),
    "Song of November": SongMeta(4, 4, 4, None, 1, 1, 3, 3, 3),
    "Spirit": SongMeta(2, 1, 1, None, 2, 2, 3, 3, 3),
    "Splinter": SongMeta(2, 0, 1, None, 2, 3, 3, 3, 3),
    "Stowaway Ants": SongMeta(3, 2, 4, None, 4, 4, 3, 3, 3),
    "Strangers Once Again (feat. Treb and Ofir Tabakov)": SongMeta(4, 3, 6, None, 4, 6, 5, 5, 5),
    "Sweet Victory": SongMeta(3, 1, 2, None, 3, 3, 3, 3, 3),
    "Synthespian": SongMeta(5, 5, 6, None, None, None, 2, 2, None),
    "They Call": SongMeta(4, 4, 4, None, None, None, 2, 2, 2),
    "Time": SongMeta(3, 2, 4, 4, 0, 0, 3, 3, 3),
    "To Let Go": SongMeta(3, 3, 4, None, 1, 1, 4, 4, 4),
    "Vehemence": SongMeta(6, 4, 6, None, None, None, None, None, None),
    "Voidwalker": SongMeta(4, 3, 5, None, 0, 0, 0, 0, 0),
    "We All Float Down Here": SongMeta(6, 4, 5, None, None, None, 2, 2, None)
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
    
    