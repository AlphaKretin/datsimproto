﻿init -2 define char_delinquent = Girl("delinquent", "Delinquent", ["alleyway", "alleyway", None])

label scene_delinquent_alleyway(sayer):
    show delinquent at center, size_normal

    sayer "Better watch out in this part of town."
    call boost_stat(cun)

    return