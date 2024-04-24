# Dies ist in einer Gruppenarbeit entstanden


# Definieren der Klasse CoffeeMashine
from operator import index
from cl_Container import Container
from cl_Recepies import Recepies

class CoffeeMashine:
    def __init__(self):
        self.__container = [Container("Milch", 100), 
                            Container("Kaffeebohnen", 100),
                            Container("Zucker", 100), 
                            Container("Kaffeesatz", 100), 
                            Container("Auffangschale", 100), 
                            Container("Whiskey", 100) 
                            #Container("Caramelaroma", 100), 
                            #Container("Vanillearoma", 100)
                            ]
        
        self.__recepies = [Recepies("Kaffee schwarz", 0, 4, 0, 4, 4, 0),
                           Recepies("Kaffee mit Zucker", 0, 4, 2, 4, 4, 0),
                           Recepies("Milchkaffee", 4, 4, 0, 4, 6, 0),
                           Recepies("Milchkaffee mit Zucker", 4, 4,2,4,6,0),
                           Recepies("Latte Macchiato", 4,6,0,6,8,0),
                           #Recepies("Latte Macchiato Caramel", 4,6,1,6,8,0,4,0),
                           #Recepies("Latte Macchiato Vanille", 4,6,1,6,8,0,0,4),
                           #Recepies("Espresso", 0,6,2,6,6,0,0,0,),
                           Recepies("Espresso doppelt", 0, 10, 0, 10, 10, 0)
                           #Recepies("Irish Coffee",4, 6, 0, 6, 8, 2, 0, 0,)
                           ]

                          
        self.__cleaning_count = 0


    def get_cleaning_count(self):        
        return self.__cleaning_count
    
    def get_container_List(self):
        liste = []
        for i in self.__container:
            liste.append(i.__str__())
        return liste
    
    def get_container_dict(self):
        liste = {}
        for i in self.__container:
            liste[i.get_name()] = i.get_capacity()
        return liste
    
        
    def get_recepies(self):
        liste = []
        for i in self.__recepies:
            liste.append(i.get_name())
        return liste
    
    # überprüft ob Getränk zubreitet werden kann
    def check_selection(self, index):
        i = 0
        zutaten = self.__recepies[index].get_Quantiy()
        for quantity in zutaten:
            if quantity > self.__container[i].get_capacity():
                raise IndexError
            i+=1    


    def execute_selection(self, index):
        self.check_selection(index)
        i= 0
        zutaten = self.__recepies[index].get_Quantiy()
        for quantiy in zutaten:
            self.__container[i].set_capacity(self.__container[i].get_capacity() - quantiy) 
            i +=1
        self.__cleaning_count += 1
        

    # Funktion um Füllstände auf 100% zusetzen
    def refill(self, index):
        # index = listbox
        self.__container[index].set_capacity(100)

    def cleaning(self):
        reinigung = ["Reinigung läuft ...", "...", "fertig"]
        self.__cleaning_count = 0
        return reinigung

    # Anzeigen des Füllstandes der Behälter
    def fillstand(self):
        filllevel = []
        for container in self.__container:
            filllevel.append(f"{container.get_name()} : {container.get_capacity()}")
        return filllevel





        


