# Einbinden der Elternklasse Geist
from .clGeist import Geist

class Geisterjunge(Geist):
    def __init__(self, name, groesse):
        super().__init__(name, groesse)

    def spuken(self):
        print(f"Ich heiße {self.name} und kann nicht spuken")

    def sichtbar_machen(self, other):
        other.sichtbar = True
