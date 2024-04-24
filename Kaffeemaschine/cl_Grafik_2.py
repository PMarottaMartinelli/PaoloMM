# ohne Fenster title
from cl_CoffeeMashine import CoffeeMashine
import tkinter as tk


class CoffeeMaker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__coffeemashine = CoffeeMashine
        self.title("Best Coffee")
        self.resizable(False, False)

        self.overrideredirect(True)

        self.photo= tk.PhotoImage(file="KaffeeMaschine/KaffeeMaschine_2.png") 

        self.style_cv = {"master":self, "width":750, "height":950 }

        self.cv = tk.Canvas(**self.style_cv)
        self.cv.grid(column=0, row=0, padx=2, pady=2)

        self.cv.create_image(0,0, anchor=tk.NW, image=self.photo, tags="cvid")
      
        #Buttons
        self.style_btn = {"master":self, "width":8, "height":0, "background":"black", "fg":"skyblue", "font":("Calibri bold", 10)}

        self.btn_exit = tk.Button(text="Exit", command=quit, **self.style_btn)
        tk.Button.configure(self.btn_exit, fg="red")
        self.btn_exit.place(relx=0.24, rely=0.29)

        self.btn_info = tk.Button(text="Füllstand", **self.style_btn, command= self.__coffeemashine.fillstand)
        self.btn_info.place(relx=0.24, rely=0.32)

        self.btn_up = tk.Button(text="Up", **self.style_btn)
        self.btn_up.place(relx=0.39, rely=0.23)

        self.btn_down = tk.Button(text="Down", **self.style_btn)
        self.btn_down.place(relx=0.39, rely=0.26)

        self.btn_start = tk.Button(text="Start", **self.style_btn, command= self.__coffeemashine.check_selection)
        self.btn_start.place(relx=0.39, rely=0.29)

        #self.btn_stop = tk.Button(text="Stop", **self.style_btn)
        #self.btn_stop.place(relx=0.39, rely=0.32)

        self.style_lbl = {"master": self, "width": 30, "bg": "darkgray", "font":("Calibri italic", 7), "relief": "groove"}
        self.lbl_text = tk.Label(text="Bitte Kaffee auswählen", **self.style_lbl)
        self.lbl_text.place(relx=0.555, rely=0.221)

        #Label für Menü
        self.style_lb = {"master":self, "width": 22, "height":6, "background":"black", "fg":"skyblue", "font": ("Calibri", 10)}
        self.listbox_auswahl = tk.Listbox(**self.style_lb)
        tk.Listbox.configure(self.listbox_auswahl, highlightthickness=2, highlightbackground="skyblue")
        self.listbox_auswahl.place(relx=0.555, rely=0.240)
        self.listbox_auswahl.insert("end", *["  Kaffee schwarz",
                                        "  Kaffee mit Zucker", 
                                        "  Milchkaffee", 
                                        "  Milchkaffee mit Zucker", 
                                        "  Latte Macchiato",
                                        "  Latte Macchiato Caramel",
                                        "  Latte Macchiato Vanille",  
                                        "  Espresso",
                                        "  Espresso doppelt", 
                                        "  Irish Coffee"])
        self.listbox_auswahl.bind("<<ListboxSelect>>", self.f_kaffee_ausgewaehlt)

        #self.listbox_auswahl.

    def f_kaffee_ausgewaehlt(self, event):
        coffee = "".join(self.listbox_auswahl.get(i) for i in self.listbox_auswahl.curselection() )
        self.lbl_text["text"] = "ausgewählt: " + coffee
        self.lbl_text.config(background="skyblue")


        def move_app(e):
            x, y = self.winfo_pointerxy()
            self.geometry(f"+{x}+{y}")

        self.bind('<B1-Motion>', move_app)

if __name__ == "__main__":
    CoffeeMaker().mainloop()