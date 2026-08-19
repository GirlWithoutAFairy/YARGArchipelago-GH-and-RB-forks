from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups

class YARGBandHeroWebWorld(WebWorld):
    game = "YARGBandHero"

    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up YARG for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Energymaster22"],
    )
    
    tutorials = [setup_en]

    option_groups = option_groups