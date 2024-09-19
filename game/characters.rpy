init -3 python:
    class Girl():
        def __init__(self, char_name, name_pretty, schedule, color=None):
            self.name = char_name
            self.name_pretty = name_pretty
            if color != None:
                self.sayer = Character(name_pretty, color)
            else:
                self.sayer = Character(name_pretty)
            self.schedule = schedule
            self.affection = 0
        
        def boost_affection(self,amount=1):
            self.affection = self.affection + amount
            

init -1 define characters = {
    "sporty": char_sporty, 
    "artsy": char_artsy, 
    "nerdy": char_nerdy, 
    "popular": char_popular, 
    "delinquent": char_delinquent
}

label boost_affection(char_name):
    $ pretty_name = characters[char_name].name_pretty
    $ characters[char_name].boost_affection()
    "I feel a bit closer to [pretty_name]."
    return

transform size_normal:
    ysize 600
    fit "contain"