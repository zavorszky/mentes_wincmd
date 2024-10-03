import csv

print("\n\n")
with open("test_csv.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";", quotechar='"')
    fejsor=next(reader)
    print(fejsor)
    print("<table>")
    for sor in reader:
        print("<tr>")
        for j in range(len(sor)):
            print(f"<td>{sor[j]}</td>")
        print("</tr>")
    print("</table>")
