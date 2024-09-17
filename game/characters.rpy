init -1 define characters = {
    "sporty": char_sporty, 
    "artsy": char_artsy, 
    "nerdy": char_nerdy, 
    "popular": char_popular, 
    "delinquent": char_delinquent
}

init define affections = {
    "sporty": 0,
    "artsy": 0,
    "nerdy": 0,
    "popular": 0,
    "delinquent": 0
}

label boost_affection(name):
    $ affections[name] += 1
    $ pretty_name = characters[name]["name_pretty"]
    "I feel a bit closer to [pretty_name]."
    return

transform size_normal:
    ysize 600
    fit "contain"