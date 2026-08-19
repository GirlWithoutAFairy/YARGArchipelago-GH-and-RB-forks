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

Songs: Dict[int, SongMeta] = {
#Band Hero
#4424
    442401: SongMeta("Like Whoa", "Aly & AJ", "Band Hero", "bh", 2, 2, 3, None, None, None, 4, None, None, None),
    442402: SongMeta("When I'm Gone", "3 Doors Down", "Band Hero", "bh", 2, 2, 2, None, None, None, 3, None, None, None),
    442403: SongMeta("Put Your Records On", "Corinne Bailey Rae", "Band Hero", "bh", 2, 2, 1, None, None, None, 5, None, None, None),
    442404: SongMeta("Kung Fu Fighting", "Carl Douglas", "Band Hero", "bh", 3, 2, 2, None, None, None, 4, None, None, None),
    442405: SongMeta("Steal My Kisses", "Ben Harper and the Innocent Criminals", "Band Hero", "bh", 1, 3, 2, None, None, None, 4, None, None, None),
    442406: SongMeta("Hang Me Up to Dry", "Cold War Kids", "Band Hero", "bh", 1, 1, 1, None, None, None, 1, None, None, None),
    442407: SongMeta("Fascination", "Alphabeat", "Band Hero", "bh", 2, 2, 3, None, None, None, 3, None, None, None),
    442408: SongMeta("I Want You to Want Me (Live)", "Cheap Trick", "Band Hero", "bh", 3, 2, 1, None, None, None, 2, None, None, None),
    442409: SongMeta("The Adventure", "Angels & Airwaves", "Band Hero", "bh", 3, 2, 4, None, None, None, 2, None, None, None),
    442410: SongMeta("In a Big Country", "Big Country", "Band Hero", "bh", 2, 3, 1, None, None, None, 3, None, None, None),
    442411: SongMeta("Whip It", "Devo", "Band Hero", "bh", 2, 2, 3, None, None, None, 2, None, None, None),
    442412: SongMeta("Do You Really Want to Hurt Me", "Culture Club", "Band Hero", "bh", 1, 2, 1, None, None, None, 1, None, None, None),
    442413: SongMeta("Warwick Avenue", "Duffy", "Band Hero", "bh", 2, 2, 2, None, None, None, 4, None, None, None),
    442414: SongMeta("Hands Down", "Dashboard Confessional", "Band Hero", "bh", 2, 2, 4, None, None, None, 3, None, None, None),
    442415: SongMeta("Let's Dance", "David Bowie", "Band Hero", "bh", 1, 1, 1, None, None, None, 3, None, None, None),
    442416: SongMeta("Angels of the Silences", "Counting Crows", "Band Hero", "bh", 2, 2, 2, None, None, None, 3, None, None, None),
    442417: SongMeta("Our Lips Are Sealed", "Go-Go's", "Band Hero", "bh", 2, 2, 2, None, None, None, 3, None, None, None),
    442418: SongMeta("Paralyzer", "Finger Eleven", "Band Hero", "bh", 3, 1, 3, None, None, None, 2, None, None, None),
    442419: SongMeta("So Yesterday", "Hilary Duff", "Band Hero", "bh", 2, 1, 2, None, None, None, 2, None, None, None),
    442420: SongMeta("ABC", "Jackson 5", "Band Hero", "bh", 1, 1, 1, None, None, None, 6, None, None, None),
    442421: SongMeta("Rio", "Duran Duran", "Band Hero", "bh", 2, 3, 4, None, None, None, 4, None, None, None),
    442422: SongMeta("Lips of an Angel", "Hinder", "Band Hero", "bh", 2, 2, 2, None, None, None, 2, None, None, None),
    442423: SongMeta("Black Horse and the Cherry Tree", "KT Tunstall", "Band Hero", "bh", 3, 1, 3, None, None, None, 3, None, None, None),
    442424: SongMeta("Beautiful Soul", "Jesse McCartney", "Band Hero", "bh", 2, 1, 2, None, None, None, 4, None, None, None),
    442425: SongMeta("Bad Reputation", "Joan Jett", "Band Hero", "bh", 2, 2, 3, None, None, None, 3, None, None, None),
    442426: SongMeta("Black Cat", "Janet Jackson", "Band Hero", "bh", 2, 2, 1, None, None, None, 3, None, None, None),
    442427: SongMeta("You Had Me", "Joss Stone", "Band Hero", "bh", 3, 2, 1, None, None, None, 4, None, None, None),
    442428: SongMeta("Take What You Take", "Lily Allen", "Band Hero", "bh", 1, 2, 3, None, None, None, 3, None, None, None),
    442429: SongMeta("I Heard It Through the Grapevine", "Marvin Gaye", "Band Hero", "bh", 1, 1, 2, None, None, None, 3, None, None, None),
    442430: SongMeta("Take a Picture", "Filter", "Band Hero", "bh", 3, 3, 2, None, None, None, 2, None, None, None),
    442431: SongMeta("Walking on Sunshine", "Katrina and the Waves", "Band Hero", "bh", 2, 2, 2, None, None, None, 4, None, None, None),
    442432: SongMeta("American Pie", "Don McLean", "Band Hero", "bh", 2, 2, 1, None, None, None, 5, None, None, None),
    442433: SongMeta("Every Rose Has Its Thorn", "Poison", "Band Hero", "bh", 2, 1, 1, None, None, None, 3, None, None, None),
    442434: SongMeta("Turn Off the Light", "Nelly Furtado", "Band Hero", "bh", 2, 2, 1, None, None, None, 5, None, None, None),
    442435: SongMeta("Bring Me to Life", "Evanescence", "Band Hero", "bh", 2, 2, 3, None, None, None, 2, None, None, None),
    442436: SongMeta("Don't Speak", "No Doubt", "Band Hero", "bh", 2, 2, 2, None, None, None, 2, None, None, None),
    442437: SongMeta("Oh Pretty Woman", "Roy Orbison", "Band Hero", "bh", 2, 2, 1, None, None, None, 3, None, None, None),
    442438: SongMeta("Rock Star", "N*E*R*D", "Band Hero", "bh", 2, 3, 3, None, None, None, 3, None, None, None),
    442439: SongMeta("Just a Girl", "No Doubt", "Band Hero", "bh", 2, 2, 2, None, None, None, 3, None, None, None),
    442440: SongMeta("Lifeline", "Papa Roach", "Band Hero", "bh", 3, 2, 2, None, None, None, 3, None, None, None),
    442441: SongMeta("She Will Be Loved", "Maroon 5", "Band Hero", "bh", 1, 1, 3, None, None, None, 1, None, None, None),
    442442: SongMeta("Love is a Battlefield", "Pat Benatar", "Band Hero", "bh", 3, 2, 1, None, None, None, 3, None, None, None),
    442443: SongMeta("Kids", "Robbie Williams and Kylie Minogue", "Band Hero", "bh", 2, 2, 2, None, None, None, 6, None, None, None),
    442444: SongMeta("Love Story", "Taylor Swift", "Band Hero", "bh", 2, 1, 2, None, None, None, 3, None, None, None),
    442445: SongMeta("A Million Ways", "OK Go", "Band Hero", "bh", 2, 2, 2, None, None, None, 2, None, None, None),
    442446: SongMeta("Take Back the City", "Snow Patrol", "Band Hero", "bh", 2, 2, 3, None, None, None, 2, None, None, None),
    442447: SongMeta("Mr. Roboto", "Styx", "Band Hero", "bh", 2, 2, 3, None, None, None, 3, None, None, None),
    442448: SongMeta("Santa Monica", "Everclear", "Band Hero", "bh", 2, 1, 2, None, None, None, 4, None, None, None),
    442449: SongMeta("Pictures of You", "The Last Goodnight", "Band Hero", "bh", 2, 1, 3, None, None, None, 3, None, None, None),
    442450: SongMeta("Honky Tonk Women", "The Rolling Stones", "Band Hero", "bh", 2, 1, 1, None, None, None, 4, None, None, None),
    442451: SongMeta("You Belong With Me", "Taylor Swift", "Band Hero", "bh", 2, 1, 2, None, None, None, 4, None, None, None),
    442452: SongMeta("Dirty Little Secret", "The All-American Rejects", "Band Hero", "bh", 2, 2, 2, None, None, None, 2, None, None, None),
    442453: SongMeta("Ocean Avenue", "Yellowcard", "Band Hero", "bh", 3, 3, 4, None, None, None, 5, None, None, None),
    442454: SongMeta("Back Again", "Paracute", "Band Hero", "bh", 2, 2, 2, None, None, None, 4, None, None, None),
    442455: SongMeta("L.E.S. Artistes", "Santigold", "Band Hero", "bh", 1, 1, 2, None, None, None, 3, None, None, None),
    442456: SongMeta("Naive", "The Kooks", "Band Hero", "bh", 3, 2, 3, None, None, None, 4, None, None, None),
    442457: SongMeta("If You Could Only See", "Tonic", "Band Hero", "bh", 2, 2, 2, None, None, None, 3, None, None, None),
    442458: SongMeta("Wannabe", "Spice Girls", "Band Hero", "bh", 1, 1, 1, None, None, None, 4, None, None, None),
    442459: SongMeta("Happy Together", "The Turtles", "Band Hero", "bh", 1, 1, 2, None, None, None, 3, None, None, None),
    442460: SongMeta("Picture to Burn", "Taylor Swift", "Band Hero", "bh", 3, 2, 2, None, None, None, 2, None, None, None),
    442461: SongMeta("Y.M.C.A.", "Village People", "Band Hero", "bh", 3, 3, 3, None, None, None, 3, None, None, None),
    442462: SongMeta("Sugar, We're Goin Down", "Fall Out Boy", "Band Hero", "bh", 2, 1, 3, None, None, None, 3, None, None, None),
    442463: SongMeta("Gasoline", "The Airborne Toxic Event", "Band Hero", "bh", 2, 2, 2, None, None, None, 4, None, None, None),
    442464: SongMeta("The Impression That I Get", "The Mighty Mighty Bosstones", "Band Hero", "bh", 3, 3, 3, None, None, None, 4, None, None, None),
    442465: SongMeta("Believe", "The Bravery", "Band Hero", "bh", 2, 2, 2, None, None, None, 2, None, None, None),
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
    
    