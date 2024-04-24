# Definition der Klasse Geist
class Geist():
    def __init__(self, name , groesse):
        self.name = name
        self.groesse = groesse
        self.sichtbar = False
        self.gefangen = False

    def spuken(self):
        print(f"Ich heiße {self.name} und mache 'Buuuhhh'")

    def __str__(self):
        return f"Meine Name ist {self.name} und ich habe eine Größe von {self.groesse}" \
               f" und ich bin {'sichtbar' if self.sichtbar else 'unsichtbar'}"