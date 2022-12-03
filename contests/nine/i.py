with open ("input.txt", "r") as f:
    n = int(f.readline())
    hole = set()
    uniq = set()

    for i in range(n):
        m = int(f.readline())
        tmp = set()
        for j in range(m):
            tmp.update(set([f.readline()]))
        if(len(tmp) > len(hole)):
            hole = set()
            hole.update(tmp)
        # hole.update(tmp)
        if(len(uniq)):
            uniq.intersection_update(tmp)
        else:
            uniq.update(tmp)

    print(len(uniq))
    print(*uniq, sep="")
    print(len(hole))
    print(*hole, sep="")