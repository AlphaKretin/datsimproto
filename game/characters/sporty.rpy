init -2 define char_sporty = {
    "name": "sporty",
    "name_pretty": "Sporty",
    "sayer": Character("Sporty"),
    "schedule": ["park", "park", None]
}

label scene_sporty_park(sayer):
    show sporty at center, size_normal

    sayer "Hey, let's go for a jog!"
    call boost_stat(fit)

    return
