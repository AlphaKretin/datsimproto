init -3 python:
    class Location():
        def __init__(self, loc_name, location):
            self.name = loc_name
            self.name_pretty = location["name_pretty"]
            self.pos = (location["pos_x"], location["pos_y"])
            self.button = f"images/icons/button_{self.name}_%s.png"
