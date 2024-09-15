define d = Character("Delinquent")

label delinquent:

    scene bg alley

    show delinquent

    n "Better watch out in this part of town."
    call boost_stat(cun)

    return
