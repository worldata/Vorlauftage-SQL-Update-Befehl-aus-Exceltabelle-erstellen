import csv
import sys
import os.path, time
from datetime import datetime
import xlrd
import glob
import pandas as pd


datum_now = datetime.now().strftime('%d.%m.%Y')

# Hier bitte den Dateinamen einfügen inkl. Dateiendung! (Muss eine CSV Datei mit Trennzeichen ";" sein.)
Dateiname = "zensiert.csv"

# Input Pfad (Datei in diesen Pfad oder Pfad ändern)



# Hier bitte die gewünschte Endung der Output Datei einfügen z.B. .xlxs oder .sql oder .txt..
Endung = ".sql"

# Output Pfad (Hier kann der Outputpfad des Ergebnisses beeinflusst werden & der Output-Dateiname angepasst werden)
o = "C:\\Users\Maximilian.Rasch\\Desktop\\Testordner\\Update TG Tage\\" + "Update TG Vorlauftage " + str(datum_now) + Endung



#--select * from pricequote where lf_id in (2,3,4,5,6,7,9,10,11,13,14,15,17,36,44,77,109,262,263,264,265,266) and PQ_ORDER_LEADDAYS is not null

#-- update PRICEQUOTE set PQ_ORDER_LEADDAYS = null where lf_id in (2,3,4,5,6,7,9,10,11,13,14,15,17,36,44,77,109,262,263,264,265,266, 19) and PQ_ORDER_LEADDAYS is not null

# LagerIdentNummer von eigener DB
HamburgW = "5,264"
TottenhamW = "13,265"
LiverpoolW = "6"
DresdenW = "14"
BayreuthW = "3"
BremenW = "15,262"
MoskauW = "44,266"
DortmundW = "109"
BernW = "7"
WarschauW = "36"
KemptenW = "9"
BerlinW = "4"
HalleW = "17,263"
MadridW = "10"
KölnW = "2"

# LagerIdentNummer von Lieferanten
HamburgL = "10"
TottenhamL = "48"
LiverpoolL = "50"
DresdenL = "51"
BayreuthL = "52"
BremenL = "53"
MoskauL = "54"
DortmundL = "55"
BernL = "57"
WarschauL = "58"
KemptenL = "59"
BerlinL = "80"
HalleL = "82"
MadridL = "85"
KölnL = "86"


End1 = ".xlsx"

def converter():
    for file in glob.glob("C:\\Users\\Maximilian.Rasch\\Desktop\\Testordner\\" + "*" + End1):
        data_xls = pd.read_excel((file), 0, index_col=None)
        data_xls.to_csv((file[:-5]) + ".csv", encoding='ANSI')
        global p
        p = file

    
converter()
    

def automat(Spalte, Nummer_LagerLieferant, Nummer_Lager_eigeneDB):
    with open(p, "r", newline="", encoding='ANSI') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        for column in csv_reader:
            if column[Spalte] != str(Nummer_Lager):
                print(
                    "Achtung: In dieser Spalte steht nicht die -"
                    + Nummer_Lager
                    + "- für das Transgourmet Lager. Vorgang abgebrochen bitte Datenquelle prüfen"
                )
                break
            else:
                for column in csv_reader:
                    if column[Spalte] != "":
                        print(
                            "update pricequote set pq_order_leaddays ='"
                            + column[Spalte]
                            + "' where lf_id in ("
                            + Nummer_Lager_Aramark
                            + ") and pq_artnr in('"
                            + column[0].zfill(6)
                            + "','"
                            + column[0].zfill(6)
                            + "A')"
                        ) #zfill -> Artikel auffüllen + Anbruchartikel mit "A" erzeugen


class StdoutRedirection:
    """Standard output redirection context manager"""

    def __init__(self, path):
        self._path = path

    def __enter__(self):
        sys.stdout = open(self._path, mode="w")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = sys.__stdout__

# Spaltennummer in Excel, Lagernummer eigene DB, Lagernummer LF,
with StdoutRedirection(o):
    automat(7, HamburgW, HamburgL)
    automat(8, TottenhamW, TottenhamL)
    automat(9, LiverpoolW, LiverpoolL)
    automat(10, DresdenW, DresdenL)
    automat(11, BayreuthW, BayreuthL)
    automat(12, BremenW, BremenL)
    automat(13, MoskauW, MoskauL)
    automat(14, DortmundW, DortmundL)
    automat(15, BernW, BernL)
    automat(16, BerlinW, BerlinL)
    automat(17, HalleW, HalleL)
    automat(18, MadridW, MadridL)
    automat(19, KölnW, KölnL)
