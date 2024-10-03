import csv

teszt_kod = 5

print("\n--ELEJE--")
print("teszt_kod", teszt_kod)
print("")

if 1 == teszt_kod:
    for i in range(1, (2 + 1)):
        print(i)

if 2 == teszt_kod:
    for i in range(1, (1 + 1)):
        print(i)

if 3 == teszt_kod:
    for i in range(1, (0 + 1)):
        print(i)

if 4 == teszt_kod:
    print(sorted([["aaaa", "zzzz"], ["bbbbb", "yyyyyyy"]], key=lambda x: x[0]))

if 5 == teszt_kod:
    fejsorok_szama = 2
    with open("test_csv_fejsorok.csv", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";", quotechar='"')

        fejsorok = list()
        for i in range(1, (fejsorok_szama + 1)):
            fejsorok.append(next(reader))

        torzssorok = sorted(reader, key=lambda x: x[0], reverse=False)

        if len(fejsorok) + len(torzssorok) > 0:
            print("<table>")
            for fejsor in fejsorok:
                print("<tr>")
                for cella in fejsor:
                    print(f"<th>{cella}</th>")
                print("</tr>")
            for torzssor in torzssorok:
                print("<tr>")
                for cella in torzssor:
                    print(f"<td>{cella}</td>")
                print("</tr>")
            print("</table>")
print("\n--VÉGE--")
