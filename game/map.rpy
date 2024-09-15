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