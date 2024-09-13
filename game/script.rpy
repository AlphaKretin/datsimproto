# The script of the game goes in this file.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    label map_menu:

    scene bg city

    menu:
        "Where should I go?"

        "Park":
            call sporty
        
        "Library":
            call nerdy
        
        "Mall":
            call popular

        "Gallery":
            call artsy

        "Alleyway":
            call delinquent
        
        "(DEBUG) Check Stats":
            call check_stats

    jump map_menu
