"""
Modul
    mod_generalas.py
    table .html fragment/snippet készítése.
"""

import mod_global_valtozok as gv
import csv


def tabla_generalas(
    p_csv_nev: str,
    p_fejsorok_szama: int,
    p_rendezes_oszlop: int,
    p_rendezes_irany: int,
    p_css_osztaly: str,
) -> None:
    with open(p_csv_nev, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";", quotechar='"')

        # Fejsorok leválasztása
        # ---------------------
        fejsorok = list()
        for i in range(1, (p_fejsorok_szama + 1)):
            fejsorok.append(next(reader))

        # Rendezés, ha kell
        # -----------------
        if p_rendezes_irany == gv.rendezes_nincs:
            torzssorok = list()
            for torzssor in reader:
                torzssorok.append(torzssor)
        else:
            # torzssorok = sorted(reader, key=lambda x: x[0], reverse=False)
            torzssorok = sorted(
                reader,
                key=lambda x: x[p_rendezes_oszlop],
                reverse=(False if p_rendezes_irany == gv.rendezes_novekvo else False),
            )

        # HTML táblázat készítés, ha lehet
        # --------------------------------
        if len(fejsorok) + len(torzssorok) > 0:

            # A táblázat css osztályának beírása, ha van.
            if p_css_osztaly == "":
                print("<table>")
            else:
                print(f'<table class="{p_css_osztaly}">')

            # Fejsorok, ha vannak
            for fejsor in fejsorok:
                print("<tr>")
                for cella in fejsor:
                    print(f"<th>{cella}</th>")
                print("</tr>")

            # Törzssorok, ha vannak
            for torzssor in torzssorok:
                print("<tr>")
                for cella in torzssor:
                    print(f"<td>{cella}</td>")
                print("</tr>")

            print("</table>")
