class Recepies():
    def __init__(self, name, milch, kaffeebohnen ,zucker, kaffeesatz, 
                 auffangschale ,  whiskey):
        self.__name = name
        self.__ingredients = {"Milch": milch,
                          "Kaffeebohnen": kaffeebohnen,
                          "Zucker": zucker,
                          "Kaffeesatz": kaffeesatz,
                          "Auffangschale": auffangschale,
                          "Whiskey":whiskey,
                          }

    def get_name(self):
        return f"  {self.__name}"
    
    def get_ingredients(self):
        return f"  {self.__ingredients}"
    
    def get_Quantiy(self):
        quantity = self.__ingredients.values()
        return quantity
    
    def __str__(self):
        return f"{self.__name} {self.__ingredients}"





