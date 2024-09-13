# The script of the game goes in this file.

define s = Character("Sporty")

# The game starts here.

label sporty:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg park

    show sporty

    s "Hey, let's go for a jog!"
    call boost_stat(fit)

    return
