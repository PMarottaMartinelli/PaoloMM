# Einbinden der Elternklasse Geist
from .clGeist import Geist

class Schleimgeist(Geist):
    def __init__(self, name, groesse):
        super().__init__(name, groesse)

    def spuken(self):
        super().spuken()
        self.schleimen()

    def schleimen(self):
        print("..... hinterlässt Schleimspur")
