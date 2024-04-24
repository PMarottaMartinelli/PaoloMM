class Container():
    def __init__(self, name, capacity):
        self.__name = name
        self.__capacity = capacity

    def get_name(self):
        return self.__name

    def set_capacity(self, capacity):
        if capacity >= 0 and capacity <= 100:
            self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def __str__(self):
        return f"  {self.__capacity:5}% : {self.__name:<15}"        
    
    

