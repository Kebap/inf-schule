import random
from tkinter import Tk, Label, Button, Entry, END, Frame, \
                    Radiobutton, IntVar, PhotoImage, \
                    NORMAL, DISABLED


def wuerfle():
    return random.randint(1,6)


def prototyp1():
    # Nur mal schauen, wie die Spiellogik aussehen sollte.
    # Zahl 1-6 wählen, 3x würfeln, für jeden Treffer 1e zurück erhalten
    vorhersage = 5
    ergebnisse = wuerfle(3)
    lohn = 0
    for ergebnis in ergebnisse:
        if ergebnis == vorhersage:
            lohn += 1
    template = "Vorhersage war: {%s}, gewuerfelt wurde {%s}, somit ergibt sich Lohn: {%s}"
    ergebnis_str = " und ".join(map(str, ergebnisse))
    print(template.format(vorhersage, ergebnis_str, lohn))


def prototyp2():
    # Fenster erstellen
    tkFenster = Tk()
    tkFenster.title("chuck a luck")
    tkFenster.geometry("360x165")

    # Label mit Überschrift 
    label_ueberschrift_konto = Label(
        master = tkFenster,
        text = "chuck a luck",
        font = "Arial 16",
        foreground = "white",
        background = "#889E9D"
    )
    label_ueberschrift_konto.place(x = 10, y = 10, width = 340, height = 30)

    # Label mit Überschrift fürs Konto
    label_ueberschrift_konto = Label(
        master = tkFenster,
        text = "Konto",
        background = "#FFCFC9"
    )
    label_ueberschrift_konto.place(x = 10, y = 50, width = 100, height = 20)

    # Label fuer den Kontostand
    label_konto = Label(master = tkFenster)
    label_konto.config(text = "100")
    label_konto.config(background = "#FFCFC9")
    label_konto.place(x=45, y=80, width=30, height=30)

    # Label mit Überschrift für Würfel
    label_ueberschrift_konto = Label(
        master = tkFenster,
        text = "Würfel",
        background = "#FBD975"
    )
    label_ueberschrift_konto.place(x = 250, y = 50, width = 100, height = 20)

    # Label fuer den ersten Würfel
    label_konto = Label(master = tkFenster)
    label_konto.config(text = "0")
    label_konto.config(background = "#FBD975")
    label_konto.place(x=250, y=80, width=30, height=30)

    # Label fuer den zweiten Würfel
    label_konto = Label(master = tkFenster)
    label_konto.config(text = "0")
    label_konto.config(background = "#FBD975")
    label_konto.place(x=285, y=80, width=30, height=30)

    # Label fuer den dritten Würfel
    label_konto = Label(master = tkFenster)
    label_konto.config(text = "0")
    label_konto.config(background = "#FBD975")
    label_konto.place(x=320, y=80, width=30, height=30)

    # Fenster aktivieren
    tkFenster.mainloop()


def prototyp3():
    tk_fenster = Tk()
    tk_fenster.title("Test")
    tk_fenster.geometry("120x110")

    # Eingabefeld für die Zahl
    global label_konto
    label_konto = Label(master = tk_fenster,
                        text = "100",
                        background = "#FFCFC9")
    label_konto.place(x = 45, y = 40, width = 30, height = 30)

    # Button zum Auswerten
    button_einsatz = Button(master = tk_fenster,
                            text = "Einsatz zahlen",
                            command = button_einsatz_click)
    button_einsatz.place(x = 10, y = 80, width = 100, height = 20)

    # Aktivierung des Fensters
    tk_fenster.mainloop()


def button_einsatz_click():
    # Ereignisverarbeitung
    # Verwaltung der Daten
    global label_konto
    konto = int(label_konto.cget('text'))
    # Verarbeitung der Daten
    konto -= 1
    # Anzeige der Daten
    label_konto.config(text = str(konto))
    

def prototyp4():
    def button_wuerfeln_click():
        # Ereignisverarbeitung
        # Verwaltung der Daten
        # Verarbeitung der Daten
        wurf = wuerfle()
        # Anzeige der Daten
        label_wuerfel.config(text = str(wurf))
        
    tk_fenster = Tk()
    tk_fenster.title("Test")
    tk_fenster.geometry("120x110")

    # Ausgabefeld für einen Würfel
    label_wuerfel = Label(master = tk_fenster,
                        text = "?",
                        background = "#FBD975")
    label_wuerfel.place(x = 45, y = 40, width = 30, height = 30)

    # Button zum Würfeln
    button_wuerfeln = Button(master = tk_fenster,
                             text = "Würfel werfen",
                             command = button_wuerfeln_click)
    button_wuerfeln.place(x = 10, y = 80, width = 100, height = 20)

    # Aktivierung des Fensters
    tk_fenster.mainloop()



