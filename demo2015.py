# Annaliis Täheväli

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from algod import *

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def puhasta():
    tahvel.delete('all')

def color_picker(protsess):
    colors = ["green", "yellow", "orange", "red", "#8CD1F1", "#AFE88C", "#F8DAE3", "cyan", "#F1ED8C", "#C18FDE", "#B2A9F3", "#F955B3", "#EFEFEF"]
    color = ''
    
    if protsess == ' ':
        color = colors[-1]
    else:
        color = colors[alphabet.index(protsess)]

    return color


# joonistab tahvlile protsesse kujutavad ristkülikud numbrite ja protsesside nimedega
def joonista(jarjend):
    #print(jarjend)
    puhasta()
    eelmise_loppx = 110
    nr_x = 118
    y_koordinaat = 60
    y_koordinaat2 = 80
    kaugus = 0
    for i in range(len(jarjend)):
        print("I:" + str(i))
        for j in range(50):
            print("J:" + str(j))
            protsess = jarjend[i][j]
            kestus = 1
            kujund = tahvel.create_rectangle(eelmise_loppx, y_koordinaat, eelmise_loppx + kestus * 16,y_koordinaat2, fill=color_picker(protsess))
            keskpaik = eelmise_loppx+kestus * 8
            protsessi_id = tahvel.create_text(keskpaik, y_koordinaat+10, text=protsess)

            if i == 0:
                nr = tahvel.create_text(nr_x, 50, text=str(kaugus)) # 0-49
            kaugus += kestus
            eelmise_loppx += kestus*16
            nr_x += kestus*16

            # etapi nr ja lisatud protsessid
            etapp = tahvel.create_text(15, y_koordinaat+10, text=str(i + 1))
            try:
                protsess = tahvel.create_text(70, y_koordinaat+10, text=alphabet[i] + " : " + str(massiiviMeister()[i]))
            except:
                protsess = tahvel.create_text(70, y_koordinaat+10, text="-") 

        y_koordinaat += 20
        y_koordinaat2 += 20
        eelmise_loppx = 110
    etapi_silt = tahvel.create_text(20, 50, text="Etapp", font='Helvetica 9 bold')
    protsessi_silt = tahvel.create_text(70, 50, text="Protsess", font='Helvetica 9 bold')

# teeb järjendist kahetasemelise listi, mida on mugavam töödelda
def massiiviks(input_jarjend):
    valjund = []
    jupid = input_jarjend.split(";")
    for i in range(len(jupid)):
        hakkliha = jupid[i].split(",")
        saabumine = int(hakkliha[0])
        kestus = int(hakkliha[1])
        valjund.append([saabumine, kestus])
    return valjund

# otsustab, millist järjendit teha kahetasemeliseks massiiviks
def massiiviMeister():
    jarjend = []
    if var.get() == 1:
        return massiiviks(predef1)
    elif var.get() == 2:
        return massiiviks(predef2)
    elif var.get() == 3:
        return massiiviks(predef3)
    elif var.get() == 4:
        try:
            return massiiviks(kasutaja_jarjend.get())
        except:
            messagebox.showerror(title="Viga sisendis", message="Vigane kasutaja muster!")
            return massiiviks(predef1)
    else:
        return massiiviks(predef1)


# näitab programmis käimasolevat protsessijada
def massiiviTeavitaja(massiiv):
    text.delete(1.0, END)
    text.insert(INSERT, "Allesjäänud failidest on fragmenteerunud " + str(massiiv[0]) + "%." + "\n")
    text.insert(INSERT, "Fragmenteerunud failidele kuulub " + str(massiiv[1]) + "% kasutatud ruumist.")

def jooksuta_algoritmi():
    jarjend = massiiviMeister()
    valjund = kaivita(jarjend)
    massiiviTeavitaja([valjund[1], valjund[2]])
    joonista(valjund[0])

predef1 = "A,2;B,3;A,-;C,4;B,+3;D,5;E,15;C,-;F,55"
predef2 = "A,4;B,3;C,6;D,5;C,+2;B,-;E,5;A,-;F,10"
predef3 = "A,2;B,3;C,4;D,5;B,-;E,7;D,-;E,+3;F,10"


# GUI
raam = Tk()
raam.title("Planeerimisalgoritmid")
raam.resizable(False, False)
raam.geometry("930x500")

var = IntVar()
var.set(1)
Radiobutton(raam, text="Esimene", variable=var, value=1).place(x=10,y=40)
Radiobutton(raam, text="Teine", variable=var, value=2).place(x=10,y=70)
Radiobutton(raam, text="Kolmas", variable=var, value=3).place(x=10,y=100)
Radiobutton(raam, text="Enda oma", variable=var, value=4).place(x=10,y=130)

silt_vali = ttk.Label(raam, text="Vali või sisesta järjend (kujul A,2;B,3;A,-;C,4;B,+3;D,5;E,15;C,-;F,5)")
silt_vali.place(x=10, y=10)

silt1 = ttk.Label(raam, text=predef1)
silt1.place(x=120, y=40)

silt2 = ttk.Label(raam, text=predef2)
silt2.place(x=120, y=70)

silt3 = ttk.Label(raam, text=predef3)
silt3.place(x=120, y=100)

silt_run = ttk.Label(raam, text="Algoritmi käivitamiseks klõpsa nupule")
silt_run.place(x=10, y=160)

silt_tahvel = ttk.Label(raam, text="Arvutused:")
silt_tahvel.place(x=450, y=10)

kasutaja_jarjend = ttk.Entry(raam)
kasutaja_jarjend.place(x=120, y=130, height=25, width=240)
kasutaja_jarjend.insert(END,"A,2;B,3;A,-;C,4;B,+3;D,5;E,15;C,-;F,5")

tahvel = Canvas(raam, width=930, height=280, background="white")
tahvel.place(x=0, y=220)

kaivita_nupp = ttk.Button(raam, text="Käivita", command = lambda : jooksuta_algoritmi())
kaivita_nupp.place(x=10, y=190,height=25, width=80)

puhasta_nupp = ttk.Button(raam, text="Puhasta väljund", command = lambda : puhasta() )
puhasta_nupp.place(x=500, y=190,height=25, width=130)

text = Text(raam, width=25, height=9)
text.place(x=450, y=30)

raam.mainloop()
