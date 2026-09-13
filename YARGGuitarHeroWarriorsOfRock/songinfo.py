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
#Guitar Hero Warriors Of Rock
#4406
    420601: SongMeta("No More Mr. Nice Guy", "Alice Cooper", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420602: SongMeta("Ties That Bind", "Alter Bridge", "Guitar Hero Warriors of Rock", "ghwor", 5, 4, 5, None, None, None, 0, None, None, None),
    420603: SongMeta("I Know What I Am", "Band of Skulls", "Guitar Hero Warriors of Rock", "ghwor", 1, 0, 1, None, None, None, 0, None, None, None),
    420604: SongMeta("Cryin'", "Aerosmith", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 1, None, None, None, 0, None, None, None),
    420605: SongMeta("Fortunate Son", "Creedence Clearwater Revival", "Guitar Hero Warriors of Rock", "ghwor", 1, 1, 1, None, None, None, 0, None, None, None),
    420606: SongMeta("Dancing Through Sunday", "AFI", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 4, None, None, None, 0, None, None, None),
    420607: SongMeta("Re-Ignition (Live)", "Bad Brains", "Guitar Hero Warriors of Rock", "ghwor", 3, 3, 3, None, None, None, 0, None, None, None),
    420608: SongMeta("Free Ride", "Edgar Winter", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 2, None, None, None, 0, None, None, None),
    420609: SongMeta("The Feel Good Drag", "Anberlin", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 2, None, None, None, 0, None, None, None),
    420610: SongMeta("The Outsider", "A Perfect Circle", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 3, None, None, None, 0, None, None, None),
    420611: SongMeta("Tones of Home", "Blind Melon", "Guitar Hero Warriors of Rock", "ghwor", 3, 3, 4, None, None, None, 0, None, None, None),
    420612: SongMeta("Children of the Grave", "Black Sabbath", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 4, None, None, None, 0, None, None, None),
    420613: SongMeta("Burnin' for You", "Blue Oyster Cult", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 1, None, None, None, 0, None, None, None),
    420614: SongMeta("If You Want Peace... Prepare for War", "Children of Bodom", "Guitar Hero Warriors of Rock", "ghwor", 6, 6, 5, None, None, None, None, None, None, None),
    420615: SongMeta("Indians", "Anthrax", "Guitar Hero Warriors of Rock", "ghwor", 5, 4, 5, None, None, None, 0, None, None, None),
    420616: SongMeta("What Do I Get?", "Buzzcocks", "Guitar Hero Warriors of Rock", "ghwor", 1, 2, 3, None, None, None, 0, None, None, None),
    420617: SongMeta("Ravenous", "Atreyu", "Guitar Hero Warriors of Rock", "ghwor", 5, 3, 4, None, None, None, 0, None, None, None),
    420618: SongMeta("Bat Country", "Avenged Sevenfold", "Guitar Hero Warriors of Rock", "ghwor", 5, 3, 6, None, None, None, 0, None, None, None),
    420619: SongMeta("Been Caught Stealing", "Jane's Addiction", "Guitar Hero Warriors of Rock", "ghwor", 3, 3, 3, None, None, None, 0, None, None, None),
    420620: SongMeta("Move It On Over (Live)", "George Thorogood & The Destroyers", "Guitar Hero Warriors of Rock", "ghwor", 4, 4, 5, None, None, None, 0, None, None, None),
    420621: SongMeta("This Day We Fight!", "Megadeth", "Guitar Hero Warriors of Rock", "ghwor", 6, 6, 5, None, None, None, 0, None, None, None),
    420622: SongMeta("Bloodlines", "Dethklok", "Guitar Hero Warriors of Rock", "ghwor", 3, 1, 6, None, None, None, None, None, None, None),
    420623: SongMeta("Slow Hands", "Interpol", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420624: SongMeta("Paranoid (Live)", "Metallica & Ozzy Osbourne", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 1, None, None, None, 0, None, None, None),
    420625: SongMeta("No Way Back", "Foo Fighters", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420626: SongMeta("Bleed It Out", "Linkin Park", "Guitar Hero Warriors of Rock", "ghwor", 1, 1, 1, None, None, None, 0, None, None, None),
    420627: SongMeta("Sudden Death", "Megadeth", "Guitar Hero Warriors of Rock", "ghwor", 6, 3, 5, None, None, None, 0, None, None, None),
    420628: SongMeta("Suffocated", "Orianthi", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 3, None, None, None, 0, None, None, None),
    420629: SongMeta("Bodies", "Drowning Pool", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 2, None, None, None, 0, None, None, None),
    420630: SongMeta("Money for Nothing", "Dire Straits", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 2, None, None, None, 0, None, None, None),
    420631: SongMeta("Dance, Dance", "Fall Out Boy", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420632: SongMeta("Hard to See", "Five Finger Death Punch", "Guitar Hero Warriors of Rock", "ghwor", 3, 3, 3, None, None, None, 0, None, None, None),
    420633: SongMeta("Feels Like the First Time", "Foreigner", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 1, None, None, None, 0, None, None, None),
    420634: SongMeta("Again", "Flyleaf", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 2, None, None, None, 0, None, None, None),
    420635: SongMeta("How You Remind Me", "Nickelback", "Guitar Hero Warriors of Rock", "ghwor", 1, 1, 1, None, None, None, 0, None, None, None),
    420636: SongMeta("Nemesis", "Arch Enemy", "Guitar Hero Warriors of Rock", "ghwor", 6, 5, 5, None, None, None, None, None, None, None),
    420637: SongMeta("Lunatic Fringe", "Red Rider", "Guitar Hero Warriors of Rock", "ghwor", 1, 1, 2, None, None, None, 0, None, None, None),
    420638: SongMeta("Savior", "Rise Against", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 4, None, None, None, 0, None, None, None),
    420639: SongMeta("Burn", "Deep Purple", "Guitar Hero Warriors of Rock", "ghwor", 5, 3, 4, None, None, None, 0, None, None, None),
    420640: SongMeta("Lasso", "Phoenix", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420641: SongMeta("Unskinny Bop", "Poison", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 4, None, None, None, 0, None, None, None),
    420642: SongMeta("Bohemian Rhapsody", "Queen", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 1, None, None, None, 0, None, None, None),
    420643: SongMeta("Wish", "Nine Inch Nails", "Guitar Hero Warriors of Rock", "ghwor", 2, 0, 2, None, None, None, 0, None, None, None),
    420644: SongMeta("Uprising", "Muse", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420645: SongMeta("I'm Broken", "Pantera", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 2, None, None, None, 0, None, None, None),
    420646: SongMeta("(You Can Still) Rock in America", "Night Ranger", "Guitar Hero Warriors of Rock", "ghwor", 4, 2, 2, None, None, None, 0, None, None, None),
    420647: SongMeta("Waidmanns Heil", "Rammstein", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420648: SongMeta("Pour Some Sugar on Me (Live)", "Def Leppard", "Guitar Hero Warriors of Rock", "ghwor", 2, 0, 2, None, None, None, 0, None, None, None),
    420649: SongMeta("Machinehead", "Bush", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 2, None, None, None, 0, None, None, None),
    420650: SongMeta("Black Widow of La Porte", "John 5 featuring Jim Root", "Guitar Hero Warriors of Rock", "ghwor", 6, 4, 4, None, None, None, None, None, None, None),
    420651: SongMeta("Holy Wars... The Punishment Due", "Megadeth", "Guitar Hero Warriors of Rock", "ghwor", 6, 6, 5, None, None, None, 0, None, None, None),
    420652: SongMeta("2112 Pt. 3 - Discovery", "Rush", "Guitar Hero Warriors of Rock", "ghwor", 2, 0, None, None, None, None, 0, None, None, None),
    420653: SongMeta("I'm Not Okay (I Promise)", "My Chemical Romance", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420654: SongMeta("2112 Pt. 2 - The Temples of Syrinx", "Rush", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420655: SongMeta("2112 Pt. 1 - Overture", "Rush", "Guitar Hero Warriors of Rock", "ghwor", 3, 3, 3, None, None, None, 0, None, None, None),
    420656: SongMeta("2112 Pt. 4 - Presentation", "Rush", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 4, None, None, None, 0, None, None, None),
    420657: SongMeta("Fury of the Storm", "DragonForce", "Guitar Hero Warriors of Rock", "ghwor", 6, 6, 6, None, None, None, 0, None, None, None),
    420658: SongMeta("Call Me the Breeze (Live)", "Lynyrd Skynyrd", "Guitar Hero Warriors of Rock", "ghwor", 5, 2, 3, None, None, None, 0, None, None, None),
    420659: SongMeta("2112 Pt. 5 - Oracle: The Dream", "Rush", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 2, None, None, None, 0, None, None, None),
    420660: SongMeta("It's Only Another Parsec...", "RX Bandits", "Guitar Hero Warriors of Rock", "ghwor", 4, 3, 5, None, None, None, 0, None, None, None),
    420661: SongMeta("Jet City Woman", "Queensrÿche", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420662: SongMeta("Rockin' in the Free World", "Neil Young", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 1, None, None, None, 0, None, None, None),
    420663: SongMeta("Stray Cat Blues", "The Rolling Stones", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 1, None, None, None, 0, None, None, None),
    420664: SongMeta("2112 Pt. 6 - Soliloquy", "Rush", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 1, None, None, None, 0, None, None, None),
    420665: SongMeta("Aqualung", "Jethro Tull", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 3, None, None, None, 0, None, None, None),
    420666: SongMeta("Love Gun", "Kiss", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 1, None, None, None, 0, None, None, None),
    420667: SongMeta("Sharp Dressed Man (Live)", "ZZ Top", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 2, None, None, None, 0, None, None, None),
    420668: SongMeta("Listen to Her Heart", "Tom Petty & The Heartbreakers", "Guitar Hero Warriors of Rock", "ghwor", 1, 1, 1, None, None, None, 0, None, None, None),
    420669: SongMeta("Sudden Death (Career Version)", "Megadeth", "Guitar Hero Warriors of Rock", "ghwor", 6, 3, 5, None, None, None, 0, None, None, None),
    420670: SongMeta("2112 Pt. 7 - Grand Finale", "Rush", "Guitar Hero Warriors of Rock", "ghwor", 4, 3, 5, None, None, None, None, None, None, None),
    420671: SongMeta("Ghost", "Slash ft Ian Astbury", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 2, None, None, None, 0, None, None, None),
    420672: SongMeta("Psychosocial", "Slipknot", "Guitar Hero Warriors of Rock", "ghwor", 4, 3, 4, None, None, None, 0, None, None, None),
    420673: SongMeta("Losing My Religion", "R.E.M.", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 1, None, None, None, 0, None, None, None),
    420674: SongMeta("Cherry Bomb", "The Runaways", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 2, None, None, None, 0, None, None, None),
    420675: SongMeta("There's No Secrets This Year", "Silversun Pickups", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420676: SongMeta("Self Esteem", "The Offspring", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420677: SongMeta("Tick Tick Boom", "The Hives", "Guitar Hero Warriors of Rock", "ghwor", 2, 1, 3, None, None, None, 0, None, None, None),
    420678: SongMeta("Theme from Spiderman", "The Ramones", "Guitar Hero Warriors of Rock", "ghwor", 1, 2, 3, None, None, None, 0, None, None, None),
    420679: SongMeta("Interstate Love Song", "Stone Temple Pilots", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 1, None, None, None, 0, None, None, None),
    420680: SongMeta("Black Rain", "Soundgarden", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420681: SongMeta("Setting Fire to Sleeping Giants", "The Dillinger Escape Plan", "Guitar Hero Warriors of Rock", "ghwor", 5, 2, 5, None, None, None, 0, None, None, None),
    420682: SongMeta("Renegade", "Styx", "Guitar Hero Warriors of Rock", "ghwor", 3, 1, 3, None, None, None, 0, None, None, None),
    420683: SongMeta("Calling", "Strung Out", "Guitar Hero Warriors of Rock", "ghwor", 6, 2, 5, None, None, None, 0, None, None, None),
    420684: SongMeta("Modern Day Cowboy", "Tesla", "Guitar Hero Warriors of Rock", "ghwor", 3, 1, 3, None, None, None, 0, None, None, None),
    420685: SongMeta("Seven Nation Army", "The White Stripes", "Guitar Hero Warriors of Rock", "ghwor", 1, 1, 0, None, None, None, 0, None, None, None),
    420686: SongMeta("Scumbag Blues", "Them Crooked Vultures", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420687: SongMeta("We're Not Gonna Take It", "Twisted Sister", "Guitar Hero Warriors of Rock", "ghwor", 1, 2, 3, None, None, None, 0, None, None, None),
    420688: SongMeta("Graduate", "Third Eye Blind", "Guitar Hero Warriors of Rock", "ghwor", 3, 2, 2, None, None, None, 0, None, None, None),
    420689: SongMeta("Deadfall", "Snot", "Guitar Hero Warriors of Rock", "ghwor", 6, 6, 6, None, None, None, None, None, None, None),
    420690: SongMeta("Motivation", "Sum 41", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 3, None, None, None, 0, None, None, None),
    420691: SongMeta("Chemical Warfare", "Slayer", "Guitar Hero Warriors of Rock", "ghwor", 6, 6, 6, None, None, None, 0, None, None, None),
    420692: SongMeta("Fascination Street", "The Cure", "Guitar Hero Warriors of Rock", "ghwor", 1, 1, 3, None, None, None, 0, None, None, None),
    420693: SongMeta("Get Free", "The Vines", "Guitar Hero Warriors of Rock", "ghwor", 2, 2, 2, None, None, None, 0, None, None, None),
    420694: SongMeta("Speeding (Vault Version)", "Steve Vai", "Guitar Hero Warriors of Rock", "ghwor", 6, 5, 5, None, None, None, None, None, None, None),
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
    
    