# ohne Fenster title
from cl_CoffeeMashine import CoffeeMashine
import tkinter as tk


class CoffeeMaker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.coffeemashine = CoffeeMashine()
        self.title("Best Coffee")
        self.resizable(False, False)

        self.overrideredirect(True)

        self.photo= tk.PhotoImage(file="C:\\Users\\Umschueler\\Desktop\\AnwP Python\\Kaffeemaschine\\KaffeeMaschine_2.png") 

        self.style_cv = {"master":self, "width":750, "height":950 }

        self.cv = tk.Canvas(**self.style_cv)
        self.cv.grid(column=0, row=0, padx=2, pady=2)

        self.cv.create_image(0,0, anchor=tk.NW, image=self.photo, tags="cvid")
      
        #Buttons
        self.style_btn = {"master":self, "width":8, "height":0, "background":"black", "fg":"skyblue", "font":("Calibri bold", 10)}

        self.btn_exit = tk.Button(text="Exit", command=quit, **self.style_btn)
        tk.Button.configure(self.btn_exit, fg="red")
        self.btn_exit.place(relx=0.46, rely=0.65)

        self.btn_up = tk.Button(text="Up", **self.style_btn)
        self.btn_up.place(relx=0.44, rely=0.23)

        self.btn_down = tk.Button(text="Down", **self.style_btn)
        self.btn_down.place(relx=0.44, rely=0.31)

        self.btn_start = tk.Button(text="O", **self.style_btn) #command= self.__coffeemashine.check_selection)
        self.btn_start.place(relx=0.44, rely=0.27)

        self.btn_zurück = tk.Button(text ="<<<", **self.style_btn)
        self.btn_zurück.place(relx=0.25, rely=0.27)
        
        #Listbox
        self.style_lb = {"master":self, "width": 22, "height":6, "background":"black", "fg":"skyblue", "font": ("Calibri", 10)}
        self.listbox_auswahl = tk.Listbox(**self.style_lb)
        tk.Listbox.configure(self.listbox_auswahl, highlightthickness=2, highlightbackground="skyblue")
        self.listbox_auswahl.place(relx=0.555, rely=0.240)
        
        def move_app(self):
            x, y = self.winfo_pointerxy()
            self.geometry(f"+{x}+{y}")

            self.bind('<B1-Motion>', move_app)



        




    
