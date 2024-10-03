"""
.Modul
    main.py
    fő modul
.Paraméterek
    sys.argv[1] : A .csv táblázat neve.
    sys.argv[2] : A fejsorok száma: 0|1|2...
    sys.argv[3] : A rendezés oszlopa: 1|2|...
    sys.argv[4] : A rendezés iránya: -1=Csökkenő, 0=Nincs rendezés, 1=Növekvő.
    sys.argv[5] : A 'table' elem CSS osztályának a neve.

.Eredmény file
    A táblázatot töredéket (fragment/snippet) tartalmazó file.
    _html_fragment_table.html

.Indítás példa
    > python main.py c:\\mentes\\mentes.csv 1 1 1 class_simple_table

"""

import sys
import os
import re
import mod_global_valtozok as gv
import mod_generalas as ge


# Függvények, osztályok
# ---------------------


def informacio_inditashoz() -> None:
    print("Alkalmazás indítás:")
    print(
        f"> pyton main.py {gv.argv_parameter_nevek[gv.argv_csv_nev]}",
        f"{gv.argv_parameter_nevek[gv.argv_fejsorok_szama]}",
        f"{gv.argv_parameter_nevek[gv.argv_rendezes_oszlop]}",
        f"{gv.argv_parameter_nevek[gv.argv_rendezes_irany]}",
        f"{gv.argv_parameter_nevek[gv.argv_css_osztaly]}",
    )
    print(
        f"\t{gv.argv_parameter_nevek[gv.argv_csv_nev]} :",
        "ebből a csv táblázatból készül a 'table' .html elem.",
    )
    print(
        f"\t{gv.argv_parameter_nevek[gv.argv_fejsorok_szama]} :",
        "a csv első sorai fejsorok lehetnek: 0|1|2|..."
    )
    print(
        f"\t{gv.argv_parameter_nevek[gv.argv_rendezes_oszlop]} :",
        "a csv táblázat oszlopa, a rendezés oszlopa: 0|1|2|..."
    )
    print(f"\t{gv.argv_parameter_nevek[gv.argv_rendezes_irany]} :",
          "-1 | 0 | 1.")
    print(
        f"\t{gv.argv_parameter_nevek[gv.argv_css_osztaly]} :",
        "a 'table' elem CSS osztályának a neve."
    )


# Programvezérlő osztályok
class exce_argumentum_hiba(Exception):
    pass


class exce_program_vege(Exception):
    pass


def main() -> None:
    print(f"Táblázat Generáló Alkalmazás Egyszerű ( TGAE v{gv.prg_verzio})")
    print("Paraméterek:")
    for i in range(len(sys.argv)):
        if i > 0:
            print(f"\t{i}. {gv.argv_parameter_nevek[i]} = {sys.argv[i]}")

    try:
        # Ellenőrzések

        # Paraméterek száma rendben?
        # --------------------------
        if (len(sys.argv) - 1) != gv.argv_n:
            print(gv.huzenet[1].format(gv.argv_n, (len(sys.argv) - 1)))
            raise exce_argumentum_hiba()

        # A css file létezik?
        # -------------------
        if not os.path.isfile(sys.argv[gv.argv_csv_nev]):
            print(gv.huzenet[2].format(sys.argv[gv.argv_csv_nev]))
            raise exce_argumentum_hiba()

        # A fejsorok száma rendben?
        # -------------------------
        try:
            v_fejsorok_szama = int(sys.argv[gv.argv_fejsorok_szama])
        except ValueError as e:
            print(gv.huzenet[3].format(sys.argv[gv.argv_fejsorok_szama]))
            raise exce_argumentum_hiba()
        except Exception as e:
            print(gv.huzenet[4])
            print(e)
            raise exce_argumentum_hiba()

        if v_fejsorok_szama < 0:
            print(gv.huzenet[5].format(sys.argv[gv.argv_fejsorok_szama]))
            raise exce_argumentum_hiba()

        # A rendezés oszlop rendben?
        # --------------------------
        try:
            v_rendezes_oszlop = int(sys.argv[gv.argv_rendezes_oszlop])
        except ValueError as e:
            print(gv.huzenet[6].format(sys.argv[gv.argv_rendezes_oszlop]))
            raise exce_argumentum_hiba()
        except Exception as e:
            print(gv.huzenet[7])
            print(e)
            raise exce_argumentum_hiba()

        if v_rendezes_oszlop < 0:
            print(gv.huzenet[8].format(sys.argv[gv.argv_rendezes_oszlop]))
            raise exce_argumentum_hiba()

        # A rendezés irány rendben?
        # -------------------------
        try:
            v_rendezes_irany = int(sys.argv[gv.argv_rendezes_irany])
        except ValueError as e:
            print(gv.huzenet[9].format(sys.argv[gv.argv_rendezes_irany]))
            raise exce_argumentum_hiba()
        except Exception as e:
            print(gv.huzenet[10])
            print(e)
            raise exce_argumentum_hiba()

        if v_rendezes_irany not in gv.rendezes_helyesertekek:
            print(
                gv.huzenet[11].format(
                    sys.argv[gv.argv_rendezes_irany], gv.rendezes_helyesertekek
                )
            )
            raise exce_argumentum_hiba()

        if ((v_rendezes_oszlop != 0) and (v_rendezes_irany == 0)) or (
            (v_rendezes_oszlop == 0) and (v_rendezes_irany != 0)
        ):
            print(gv.huzenet[13].format(v_rendezes_oszlop, v_rendezes_irany))
            raise exce_argumentum_hiba()

        # A 'table' elem osztálya rendben?
        # --------------------------------
        if not re.match(gv.regex_css_osztaly, sys.argv[gv.argv_css_osztaly]):
            print(gv.huzenet[12].format(sys.argv[gv.argv_css_osztaly]))
            raise exce_argumentum_hiba()

        ge.tabla_generalas(
            sys.argv[gv.argv_csv_nev],
            v_fejsorok_szama,
            v_rendezes_oszlop,
            v_rendezes_irany,
            sys.argv[gv.argv_css_osztaly],
        )

    except exce_argumentum_hiba:
        informacio_inditashoz()
    except exce_program_vege:
        pass


# Program indítás
# ---------------

main()
