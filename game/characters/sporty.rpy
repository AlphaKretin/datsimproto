init -2 define char_sporty = Girl("sporty", "Sporty", ["park", "park", None])

label scene_sporty_park(sayer):
    show sporty at center, size_normal

    sayer "Hey, let's go for a jog!"
    call boost_stat(fit)

    return
