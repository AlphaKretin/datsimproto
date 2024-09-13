define fit = "fitness"
define kno = "knowledge"
define fas = "fashion"
define cun = "cunning"
define cre = "creativity"

define stats = {
    "fitness": 0,
    "knowledge": 0,
    "fashion": 0,
    "cunning": 0,
    "creativity": 0
}

label boost_stat(stat):
    $ stats[stat] += 1
    "Your [stat] increased."
    return

label check_stats:
    "Fitness: [stats[fit]]"
    "Knowledge: [stats[kno]]"
    "Fashion: [stats[fas]]"
    "Cunning: [stats[cun]]"
    "Creativity: [stats[cre]]"