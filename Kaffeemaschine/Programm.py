from cl_GUI import CoffeeMaker
import tkinter as tk
from functools import partial

kaffee = CoffeeMaker()

def Hauptmenü():
        list = ["Kaffeeauswahl", "Füllstand", "Reinigen"]
        return list

def index_Auslesen():
        index = kaffee.listbox_auswahl.curselection() 
        index = index[0]
        return index

def list_Auslesen():
        listtarget = []
        listsource = kaffee.listbox_auswahl.get(0, "end")
        
        for i in listsource:
                listtarget.append(i)
        
        return listtarget
        
def Listvariabel(liste):
        
        inhalt = tk.Variable(value = liste)
        kaffee.listbox_auswahl.configure(listvariable= inhalt)
        return liste 

def selection_Curser_Down():
        index = index_Auslesen()
        list = list_Auslesen()
        if index == len(list)-1:
                kaffee.listbox_auswahl.select_clear(first = index)
                return kaffee.listbox_auswahl.selection_set(first = 0)
               
        kaffee.listbox_auswahl.select_clear(first = index)
        index += 1
        kaffee.listbox_auswahl.selection_set(first = index)


def selection_Curser_Up():
        index = index_Auslesen()
        list = list_Auslesen()
        if index == 0:
                kaffee.listbox_auswahl.select_clear(first = index)
                return kaffee.listbox_auswahl.selection_set(first = len(list)-1)
               
        kaffee.listbox_auswahl.select_clear(first = index)
        index -= 1
        kaffee.listbox_auswahl.selection_set(first = index)


def selection_Menü():
        
        check = list_Auslesen()
        
        if check == Listvariabel(kaffee.coffeemashine.get_recepies()):
                index = index_Auslesen()
                kaffee.listbox_auswahl.select_clear(first = index)
                kaffee.listbox_auswahl.selection_set(first= 0)
                kaffee.coffeemashine.execute_selection(index)
                list = ["Kaffee wird zubereitet",
                        "Fertig",
                        "Getränk entnehmen!"]
                
                Listvariabel(list)
                kaffee.listbox_auswahl.select_clear(first = index)
                
                
        elif check == Listvariabel(kaffee.coffeemashine.get_container_List()):
                index = index_Auslesen()
                kaffee.listbox_auswahl.select_clear(first = index)
                kaffee.listbox_auswahl.selection_set(first= 0)
                kaffee.coffeemashine.refill(index)
                Listvariabel(Hauptmenü())
                
                
        elif check == Hauptmenü():
                
                if index_Auslesen() == 0:
                        Listvariabel(kaffee.coffeemashine.get_recepies())
                        kaffee.listbox_auswahl.select_clear(first = 0)
                        kaffee.listbox_auswahl.selection_set(first= 0)
                        
                
                elif index_Auslesen() == 1:
                        Listvariabel(kaffee.coffeemashine.get_container_List())
                        kaffee.listbox_auswahl.select_clear(first = 1)
                        kaffee.listbox_auswahl.selection_set(first= 0)
                       
                
                elif index_Auslesen() == 2:
                        list = ["Kaffeemaschine gereinigt"]
                        Listvariabel(list)


Listvariabel(Hauptmenü())
kaffee.listbox_auswahl.selection_set(first= 0)                        
                       
tk.Button.configure(kaffee.btn_start, command = selection_Menü)
tk.Button.configure(kaffee.btn_zurück, command = partial(Listvariabel, Hauptmenü()))
tk.Button.configure(kaffee.btn_down, command = selection_Curser_Down)
tk.Button.configure(kaffee.btn_up, command = selection_Curser_Up)


kaffee.mainloop()