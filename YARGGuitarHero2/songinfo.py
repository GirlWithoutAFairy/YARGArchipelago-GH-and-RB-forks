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
#Guitar Hero 2
#4402
    440201: SongMeta("Gemini", "Brian Kahanek", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440202: SongMeta("Arterial Black", "Drist", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440203: SongMeta("Collide", "Anarchy Club", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440204: SongMeta("Six", "All That Remains", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440205: SongMeta("Surrender", "Cheap Trick (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440206: SongMeta("Push Push (Lady Lightning)", "Bang Camaro", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440207: SongMeta("Misirlou", "Dick Dale (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440208: SongMeta("Beast And the Harlot", "Avenged Sevenfold (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440209: SongMeta("War Pigs", "Black Sabbath (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440210: SongMeta("Jordan", "Buckethead", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440211: SongMeta("Madhouse", "Anthrax (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440212: SongMeta("The New Black", "Every Time I Die", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440213: SongMeta("Radium Eyes", "Count Zero", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440214: SongMeta("Them Bones", "Alice in Chains (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440215: SongMeta("Monkey Wrench", "Foo Fighters (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440216: SongMeta("Thunderhorse", "Dethklok", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440217: SongMeta("Mother", "Danzig (WaveGroup)", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440218: SongMeta("Last Child", "Aerosmith (WaveGroup)", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440219: SongMeta("Less Talk More Rokk", "FreezePop", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440220: SongMeta("Shout At The Devil", "Mötley Crüe (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440221: SongMeta("Heart-Shaped Box", "Nirvana (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440222: SongMeta("Yes We Can", "Made in Mexico", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440223: SongMeta("Soy Bomb", "Honest Bob and the Factory-to-Dealer Incentives", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440224: SongMeta("Hangar 18", "Megadeth (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440225: SongMeta("Girlfriend", "Matthew Sweet (WaveGroup)", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440226: SongMeta("Laid To Rest", "Lamb of God (WaveGroup)", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440227: SongMeta("Free Bird", "Lynyrd Skynyrd (WaveGroup)", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440228: SongMeta("YYZ", "Rush (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440229: SongMeta("Psychobilly Freakout", "Reverend Horton Heat (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440230: SongMeta("Killing In The Name", "Rage Against The Machine (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440231: SongMeta("The Light That Blinds", "Shadows Fall", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440232: SongMeta("Tonight I'm Gonna Rock You Tonight", "Spinal Tap (WaveGroup)", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440233: SongMeta("Sweet Child O' Mine", "Guns n' Roses (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440234: SongMeta("Stop", "Jane's Addiction", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440235: SongMeta("Search and Destroy", "Iggy Pop and the Stooges (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440236: SongMeta("Elephant Bones", "That Handsome Devil", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440237: SongMeta("Carry On Wayward Son", "Kansas (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440238: SongMeta("Red Lottery", "Megasus", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440239: SongMeta("John the Fisherman", "Primus", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440240: SongMeta("Crazy on You", "Heart (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440241: SongMeta("Trippin' on a Hole in a Paper Heart", "Stone Temple Pilots (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440242: SongMeta("Who Was In My Room Last Night?", "The Butthole Surfers (WaveGroup)", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440243: SongMeta("Raw Dog", "The Last Vegas", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440244: SongMeta("You Really Got Me", "Van Halen (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440245: SongMeta("Institutionalized", "Suicidal Tendencies (WaveGroup)", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440246: SongMeta("Mr. Fix It", "The Amazing Crowns", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440247: SongMeta("Woman", "Wolfmother (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440248: SongMeta("Cherry Pie", "Warrant (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440249: SongMeta("Laughtrack", "The Acro-brats", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440250: SongMeta("Fall Of Pangea", "Valient Thorr", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440251: SongMeta("Rock This Town", "Stray Cats (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440252: SongMeta("Jessica", "The Allman Brothers Band (WaveGroup)", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440253: SongMeta("Bad Reputation", "Thin Lizzy (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440254: SongMeta("Carry Me Home", "The Living End (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440255: SongMeta("Trogdor", "Strong Bad", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440256: SongMeta("X-Stream", "Voivod", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440257: SongMeta("Parasite", "The Neighborhoods", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440258: SongMeta("Freya", "The Sword (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440259: SongMeta("Tattooed Love Boys", "The Pretenders (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440260: SongMeta("Strutter", "Kiss (WaveGroup)", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440261: SongMeta("One For the Road", "Breaking Wheel", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440262: SongMeta("Message In A Bottle", "The Police (WaveGroup)", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440263: SongMeta("Can't You Hear Me Knockin'", "The Rolling Stones (WaveGroup)", "Guitar Hero 2", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440264: SongMeta("FTK", "Vagiant", "Guitar Hero 2", "gh2", 0, 0, None, None, None, None, None, None, None, None),
#GH2 360 Exlcusives
    440265: SongMeta("Hush", "Deep Purple (WaveGroup)", "GH2 360 Exclusives", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440266: SongMeta("Rock and Roll Hoochie Koo", "Rick Derringer (WaveGroup)", "GH2 360 Exclusives", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440267: SongMeta("Kicked To The Curb", "Noble Rot", "GH2 360 Exclusives", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440268: SongMeta("Drink Up", "Ounce of Self", "GH2 360 Exclusives", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440269: SongMeta("Possum Kingdom", "Toadies", "GH2 360 Exclusives", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440270: SongMeta("The Trooper", "Iron Maiden (WaveGroup)", "GH2 360 Exclusives", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440271: SongMeta("Life Wasted", "Pearl Jam (WaveGroup)", "GH2 360 Exclusives", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440272: SongMeta("Billion Dollar Babies", "Alice Cooper (WaveGroup)", "GH2 360 Exclusives", "gh2", 0, 0, None, None, None, None, None, None, None, None),
    440273: SongMeta("Dead!", "My Chemical Romance", "GH2 360 Exclusives", "gh2", 0, None, None, None, None, None, None, None, None, None),
    440274: SongMeta("Salvation", "Rancid (WaveGroup)", "GH2 360 Exclusives", "gh2", 0, 0, None, None, None, None, None, None, None, None),
#GH2 Co-op
    440275: SongMeta("Mother (Co-op)", "Danzig (WaveGroup)", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440276: SongMeta("Last Child (Co-op)", "Aerosmith (WaveGroup)", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440277: SongMeta("Arterial Black (Co-op)", "Drist", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440278: SongMeta("Trogdor (Co-op)", "Strong Bad", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440279: SongMeta("Institutionalized (Co-op)", "Suicidal Tendencies (WaveGroup)", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440280: SongMeta("Soy Bomb (Co-op)", "Honest Bob and the Factory-to-Dealer Incentives", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440281: SongMeta("Laid To Rest (Co-op)", "Lamb of God (WaveGroup)", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440282: SongMeta("Can't You Hear Me Knockin' (Co-op)", "The Rolling Stones (WaveGroup)", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440283: SongMeta("Who Was In My Room Last Night? (Co-op)", "The Butthole Surfers (WaveGroup)", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440284: SongMeta("Less Talk More Rokk (Co-op)", "FreezePop", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440285: SongMeta("Girlfriend (Co-op)", "Matthew Sweet (WaveGroup)", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440286: SongMeta("Free Bird (Co-op)", "Lynyrd Skynyrd (WaveGroup)", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440287: SongMeta("Strutter (Co-op)", "Kiss (WaveGroup)", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440288: SongMeta("Jessica (Co-op)", "The Allman Brothers Band (WaveGroup)", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440289: SongMeta("Laughtrack (Co-op)", "The Acro-brats", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440290: SongMeta("Tonight I'm Gonna Rock You Tonight (Co-op)", "Spinal Tap (WaveGroup)", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
    440291: SongMeta("Dead! (Co-op)", "My Chemical Romance", "GH2 Co-op", "gh2", 0, None, None, None, None, None, None, None, None, 0),
}