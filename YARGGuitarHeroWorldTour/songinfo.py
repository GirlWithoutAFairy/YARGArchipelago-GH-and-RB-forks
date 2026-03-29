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
#Guitar Hero World Tour
#4404
    440401: SongMeta("Good God", "Anouk", "Guitar Hero World Tour", "ghwt", 3, 1, 1, None, None, None, 5, None, None, None,),
    440402: SongMeta("The Kill", "30 Seconds to Mars", "Guitar Hero World Tour", "ghwt", 3, 2, 4, None, None, None, 3, None, None, None,),
    440403: SongMeta("One Armed Scissor", "At the Drive-In", "Guitar Hero World Tour", "ghwt", 2, 2, 4, None, None, None, 3, None, None, None,),
    440404: SongMeta("Stillborn", "Black Label Society", "Guitar Hero World Tour", "ghwt", 5, 2, 2, None, None, None, 2, None, None, None,),
    440405: SongMeta("One Way or Another", "Blondie", "Guitar Hero World Tour", "ghwt", 3, 1, 4, None, None, None, 5, None, None, None,),
    440406: SongMeta("Rebel Yell", "Billy Idol", "Guitar Hero World Tour", "ghwt", 5, 2, 2, None, None, None, 4, None, None, None,),
    440407: SongMeta("Scream Aim Fire", "Bullet for My Valentine", "Guitar Hero World Tour", "ghwt", 6, 3, 6, None, None, None, 3, None, None, None,),
    440408: SongMeta("Livin' on a Prayer", "Bon Jovi", "Guitar Hero World Tour", "ghwt", 2, 2, 1, None, None, None, 2, None, None, None,),
    440409: SongMeta("Hey Man, Nice Shot", "Filter", "Guitar Hero World Tour", "ghwt", 3, 4, 3, None, None, None, 4, None, None, None,),
    440410: SongMeta("Pull Me Under", "Dream Theater", "Guitar Hero World Tour", "ghwt", 6, 5, 6, None, None, None, 4, None, None, None,),
    440411: SongMeta("Satch Boogie", "Joe Satriani", "Guitar Hero World Tour", "ghwt", 6, 4, 4, None, None, None, None, None, None, None,),
    440412: SongMeta("Weapon of Choice", "Black Rebel Motorcycle Club", "Guitar Hero World Tour", "ghwt", 3, 1, 1, None, None, None, 2, None, None, None,),
    440413: SongMeta("The Middle", "Jimmy Eat World", "Guitar Hero World Tour", "ghwt", 4, 1, 2, None, None, None, 2, None, None, None,),
    440414: SongMeta("Freak on a Leash", "Korn", "Guitar Hero World Tour", "ghwt", 1, 2, 3, None, None, None, 2, None, None, None,),
    440415: SongMeta("Mountain Song", "Jane's Addiction", "Guitar Hero World Tour", "ghwt", 3, 2, 3, None, None, None, 2, None, None, None,),
    440416: SongMeta("Vinternoll2", "Kent", "Guitar Hero World Tour", "ghwt", 0, 2, 2, None, None, None, 3, None, None, None,),
    440417: SongMeta("Hotel California", "Eagles", "Guitar Hero World Tour", "ghwt", 3, 2, 4, None, None, None, 2, None, None, None,),
    440418: SongMeta("La Bamba", "Los Lobos", "Guitar Hero World Tour", "ghwt", 5, 2, 3, None, None, None, 3, None, None, None,),
    440419: SongMeta("Our Truth", "Lacuna Coil", "Guitar Hero World Tour", "ghwt", 3, 3, 3, None, None, None, 3, None, None, None,),
    440420: SongMeta("Are You Gonna Go My Way", "Lenny Kravitz", "Guitar Hero World Tour", "ghwt", 3, 2, 1, None, None, None, 1, None, None, None,),
    440421: SongMeta("Float On", "Modest Mouse", "Guitar Hero World Tour", "ghwt", 1, 1, 1, None, None, None, 3, None, None, None,),
    440422: SongMeta("Everlong", "Foo Fighters", "Guitar Hero World Tour", "ghwt", 3, 2, 5, None, None, None, 2, None, None, None,),
    440423: SongMeta("Beat It", "Michael Jackson", "Guitar Hero World Tour", "ghwt", 6, 1, 1, None, None, None, 4, None, None, None,),
    440424: SongMeta("Hollywood Nights", "Bob Seger & the Silver Bullet Band", "Guitar Hero World Tour", "ghwt", 4, 5, 5, None, None, None, 5, None, None, None,),
    440425: SongMeta("Kick Out the Jams", "MC5's Wayne Kramer", "Guitar Hero World Tour", "ghwt", 4, 3, 6, None, None, None, 4, None, None, None,),
    440426: SongMeta("Sweet Home Alabama (Live)", "Lynyrd Skynyrd", "Guitar Hero World Tour", "ghwt", 5, 4, 3, None, None, None, 3, None, None, None,),
    440427: SongMeta("Soul Doubt", "NOFX", "Guitar Hero World Tour", "ghwt", 5, 4, 5, None, None, None, 4, None, None, None,),
    440428: SongMeta("Overkill", "Motörhead", "Guitar Hero World Tour", "ghwt", 6, 5, 5, None, None, None, 3, None, None, None,),
    440429: SongMeta("About a Girl (Unplugged Live)", "Nirvana", "Guitar Hero World Tour", "ghwt", 0, 0, 0, None, None, None, 0, None, None, None,),
    440430: SongMeta("Some Might Say", "Oasis", "Guitar Hero World Tour", "ghwt", 1, 1, 1, None, None, None, 2, None, None, None,),
    440431: SongMeta("Assassin", "Muse", "Guitar Hero World Tour", "ghwt", 5, 4, 5, None, None, None, 2, None, None, None,),
    440432: SongMeta("Trapped Under Ice", "Metallica", "Guitar Hero World Tour", "ghwt", 6, 5, 6, None, None, None, 4, None, None, None,),
    440433: SongMeta("Heartbreaker", "Pat Benatar", "Guitar Hero World Tour", "ghwt", 5, 5, 4, None, None, None, 3, None, None, None,),
    440434: SongMeta("Misery Business", "Paramore", "Guitar Hero World Tour", "ghwt", 2, 2, 4, None, None, None, 4, None, None, None,),
    440435: SongMeta("Shiver", "Coldplay", "Guitar Hero World Tour", "ghwt", 3, 2, 2, None, None, None, 2, None, None, None,),
    440436: SongMeta("Up Around the Bend", "Creedence Clearwater Revival", "Guitar Hero World Tour", "ghwt", 2, 1, 1, None, None, None, 0, None, None, None,),
    440437: SongMeta("Mr. Crowley", "Ozzy Osbourne", "Guitar Hero World Tour", "ghwt", 6, 3, 3, None, None, None, 2, None, None, None,),
    440438: SongMeta("Feel the Pain", "Dinosaur Jr.", "Guitar Hero World Tour", "ghwt", 5, 2, 4, None, None, None, 0, None, None, None,),
    440439: SongMeta("Spiderwebs", "No Doubt", "Guitar Hero World Tour", "ghwt", 5, 3, 3, None, None, None, 4, None, None, None,),
    440440: SongMeta("Go Your Own Way", "Fleetwood Mac", "Guitar Hero World Tour", "ghwt", 2, 1, 1, None, None, None, 2, None, None, None,),
    440441: SongMeta("Escuela de Calor", "Radio Futura", "Guitar Hero World Tour", "ghwt", 4, 2, 4, None, None, None, 5, None, None, None,),
    440442: SongMeta("The One I Love", "R.E.M.", "Guitar Hero World Tour", "ghwt", 0, 0, 1, None, None, None, 1, None, None, None,),
    440443: SongMeta("Hail to the Freaks", "Beatsteaks", "Guitar Hero World Tour", "ghwt", 2, 1, 1, None, None, None, 1, None, None, None,),
    440444: SongMeta("Nuvole e Lenzuola", "Negramaro", "Guitar Hero World Tour", "ghwt", 2, 2, 2, None, None, None, 2, None, None, None,),
    440445: SongMeta("Too Much, Too Young, Too Fast", "Airbourne", "Guitar Hero World Tour", "ghwt", 2, 1, 1, None, None, None, 1, None, None, None,),
    440446: SongMeta("Toy Boy", "Stuck in the Sound", "Guitar Hero World Tour", "ghwt", 5, 1, 5, None, None, None, 5, None, None, None,),
    440447: SongMeta("Never Too Late", "The Answer", "Guitar Hero World Tour", "ghwt", 5, 3, 5, None, None, None, 5, None, None, None,),
    440448: SongMeta("Santeria", "Sublime", "Guitar Hero World Tour", "ghwt", 3, 3, 4, None, None, None, 4, None, None, None,),
    440449: SongMeta("Obstacle 1", "Interpol", "Guitar Hero World Tour", "ghwt", 1, 2, 4, None, None, None, 2, None, None, None,),
    440450: SongMeta("Stranglehold", "Ted Nugent", "Guitar Hero World Tour", "ghwt", 6, 5, 5, None, None, None, 4, None, None, None,),
    440451: SongMeta("L'Via L'Viaquez", "The Mars Volta", "Guitar Hero World Tour", "ghwt", 5, 4, 4, None, None, None, 4, None, None, None,),
    440452: SongMeta("Today", "The Smashing Pumpkins", "Guitar Hero World Tour", "ghwt", 0, 2, 1, None, None, None, 1, None, None, None,),
    440453: SongMeta("Demolition Man (Live)", "The Police", "Guitar Hero World Tour", "ghwt", 5, 5, 5, None, None, None, 5, None, None, None,),
    440454: SongMeta("Pretty Vacant", "The Sex Pistols", "Guitar Hero World Tour", "ghwt", 2, 1, 3, None, None, None, 1, None, None, None,),
    440455: SongMeta("Love Me Two Times", "The Doors", "Guitar Hero World Tour", "ghwt", 5, 2, 4, None, None, None, 4, None, None, None,),
    440456: SongMeta("Ramblin' Man", "The Allman Brothers Band", "Guitar Hero World Tour", "ghwt", 3, 5, 2, None, None, None, 3, None, None, None,),
    440457: SongMeta("Rooftops (A Liberation Broadcast)", "Lostprophets", "Guitar Hero World Tour", "ghwt", 2, 2, 3, None, None, None, 2, None, None, None,),
    440458: SongMeta("Purple Haze (Live at San Diego)", "The Jimi Hendrix Experience", "Guitar Hero World Tour", "ghwt", 6, 5, 6, None, None, None, 5, None, None, None,),
    440459: SongMeta("Crazy Train", "Ozzy Osbourne", "Guitar Hero World Tour", "ghwt", 6, 2, 5, None, None, None, 5, None, None, None,),
    440460: SongMeta("Parabola", "Tool", "Guitar Hero World Tour", "ghwt", 4, 5, 5, None, None, None, 4, None, None, None,),
    440461: SongMeta("Monsoon", "Tokio Hotel", "Guitar Hero World Tour", "ghwt", 0, 1, 1, None, None, None, 1, None, None, None,),
    440462: SongMeta("On the Road Again (Live)", "Willie Nelson", "Guitar Hero World Tour", "ghwt", 3, 1, 2, None, None, None, 2, None, None, None,),
    440463: SongMeta("Eye of the Tiger", "Survivor", "Guitar Hero World Tour", "ghwt", 3, 1, 1, None, None, None, 2, None, None, None,),
    440464: SongMeta("Vicarious", "Tool", "Guitar Hero World Tour", "ghwt", 5, 5, 6, None, None, None, 4, None, None, None,),
    440465: SongMeta("Hot for Teacher", "Van Halen", "Guitar Hero World Tour", "ghwt", 6, 6, 6, None, None, None, 4, None, None, None,),
    440466: SongMeta("B.Y.O.B.", "System of a Down", "Guitar Hero World Tour", "ghwt", 6, 6, 5, None, None, None, 4, None, None, None,),
    440467: SongMeta("Prisoner of Society", "The Living End", "Guitar Hero World Tour", "ghwt", 5, 5, 3, None, None, None, 2, None, None, None,),
    440468: SongMeta("The Wind Cries Mary", "The Jimi Hendrix Experience", "Guitar Hero World Tour", "ghwt", 4, 2, 3, None, None, None, 4, None, None, None,),
    440469: SongMeta("Aggro", "The Enemy", "Guitar Hero World Tour", "ghwt", 2, 1, 2, None, None, None, 1, None, None, None,),
    440470: SongMeta("Love Spreads", "The Stone Roses", "Guitar Hero World Tour", "ghwt", 5, 4, 5, None, None, None, 4, None, None, None,),
    440471: SongMeta("American Woman", "The Guess Who", "Guitar Hero World Tour", "ghwt", 2, 2, 5, None, None, None, 5, None, None, None,),
    440472: SongMeta("Band on the Run", "Paul McCartney & Wings", "Guitar Hero World Tour", "ghwt", 1, 1, 0, None, None, None, 1, None, None, None,),
    440473: SongMeta("You're Gonna Say Yeah!", "HushPuppies", "Guitar Hero World Tour", "ghwt", 2, 2, 3, None, None, None, 2, None, None, None,),
    440474: SongMeta("Schism", "Tool", "Guitar Hero World Tour", "ghwt", 4, 3, 5, None, None, None, 3, None, None, None,),
    440475: SongMeta("Do It Again", "Steely Dan", "Guitar Hero World Tour", "ghwt", 5, 2, 2, None, None, None, 4, None, None, None,),
    440476: SongMeta("Antisocial", "Trust", "Guitar Hero World Tour", "ghwt", 3, 3, 3, None, None, None, 3, None, None, None,),
    440477: SongMeta("No Sleep Till Brooklyn", "Beastie Boys ft. Kerry King", "Guitar Hero World Tour", "ghwt", 5, 2, 2, None, None, None, None, None, None, None,),
    440478: SongMeta("Dammit (Growing Up)", "Blink-182", "Guitar Hero World Tour", "ghwt", 3, 3, 4, None, None, None, 3, None, None, None,),
    440479: SongMeta("Beautiful Disaster", "311", "Guitar Hero World Tour", "ghwt", 1, 2, 2, None, None, None, 2, None, None, None,),
    440480: SongMeta("Love Removal Machine", "The Cult", "Guitar Hero World Tour", "ghwt", 6, 3, 4, None, None, None, 4, None, None, None,),
    440481: SongMeta("The Joker", "Steve Miller Band", "Guitar Hero World Tour", "ghwt", 2, 2, 2, None, None, None, 3, None, None, None,),
    440482: SongMeta("Re-Education (Through Labor)", "Rise Against", "Guitar Hero World Tour", "ghwt", 2, 2, 2, None, None, None, 2, None, None, None,),
    440483: SongMeta("Lazy Eye", "Silversun Pickups", "Guitar Hero World Tour", "ghwt", 4, 2, 3, None, None, None, 1, None, None, None,),
    440484: SongMeta("What I've Done", "Linkin Park", "Guitar Hero World Tour", "ghwt", 0, 0, 0, None, None, None, 0, None, None, None,),
#GHWT Guitar Battles
#Made optional because some people would not want to play these.
    1440401: SongMeta("Ted Nugent Guitar Battle (Career)", "Ted Nugent", "GHWT Guitar Battles", "ghwt", 5, None, 2, None, None, None, None, None, None, 0,),
    1440402: SongMeta("Zakk Wylde Guitar Battle (Career)", "Zakk Wylde", "GHWT Guitar Battles", "ghwt", 5, None, 2, None, None, None, None, None, None, 0,),
}