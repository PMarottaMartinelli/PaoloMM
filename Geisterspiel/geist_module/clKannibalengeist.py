# Einbinden der Elternklasse Geist
from .clGeist import Geist

class Kannibalengeist(Geist):
    def __init__(self, name, groesse):
        super().__init__(name, groesse)

    def fressen(self, other):
        self.groesse += other.groesse
        print(f"\t{self.name} frisst {other.name}")
        other.groesse = 0
