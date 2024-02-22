import csv

mn = set()
sp = ['9г', '9т', '11в', '8х', '11и']
summ = [0] * 5
kol = [0] * 5
with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)
    #print(answer) вывожу список списков для анализа

    for id, name, title, clas, score in answer:
        if "Хадаров Владимир" in name:
            print("Ты получил:", score, "за проект -", title)
        '''if score == "None":
            mn.add(clas)
            Узнаем какие классы имеют пустые оценки по проектам
            '''
        if score != "None" and (clas in sp):
            i = sp.index(clas) #узнаем по какому индексу находится класс
            summ[i] = summ[i] + int(score)
            kol[i] = kol[i] + 1
#print(mn) выводим классы с пустыми полями
with open("student_new.csv", "w", newline="") as file2:
    writer = csv.writer(file2)
    for id, name, title, clas, score in answer:
        if score == "None":
            i = sp.index(clas)
            score = str(summ[i] / kol[i])[:-13]
        writer.writerow([id, name, title, clas, score])

with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)[1:]
    for i in range(len(answer)-1):
        id, name, title, clas, score = answer[i]
        if score == "None":
            score = 0
        #while i-1 > 0 and answer[i][4] > answer[i-1][4]:





