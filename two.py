import csv

with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)
for id, name, titleProject_id, clas, score in answer:
    if score == "None":
        score = str(0)
for i in range(2, len(answer)):
    while i > 1 and answer[i][4] > answer[i - 1][4]:
        answer[i], answer[i - 1] = answer[i - 1], answer[i]
        i = i - 1
kol = 0
for id, name, titleProject_id, clas, score in answer:
    if clas[:2] == "10" and kol != 3:
        kol = kol + 1
        sp = name.split()
        print(kol, "место: " + sp[1][0] + "." + sp[0])