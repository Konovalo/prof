import csv

with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)
    for id, name, titleProject_id, clas, score in answer:
        if "Хадаров Владимир" in name:
            print("Ты получил:", score, "за проект -", titleProject_id)

""" Множество (mn) используя для поиска 
классов проектов без оценки."""

mn = set()
for id, name, titleProject_id, clas, score in answer:
    if score == "None":
        mn.add(clas)
sp = ['9г', '11и', '8х', '11в', '9т']
sp1 = [0] * 5
sp2 = [0] * 5
""" Ищу сумму и количество
Описание аргументов:
 sp1 – список сумм
 sp2 – список количеств
"""
for id, name, titleProject_id, clas, score in answer:
    if clas in sp and score != "None":
        ind = sp.index(clas)
        sp1[ind] += int(score)
        sp2[ind] += 1
with open("student_new3.csv", "w", newline="") as file2:
    writer = csv.writer(file2)
    for id, name, titleProject_id, clas, score in answer:
        if score == "None":
            ind = sp.index(clas)
            score = str(round(sp1[ind]/sp2[ind], 3))
        writer.writerow([id, name, titleProject_id, clas, score])

with open("student_new3.csv") as file:
    reader = csv.reader(file)
    answer = list(reader)
print(answer)
