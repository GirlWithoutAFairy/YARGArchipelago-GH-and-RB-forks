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
#Rock Band 2
#7202
    720201: SongMeta("Hello There", "Cheap Trick", "Rock Band 2", "rb2", 1, 3, 1, None, None, None, 0, None, None, None),
    720202: SongMeta("E-Pro", "Beck", "Rock Band 2", "rb2", 2, 1, 3, None, None, None, 2, None, None, None),
    720203: SongMeta("Rebel Girl", "Bikini Kill", "Rock Band 2", "rb2", 1, 2, 0, None, None, None, 1, None, None, None),
    720204: SongMeta("Man in the Box", "Alice in Chains", "Rock Band 2", "rb2", 2, 1, 1, None, None, None, 0, None, None, None),
    720205: SongMeta("You Oughta Know", "Alanis Morissette", "Rock Band 2", "rb2", 3, 5, 3, None, None, None, 4, None, None, None),
    720206: SongMeta("Night Lies", "Bang Camaro", "Rock Band 2", "rb2", 5, 4, 4, None, None, None, 2, None, None, None),
    720207: SongMeta("One Way or Another", "Blondie", "Rock Band 2", "rb2", 4, 3, 3, None, None, None, 3, None, None, None),
    720208: SongMeta("Shoulder to the Plow", "Breaking Wheel", "Rock Band 2", "rb2", 6, 6, 6, None, None, None, 1, None, None, None),
    720209: SongMeta("Down with the Sickness", "Disturbed", "Rock Band 2", "rb2", 4, 4, 4, None, None, None, 5, None, None, None),
    720210: SongMeta("White Wedding (Part 1)", "Billy Idol", "Rock Band 2", "rb2", 2, 4, 2, None, None, None, 4, None, None, None),
    720211: SongMeta("Get Clean", "Anarchy Club", "Rock Band 2", "rb2", 6, 4, 5, None, None, None, 4, None, None, None),
    720212: SongMeta("Girl's Not Grey", "AFI", "Rock Band 2", "rb2", 4, 4, 4, None, None, None, 3, None, None, None),
    720213: SongMeta("Hungry Like the Wolf", "Duran Duran", "Rock Band 2", "rb2", 0, 2, 0, None, None, None, 0, None, None, None),
    720214: SongMeta("So What'cha Want", "Beastie Boys", "Rock Band 2", "rb2", 1, 0, 1, None, None, None, 3, None, None, None),
    720215: SongMeta("Shackler's Revenge", "Guns N' Roses", "Rock Band 2", "rb2", 5, 4, 3, None, None, None, 2, None, None, None),
    720216: SongMeta("Uncontrollable Urge", "Devo", "Rock Band 2", "rb2", 5, 5, 4, None, None, None, 5, None, None, None),
    720217: SongMeta("Livin' on a Prayer", "Bon Jovi", "Rock Band 2", "rb2", 3, 4, 1, None, None, None, 4, None, None, None),
    720218: SongMeta("Shooting Star", "Bad Company", "Rock Band 2", "rb2", 3, 3, 1, None, None, None, 2, None, None, None),
    720219: SongMeta("Alabama Getaway", "Grateful Dead", "Rock Band 2", "rb2", 5, 2, 4, None, None, None, 4, None, None, None),
    720220: SongMeta("Feel the Pain", "Dinosaur Jr.", "Rock Band 2", "rb2", 2, 4, 3, None, None, None, 1, None, None, None),
    720221: SongMeta("Tangled Up in Blue", "Bob Dylan", "Rock Band 2", "rb2", 4, 2, 1, None, None, None, 6, None, None, None),
    720222: SongMeta("Everlong", "Foo Fighters", "Rock Band 2", "rb2", 4, 4, 6, None, None, None, 2, None, None, None),
    720223: SongMeta("Pump It Up", "Elvis Costello", "Rock Band 2", "rb2", 3, 2, 3, None, None, None, 1, None, None, None),
    720224: SongMeta("Go Your Own Way", "Fleetwood Mac", "Rock Band 2", "rb2", 3, 3, 2, None, None, None, 3, None, None, None),
    720225: SongMeta("Visions", "Abnormality", "Rock Band 2", "rb2", 6, 6, 6, None, None, None, 1, None, None, None),
    720226: SongMeta("Let There Be Rock", "AC/DC", "Rock Band 2", "rb2", 5, 1, 2, None, None, None, 3, None, None, None),
    720227: SongMeta("Almost Easy", "Avenged Sevenfold", "Rock Band 2", "rb2", 5, 5, 5, None, None, None, 4, None, None, None),
    720228: SongMeta("Panic Attack", "Dream Theater", "Rock Band 2", "rb2", 6, 6, 6, None, None, None, 5, None, None, None),
    720229: SongMeta("Welcome to the Neighborhood", "Libyans", "Rock Band 2", "rb2", 3, 3, 4, None, None, None, 3, None, None, None),
    720230: SongMeta("Bad Reputation", "Joan Jett", "Rock Band 2", "rb2", 3, 3, 5, None, None, None, 3, None, None, None),
    720231: SongMeta("Painkiller", "Judas Priest", "Rock Band 2", "rb2", 6, 6, 6, None, None, None, 6, None, None, None),
    720232: SongMeta("One Step Closer", "Linkin Park", "Rock Band 2", "rb2", 0, 1, 4, None, None, None, 4, None, None, None),
    720233: SongMeta("Pretend We're Dead", "L7", "Rock Band 2", "rb2", 0, 1, 1, None, None, None, 0, None, None, None),
    720234: SongMeta("Aqualung", "Jethro Tull", "Rock Band 2", "rb2", 4, 5, 5, None, None, None, 4, None, None, None),
    720235: SongMeta("Peace Sells", "Megadeth", "Rock Band 2", "rb2", 6, 6, 6, None, None, None, 2, None, None, None),
    720236: SongMeta("Round and Round", "Ratt", "Rock Band 2", "rb2", 5, 1, 3, None, None, None, 4, None, None, None),
    720237: SongMeta("Give It All", "Rise Against", "Rock Band 2", "rb2", 4, 4, 6, None, None, None, 4, None, None, None),
    720238: SongMeta("Give It Away", "Red Hot Chili Peppers", "Rock Band 2", "rb2", 2, 4, 1, None, None, None, 4, None, None, None),
    720239: SongMeta("I Was Wrong", "Social Distortion", "Rock Band 2", "rb2", 1, 3, 0, None, None, None, 0, None, None, None),
    720240: SongMeta("Ace of Spades '08", "Motörhead", "Rock Band 2", "rb2", 5, 6, 6, None, None, None, 3, None, None, None),
    720241: SongMeta("Testify", "Rage Against the Machine", "Rock Band 2", "rb2", 5, 4, 4, None, None, None, 3, None, None, None),
    720242: SongMeta("Alive", "Pearl Jam", "Rock Band 2", "rb2", 4, 4, 4, None, None, None, 3, None, None, None),
    720243: SongMeta("Bodhisattva", "Steely Dan", "Rock Band 2", "rb2", 6, 5, 5, None, None, None, 1, None, None, None),
    720244: SongMeta("Carry on Wayward Son", "Kansas", "Rock Band 2", "rb2", 5, 5, 2, None, None, None, 5, None, None, None),
    720245: SongMeta("PDA", "Interpol", "Rock Band 2", "rb2", 3, 3, 4, None, None, None, 3, None, None, None),
    720246: SongMeta("Mountain Song", "Jane's Addiction", "Rock Band 2", "rb2", 2, 4, 4, None, None, None, 4, None, None, None),
    720247: SongMeta("Lazy Eye", "Silversun Pickups", "Rock Band 2", "rb2", 5, 2, 3, None, None, None, 0, None, None, None),
    720248: SongMeta("The Middle", "Jimmy Eat World", "Rock Band 2", "rb2", 4, 3, 4, None, None, None, 3, None, None, None),
    720249: SongMeta("That's What You Get", "Paramore", "Rock Band 2", "rb2", 0, 0, 2, None, None, None, 3, None, None, None),
    720250: SongMeta("Colony of Birchmen", "Mastodon", "Rock Band 2", "rb2", 6, 5, 5, None, None, None, 5, None, None, None),
    720251: SongMeta("Teen Age Riot", "Sonic Youth", "Rock Band 2", "rb2", 5, 3, 5, None, None, None, 1, None, None, None),
    720252: SongMeta("Spirit in the Sky", "Norman Greenbaum", "Rock Band 2", "rb2", 2, 1, 2, None, None, None, 0, None, None, None),
    720253: SongMeta("Drain You", "Nirvana", "Rock Band 2", "rb2", 1, 2, 2, None, None, None, 1, None, None, None),
    720254: SongMeta("Spoonman", "Soundgarden", "Rock Band 2", "rb2", 5, 5, 5, None, None, None, 6, None, None, None),
    720255: SongMeta("Eye of the Tiger", "Survivor", "Rock Band 2", "rb2", 0, 0, 0, None, None, None, 2, None, None, None),
    720256: SongMeta("Conventional Lover", "Speck", "Rock Band 2", "rb2", 2, 3, 3, None, None, None, 2, None, None, None),
    720257: SongMeta("Chop Suey", "System of a Down", "Rock Band 2", "rb2", 5, 6, 4, None, None, None, 6, None, None, None),
    720258: SongMeta("My Own Worst Enemy", "Lit", "Rock Band 2", "rb2", 0, 1, 0, None, None, None, 0, None, None, None),
    720259: SongMeta("Cool for Cats", "Squeeze", "Rock Band 2", "rb2", 0, 3, 1, None, None, None, 0, None, None, None),
    720260: SongMeta("Float On", "Modest Mouse", "Rock Band 2", "rb2", 0, 0, 1, None, None, None, 2, None, None, None),
    720261: SongMeta("Any Way You Want It", "Journey", "Rock Band 2", "rb2", 5, 4, 4, None, None, None, 5, None, None, None),
    720262: SongMeta("Nine in the Afternoon", "Panic! At the Disco", "Rock Band 2", "rb2", 1, 2, 0, None, None, None, 2, None, None, None),
    720263: SongMeta("The Trees (Vault Edition)", "Rush", "Rock Band 2", "rb2", 5, 5, 6, None, None, None, 5, None, None, None),
    720264: SongMeta("Our Truth", "Lacuna Coil", "Rock Band 2", "rb2", 2, 5, 4, None, None, None, 5, None, None, None),
    720265: SongMeta("Battery", "Metallica", "Rock Band 2", "rb2", 6, 6, 6, None, None, None, 3, None, None, None),
    720266: SongMeta("Rock'n Me", "Steve Miller Band", "Rock Band 2", "rb2", 5, 3, 2, None, None, None, 3, None, None, None),
    720267: SongMeta("Souls of Black", "Testament", "Rock Band 2", "rb2", 6, 6, 5, None, None, None, 4, None, None, None),
    720268: SongMeta("A Jagged Gorgeous Winter", "The Main Drag", "Rock Band 2", "rb2", 3, 3, 3, None, None, None, 2, None, None, None),
    720269: SongMeta("American Woman", "The Guess Who", "Rock Band 2", "rb2", 1, 2, 4, None, None, None, 3, None, None, None),
    720270: SongMeta("Lump", "The Presidents of the United States of America", "Rock Band 2", "rb2", 1, 4, 5, None, None, None, 0, None, None, None),
    720271: SongMeta("Pinball Wizard", "The Who", "Rock Band 2", "rb2", 4, 3, 5, None, None, None, 3, None, None, None),
    720272: SongMeta("Alex Chilton", "The Replacements", "Rock Band 2", "rb2", 4, 4, 4, None, None, None, 2, None, None, None),
    720273: SongMeta("Master Exploder", "Tenacious D", "Rock Band 2", "rb2", 6, 2, 5, None, None, None, 5, None, None, None),
    720274: SongMeta("Come Out and Play (Keep 'Em Separated)", "The Offspring", "Rock Band 2", "rb2", 4, 0, 3, None, None, None, 4, None, None, None),
    720275: SongMeta("Psycho Killer", "Talking Heads", "Rock Band 2", "rb2", 2, 3, 0, None, None, None, 5, None, None, None),
    720276: SongMeta("Where'd You Go?", "The Mighty Mighty Bosstones", "Rock Band 2", "rb2", 4, 4, 2, None, None, None, 1, None, None, None),
    720277: SongMeta("We Got the Beat", "The Go-Go's", "Rock Band 2", "rb2", 0, 3, 3, None, None, None, 1, None, None, None),
    720278: SongMeta("Today", "The Smashing Pumpkins", "Rock Band 2", "rb2", 0, 3, 3, None, None, None, 1, None, None, None),
    720279: SongMeta("Kids in America", "The Muffs", "Rock Band 2", "rb2", 2, 2, 5, None, None, None, 1, None, None, None),
    720280: SongMeta("Rob the Prez-O-Dent", "That Handsome Devil", "Rock Band 2", "rb2", 4, 5, 5, None, None, None, 3, None, None, None),
    720281: SongMeta("Supreme Girl", "The Sterns", "Rock Band 2", "rb2", 4, 3, 4, None, None, None, 3, None, None, None),
    720282: SongMeta("De-Luxe", "Lush", "Rock Band 2", "rb2", 3, 0, 3, None, None, None, 2, None, None, None),
    720283: SongMeta("Ramblin' Man", "The Allman Brothers Band", "Rock Band 2", "rb2", 6, 6, 5, None, None, None, 5, None, None, None),
    720284: SongMeta("New Kid in School", "The Donnas", "Rock Band 2", "rb2", 1, 2, 0, None, None, None, 4, None, None, None),
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
    
    