from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range

from .songinfo import Songs

class TotalSongs(Range):
    """
    The total amount of songs in the multiworld.
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


@dataclass
class YARGOptions(PerGameCommonOptions):
    total_songs: TotalSongs
    percent_of_gems_generated: PercentOfGemsGenerated
    goal_song_visibility: GoalSongVisibility
    deathlink: DeathLink

option_groups = [
    OptionGroup(
        "Song Selection Options",
        [TotalSongs, PercentOfGemsGenerated],
    ),
    OptionGroup(
        "Visibility Options",
        [GoalSongVisibility]
    ),
]