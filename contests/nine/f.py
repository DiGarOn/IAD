with open("input.txt") as f:
    s = set()
    for line in f:
        s.update(set(list(map(str,line.split()))))
    print(len(s))