def prototyp5():
# http://inf-schule.de/software/gui/miniprojekt_chuckaluck/implementierungeinfachegui/schaltflaechen

    # Fenster erstellen
    tk_fenster = Tk()
    tk_fenster.title("chuck a luck")
    tk_fenster.geometry("360x165")

    # Label mit Überschrift 
    label_ueberschrift_konto = Label(
        master = tk_fenster,
        text = "chuck a luck",
        font = "Arial 16",
        foreground = "white",
        background = "#889E9D"
    )
    label_ueberschrift_konto.place(x = 10, y = 10, width = 340, height = 35)



    # Rahmen für das Konto
    frame_konto = Frame(master=tk_fenster,
                        background="#FFCFC9")
    frame_konto.place(x=10, y=50, width=110, height=100)
    
    # Label mit Überschrift fürs Konto
    label_ueberschrift_konto = Label(
        master = frame_konto,
        text = "Konto",
        background = "white"
    )
    label_ueberschrift_konto.place(x = 5, y = 5, width = 100, height = 20)

    # Label fuer den Kontostand
    label_konto = Label(master = frame_konto)
    label_konto.config(text = "100")
    label_konto.config(background = "white")
    label_konto.place(x=40, y=35, width=30, height=30)

    def button_einsatz_click():
        # Verwaltung der Daten
        konto = int(label_konto.cget('text'))
        # Verarbeitung der Daten
        konto -= 1
        # Anzeige der Daten
        label_konto.config(text = str(konto))

    # Button zum Einsatz zahlen
    button_wuerfeln = Button(master = frame_konto,
                             text = "Einsatz zahlen",
                             command = button_einsatz_click)
    button_wuerfeln.place(x = 5, y = 75, width = 100, height = 20)

   

    # Rahmen für Gewinnzahl
    frame_gewinn = Frame(master=tk_fenster,
                        background="#D5E88F")
    frame_gewinn.place(x=125, y=50, width=110, height=100)

    # Label mit Überschrift für Gewinnzahl
    label_ueberschrift_zahl = Label(
        master = frame_gewinn,
        text = "Zahl",
        background = "white"
    )
    label_ueberschrift_zahl.place(x = 5, y = 5, width = 100, height = 20)

    # Eingabefeld für Gewinnzahl
    entry_zahl = Entry(master = frame_gewinn,
                       background = "white")
    entry_zahl.place(x=40, y=35, width=30, height=30)
    entry_zahl.insert(0, "?")
    
    def button_auszahlen_click():
        # Verwaltung der Daten
        kontostand = int(label_konto.cget("text"))
        gewinnzahl = int(entry_zahl.get())
        wuerfe = [int(wuerfel.cget("text")) for wuerfel in label_wuerfel]
        gewinn = 0
        # Verarbeitung der Daten
        for wurf in wuerfe:
            if gewinnzahl == wurf:
                gewinn += 1
        # Anzeige der Daten
        label_konto.config(text = str(kontostand + gewinn))

    # Button für Gewinn auszahlen
    button_auszahlen = Button(master = frame_gewinn,
                              text = "Gewinn auszahlen",
                              command = button_auszahlen_click)
    button_auszahlen.place(x = 5, y = 75, width = 100, height = 20)



    # Rahmen für die Würfel
    frame_gewinn = Frame(master=tk_fenster,
                        background="#FBD975")
    frame_gewinn.place(x=240, y=50, width=110, height=100)

    # Label mit Überschrift für Würfel
    label_ueberschrift_konto = Label(
        master = frame_gewinn,
        text = "Würfel",
        background = "white"
    )
    label_ueberschrift_konto.place(x = 5, y = 5, width = 100, height = 20)

    # Label fuer den ersten Würfel
    label_wuerfel = []
    label_wuerfel.append(Label(master = frame_gewinn))
    label_wuerfel[0].config(text = "0")
    label_wuerfel[0].config(background = "white")
    label_wuerfel[0].place(x=5, y=35, width=30, height=30)

    # Label fuer den zweiten Würfel
    label_wuerfel.append(Label(master = frame_gewinn))
    label_wuerfel[1].config(text = "0")
    label_wuerfel[1].config(background = "white")
    label_wuerfel[1].place(x=40, y=35, width=30, height=30)

    # Label fuer den dritten Würfel
    label_wuerfel.append(Label(master = frame_gewinn))
    label_wuerfel[2].config(text = "0")
    label_wuerfel[2].config(background = "white")
    label_wuerfel[2].place(x=75, y=35, width=30, height=30)


    def button_wuerfeln_click():
        # Verwaltung der Daten
        # Verarbeitung der Daten
        wuerfe = wuerfle(), wuerfle(), wuerfle()
        # Anzeige der Daten
        for i, wuerfel in enumerate(label_wuerfel):
            wuerfel.config(text = str(wuerfe[i]))

    # Button zum Würfeln
    button_wuerfeln = Button(master = frame_gewinn,
                             text = "Würfel werfen",
                             command = button_wuerfeln_click)
    button_wuerfeln.place(x = 5, y = 75, width = 100, height = 20)

    # Fenster aktivieren
    tk_fenster.mainloop()


