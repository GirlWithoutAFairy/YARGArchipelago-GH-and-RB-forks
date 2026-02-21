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
#03 represents third entry (Rock Band 3)
#ZZ represents unique song identifier (incremental)

Songs: Dict[int, SongMeta] = {
    "720301": SongMeta("Whip It", "Devo", "Rock Band 3", "rb3",  2, 3, 3, None, 0, 0, 0, 0, None, None,),
    "720302": SongMeta("King George", "Dover", "Rock Band 3", "rb3",  4, 3, 4, None, None, None, 3, 3, 3, None,),
    "720303": SongMeta("Get Up, Stand Up", "Bob Marley and the Wailers", "Rock Band 3", "rb3",  1, 4, 2, None, 3, 2, 5, 5, 5, None,),
    "720304": SongMeta("MidLife Crisis", "Faith No More", "Rock Band 3", "rb3",  1, 1, 3, None, 1, 3, 4, 4, 4, None,),
    "720305": SongMeta("Rehab", "Amy Winehouse", "Rock Band 3", "rb3",  0, 1, 4, None, 4, 4, 3, 3, 3, None,),
    "720306": SongMeta("One Armed Scissor", "At the Drive-In", "Rock Band 3", "rb3",  5, 4, 5, None, None, None, 6, 6, None, None,),
    "720307": SongMeta("Foolin'", "Def Leppard", "Rock Band 3", "rb3",  4, 4, 2, None, 2, 2, 6, 6, 6, None,),
    "720308": SongMeta("Walk of Life", "Dire Straits", "Rock Band 3", "rb3",  6, 5, 0, None, 5, 2, 3, 3, 3, None,),
    "720309": SongMeta("Heart of Glass", "Blondie", "Rock Band 3", "rb3",  2, 1, 4, None, 1, 1, 3, 3, None, None,),
    "720310": SongMeta("Smoke on the Water", "Deep Purple", "Rock Band 3", "rb3",  0, 0, 6, None, 5, 5, 1, 1, None, None,),
    "720311": SongMeta("Space Oddity", "David Bowie", "Rock Band 3", "rb3",  1, 2, 1, None, 3, 3, 1, 1, 1, None,),
    "720312": SongMeta("Beast and the Harlot", "Avenged Sevenfold", "Rock Band 3", "rb3",  5, 6, 6, None, None, None, 5, 5, 5, None,),
    "720313": SongMeta("In a Big Country", "Big Country", "Rock Band 3", "rb3",  3, 6, 1, None, 4, 5, 2, 2, 2, None,),
    "720314": SongMeta("The Killing Moon", "Echo & The Bunnymen", "Rock Band 3", "rb3",  4, 3, 5, None, 2, 2, 3, None, None, None,),
    "720315": SongMeta("Rainbow in the Dark", "Dio", "Rock Band 3", "rb3",  6, 4, 2, None, 1, 0, 2, 2, None, None,),
    "720316": SongMeta("Caught in a Mosh", "Anthrax", "Rock Band 3", "rb3",  6, 6, 6, None, None, None, 5, 5, 5, None,),
    "720317": SongMeta("25 or 6 to 4", "Chicago", "Rock Band 3", "rb3",  6, 5, 6, None, 5, 4, 4, 4, 4, None,),
    "720318": SongMeta("Saturday Night's Alright for Fighting", "Elton John", "Rock Band 3", "rb3",  5, 5, 2, None, 6, 6, 2, None, None, None,),
    "720319": SongMeta("Killing Loneliness", "H.I.M.", "Rock Band 3", "rb3",  5, 2, 1, None, 3, 3, 2, 2, 2, None,),
    "720320": SongMeta("Oh My God", "Ida Maria", "Rock Band 3", "rb3",  3, 3, 4, None, 0, 0, 4, 4, 4, None,),
    "720321": SongMeta("Been Caught Stealing", "Jane's Addiction", "Rock Band 3", "rb3",  6, 5, 5, None, None, None, 5, 5, 5, None,),
    "720322": SongMeta("Imagine", "John Lennon", "Rock Band 3", "rb3",  None, 0, 0, None, 2, 2, 0, None, None, None,),
    "720323": SongMeta("Cold as Ice", "Foreigner", "Rock Band 3", "rb3",  0, 2, 3, None, 6, 5, 4, 4, 4, None,),
    "720324": SongMeta("The Power of Love", "Huey Lewis and the News", "Rock Band 3", "rb3",  5, 4, 0, None, 3, 3, 5, 5, 5, None,),
    "720325": SongMeta("Hey Man Nice Shot", "Filter", "Rock Band 3", "rb3",  3, 6, 1, None, None, None, 2, None, None, None,),
    "720326": SongMeta("Viva la Resistance", "Hypernova", "Rock Band 3", "rb3",  4, 4, 6, None, None, None, 5, 5, None, None,),
    "720327": SongMeta("I Got You (I Feel Good)", "James Brown", "Rock Band 3", "rb3",  4, 6, 3, None, 6, 6, 6, None, None, None,),
    "720328": SongMeta("Need You Tonight", "INXS", "Rock Band 3", "rb3",  0, 0, 4, None, 0, 0, 5, 5, 5, None,),
    "720329": SongMeta("Combat Baby", "Metric", "Rock Band 3", "rb3",  3, 3, 3, None, 0, 0, 4, None, None, None,),
    "720330": SongMeta("The Beautiful People", "Marilyn Manson", "Rock Band 3", "rb3",  3, 3, 5, None, 0, 0, 2, 2, None, None,),
    "720331": SongMeta("I Love Rock N' Roll", "Joan Jett & The Blackhearts", "Rock Band 3", "rb3",  1, 0, 0, None, 1, 1, 0, 0, None, None,),
    "720332": SongMeta("Me Enamora", "Juanes", "Rock Band 3", "rb3",  1, 1, 4, None, 4, 4, 6, 6, 6, None,),
    "720333": SongMeta("Radar Love", "Golden Earring", "Rock Band 3", "rb3",  6, 5, 6, None, 0, 0, 1, 1, 1, None,),
    "720334": SongMeta("Sister Christian", "Night Ranger", "Rock Band 3", "rb3",  5, 0, 1, None, 5, 6, 2, 2, 2, None,),
    "720335": SongMeta("Oye Mi Amor", "ManÃ¡", "Rock Band 3", "rb3",  1, 1, 3, None, 2, 2, 4, 4, None, None,),
    "720336": SongMeta("Free Bird", "Lynyrd Skynyrd", "Rock Band 3", "rb3",  6, 6, 3, None, 6, 6, 0, None, None, None,),
    "720337": SongMeta("Crazy Train", "Ozzy Osbourne", "Rock Band 3", "rb3",  6, 6, 6, None, None, None, 0, 0, None, None,),
    "720338": SongMeta("Jerry Was a Race Car Driver", "Primus", "Rock Band 3", "rb3",  2, 5, 6, None, None, None, 0, None, None, None,),
    "720339": SongMeta("Misery Business", "Paramore", "Rock Band 3", "rb3",  3, 4, 5, None, None, None, 6, 6, 6, None,),
    "720340": SongMeta("Lasso", "Phoenix", "Rock Band 3", "rb3",  5, 5, 4, None, None, None, 6, None, None, None,),
    "720341": SongMeta("Bohemian Rhapsody", "Queen", "Rock Band 3", "rb3",  4, 4, 3, None, 6, 6, 6, 6, 6, None,),
    "720342": SongMeta("Don't Bury Me... I'm Still Not Dead", "Riverboat Gamblers", "Rock Band 3", "rb3",  3, 2, 4, None, None, None, 2, 2, None, None,),
    "720343": SongMeta("Fly Like an Eagle", "Steve Miller Band", "Rock Band 3", "rb3",  0, 5, 5, None, 5, 5, 1, 1, None, None,),
    "720344": SongMeta("Du Hast", "Rammstein", "Rock Band 3", "rb3",  2, 1, 4, None, 5, 5, 3, 3, 3, None,),
    "720345": SongMeta("Walking on the Sun", "Smash Mouth", "Rock Band 3", "rb3",  0, 0, 0, None, 2, 2, 3, 3, None, None,),
    "720346": SongMeta("The Look", "Roxette", "Rock Band 3", "rb3",  4, 6, 2, None, 5, 5, 1, 1, 1, None,),
    "720347": SongMeta("In the Meantime", "Spacehog", "Rock Band 3", "rb3",  4, 1, 4, None, 1, 1, 5, 5, 5, None,),
    "720348": SongMeta("No One Knows", "Queens of the Stone Age", "Rock Band 3", "rb3",  5, 6, 6, None, None, None, 3, 3, 3, None,),
    "720349": SongMeta("Llama", "Phish", "Rock Band 3", "rb3",  6, 6, 6, None, 6, 6, 6, 6, 6, None,),
    "720350": SongMeta("Something Bigger, Something Brighter", "Pretty Girls Make Graves", "Rock Band 3", "rb3",  6, 1, 3, None, 4, 4, 0, 0, None, None,),
    "720351": SongMeta("Before I Forget", "Slipknot", "Rock Band 3", "rb3",  6, 5, 5, None, 0, 0, 0, 0, None, None,),
    "720352": SongMeta("Antibodies", "Poni Hoax", "Rock Band 3", "rb3",  2, 6, 3, None, 6, 6, 1, None, None, None,),
    "720353": SongMeta("Portions for Foxes", "Rilo Kiley", "Rock Band 3", "rb3",  4, 2, 3, None, 4, 4, 1, 1, 1, None,),
    "720354": SongMeta("Plush", "Stone Temple Pilots", "Rock Band 3", "rb3",  3, 2, 2, None, None, None, 2, None, None, None,),
    "720355": SongMeta("Good Vibrations (Live)", "The Beach Boys", "Rock Band 3", "rb3",  1, 1, 1, None, 3, 4, 6, 6, 6, None,),
    "720356": SongMeta("The Con", "Tegan and Sara", "Rock Band 3", "rb3",  2, 2, 2, None, 0, 1, 6, 6, None, None,),
    "720357": SongMeta("20th Century Boy", "T. Rex", "Rock Band 3", "rb3",  4, 3, 2, None, 4, 5, 4, 4, 4, None,),
    "720358": SongMeta("Break on Through (To the Other Side)", "The Doors", "Rock Band 3", "rb3",  3, 5, 4, None, 4, 4, 1, None, None, None,),
    "720359": SongMeta("Centerfold", "The J. Geils Band", "Rock Band 3", "rb3",  2, 4, 0, None, 4, 4, 5, 5, 5, None,),
    "720360": SongMeta("Just Like Heaven", "The Cure", "Rock Band 3", "rb3",  1, 0, 0, None, 0, 1, 1, 1, None, None,),
    "720361": SongMeta("Outer Space", "The Muffs", "Rock Band 3", "rb3",  0, 0, 0, None, None, None, 5, 5, 5, None,),
    "720362": SongMeta("Living in America", "The Sounds", "Rock Band 3", "rb3",  0, 2, 2, None, 4, 4, 2, 2, None, None,),
    "720363": SongMeta("I Wanna Be Sedated", "Ramones", "Rock Band 3", "rb3",  2, 1, 0, None, None, None, 0, None, None, None,),
    "720364": SongMeta("I Need to Know", "Tom Petty and the Heartbreakers", "Rock Band 3", "rb3",  3, 2, 1, None, 3, 3, 4, 4, None, None,),
    "720365": SongMeta("Dead End Friends", "Them Crooked Vultures", "Rock Band 3", "rb3",  5, 5, 5, None, 4, 4, 4, 4, None, None,),
    "720366": SongMeta("The Hardest Button to Button", "The White Stripes", "Rock Band 3", "rb3",  0, 0, 2, None, None, None, 5, None, None, None,),
    "720367": SongMeta("Last Dance", "The Raveonettes", "Rock Band 3", "rb3",  0, 0, 1, None, 2, 1, 1, 1, 1, None,),
    "720368": SongMeta("Werewolves of London", "Warren Zevon", "Rock Band 3", "rb3",  1, 4, 1, None, 1, 1, 0, None, None, None,),
    "720369": SongMeta("False Alarm", "The Bronx", "Rock Band 3", "rb3",  5, 4, 5, None, None, None, 1, None, None, None,),
    "720370": SongMeta("This Bastard's Life", "Swingin' Utters", "Rock Band 3", "rb3",  2, 5, 1, None, 5, 5, 2, 2, 2, None,),
    "720371": SongMeta("Roundabout", "Yes", "Rock Band 3", "rb3",  6, 6, 6, None, 6, 6, 5, 5, 5, None,),
    "720372": SongMeta("Rock Lobster", "The B-52's", "Rock Band 3", "rb3",  4, 2, 5, None, 1, 1, 5, 5, 5, None,),
    "720373": SongMeta("China Grove", "The Doobie Brothers", "Rock Band 3", "rb3",  2, 3, 3, None, 6, 6, 3, 3, 3, None,),
    "720374": SongMeta("Crosstown Traffic", "The Jimi Hendrix Experience", "Rock Band 3", "rb3",  5, 4, 4, None, 5, 5, 6, 6, 6, None,),
    "720375": SongMeta("Everybody Wants to Rule the World", "Tears for Fears", "Rock Band 3", "rb3",  1, 3, 5, None, 2, 2, 3, 3, None, None,),
    "720376": SongMeta("Yoshimi Battles the Pink Robots Pt. 1", "The Flaming Lips", "Rock Band 3", "rb3",  2, 0, 1, None, 1, 2, 0, 0, 0, None,),
    "720377": SongMeta("Get Free", "The Vines", "Rock Band 3", "rb3",  1, 2, 2, None, None, None, 4, 4, 4, None,),
    "720378": SongMeta("Don't Stand So Close to Me", "The Police", "Rock Band 3", "rb3",  4, 3, 1, None, 2, 3, 4, 4, 4, None,),
    "720379": SongMeta("Low Rider", "WAR", "Rock Band 3", "rb3",  0, 3, 0, None, 3, 3, 1, None, None, None,),
    "720380": SongMeta("Humanoid", "Tokio Hotel", "Rock Band 3", "rb3",  3, 3, 5, None, 3, 1, 6, 6, 6, None,),
    "720381": SongMeta("I Can See for Miles", "The Who", "Rock Band 3", "rb3",  2, 1, 6, None, None, None, 2, 2, 2, None,),
    "720382": SongMeta("Here I Go Again", "Whitesnake", "Rock Band 3", "rb3",  5, 1, 2, None, 2, 3, 4, 4, None, None,),
    "720383": SongMeta("Stop Me if You Think You've Heard This One Before", "The Smiths", "Rock Band 3", "rb3",  3, 2, 0, None, 1, 0, 3, None, None, None,),
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
    
    