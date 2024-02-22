import csv

with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    sp = list(reader)

for i in range(2, len(sp)):
    while i > 1 and sp[i][4] > sp[i-1][4]:
        sp[i], sp[i-1] = sp[i-1], sp[i]
        i -= 1
kol = 1
print("10 класс:")
for id, name, titleProject_id, clas, score in sp:
    if score != "None" and "10" in clas and kol <= 3:
        fio = name.split()
        print(kol, "место:", fio[1][0] + "." + fio[0])
        kol += 1

