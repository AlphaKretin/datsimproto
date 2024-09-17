init -2 define char_popular = {
    "name": "popular",
    "name_pretty": "Popular",
    "sayer": Character("Popular"),
    "schedule": ["mall", "mall", "gallery"]
}

label scene_popular_mall(sayer):
    show popular at center, size_normal
    sayer "Let's go shopping!"
    call boost_stat(fas)

    return

label scene_popular_gallery(sayer):
    show popular at center, size_normal

    sayer "This art is as pretty as me!"
    call boost_stat(cre)

    return
