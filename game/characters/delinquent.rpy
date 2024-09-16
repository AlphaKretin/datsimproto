init -2 define char_delinquent = {
    "name": "delinquent",
    "sayer": Character("Delinquent"),
    "schedule": ["alleyway", "alleyway", None]
}

label scene_delinquent_alleyway(sayer):
    show delinquent

    sayer "Better watch out in this part of town."
    call boost_stat(cun)

    return