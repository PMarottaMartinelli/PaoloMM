

class Bruch:
    def __init__(self, zaehler=1, nenner=1):
        self.zaehler = zaehler
        self.nenner = nenner
        if nenner == 0:
            self.nenner = 1
        else:
            self.nenner = nenner
        self.__kuerzen()

    def __str__(self):
        return f"{self.zaehler} / {self.nenner}"

    def __kuerzen(self):
        z = self.zaehler
        n = self.nenner
        if self.zaehler != 0:
            while z != 1 and n != 1 and z != n:
                z, n = min(z, n), abs(z-n)
            if z == n:
                self.zaehler = self.zaehler // z
                self.nenner = self.nenner // z

    def __add__(self, other):
        z = self.zaehler * other.nenner + self.nenner * other.zaehler
        n = self.nenner * other.nenner
        return Bruch(z, n)

    def __sub__(self, other):
        z = self.zaehler * other.nenner - self.nenner * other.zaehler
        n = self.nenner * other.nenner
        return Bruch(z, n)


    def __mul__(self, other):
        z = self.zaehler * other.zaehler
        n = self.nenner * other.nenner
        return Bruch(z, n)
        
        
    def __truediv__(self, other):
        z = self.zaehler * other.nenner
        n = self.nenner * other.zaehler
        return Bruch(z, n)

    def __eq__(self, other):
        return self.zaehler == other.zaehler and self.nenner == other.nenner


    def __float__(self):
        return self.zaehler / self.nenner

