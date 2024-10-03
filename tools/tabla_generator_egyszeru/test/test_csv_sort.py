import csv

teszt_kod = 1
teszt_kod = 2
teszt_kod = 3

print("\n--ELEJE--")
print("teszt_kod", teszt_kod)

if 1 == teszt_kod:
    with open("test_csv_sort.csv", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";", quotechar='"')
        for sor in reader:
            print(sor)

if 2 == teszt_kod:
    with open("test_csv_sort.csv", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";", quotechar='"')
        # for sor in reader:
        #     print(sor)
        listv = sorted(reader, key=lambda x: x[1], reverse=False)
        print("<table>")
        for rendezett_sor in listv:
            print("<tr>")
            print(rendezett_sor)
            print("</tr>")
        print("</table>")

if 3 == teszt_kod:
    with open("test_csv_sort.csv", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";", quotechar='"')
        listv = sorted(reader, key=lambda x: x[1], reverse=False)
        print("<table>")
        for rendezett_sor in listv:
            print("<tr>")
            # print(rendezett_sor)
            for cella in rendezett_sor:
                print(f"<td>{cella}</td>")
            print("</tr>")
        print("</table>")

print("--VÉGE--\n")
