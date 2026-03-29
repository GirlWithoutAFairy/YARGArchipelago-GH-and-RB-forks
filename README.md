This is an Archipelago implementation for the open source, plastic band rhythm game, YARG!

# Setup
1. Download the YARC Launcher from https://yarg.in/
2. Inside the YARC Launcher download "YARG Nightly" and the "YARG Official Setlist"
3. Download the YARGAPClient from https://github.com/energymaster22/YARGAPClient/releases/latest
4. Download Archipelago from https://github.com/ArchipelagoMW/Archipelago/releases/latest
5. Set up Archipelago
6. Download any of the apworlds from the Releases tab.
7. Make sure to check the Current Notes section of this readme for any specific information about your apworld. If you're using the AllSetlists world, take note of any notes mentioned for any of the setlists you intend to use.
8. Double click the apworld to install it into Archipelago
9. Select "Generate Template Options" from within Archipelago to get a default YAML
10. Edit the yaml to your liking and put it in your "Players" folder (should be one folder up from the "Templates" folder the previous step opened)
11. Select "Generate" from within Archipelago
12. Host your outputed multiworld either on https://archipelago.gg/ or locally
13. Launch the YARGAPClient
14. Scan the directory that contains your songs in the YARG Settings menu
15. Click "Archipelago" on the main menu to open the login screen
16. Input the host address, port, slot name, and game ID and press connect! (Game ID should not be left blank if playing on a fork) (A blank Game ID field will make the client try to use the default YARG apworld) (The Game ID is always the string of characters in the name of the apworld file after YARG)

# Ripping Songs
I will not provide a tutorial on how to dump your ISOs as that is console dependant. Consult guides for your specific console.

Unless stated otherwise, the Xbox 360 version was used as the template for this process.

For Guitar Hero 1, the PS2 version was used.

Your mileage may vary if you use an ISO from a different platform.

ISOs from the PC versions of Guitar Hero 3, Guitar Hero Aerosmith, and Guitar Hero World Tour will NOT work. These were installation discs.

If you have already ripped your songs for use in YARG, skip to the section on testing your rips.

1. Download Onyx rhythm game toolkit and install it. Version 20251011 was used for this guide. https://github.com/mtolly/onyx/releases/tag/20251011
2. Launch Onyx
3. Click the button labeled Batch Recompile
4. Click the button labeled Add Song in the second window that popped up and select your ISO
5. Click the Clone Hero tab at the top of the window and click the button labeled Create CH Folders
6. Wait. This will take some time.
7. Feel free to delete any charts that are labeled as Dummy, Test, Callibration, Tutorial, or Co-op. They will not be used.

# Testing Your Rips
1. Ensure that your rips are scanned into YARG and appear in the Quickplay menu.
2. Generate a seed with the maximum amount of songs. Take note of the Enabled Setlists and Total Songs settings.
3. Host your seed either on archipelago.gg or locally and connect the client.
4. Make sure to enter the Game ID for your specific apworld.
5. If it tells you there are missing songs and those songs don't show up in Quickplay, then either they are missing from your folders or you did not scan your songs.
6. If it tells you there are missing songs and those songs do show up in Quickplay, then they have incorrect metadata. Refer to the Metadata section.
7. If it doesn't give you an error, then you're all set.

# Metadata
1. If the error you got in the client only showed a few songs, you can download the necessary fixes by browsing the files in the repository under the metadata folder.
2. If the error showed a lot of missing songs, you can download these in a batch using the .zip files in the Releases tab.
3. Copy past the song.ini files I provided into the folders with your songs. Overwrite the original file.
4. Make sure to scan your songs in YARG again before attempting to reconnect.
5. Repeat the steps in the Testing Your Rips section and this section until it says that no songs are missing.

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

The YARGAllSetlists apworld uses slightly longer item and location names to account for the same song appearing in multiple setlists.

## Valid Setlists
These are the exact names of the setlists used for the Enabled Setlists setting in your yaml. I highly recommend using the Options Creator for this specific setting.

### Guitar Hero 1
- Guitar Hero 1
- GH! Hidden Songs

The Hidden Songs are Trippolette and Graveyard Shift. These songs were present on the Guitar Hero 1 disc but were only accessible when using cheat devices. They have been made optional for purity.

### Guitar Hero World Tour
- Guitar Hero World Tour
- GHWT Guitar Battles

The Guitar Battles can be slightly boring to play alone and they are also not licensed songs. They have been made optional because some people will likely want to just exclude them. Do note that the Guitar Battles are the only songs to support the Rhythm Guitar instrument. If you enable Rhythm Guitar within Instrument Shuffle without this setlist enabled, generation is likely to fail.

### Rock Band 3
- Rock Band 3
- RB3 Oye Mi Amor

Oye Mi Amor is prone to not ripping properly depending on the specific version of the game you rip the song from. This is made worse by the fact that Rock Band 3 had multiple physical versions released on some platforms. This song has been made optional to account for people who may have trouble with this song not working. I highly recommend you attempt a full playthrough of this song in YARG to make sure it works properly before enabling it in your seeds.

### All Setlists
All the above setlists and warnings apply.
 - YARG Official Setlist
 - Assorted Rock 1
 - Assorted Electronic 1
 - SUMMERTIDE
 - WNADERKID
 - Classical Keys Pack 1
 - Children's Keys Pack 1
 - Christmas Keys 1
 - Assorted Metal 1
 - Classical Keys Pack 2
 - Children's Keys Pack 2
 - Assorted Rock 2
 - The Slip
 - Assorted Metal 2
 - Christmas Keys 2
 - UNBEATABLE 01
 - YARN Pack 1
 - Mini-Wave 0
 - Abyss of Time
 - FX4
 - YARN Pack 2
 - Plastic Death
 - The Water Cycle
 - YARN Pack 3
 - Teto Pack
 - YARN Request Pack 1
