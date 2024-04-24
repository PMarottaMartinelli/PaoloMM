# Die Ampel wird mit Tkinter dargestellt.
# Man kann die Ampelzustände durchschalten.


import tkinter as tk

from class_Ampel import Ampel_Auto, Ampel_Fussgänger

class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        self.ampel = Ampel_Auto()

        self.title("AutoAmpel")
        self.resizable(False, False)

        # Hintergrundbild einbinden (Bild muss im gleichen Verzeichnis wie das Skript sein)
        self.hintergrundbild = tk.PhotoImage(file="Straße.png")

        # Canvas erstellen und Hintergrundbild setzen
        self.canvas = tk.Canvas(self, width=532, height=367)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.hintergrundbild)

        # Buttons
        self.style_btn = {"master": self, "width": 12, "font": ("Calibri bold", 12)}

        self.btn_weiter = tk.Button(text="weiter", command=self.fnc_weiter, **self.style_btn)
        self.btn_weiter.place(relx=0.1, rely=0.13)  # Relative Position auf der Canvas

        self.btn_exit = tk.Button(text="Exit", command=quit, **self.style_btn)
        self.btn_exit.place(relx=0.1, rely=0.4)  # Relative Position auf der Canvas

        # Frame "Ampel"
        self.cnv_ampel = tk.Canvas(self, width=40, height=100, bg="#a0a0a0", highlightthickness=0)
        self.cnv_ampel.place(relx=0.873, rely=0.08)

        # Frame Lights Ampel
        style_light = {"master": self, "width": 20, "height": 20, "bg":"#000000", "highlightthickness": 0}

        self.light_1 = tk.Canvas(**style_light)
        self.light_1.place(relx=0.892, rely=0.11)

        self.light_2 = tk.Canvas(**style_light)
        self.light_2.place(relx=0.892, rely=0.19)

        self.light_3 = tk.Canvas(**style_light)
        self.light_3.place(relx=0.892, rely=0.27)

        self.update_colors()


    def fnc_weiter(self):
        self.ampel.cycle_phase()
        self.update_colors()


    def update_colors(self):
        colors = self.ampel.get_colors()
        lights = [self.light_1, self.light_2, self.light_3]
        for i in range(len(lights)):
            try:
                color = colors[i]
            except IndexError:
                color = "#000000"

            lights[i].configure(bg=color)


if __name__ == "__main__":
    Main().mainloop()
