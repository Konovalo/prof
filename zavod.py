import csv

answer = []
with open("zavod.txt", encoding="utf8") as file:
    for s in file:
        sp = s.split("*")
        answer.append(sp)

print(answer)
with open("rezult.csv", "w", newline="") as file2:
    writer = csv.writer(file2)
    an = writer.writerows(answer)