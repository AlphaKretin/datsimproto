init python:
    import json
    locations_file = renpy.open_file("locations.json", "utf-8")
    locations = json.load(locations_file)

screen map_screen():
    vbox:
        for name in locations:
            $ print(locations[name])
            $ name_pretty = locations[name]["name_pretty"]
            textbutton "[name_pretty]" action [Call("load_map",name)]

label load_map(name):
    scene expression "bg " + name
    "test message"

label map_menu:

    scene bg city

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