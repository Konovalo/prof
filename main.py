import csv


mn = set()
# 9г - 0, 11в - 1, 9т - 2, 9х - 3, 11и - 4
sp = ['9г', '11в', '9т', '8х', '11и']
sp1 = [0] * 5 #сумма
sp2 = [0] * 5 #количество
g = gk = gv = v = x = gx = i = gi = t = gt = 0
with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)
    #print(answer)
    for id, name, title, clas, score in answer:
        if "Старокожев Артём" in name:
            print("Он учится в", clas)
        if score != 'None':
            for i in range(len(sp)):
                if clas == sp[i]:
                    sp1[i] = sp1[i] + int(score)
                    sp2[i] = sp2[i] + 1

with open("stu2.csv", "w", newline="") as file2:
    write = csv.writer(file2)
    write.writerow(answer[0])
    answer = answer[1:]
    for id, name, title, clas, score in answer:
        if score != 'None':
            write.writerow([id, name, title, clas, score])
        else:
            k = str((sp1[sp.index(clas)] /sp2[sp.index(clas)]))
            write.writerow([id, name, title, clas,k] )




