This is an Archipelago implementation for the open source, plastic band rhythm game, YARG!

# Setup
1. Download the YARC Launcher from https://yarg.in/
2. Inside the YARC Launcher download "YARG Nightly" and the "YARG Official Setlist"
3. Download the YARGAPClient from https://github.com/energymaster22/YARGAPClient/releases/latest
4. Download Archipelago from https://github.com/ArchipelagoMW/Archipelago/releases/latest
5. Set up Archipelago
6. Download any of the apworlds from the Releases tab.
7. Double click the apworld to install it into Archipelago
8. Select "Generate Template Options" from within Archipelago to get a default YAML
9. Edit the yaml to your liking and put it in your "Players" folder (should be one folder up from the "Templates" folder the previous step opened)
10. Select "Generate" from within Archipelago
11. Host your outputed multiworld either on https://archipelago.gg/ or locally
12. Launch the YARGAPClient
13. Scan the directory that contains your songs in the YARG Settings menu
14. Click "Archipelago" on the main menu to open the login screen
15. Input the host address, port, slot name, and game ID and press connect! (Game ID should not be left blank if playing on a fork) (A blank Game ID field will make the client try to use the default YARG apworld) (The Game ID is always the string of characters in the name of the apworld file after YARG)

# Ripping Song
I will not provide a tutorial on how to dump your ISOs as that is console dependant. Consult guides for your specific console.
Unless stated otherwise, the Xbox 360 version was used as the template for this process.
For Guitar Hero 1, the PS2 version was used.
Your mileage may vary if you use an ISO from a different platform.
ISOs from the PC versions of Guitar Hero 3, Guitar Hero Aerosmith, and Guitar Hero World Tour will NOT work. These were installation discs.
If you have already ripped your songs for use in YARG, skip to the section on preparing your metadata.

1. Download Onyx rhythm game toolkit and install it. Version 20251011 was used for this guide. https://github.com/mtolly/onyx/releases/tag/20251011
2. Launch Onyx
3. Click the button labeled Batch Recompile
4. Click the button labeled Add Song in the second window that popped up and select your ISO
5. Click the Clone Hero tab at the top of the window and click the button labeled Create CH Folders
6. Wait. This will take some time.
7. Feel free to delete any charts that are labeled as Dummy, Test, Callibration, Tutorial, or Co-op. They will not be used.

# Preparing Your Metadata
There are 3 pieces of song Metadata that are expected to match in order for your songs to work.
- Song Title
- Artist
- Source
All 3 are CASE SENSITIVE.
Master spreadsheet: https://docs.google.com/spreadsheets/d/10wdItB0AMLqFk3yumJRU-aoA8UbUQdULTFpIY-ob3mw/edit?usp=sharing

1. Open the YARG AP Client
2. In the Songs Tab under the settings menu, add your folders which contain your rips. For readability, it's best if these are the only songs in your library.
3. Click the Scan Songs button.
4. Click the All Settings Tab.
5. Select the File Management submenu.
6. Click the button labeled Export Songs List (For Ouvert Bot)
7. Open SongDictTemplate.txt
8. If the songs are listed with "Unknown Source", you will need to open each song's song.ini file and add a line defining the icon for the song. Refer to the spreadsheet linked above for this data.
      Example: icon = gh1
      Note: Any changes made to song.ini will require you to use the Scan Songs button again.
10. Song Title and Artist are slightly more tricky to easily compare. Thankfully, we can do this with an Archipelago connection test.
11. Create a yaml for the specific game's setlist you are using. Make sure to set the Total Songs setting to the maximum and enable all the toggleable setlist in the Enabled Setlists setting.
12. Generate the seed.
13. Go to archipelago.gg and select Host Game under the Get Started dropdown.
14. Upload the .zip file from your Archipelago output folder and select Create New Room.
15. Connect the YARG AP client to the room. Make sure to include the game ID for your specific apworld.
16. The Client will display an error if there are any mismatches with the Song Title and Artist and will list out which songs are causing them. If no error appears, then all your songs will work.
17. Fix these errors in your song.ini files by changing the name and artist lines to match those in the spreadsheet linked above.
These are case sensitive.
Make sure to also keep an eye out for special characters such as accented letters.
18. Rescan your songs and perform a connection test again.

# Gameplay
1. Your goal in YARG AP is to find and complete your goal song!
2. The goal song may or may not be known depending on yaml settings.
3. Go into "Quickplay"
4. All of your collected songs will appear at the top in an "AP Songs" catagory
5. Play the songs that appear there to get checks for your multiworld!
6. When you get your goal song it will appear in an "AP Goal Song" catagory along with details on what you still need.
7. Collect the rest of the YARG Gems in the multiworld to fully unlock the goal song.
7. Play that song to finish the seed!

# Current Notes
"Star Power Bonus" items grant 25% Star Power upon collection\
\
If a song does not support your current instrument, or you otherwise cannot complete the song, you can use a bot player to clear it

