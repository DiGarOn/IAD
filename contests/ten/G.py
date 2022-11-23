with open("input.txt") as f:
    d = {}
    k = 0
    for line in f:
        if(line in d.keys()):
            d[line] += 1
        else:
            d[line] = 1
        k += 1
    l = []
    for i in d.keys():
        l.append((d[i], i))
    l.sort(reverse=True)
    if(l[0][0] > k/2):
        print(l[0][1])
    else:
        print(l[0][1])
        print(l[1][1])