"""
Modul
    mod_global_valtozok.py
    Közös változók
"""

prg_verzio = "2.0"

# Az argumentumok száma
argv_n = 5

# Az argv indexei
argv_program_modul = 0
argv_csv_nev = 1
argv_fejsorok_szama = 2
argv_rendezes_oszlop = 3
argv_rendezes_irany = 4
argv_css_osztaly = 5

argv_parameter_nevek = [
    "Program modul név",
    "csv_név",
    "fejsorok_száma",
    "rendezés_oszlop",
    "rendezés_irány",
    "css_osztály",
]

# Rendezés iránya
rendezes_csokkeno = -1
rendezes_nincs = 0
rendezes_novekvo = 1
rendezes_helyesertekek = [rendezes_csokkeno, rendezes_nincs, rendezes_novekvo]

#
regex_css_osztaly = "^([a-zA-Z]|[0-9]|[_])*$"

#
csv_delimiter = ";"

# Hibaüzenetek
huzenet = [
    "Hincs hiba",
    "Hiba-1:A paraméterek száma csak {0} lehet. Helytelen érték: {1}.",
    "Hiba-2:A csv file ({0}) nem található.",
    "Hiba-3:A fejsorok száma nem egész szám. Hibás érték: {0}",
    "Hiba-4:Hiba a fejsorok számának közben.",
    "Hiba-5:A fejsorok száma csak nulla vagy pozitív szám lehet. Hibás érték{0}",
    "Hiba-6:A rendezés oszlop paraméter típusa nem egész szám. Hibás érték: {0}",
    "Hiba-7:Hiba a rendezés oszlop paraméter feldolgozása közben.",
    "Hiba-8:A rendezés oszlop paraméter csak 0 vagy pozitív szám lehet. Hibás érték: {0}",
    "Hiba-9:A rendezés irány paraméter típusa nem egész szám. Hibás érték: {0}.",
    "Hiba-10:Hiba a rendezés irány paraméter feldolgozása közben.",
    "Hiba-11:Hibás a rendezés iránya paraméter: {0}. Helyes: {1}.",
    "Hiba-12:Hibás a tábla CSS osztálya: {0}.",
    "Hiba-13:A rendezés oszlopa ({0}) és iránya ({1}) ellentmondó.",
]
