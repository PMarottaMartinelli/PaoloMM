class Geisterjaeger():
    def __init__(self, name):
        self.name = name
        self.gefangene_geister = []


    def __str__(self):
        return f"Mein Name ist {self.name}\n" \
               f"ich habe diese Geister gefangen:" \
               f"{[geist.name for geist in self.gefangene_geister]}"

    def geist_fangen(self, other):
        if other.sichtbar:
            other.gefangen = True
            self.gefangene_geister.append(other)
            print(f"Ich heiße {self.name} und habe {other.name} gefangen")
        else:
            print(f"Ich heiße {self.name} und habe {other.name} nicht gefangen, da er unsichtbar ist")