import csv

def gen_has(fio):
    s = "ЙЦУКЕНГШЩЗХЪДЖЭЛОРПАВЫФЯЧСМИТЬБЮЁйцукенгшщзхъэждлорпавыфячсмитьбюё "
    p = 67
    m = 10**9 + 9
    power = 1
    has = 0
    for c in fio:
        has = has + ((s.index(c) + 1) * power) % m
        power = (power * p) % m
    return has

with open("students.csv", encoding="utf8") as file:
    reader = csv.reader(file, delimiter=",")
    answer = list(reader)
print(answer)
for i in range(len(answer)):
    if answer[i][0] == "id":
        answer[i][0] = "id_has"
    else:
        answer[i][0] = str(gen_has(answer[i][1]))
print(answer)
with open("students_with_hash.csv", "w", newline="") as file2:
    writer = csv.writer(file2)
    otv = writer.writerows(answer)