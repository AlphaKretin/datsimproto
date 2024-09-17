init -2 define char_nerdy = {
    "name": "nerdy",
    "name_pretty": "Nerdy",
    "sayer": Character("Nerdy"),
    "schedule": ["library", "library", "alleyway"]
}

label scene_nerdy_library(sayer):
    show nerdy at center, size_normal

    sayer "Help me study this textbook."
    call boost_stat(kno)

    return

label scene_nerdy_alleyway(sayer):
    show nerdy at center, size_normal

    sayer "I'm getting parts for my experiments."
    call boost_stat(cun)

    return