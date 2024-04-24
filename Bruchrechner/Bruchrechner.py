#Einbinden von tkinter
from tkinter import *

# Einbinden Definition der Klasse Bruch mit Attributen und Methoden
from clBruch import Bruch

# Instanziieren der Objekte der Klasse Bruch
bruch1 = Bruch()
bruch2 = Bruch()


def btnplusclick():
    # uebernehmen der Daten der Eingabefelder ( ENTRY )
    h_bruch = entbruch1.get().split("/")
    bruch1.zaehler = int(h_bruch[0])
    bruch1.nenner = int(h_bruch[1])

    h_bruch = entbruch2.get().split("/")
    bruch2.zaehler = int(h_bruch[0])
    bruch2.nenner = int(h_bruch[1])

    # Verarbeitung - Addition der Brüche
    ergebnis = bruch1 + bruch2

    # Anzeige des Ergebinsses
    lblergebnis.config(text=ergebnis)


def btnminusclick():
    # uebernehmen der Daten der Eingabefelder ( ENTRY )
    h_bruch = entbruch1.get().split("/")
    bruch1.zaehler = int(h_bruch[0])
    bruch1.nenner = int(h_bruch[1])

    h_bruch = entbruch2.get().split("/")
    bruch2.zaehler = int(h_bruch[0])
    bruch2.nenner = int(h_bruch[1])

    # Verarbeitung - Substraktion der Brüche
    ergebnis = bruch1 - bruch2

    # Anzeige des Ergebinsses
    lblergebnis.config(text=ergebnis)


def btnmultclick():
    # uebernehmen der Daten der Eingabefelder ( ENTRY )
    h_bruch = entbruch1.get().split("/")
    bruch1.zaehler = int(h_bruch[0])
    bruch1.nenner = int(h_bruch[1])

    h_bruch = entbruch2.get().split("/")
    bruch2.zaehler = int(h_bruch[0])
    bruch2.nenner = int(h_bruch[1])

    # Verarbeitung - Multiplikation der Brüche
    ergebnis = bruch1 * bruch2

    # Anzeige des Ergebinsses
    lblergebnis.config(text=ergebnis)


def btndivclick():
    # uebernehmen der Daten der Eingabefelder ( ENTRY )
    h_bruch = entbruch1.get().split("/")
    bruch1.zaehler = int(h_bruch[0])
    bruch1.nenner = int(h_bruch[1])

    h_bruch = entbruch2.get().split("/")
    bruch2.zaehler = int(h_bruch[0])
    bruch2.nenner = int(h_bruch[1])

    # Verarbeitung - Division der Brüche
    ergebnis = bruch1 / bruch2

    # Anzeige des Ergebinsses
    lblergebnis.config(text=ergebnis)
#Fenster/Window
tkwindow = Tk()
tkwindow.title("Bruchrechner")

# Frames
frmeingabe = Frame(master=tkwindow)
frmbruch1 = Frame(master=frmeingabe, bg="blue")
frmbruch2 = Frame(master=frmeingabe, bg="blue")

frmberechnen = Frame(master=tkwindow, bg="yellow")

frmbausgabe = Frame(master=tkwindow)

frmergebnis = Frame(master=frmbausgabe, bg="green")

frmeingabe.pack()
frmbruch1.pack(side=LEFT)
frmbruch2.pack(side=RIGHT)

frmberechnen.pack()
frmbausgabe.pack()
frmergebnis.pack()

#Label
lblbruch1 = Label(master=frmbruch1, bg="white", text="Bruch1")
lblbruch1.pack(padx=10, pady=10)

lblbruch2 = Label(master=frmbruch2, bg="white", text="Bruch2")
lblbruch2.pack(padx=10, pady=10)

lbltextergebnis = Label(master=frmergebnis, bg="white", text="Ergebnis")
lbltextergebnis.pack(padx=10, pady=10)

lblergebnis = Label(master=frmergebnis, bg="white", text="          ")
lblergebnis.pack(padx=10, pady=10)




#Entry
entbruch1 = Entry(master=frmbruch1, width=8)
entbruch1.pack(padx=10, pady=10)
entbruch2 = Entry(master=frmbruch2, width=8)
entbruch2.pack(padx=10, pady=10)


#Button
btnplus = Button(master=frmberechnen, text="+", command=btnplusclick)
btnplus.pack(side=LEFT, padx=10, pady=10)

btnminus = Button(master=frmberechnen, text="-", command=btnminusclick)
btnminus.pack(side=LEFT, padx=10, pady=10)

btnmulti = Button(master=frmberechnen, text="*", command=btnmultclick)
btnmulti.pack(side=LEFT, padx=10, pady=10)

btndiv = Button(master=frmberechnen, text=":", command=btndivclick)
btndiv.pack(side=LEFT, padx=10, pady=10)



# Aktivierung des Fenster/Window
tkwindow.mainloop()

