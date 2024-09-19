
init -2 define char_artsy = Girl("artsy", "Artsy", ["gallery", "gallery", None])

label scene_artsy_gallery(sayer):
    show artsy at center, size_normal

    sayer "Look at this photograph!"
    call boost_stat(cre)

    return