#ok

with open("input.txt") as f:
    n = int(f.readline())
    yes = {i for i in range(1, n+1)}
    tmp = set()
    digits = set("0123456789")
    for line in f:
        if(line[0] in digits):
            tmp = set(map(int, line.split()))
        elif line[0] == "Y":
            yes.intersection_update(tmp)
        elif line[0] == "N":
            yes.difference_update(tmp)
        elif line[0] == "H":
            print(*sorted(yes))