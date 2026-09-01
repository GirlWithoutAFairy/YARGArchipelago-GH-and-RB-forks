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
#Guitar Hero 3
#4403
    420301: SongMeta("3's & 7's", "Queens of the Stone Age", "Guitar Hero 3", "gh3", 5, 5, None, None, None, None, None, None, None, None),
    420302: SongMeta("Anarchy In The UK", "The Sex Pistols", "Guitar Hero 3", "gh3", 2, 2, None, None, None, None, None, None, None, None),
    420303: SongMeta("Avalancha", "Heroes del Silencio", "Guitar Hero 3", "gh3", 0, None, None, None, None, None, None, None, None, 0),
    420304: SongMeta("Barracuda", "Heart (WaveGroup)", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420305: SongMeta("Before I Forget", "Slipknot", "Guitar Hero 3", "gh3", 5, 5, None, None, None, None, None, None, None, None),
    420306: SongMeta("Black Magic Woman", "Santana", "Guitar Hero 3", "gh3", 4, 4, None, None, None, None, None, None, None, None),
    420307: SongMeta("Black Sunshine", "White Zombie (WaveGroup)", "Guitar Hero 3", "gh3", 4, 4, None, None, None, None, None, None, None, None),
    420308: SongMeta("Bulls on Parade", "Rage Against the Machine", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420309: SongMeta("Can't Be Saved", "Senses Fail", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420310: SongMeta("Cherub Rock", "The Smashing Pumpkins", "Guitar Hero 3", "gh3", 4, 4, None, None, None, None, None, None, None, None),
    420311: SongMeta("Cities On Flame with Rock & Roll", "Blue Oyster Cult (WaveGroup)", "Guitar Hero 3", "gh3", 4, 4, None, None, None, None, None, None, None, None),
    420312: SongMeta("Cliffs Of Dover", "Eric Johnson", "Guitar Hero 3", "gh3", 6, 6, None, None, None, None, None, None, None, None),
    420313: SongMeta("Closer", "Lacuna Coil", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420314: SongMeta("Cult Of Personality", "Living Colour", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420315: SongMeta("Don't Hold Back", "The Sleeping", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420316: SongMeta("Down N' Dirty", "L.A. Slum Lords", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420317: SongMeta("Even Flow", "Pearl Jam", "Guitar Hero 3", "gh3", 2, 2, None, None, None, None, None, None, None, None),
    420318: SongMeta("F.C.P.R.E.M.I.X.", "The Fall of Troy", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420319: SongMeta("Generation Rock", "Revolverheld", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420320: SongMeta("Go That Far", "Bret Michaels Band", "Guitar Hero 3", "gh3", 0, None, None, None, None, None, None, None, None, 0),
    420321: SongMeta("Helicopter", "Bloc Party", "Guitar Hero 3", "gh3", 5, None, None, None, None, None, None, None, None, 5),
    420322: SongMeta("Hier Kommt Alex", "Die Toten Hosen", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420323: SongMeta("Hit Me With Your Best Shot", "Pat Benatar (WaveGroup)", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420324: SongMeta("Holiday In Cambodia", "The Dead Kennedys (WaveGroup)", "Guitar Hero 3", "gh3", 3, 3, None, None, None, None, None, None, None, None),
    420325: SongMeta("I'm In The Band", "The Hellacopters", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420326: SongMeta("Impulse", "An Endless Sporadic", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420327: SongMeta("In Love", "Scouts of St. Sebastian", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420328: SongMeta("In The Belly Of A Shark", "Gallows", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420329: SongMeta("Knights of Cydonia", "Muse", "Guitar Hero 3", "gh3", 5, 5, None, None, None, None, None, None, None, None),
    420330: SongMeta("Kool Thing", "Sonic Youth", "Guitar Hero 3", "gh3", 2, 2, None, None, None, None, None, None, None, None),
    420331: SongMeta("La Grange", "ZZ Top (Steve Ouimette)", "Guitar Hero 3", "gh3", 3, 3, None, None, None, None, None, None, None, None),
    420332: SongMeta("Lay Down", "Priestess", "Guitar Hero 3", "gh3", 1, 1, None, None, None, None, None, None, None, None),
    420333: SongMeta("Mauvais Garçon", "Naast", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420334: SongMeta("Metal Heavy Lady", "Lions", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420335: SongMeta("Minus Celsius", "Backyard Babies", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420336: SongMeta("Miss Murder", "AFI", "Guitar Hero 3", "gh3", 1, 1, None, None, None, None, None, None, None, None),
    420337: SongMeta("Mississippi Queen", "Mountain (WaveGroup)", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420338: SongMeta("Monsters", "Matchbook Romance", "Guitar Hero 3", "gh3", 6, 6, None, None, None, None, None, None, None, None),
    420339: SongMeta("My Curse", "Killswitch Engage", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420340: SongMeta("My Name Is Jonas", "Weezer", "Guitar Hero 3", "gh3", 2, 2, None, None, None, None, None, None, None, None),
    420341: SongMeta("Nothing For Me Here", "Dope", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420342: SongMeta("One", "Metallica", "Guitar Hero 3", "gh3", 6, None, None, None, None, None, None, None, None, None),
    420343: SongMeta("Paint It Black", "The Rolling Stones", "Guitar Hero 3", "gh3", 1, 1, None, None, None, None, None, None, None, None),
    420344: SongMeta("Paranoid", "Black Sabbath (Steve Ouimette)", "Guitar Hero 3", "gh3", 2, 2, None, None, None, None, None, None, None, None),
    420345: SongMeta("Prayer Of The Refugee", "Rise Against", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420346: SongMeta("Pride & Joy", "Stevie Ray Vaughan (Steve Ouimette)", "Guitar Hero 3", "gh3", 4, 4, None, None, None, None, None, None, None, None),
    420347: SongMeta("Radio Song", "Superbus", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420348: SongMeta("Raining Blood", "Slayer", "Guitar Hero 3", "gh3", 6, 6, None, None, None, None, None, None, None, None),
    420349: SongMeta("Reptilia", "The Strokes", "Guitar Hero 3", "gh3", 2, 2, None, None, None, None, None, None, None, None),
    420350: SongMeta("Rock & Roll All Nite", "KISS (Steve Ouimette)", "Guitar Hero 3", "gh3", 2, 2, None, None, None, None, None, None, None, None),
    420351: SongMeta("Rock You Like A Hurricane", "Scorpions (Steve Ouimette)", "Guitar Hero 3", "gh3", 3, 3, None, None, None, None, None, None, None, None),
    420352: SongMeta("Ruby", "Kaiser Chiefs", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420353: SongMeta("Sabotage", "Beastie Boys", "Guitar Hero 3", "gh3", 1, 1, None, None, None, None, None, None, None, None),
    420354: SongMeta("Same Old Song & Dance", "Aerosmith", "Guitar Hero 3", "gh3", 3, None, None, None, None, None, None, None, None, 3),
    420355: SongMeta("School's Out", "Alice Cooper (WaveGroup)", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420356: SongMeta("She Bangs The Drums", "The Stone Roses (WaveGroup)", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420357: SongMeta("Slow Ride", "Foghat (WaveGroup)", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420358: SongMeta("Story Of My Life", "Social Distortion", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420359: SongMeta("Stricken", "Disturbed", "Guitar Hero 3", "gh3", 5, 5, None, None, None, None, None, None, None, None),
    420360: SongMeta("Suck My Kiss", "Red Hot Chili Peppers", "Guitar Hero 3", "gh3", 3, 3, None, None, None, None, None, None, None, None),
    420361: SongMeta("Sunshine of Your Love", "Cream (WaveGroup)", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420362: SongMeta("Take This Life", "In Flames", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420363: SongMeta("Talk Dirty to Me", "Poison", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420364: SongMeta("The Metal", "Tenacious D", "Guitar Hero 3", "gh3", 4, 4, None, None, None, None, None, None, None, None),
    420365: SongMeta("The Number of the Beast", "Iron Maiden", "Guitar Hero 3", "gh3", 6, 6, None, None, None, None, None, None, None, None),
    420366: SongMeta("The Seeker", "The Who (Steve Ouimette)", "Guitar Hero 3", "gh3", 1, 1, None, None, None, None, None, None, None, None),
    420367: SongMeta("The Way It Ends", "Prototype", "Guitar Hero 3", "gh3", 0, 0, None, None, None, None, None, None, None, None),
    420368: SongMeta("Through The Fire & Flames", "Dragonforce", "Guitar Hero 3", "gh3", 0, None, None, None, None, None, None, None, None, None),
    420369: SongMeta("Welcome To The Jungle", "Guns N' Roses", "Guitar Hero 3", "gh3", 3, 3, None, None, None, None, None, None, None, None),
    420370: SongMeta("When You Were Young", "The Killers", "Guitar Hero 3", "gh3", 1, 1, None, None, None, None, None, None, None, None),
#GH3 Co-op
    420371: SongMeta("Guitar Battle vs. Slash", "Slash", "GH3 Co-op", "gh3", 0, None, None, None, None, None, None, None, None, 0),
    420372: SongMeta("Guitar Battle vs. Tom Morello", "Tom Morello", "GH3 Co-op", "gh3", 0, None, None, None, None, None, None, None, None, 0),
    420373: SongMeta("One (Co-op)", "Metallica", "GH3 Co-op", "gh3", 6, None, None, None, None, None, None, None, None, 6),
    420374: SongMeta("The Devil Went Down to Georgia", "Steve Ouimette", "GH3 Co-op", "gh3", 0, None, None, None, None, None, None, None, None, 0),
    420375: SongMeta("Through The Fire & Flames (Co-op)", "Dragonforce", "GH3 Co-op", "gh3", 0, None, None, None, None, None, None, None, None, 0),
}