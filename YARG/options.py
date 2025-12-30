from dataclasses import dataclass

from Options import OptionGroup, PerGameCommonOptions, Range

from .songinfo import Songs

class TotalSongs(Range):
    """
    The total amount of songs in the multiworld.
    """

    display_name = "Total Songs"

    range_start = 5
    range_end = len(Songs)

    default = 10

@dataclass
class YARGOptions(PerGameCommonOptions):
    total_songs: TotalSongs

option_groups = [
    OptionGroup(
        "Song Selection Options",
        [TotalSongs],
    ),
]