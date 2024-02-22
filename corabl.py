def fu(n, m, t, xd, yd):
    if n > 5:
        x = n + xd
    else:
        x = -1*(n+xd) * 4 + t
    if m > 3:
        y = m + t + yd
    else:
        y = -1 *(n + yd) * m
    return x, y
answer = []
with open("space.txt", encoding="utf8") as file:
    for s in file:
        sp = s.strip().split("*")
        print(sp)
        if sp[2] == "0 0":
            ps = sp[0].split("-")
            n = int(ps[1][0])
            m = int(ps[1][1])
            t = len(sp[1])
            xd, yd = map(int,sp[3].split())
            x, y = fu(n, m, t, xd, yd)
            sp[2] = str(x) + " " + str(y)
        answer.append(sp)
with open("space_new.txt", "w") as file2:
    for i in range(len(answer)):
        print(answer[i], file=file2)
