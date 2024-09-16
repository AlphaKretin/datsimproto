init -2 define char_artsy = {
    "name": "artsy",
    "name_pretty": "Artsy",
    "sayer": Character("Artsy"),
    "schedule": ["gallery", "gallery", None]
}

label scene_artsy_gallery(sayer):
    show artsy

    sayer "Look at this photograph!"
    call boost_stat(cre)

    return