def prototyp6():
    def button_verdoppeln_click():
        # Verwaltung der Daten
        zahl = int(entry_zahl.get())
        # Verarbeitung der Daten
        zahl = zahl * 2
        # Anzeige der Daten
        entry_zahl.delete(0, END)
        entry_zahl.insert(0, str(zahl))

    # Erzeugung des Fensters
    tk_fenster = Tk()
    tk_fenster.title("Eingabe")
    tk_fenster.geometry("120x110")
    
    # Eingabefeld für die Zahl
    entry_zahl = Entry(master = tk_fenster,
                       background = "white")
    entry_zahl.place(x=45, y=40, width=30, height=30)
    entry_zahl.insert(0, 1)
    
    # Button zum Auswerten
    button_verdoppeln = Button(master = tk_fenster,
                               text="Verdoppeln!",
                               command=button_verdoppeln_click)
    button_verdoppeln.place(x=10, y=80, width=100, height=20)
    
    # Fenster aktivieren
    tk_fenster.mainloop()


def prototyp7():
    def radiobutton_click():
        # Verwaltung der Daten
        zahl = spielzahl.get()
        # Verarbeitung der Daten
        # Anzeige der Daten
        label_ausgewaehlte_zahl.config(text = str(zahl))

    # Fenster erzeugen
    tk_fenster = Tk()
    tk_fenster.title("Radio")
    tk_fenster.geometry("120x120")

    # Rahmen für die Zahl
    frame_zahl = Frame(master = tk_fenster,
                       background="#D5E88F")
    frame_zahl.place(x=5, y=5, width=110, height=100)

    # Label mit Überschrift für die Zahl
    label_ueberschrift_zahl = Label(master = frame_zahl,
                                    text = "Zahl",
                                    background = "white")
    label_ueberschrift_zahl.place(x=5, y=5, width=100, height=20)

    # Radiobuttons für die Zahl
    spielzahl = IntVar()
    radiobuttons = []
    for i in range(3):
        radiobuttons.append(Radiobutton(master=frame_zahl,
                                        text=str(i + 1),
                                        value=i + 1,
                                        variable=spielzahl,
                                        command=radiobutton_click))
        radiobuttons[i].place(x=5 + i * 35, y=30, width=30, height=18)

    # Label mit ausgewählter Zahl
    label_ausgewaehlte_zahl = Label(master = frame_zahl,
                                    text = "?",
                                    background = "white")
    label_ausgewaehlte_zahl.place(x=40, y=50, width=30, height=18)

    # Fenster aktivieren
    tk_fenster.mainloop()



