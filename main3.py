import csv

with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)
print(answer)
for i in range(1, len(answer)):
    if answer[i][4] == 'None':
        answer[i][4] = '0'
answer = answer[1:]
for i in range(1, len(answer)):
    while (i > 0 and int(answer[i][4]) > int(answer[i-1][4])):
        answer[i], answer[i-1] = answer[i-1], answer[i]
        i = i - 1
print(answer)
k = 0
for id, name, titleProject_id, clas, score in answer:
    if clas[:2] == "10" and k < 3:
        sp = name.split()
        print(sp[1] + " " + sp[0])
        k = k + 1