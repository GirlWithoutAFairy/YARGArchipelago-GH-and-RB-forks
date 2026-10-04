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
#72 represents RB (Rock Band) in T9 Notation
#YY
#03 represents third entry (Green Day Rock Band)
#ZZ represents unique song identifier (incremental)

Songs: Dict[int, SongMeta] = {
#Green Day Rock Band
#7243
    724301: SongMeta("Brain Stew/Jaded", "Green Day", "Green Day Rock Band", "gdrb", 4, 4, 0, None, None, None, 3, 3, None, None),
    724302: SongMeta("Geek Stink Breath", "Green Day", "Green Day Rock Band", "gdrb", 3, 3, 4, None, None, None, 3, 3, None, None),
    724303: SongMeta("Good Riddance (Time of Your Life)", "Green Day", "Green Day Rock Band", "gdrb", 4, 2, None, None, None, None, 2, None, None, None),
    724304: SongMeta("Pulling Teeth", "Green Day", "Green Day Rock Band", "gdrb", 1, 1, 2, None, None, None, 3, 3, None, None),
    724305: SongMeta("Letterbomb", "Green Day", "Green Day Rock Band", "gdrb", 4, 3, 4, None, None, None, 4, 4, None, None),
    724306: SongMeta("Restless Heart Syndrome", "Green Day", "Green Day Rock Band", "gdrb", 2, 1, 2, None, None, None, 2, 2, 2, None),
    724307: SongMeta("Minority", "Green Day", "Green Day Rock Band", "gdrb", 3, 2, 3, None, None, None, 1, 1, 1, None),
    724308: SongMeta("Welcome to Paradise", "Green Day", "Green Day Rock Band", "gdrb", 4, 4, 5, None, None, None, 2, 2, 2, None),
    724309: SongMeta("Before the Lobotomy", "Green Day", "Green Day Rock Band", "gdrb", 2, 1, 4, None, None, None, 3, 3, 3, None),
    724310: SongMeta("Homecoming", "Green Day", "Green Day Rock Band", "gdrb", 4, 4, 5, None, None, None, 4, 4, 4, None),
    724311: SongMeta("Peacemaker", "Green Day", "Green Day Rock Band", "gdrb", 2, 3, 5, None, None, None, 3, 3, 3, None),
    724312: SongMeta("Having a Blast", "Green Day", "Green Day Rock Band", "gdrb", 3, 3, 4, None, None, None, 4, 4, None, None),
    724313: SongMeta("Last Night on Earth", "Green Day", "Green Day Rock Band", "gdrb", 0, 0, 0, None, None, None, 1, 1, None, None),
    724314: SongMeta("Emenius Sleepus", "Green Day", "Green Day Rock Band", "gdrb", 3, 3, 5, None, None, None, 2, 2, None, None),
    724315: SongMeta("Boulevard of Broken Dreams", "Green Day", "Green Day Rock Band", "gdrb", 2, 1, 0, None, None, None, 1, 1, None, None),
    724316: SongMeta("Are We the Waiting/St. Jimmy", "Green Day", "Green Day Rock Band", "gdrb", 4, 4, 5, None, None, None, 3, 3, 3, None),
    724317: SongMeta("F.O.D.", "Green Day", "Green Day Rock Band", "gdrb", 3, 1, 4, None, None, None, 3, 3, None, None),
    724318: SongMeta("Nice Guys Finish Last", "Green Day", "Green Day Rock Band", "gdrb", 2, 3, 4, None, None, None, 2, 2, None, None),
    724319: SongMeta("Horseshoes and Handgrenades", "Green Day", "Green Day Rock Band", "gdrb", 3, 2, 3, None, None, None, 2, 2, None, None),
    724320: SongMeta("In the End", "Green Day", "Green Day Rock Band", "gdrb", 4, 1, 5, None, None, None, 4, 4, None, None),
    724321: SongMeta("Murder City", "Green Day", "Green Day Rock Band", "gdrb", 2, 2, 4, None, None, None, 3, 3, None, None),
    724322: SongMeta("Burnout", "Green Day", "Green Day Rock Band", "gdrb", 3, 3, 5, None, None, None, 2, 2, 2, None),
    724323: SongMeta("Longview", "Green Day", "Green Day Rock Band", "gdrb", 3, 3, 4, None, None, None, 3, 3, None, None),
    724324: SongMeta("Basket Case", "Green Day", "Green Day Rock Band", "gdrb", 4, 3, 4, None, None, None, 1, 1, None, None),
    724325: SongMeta("Extraordinary Girl", "Green Day", "Green Day Rock Band", "gdrb", 1, 1, 2, None, None, None, 2, 2, None, None),
    724326: SongMeta("Chump", "Green Day", "Green Day Rock Band", "gdrb", 4, 4, 5, None, None, None, 3, 3, None, None),
    724327: SongMeta("Give Me Novacaine/She's a Rebel", "Green Day", "Green Day Rock Band", "gdrb", 3, 2, 3, None, None, None, 3, 3, None, None),
    724328: SongMeta("American Eulogy", "Green Day", "Green Day Rock Band", "gdrb", 2, 2, 4, None, None, None, 3, 3, 3, None),
    724329: SongMeta("Holiday", "Green Day", "Green Day Rock Band", "gdrb", 2, 1, 4, None, None, None, 3, 3, 3, None),
    724330: SongMeta("Hitchin' a Ride", "Green Day", "Green Day Rock Band", "gdrb", 4, 3, 4, None, None, None, 3, 3, None, None),
    724331: SongMeta("21st Century Breakdown", "Green Day", "Green Day Rock Band", "gdrb", 4, 3, 5, None, None, None, 3, 3, 3, None),
    724332: SongMeta("American Idiot", "Green Day", "Green Day Rock Band", "gdrb", 2, 2, 4, None, None, None, 3, None, None, None),
    724333: SongMeta("Song of the Century", "Green Day", "Green Day Rock Band", "gdrb", None, None, None, None, None, None, 0, None, None, None),
    724334: SongMeta("Jesus of Suburbia", "Green Day", "Green Day Rock Band", "gdrb", 4, 3, 4, None, None, None, 4, 4, 4, None),
    724335: SongMeta("Sassafrass Roots", "Green Day", "Green Day Rock Band", "gdrb", 2, 3, 4, None, None, None, 1, 1, None, None),
    724336: SongMeta("Wake Me Up When September Ends", "Green Day", "Green Day Rock Band", "gdrb", 1, 1, 1, None, None, None, 1, None, None, None),
    724337: SongMeta("See the Light", "Green Day", "Green Day Rock Band", "gdrb", 2, 2, 4, None, None, None, 1, 1, None, None),
    724338: SongMeta("Whatsername", "Green Day", "Green Day Rock Band", "gdrb", 2, 2, 1, None, None, None, 2, 2, 2, None),
    724339: SongMeta("She", "Green Day", "Green Day Rock Band", "gdrb", 3, 3, 4, None, None, None, 2, 2, None, None),
    724340: SongMeta("When I Come Around", "Green Day", "Green Day Rock Band", "gdrb", 1, 3, 3, None, None, None, 3, 3, None, None),
    724341: SongMeta("The Static Age", "Green Day", "Green Day Rock Band", "gdrb", 3, 2, 4, None, None, None, 2, 2, 2, None),
    724342: SongMeta("¿Viva la Gloria? (Little Girl)", "Green Day", "Green Day Rock Band", "gdrb", 1, 1, 2, None, None, None, 3, 3, 3, None),
    724343: SongMeta("Warning", "Green Day", "Green Day Rock Band", "gdrb", 0, 1, 2, None, None, None, 1, 1, None, None),
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
    
    