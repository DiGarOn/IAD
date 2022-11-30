with open("input.txt", "r") as f:

    d = {
        9 : 0,
        10 : 0,
        11 : 0
    }

    for line in f:
        l = list(map(str, line.split()))
        key = l[2]
        value = l[3]
        # print(key, value)
        if(int(value) > d[int(key)]):
            d[int(key)] = int(value)
    print(*d.values())