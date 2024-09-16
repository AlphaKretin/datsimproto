init python:
    import json
    locations_file = renpy.open_file("locations.json", "utf-8")
    locations = json.load(locations_file)

define time = 0

screen debug_screen():
    vbox:
        text "Fitness: [stats[fit]]"
        text "Knowledge: [stats[kno]]"
        text "Fashion: [stats[fas]]"
        text "Cunning: [stats[cun]]"
        text "Creativity: [stats[cre]]"
        text "Time: [time]"

screen map_screen():
    vbox:
        for name in locations:
            $ print(locations[name])
            $ name_pretty = locations[name]["name_pretty"]
            textbutton "[name_pretty]" action [Call("load_map",name)]

label load_map(name):
    scene expression "bg " + name
    $ met_someone = False
    python:
        for character in characters:
            print(character)
            if character["schedule"][time] == name:
                met_someone = True
                renpy.call("scene_" + character["name"] + "_" + name, character["sayer"])
    if not met_someone:
        "Doesn't look like anyone's here right now..."
    $ time = (time + 1) % 3

label map_menu:

    scene bg city
    show screen debug_screen()
    call screen map_screen()

    # menu:
    #     "Where should I go?"

    #     "Park":
    #         call sporty
        
    #     "Library":
    #         call nerdy
        
    #     "Mall":
    #         call popular

    #     "Gallery":
    #         call artsy

    #     "Alleyway":
    #         call delinquent
        
    #     "(DEBUG) Check Stats":
    #         call check_stats

    return