define locations = {}

init python:
    import json
    locations_file = renpy.open_file("locations.json", "utf-8")
    locations_raw = json.load(locations_file)
    for loc_name, location in locations_raw.items():
        locations[loc_name] = Location(loc_name, location)

default time = 0

define DEBUG = True

screen map_screen():
    add "images/bgs/bg city.png"
    default hoveredIcon = ""
    text f"{hoveredIcon}" at center, top
    for map_name in locations:
        $ name_pretty = locations[map_name].name_pretty
        $ map_position = locations[map_name].pos
        $ map_button = locations[map_name].button
        imagebutton:
            pos map_position
            xysize (64,64)
            anchor (0.5,0.5)
            auto map_button
            hovered SetScreenVariable("hoveredIcon", name_pretty)
            unhovered SetScreenVariable("hoveredIcon", "")
            action Call("load_map", map_name)
    if DEBUG:
        vbox:
            text "Fitness: [stats[fit]]"
            text "Knowledge: [stats[kno]]"
            text "Fashion: [stats[fas]]"
            text "Cunning: [stats[cun]]"
            text "Creativity: [stats[cre]]"
            text "Time: [time]"
            $ chars = characters.items()
            for char in chars:
                $ name_pretty = char[1].name_pretty
                $ aff = char[1].affection
                text "[name_pretty]: [aff]"

label load_map(map_name):
    scene expression "bg " + map_name
    $ met_someone = None
    python:
        for dummy,character in characters.items():
            if character.schedule[time] == map_name:
                met_someone = character.name
                renpy.call("scene_" + character.name + "_" + map_name, character.sayer)
    if met_someone != None:
        call expression "boost_affection" pass (met_someone)
    else:
        "Doesn't look like anyone's here right now..."
    $ time = (time + 1) % 3

label map_menu:
    # scene bg city
    call screen map_screen()
    show screen debug_screen()
    return