def prototyp8():
# httphttp://inf-schule.de/software/gui/miniprojekt_chuckaluck/implementierungeinfachegui/radiobutton

    # Fenster erstellen
    tk_fenster = Tk()
    tk_fenster.title("chuck a luck")
    tk_fenster.geometry("360x165")

    # Label mit Überschrift 
    label_ueberschrift_konto = Label(
        master = tk_fenster,
        text = "chuck a luck",
        font = "Arial 16",
        foreground = "white",
        background = "#889E9D"
    )
    label_ueberschrift_konto.place(x = 10, y = 10, width = 340, height = 35)



    # Rahmen für das Konto
    frame_konto = Frame(master=tk_fenster,
                        background="#FFCFC9")
    frame_konto.place(x=10, y=50, width=110, height=100)
    
    # Label mit Überschrift fürs Konto
    label_ueberschrift_konto = Label(
        master = frame_konto,
        text = "Konto",
        background = "white"
    )
    label_ueberschrift_konto.place(x = 5, y = 5, width = 100, height = 20)

    # Label fuer den Kontostand
    label_konto = Label(master = frame_konto)
    label_konto.config(text = "100")
    label_konto.config(background = "white")
    label_konto.place(x=40, y=35, width=30, height=30)

    def button_einsatz_click():
        # Verwaltung der Daten
        konto = int(label_konto.cget('text'))
        # Verarbeitung der Daten
        konto -= 1
        # Anzeige der Daten
        label_konto.config(text = str(konto))
        einsatz_gezahlt()

    # Button zum Einsatz zahlen
    button_einsatz = Button(master = frame_konto,
                           text = "Einsatz zahlen",
                           command = button_einsatz_click)
    button_einsatz.place(x = 5, y = 75, width = 100, height = 20)

   

    # Rahmen für Gewinnzahl
    frame_zahl = Frame(master=tk_fenster,
                        background="#D5E88F")
    frame_zahl.place(x=125, y=50, width=110, height=100)

    # Label mit Überschrift für Gewinnzahl
    label_ueberschrift_zahl = Label(
        master = frame_zahl,
        text = "Zahl",
        background = "white"
    )
    label_ueberschrift_zahl.place(x = 5, y = 5, width = 100, height = 20)

    def radiobutton_click():
        # Verwaltung der Daten
        # Verarbeitung der Daten
        # Anzeige der Daten
        zahl_gewaehlt()

    # Radiobuttons für die Zahl
    spielzahl = IntVar()
    radiobuttons = []
    for i in range(3):
        radiobuttons.append(Radiobutton(master = frame_zahl,
                                        text = str(i + 1),
                                        value = i + 1,
                                        variable = spielzahl,
                                        command = radiobutton_click))
        radiobuttons[i].place(x=5 + i * 35, y=30, width=30, height=18)
    for i in range(3, 6):
        radiobuttons.append(Radiobutton(master = frame_zahl,
                                        text = str(i + 1),
                                        value = i + 1,
                                        variable = spielzahl,
                                        command = radiobutton_click))
        radiobuttons[i].place(x=5 + (i % 3) * 35, y=52, width=30, height=18)


    def button_auszahlen_click():
        # Verwaltung der Daten
        kontostand = int(label_konto.cget("text"))
        gewinnzahl = spielzahl.get()
        wuerfe = [int(wuerfel.cget("text")) for wuerfel in label_wuerfel]
        gewinn = 0
        # Verarbeitung der Daten
        for wurf in wuerfe:
            if gewinnzahl == wurf:
                gewinn += 1
        # Anzeige der Daten
        label_konto.config(text = str(kontostand + gewinn))
        einsatz_fehlt()

    # Button für Gewinn auszahlen
    button_auszahlen = Button(master = frame_zahl,
                              text = "Gewinn auszahlen",
                              command = button_auszahlen_click)
    button_auszahlen.place(x = 5, y = 75, width = 100, height = 20)




    # Rahmen für die Würfel
    frame_gewinn = Frame(master=tk_fenster,
                        background="#FBD975")
    frame_gewinn.place(x=240, y=50, width=110, height=100)

    # Label mit Überschrift für Würfel
    label_ueberschrift_konto = Label(
        master = frame_gewinn,
        text = "Würfel",
        background = "white"
    )
    label_ueberschrift_konto.place(x = 5, y = 5, width = 100, height = 20)

    # Label fuer die Würfel
    label_wuerfel = []
    for i in range(3):
        label_wuerfel.append(Label(master = frame_gewinn))
        label_wuerfel[i].config(background = "white")
        label_wuerfel[i].place(x=5 + (i * 35), y=35, width=30, height=30)
    
    # Bilder
    bilder_wuerfel = []
    for i in range(6):
        bilder_wuerfel.append(PhotoImage(file = "w{}.gif".format(i + 1)))

    def button_wuerfeln_click():
        # Verwaltung der Daten
        # Verarbeitung der Daten
        # Anzeige der Daten
        for wuerfel in label_wuerfel:
            wurf = random.randint(1,6)
            wuerfel.config(image = bilder_wuerfel[wurf - 1])
            wuerfel.config(text = str(wurf))
        wuerfel_geworfen()
            

    # Button zum Würfeln
    button_wuerfeln = Button(master = frame_gewinn,
                             text = "Würfel werfen",
                             command = button_wuerfeln_click)
    button_wuerfeln.place(x = 5, y = 75, width = 100, height = 20)


    def einsatz_gezahlt():
        button_einsatz.config(state = DISABLED)
        for r in radiobuttons:
            r.config(state = NORMAL)

    def zahl_gewaehlt():
        button_wuerfeln.config(state = NORMAL)

    def wuerfel_geworfen():
        for r in radiobuttons:
            r.config(state = DISABLED)
        button_wuerfeln.config(state = DISABLED)
        button_auszahlen.config(state = NORMAL)

    def einsatz_fehlt():
        button_einsatz.config(state = NORMAL)
        for r in radiobuttons:
            r.config(state = DISABLED)
        button_wuerfeln.config(state = DISABLED)
        button_auszahlen.config(state = DISABLED)

    # Status herstellen
    einsatz_fehlt()
    
    # Fenster aktivieren
    tk_fenster.mainloop()


