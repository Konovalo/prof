import csv
with open("student_new2.csv") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)
st = input() #
while st != "СТОП": #
    flag = True
    for id, name, title, clas, score in answer:
        if st == title:
            print("Проект № <N> делал: <И. Фамилия>он(а) получил(а) оценку - <ОЦЕНКА>.")
            flag = False
            break
    if flag:
        print("Ничего не найдено.")
    st = input()