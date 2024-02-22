import csv

with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)

for id, name, titleProject_id, clas, score in answer:
    if "Хадаров Владимир" in name:
        print("Ты получил:", score, "за проект -", titleProject_id)
mn = set()
for id, name, titleProject_id, clas, score in answer:
    if score == "None":
        mn.add(clas)
sp = ['8х', '11в', '11и', '9т', '9г']
sum = [0] * 5
kol = [0] * 5
for id, name, titleProject_id, clas, score in answer:
    if score != "None" and clas in sp:
        i = sp.index(clas)
        sum[i] = sum[i] + int(score)
        kol[i] = kol[i] + 1
with open("student_new2.csv", "w", newline="") as file2:
    writer = csv.writer(file2)
    for id, name, titleProject_id, clas, score in answer:
        if score == "None":
            i = sp.index(clas)
            score = str(round(sum[i] / kol[i], 2))
        writer.writerow([id, name, titleProject_id, clas, score])

