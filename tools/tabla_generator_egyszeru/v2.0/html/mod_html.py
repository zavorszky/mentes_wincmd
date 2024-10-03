"""
Modul
    mod_html.py
"""


# Figyelmeztetések
# ----------------
class W_etk_nincsenek_sorok(Exception):
    def __init__(self):
        self.kategoria = "W"
        self.message = f"{self.kategoria}:A táblázat készítéshez nincsenek sorok."


def t_egyszerutablakeszites(
    p_table_class: str, p_fejsorok: list, p_torzssorok: list
) -> None:
    v_fejsorok_szama = len(p_fejsorok)
    v_torzssorok_szama = len(p_torzssorok)

    try:
        # Kell készíteni HTML táblázatot?
        if v_fejsorok_szama + v_torzssorok_szama <= 0:
            raise W_etk_nincsenek_sorok

        # Tábla készítés
        print(
            "<table"
            + ("" if p_table_class == "" else f' class="{p_table_class}"')
            + ">"
        )

        # Fejsorok, ha vannak
        for v_fejsor in p_fejsorok:
            print("<tr>")
            for cella in v_fejsor:
                print(f"<th>{cella}</th>")
            print("</tr>")

        # Törzssorok, ha vannak
        for v_torzssor in p_torzssorok:
            print("<tr>")
            for cella in v_torzssor:
                print(f"<td>{cella}</td>")
            print("</tr>")

        print("</table>")
        # KÉSZ - Tábla készítés
    except W_etk_nincsenek_sorok as e:
        print(e.message)
    except Exception as e:
        print(e)