def prototyp9():
    # Fenster erzeugen
    tk_fenster = Tk()
    tk_fenster.title("Pics")
    tk_fenster.geometry("120x110")

    # Rahmen Würfel
    frame_wuerfel = Frame(master = tk_fenster,
                          background="#FBD975")
    frame_wuerfel.place(x=5, y=5, width=110, height=100)

    # Bilder
    image_wuerfel_1 = PhotoImage(file="w1.gif")

    # Label Würfel B
    label_wuerfel_B = Label(master=frame_wuerfel,
                            image = image_wuerfel_1)
    label_wuerfel_B.place(x=40, y=35, width=30, height=30)

    # Fenster aktivieren
    tk_fenster.mainloop()


def prototyp10():
    # Fenster erzeugen
    tk_fenster = Tk()
    tk_fenster.title("Dias")
    tk_fenster.geometry("120x110")

    # Rahmen Würfel
    frame_wuerfel = Frame(master = tk_fenster,
                          background = "#FBD975")
    frame_wuerfel.place(x=5, y=5, width=110, height=100)

    # Label mit Überschrift für Würfel
    label_ueberschrift_wuerfel = Label(master = frame_wuerfel,
                                       background = "white",
                                       text = "Würfel")
    label_ueberschrift_wuerfel.place(x=5, y=5, width=100, height=20)
    
    # Bilder
    bilder = []
    for i in range(6):
        bilder.append(PhotoImage(file = "w{}.gif".format(i + 1)))

    # Label Würfel Bild
    label_wuerfel_bild = Label(master = frame_wuerfel,
                               image = bilder[0])
    label_wuerfel_bild.place(x=40, y=35, width=30, height=30)

    def button_wuerfel_click():
        # Daten verwalten
        # Daten verarbeiten
        wurf = random.randint(1,6)
        # Daten anzeigen
        label_wuerfel_bild.config(image = bilder[wurf - 1])
        label_wuerfel_bild.config(text = str(wurf))

    # Button für Würfel
    button_wuerfel = Button(master = frame_wuerfel,
                            text = "Würfel werfen!",
                            command = button_wuerfel_click)
    button_wuerfel.place(x=5, y=75, width=100, height=20)

    # Fenster aktivieren
    tk_fenster.mainloop()


def prototyp11():

    # Ereignisverarbeitung

    def button1_click():
        # Daten verwalten
        # Daten verarbeiten
        button1.config(state = DISABLED)
        button2.config(state = NORMAL)
        # Daten anzeigen

    def button2_click():
        # Daten verwalten
        # Daten verarbeiten
        button1.config(state = NORMAL)
        button2.config(state = DISABLED)
        # Daten anzeigen

    # Fenster erzeugen
    tk_fenster = Tk()
    tk_fenster.title("Status")
    tk_fenster.geometry("120x110")

    # Eingabefeld für Zahlen
    button1 = Button(master = tk_fenster,
                     text = "anklicken!",
                     command = button1_click)
    button1.config(state = NORMAL)
    button1.place(x=10, y=40, width=100, height=20)

    # Button zum Auswerten
    button2 = Button(master = tk_fenster,
                     text = "anklicken!",
                     command = button2_click)
    button2.config(state = DISABLED)
    button2.place(x=10, y=80, width=100, height=20)
                     
    # Fenster aktivieren
    tk_fenster.mainloop()


def prototyp12():
    # http://inf-schule.de/software/gui/miniprojekt_chuckaluck/implementierungeinfachegui/leinwand


def main():
    #prototyp11()
    prototyp8()
                  

if __name__ == '__main__':
    main()
