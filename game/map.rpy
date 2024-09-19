init python:
    import json
    locations_file = renpy.open_file("locations.json", "utf-8")
    locations = json.load(locations_file)

default time = 0

screen debug_screen():
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
            $ aff = affections[char[1].name]
            text "[name_pretty]: [aff]"

screen map_screen():
    add "images/bgs/bg city.png"
    default hoveredIcon = ""
    text f"{hoveredIcon}" at center, top
    for name in locations:
        $ name_pretty = locations[name]["name_pretty"]
        $ x = locations[name]["pos_x"]
        $ y = locations[name]["pos_y"]
        imagebutton:
            pos (x,y)
            xysize (64,64)
            anchor (0.5,0.5)
            auto f"images/icons/button_{name}_%s.png"
            hovered SetScreenVariable("hoveredIcon", name_pretty)
            unhovered SetScreenVariable("hoveredIcon", "")
            action Call("load_map", name)

label load_map(name):
    scene expression "bg " + name
    $ met_someone = None
    python:
        for _,character in characters.items():
            if character.schedule[time] == name:
                met_someone = character.name
                renpy.call("scene_" + character.name + "_" + name, character.sayer)
    if met_someone != None:
        call expression "boost_affection" pass (met_someone)
    else:
        "Doesn't look like anyone's here right now..."
    $ time = (time + 1) % 3

label map_menu:
    # scene bg city
    show screen debug_screen()
    call screen map_screen()

    return