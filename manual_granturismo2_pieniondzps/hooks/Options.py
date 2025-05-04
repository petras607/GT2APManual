# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class TrophyHunt(Toggle):
    """
    Enables Trophy Hunt for the victory condition of your choice.
    In addition to winning a specified tier of GT League, you'll also need to collect a certain amount of Trophies to win.
    """

class TrophyTotal(Range):
    """
    How many Trophies should be added to the pool.
    Applies only if Trophy Hunt is enabled.
    Default is 15
    """
    display_name = "Trophy total"
    range_start = 1
    range_end = 250
    default = 15

class TrophyRequired(Range):
    """
    How many Trophies should be required to reach goal.
    Note that if it's set higher than trophy total it will increase the total count so it matches the required count.
    Applies only if Trophy Hunt is enabled.
    Default is 10
    """
    display_name = "Trophy required"
    range_start = 1
    range_end = 200
    default = 10

class LimitStarterCars(Choice):
    """
    Limits car permits you can get as your starting item.
    [strict] Will give a manufacturer that includes a car priced under 10k Credits and is powerful enough to reasonably clear content: Daihatsu, Honda & Acura, Mazda, Mitsubishi, Nissan, Suzuki, Toyota
    [loose] Will give a manufacturer that includes a car priced under 10k Credits with no regard to its viability: Daihatsu, Fiat, Honda & Acura, Mazda, Mitsubishi, Nissan, Suzuki, Toyota
    [none] Any manufacturer can become your starting item. Usually makes progression impossible without cheating in Credits.
    """
    display_name = "Limit starter cars"
    option_strict = 0
    option_loose = 1
    option_none = 2
    default = 0

class ProgressiveTires(Toggle):
    """
    Makes Racing Tires progressive instead of being individual items for every tire type.
    No impact on progression but may make the playthrough more difficult.
    """
    display_name = "Make Racing Tires progressive"

class SimulationHeadStart(Toggle):
    """
    Adds following upgrades to your starting items:
    Sports Tires, one Weight Reduction, one NA Tune and one Turbo.
    """
    display_name = "Simulation mode head start"

class SpecialEvents(DefaultOnToggle):
    """
    Adds races under Special Events tab to the location pool.
    """

class LicenseTests(Toggle):
    """
    Adds license tests to the location pool.
    """
    display_name = "License tests"

class RallyEvents(Choice):
    """
    Adds rallies to the location pool.
    [none] Disables rallies
    [simulation] Only adds Simulation mode rallies
    [arcade] Only adds Arcade mode rallies
    [both] Adds rallies in both Simulation and Arcade modes
    Arcade mode rallies are only added if Arcade mode is enabled.
    """
    display_name = "Rally events"
    option_none = 0
    option_simulation = 1
    option_arcade = 2
    option_both = 3
    default = 0

class EnduranceEvents(Toggle):
    """
    Adds endurance events to the location pool.
    Each location enabled with this option will take 1-2 hours to clear.
    """
    display_name = "Endurance events"

class ManufacturerEvents(Choice):
    """
    Adds manufacturer events to the location pool.
    [none] Disables manufacturer events
    [normal] Adds only Normal style events
    [racing] Adds only Racing style events
    [both] Adds both Normal and Racing styles
    Participation in Racing style events requires a race modified car.
    Requires buying and upgrading tons of cars, which may not be feasible without cheats.
    """
    display_name = "Manufacturer events"
    option_none = 0
    option_normal = 1
    option_racing = 2
    option_both = 3
    default = 0

class ArcadeMode(Toggle):
    """
    Adds Arcade mode to the location pool.
    """
    display_name = "Arcade mode content"

class ArcadeTimeTrials(Toggle):
    """
    Adds Arcade mode's time trials to the location pool.
    Applies only when Arcade mode is enabled.
    """
    display_name = "Arcade time trials"

class ArcadeReverse(Choice):
    """
    Adds Arcade mode's reversed tracks to the location pool.
    [none] Disables reversed tracks
    [race] Adds only races in reversed tracks
    [time_trial] Adds only time trials in reversed tracks
    [both] Adds both races and time trials in reversed tracks
    Applies only when Arcade mode is enabled. Unlocking reversed tracks requires winning a race in Difficult mode.
    """
    display_name = "Arcade reverse tracks"
    option_none = 0
    option_race = 1
    option_time_trial = 2
    option_both = 3
    default = 0

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["trophy_hunt"] = TrophyHunt
    options["trophy_total"] = TrophyTotal
    options["trophy_required"] = TrophyRequired
    options["limit_starter_cars"] = LimitStarterCars
    options["simulation_head_start"] = SimulationHeadStart
    options["progressive_tires"] = ProgressiveTires
    options["special_events"] = SpecialEvents
    options["license_tests"] = LicenseTests
    options["rally_events"] = RallyEvents
    options["endurance_events"] = EnduranceEvents
    options["manufacturer_events"] = ManufacturerEvents
    options["arcade"] = ArcadeMode
    options["arcade_time_trials"] = ArcadeTimeTrials
    options["arcade_reverse"] = ArcadeReverse
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options