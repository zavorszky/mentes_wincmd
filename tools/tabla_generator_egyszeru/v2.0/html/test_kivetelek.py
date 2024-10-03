"""
Modul
    test_kivetelek.py
"""

import mod_html as ht

v_tesztesetleirasok = [
    "",
    "Nincsenek sorok",
    "Vannak sorok, nincs class",
    "Vannak sorok és van class",
]
v_teszteset = 3

if v_teszteset == 1:
    print(f"\nTeszt:{v_teszteset}, {v_tesztesetleirasok[v_teszteset]}")
    v_table_class = "aaaaa"
    l_fejsorok = list()
    l_torzssorok = list()
    ht.t_egyszerutablakeszites(
        p_table_class=v_table_class, p_fejsorok=l_fejsorok, p_torzssorok=l_torzssorok
    )

if v_teszteset == 2:
    print(f"\nTeszt:{v_teszteset}, {v_tesztesetleirasok[v_teszteset]}")
    v_table_class = ""
    l_fejsorok = [["Irsz.", "Város"],]
    l_torzssorok = [["3100", "Salgótarján"],]
    ht.t_egyszerutablakeszites(
        p_table_class=v_table_class, p_fejsorok=l_fejsorok, p_torzssorok=l_torzssorok
    )

if v_teszteset == 3:
    print(f"\nTeszt:{v_teszteset}, {v_tesztesetleirasok[v_teszteset]}")
    v_table_class = "simple_table_class"
    l_fejsorok = [["Irsz", "Város"]]
    l_torzssorok = [["3100", "Salgótarján"]]
    ht.t_egyszerutablakeszites(
        p_table_class=v_table_class, p_fejsorok=l_fejsorok, p_torzssorok=l_torzssorok
    )
