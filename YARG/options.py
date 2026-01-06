from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, OptionSet, DefaultOnToggle

from .songinfo import Songs

class TotalSongs(Range):
    """
    The total amount of songs in the multiworld.

    Note: Final song count may be lowered if there are not enough songs
    in the enabled setlists.
    """

    display_name = "Total Songs"

    range_start = 5
    range_end = len(Songs)

    default = 10

class PercentOfGemsGenerated(Range):
    """
    Percent of total YARG Gems generated. Based on a percentage of Total Songs.
    """

    display_name = "Percent of Gems Generated"

    range_start = 0
    range_end = 100

    default = 80

class EnabledSetlists(OptionSet):
    """
    Select the setlists you want to play/have downloaded.
    """

    display_name = "Enabled Setlists"

    setlistkeys = set()

    for key, data in Songs.items():
        setlistkeys.add(str(data.group))

    valid_keys = setlistkeys

    defaultsetlist = ['YARG Official Setlist']
    default = frozenset(defaultsetlist)

class GoalSongVisibility(Choice):
    """
    Sets when you are able to see your goal song.
    
    Full: You can always see your goal song
    Song: You only need the song unlock to see your goal song
    Gems: You only need the amount of required gems to see your goal song
    Song and Gems: You need both the song unlock and the amount of gems to see your goal song

    Note: This does not effect logic at all
    """

    display_name = "Goal Song Visibility"

    option_full = 0
    option_song = 1
    option_gems = 2
    option_song_and_gems = 3

    default = option_full

class DeathLink(Choice):
    """
    When you die, everyone who enabled
    death link dies. Of course, the reverse
    is true too.

    One Hit: Leaves you with 1 health in the
    rock meter, one note away from failing,
    but you can recover.

    Instant: Instant fail on recieving a
    death link.
    """

    display_name = "Death Link"

    option_disabled = 0
    option_one_hit = 1
    option_instant = 2

    default = option_disabled

    alias_enabled = option_instant

class EnergyLink(DefaultOnToggle):
    """
    Adds your score at the end of a song
    to the Archipelago Energy Link!
    """

    display_name = "Energy Link"


@dataclass
class YARGOptions(PerGameCommonOptions):
    total_songs: TotalSongs
    percent_of_gems_generated: PercentOfGemsGenerated
    goal_song_visibility: GoalSongVisibility
    deathlink: DeathLink
    enabled_setlists: EnabledSetlists
    energylink: EnergyLink

option_groups = [
    OptionGroup(
        "Song Selection Options",
        [TotalSongs, PercentOfGemsGenerated, EnabledSetlists],
    ),
    OptionGroup(
        "Visibility Options",
        [GoalSongVisibility]
    ),
]