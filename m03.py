import csv

with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)
    idi = input()
    while idi != "СТОП":
        flag = False
        for id, name, titleProject_id, clas, score in answer:
            if idi == titleProject_id:
                fio = name.split()
                print("Проект №", titleProject_id, "делал:", fio[1][0] + "." + fio[0],\
                      "он(а) получил(а) оценку -", score)
                flag = True
                break
        if not flag:
            print("Ничего не найдено.")
        idi = input()
