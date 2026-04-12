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
    725301: SongMeta("A-Punk", "Vampire Weekend", "LEGO Rock Band", "lrb", 3, 3, 4, None, None, None, 1, None, None, None),
    725302: SongMeta("Accidentally in Love", "Counting Crows", "LEGO Rock Band", "lrb", 2, 1, 2, None, None, None, 2, None, None, None),
    725303: SongMeta("Aliens Exist", "Blink-182", "LEGO Rock Band", "lrb", 2, 2, 5, None, None, None, 1, None, None, None),
    725304: SongMeta("Breakout", "Foo Fighters", "LEGO Rock Band", "lrb", 2, 1, 4, None, None, None, 2, None, None, None),
    725305: SongMeta("Check Yes Juliet", "We the Kings", "LEGO Rock Band", "lrb", 1, 1, 3, None, None, None, 1, None, None, None),
    725306: SongMeta("Crash", "The Primitives", "LEGO Rock Band", "lrb", 2, 0, 3, None, None, None, 1, None, None, None),
    725307: SongMeta("Crocodile Rock", "Elton John", "LEGO Rock Band", "lrb", 2, 1, 2, None, None, None, 3, None, None, None),
    725308: SongMeta("Dig", "Incubus", "LEGO Rock Band", "lrb", 2, 2, 3, None, None, None, 3, None, None, None),
    725309: SongMeta("Dreaming of You", "The Coral", "LEGO Rock Band", "lrb", 1, 2, 1, None, None, None, 1, None, None, None),
    725310: SongMeta("Every Little Thing She Does Is Magic", "The Police", "LEGO Rock Band", "lrb", 2, 2, 4, None, None, None, 3, None, None, None),
    725311: SongMeta("Fire", "The Jimi Hendrix Experience", "LEGO Rock Band", "lrb", 4, 3, 5, None, None, None, 4, None, None, None),
    725312: SongMeta("Free Fallin'", "Tom Petty", "LEGO Rock Band", "lrb", 1, 1, 0, None, None, None, 0, None, None, None),
    725313: SongMeta("Ghostbusters", "Ray Parker Jr.", "LEGO Rock Band", "lrb", 3, 2, 3, None, None, None, 1, None, None, None),
    725314: SongMeta("Girls & Boys", "Good Charlotte", "LEGO Rock Band", "lrb", 2, 0, 2, None, None, None, 2, None, None, None),
    725315: SongMeta("Grace", "Supergrass", "LEGO Rock Band", "lrb", 2, 2, 4, None, None, None, 1, None, None, None),
    725316: SongMeta("I Want You Back", "The Jackson 5", "LEGO Rock Band", "lrb", 3, 3, 3, None, None, None, 5, None, None, None),
    725317: SongMeta("In Too Deep", "Sum 41", "LEGO Rock Band", "lrb", 4, 3, 3, None, None, None, 1, None, None, None),
    725318: SongMeta("Kung Fu Fighting", "Carl Douglas", "LEGO Rock Band", "lrb", 5, 1, 4, None, None, None, 3, None, None, None),
    725319: SongMeta("Let's Dance", "David Bowie", "LEGO Rock Band", "lrb", 1, 1, 2, None, None, None, 1, None, None, None),
    725320: SongMeta("Life Is a Highway", "Rascal Flatts", "LEGO Rock Band", "lrb", 3, 3, 3, None, None, None, 4, None, None, None),
    725321: SongMeta("Make Me Smile (Come Up and See Me)", "Steve Harley & Cockney Rebel", "LEGO Rock Band", "lrb", 2, 2, 3, None, None, None, 4, None, None, None),
    725322: SongMeta("Monster", "The Automatic", "LEGO Rock Band", "lrb", 3, 1, 4, None, None, None, 1, None, None, None),
    725323: SongMeta("Naive", "The Kooks", "LEGO Rock Band", "lrb", 3, 2, 3, None, None, None, 3, None, None, None),
    725324: SongMeta("Real Wild Child", "Everlife", "LEGO Rock Band", "lrb", 5, 1, 5, None, None, None, 6, None, None, None),
    725325: SongMeta("Ride a White Swan", "T. Rex", "LEGO Rock Band", "lrb", 3, 0, 0, None, None, None, 0, None, None, None),
    725326: SongMeta("Rooftops (A Liberation Broadcast)", "Lostprophets", "LEGO Rock Band", "lrb", 2, 2, 4, None, None, None, 1, None, None, None),
    725327: SongMeta("Ruby", "Kaiser Chiefs", "LEGO Rock Band", "lrb", 2, 1, 4, None, None, None, 1, None, None, None),
    725328: SongMeta("Short and Sweet", "Spinal Tap", "LEGO Rock Band", "lrb", 4, 4, 4, None, None, None, 1, None, None, None),
    725329: SongMeta("So What", "P!nk", "LEGO Rock Band", "lrb", 2, 1, 3, None, None, None, 3, None, None, None),
    725330: SongMeta("Song 2", "Blur", "LEGO Rock Band", "lrb", 1, 0, 3, None, None, None, 0, None, None, None),
    725331: SongMeta("Stumble and Fall", "Razorlight", "LEGO Rock Band", "lrb", 3, 1, 4, None, None, None, 2, None, None, None),
    725332: SongMeta("Suddenly I See", "KT Tunstall", "LEGO Rock Band", "lrb", 3, 1, 4, None, None, None, 3, None, None, None),
    725333: SongMeta("Summer of '69", "Bryan Adams", "LEGO Rock Band", "lrb", 0, 1, 3, None, None, None, 2, None, None, None),
    725334: SongMeta("Swing, Swing", "The All-American Rejects", "LEGO Rock Band", "lrb", 0, 1, 1, None, None, None, 2, None, None, None),
    725335: SongMeta("The Final Countdown", "Europe", "LEGO Rock Band", "lrb", 5, 2, 4, None, None, None, 2, None, None, None),
    725336: SongMeta("The Passenger", "Iggy Pop", "LEGO Rock Band", "lrb", 2, 0, 3, None, None, None, 0, None, None, None),
    725337: SongMeta("Thunder", "Boys Like Girls", "LEGO Rock Band", "lrb", 1, 0, 0, None, None, None, 1, None, None, None),
    725338: SongMeta("Tick Tick Boom", "The Hives", "LEGO Rock Band", "lrb", 2, 2, 4, None, None, None, 3, None, None, None),
    725339: SongMeta("Two Princes", "Spin Doctors", "LEGO Rock Band", "lrb", 3, 4, 5, None, None, None, 3, None, None, None),
    725340: SongMeta("Valerie", "The Zutons", "LEGO Rock Band", "lrb", 2, 2, 3, None, None, None, 2, None, None, None),
    725341: SongMeta("Walking on Sunshine", "Katrina and the Waves", "LEGO Rock Band", "lrb", 2, 3, 3, None, None, None, 2, None, None, None),
    725342: SongMeta("We Are the Champions", "Queen", "LEGO Rock Band", "lrb", 1, 1, 0, None, None, None, 2, None, None, None),
    725343: SongMeta("We Will Rock You", "Queen", "LEGO Rock Band", "lrb", 0, 0, 0, None, None, None, 3, None, None, None),
    725344: SongMeta("Word Up!", "KoRn", "LEGO Rock Band", "lrb", 2, 2, 3, None, None, None, 1, None, None, None),
    725345: SongMeta("You Give Love a Bad Name", "Bon Jovi", "LEGO Rock Band", "lrb", 3, 1, 1, None, None, None, 2, None, None, None),
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
    
    