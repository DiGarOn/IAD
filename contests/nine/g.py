with open("input.txt") as f:
    n = int(f.readline())
    no = set()
    yes = set()
    tmp = set()
    digits = set("1234567890")
    for line in f:
        # print(line)
        if(line[0] in digits):
            tmp = set(map(str, line.split()))
        elif line[0] == "Y":
            # print("here")
            if(len(yes) != 0):
                yes.intersection_update(tmp)
            else:
                yes = tmp
        elif line[0] == "N":
            no.update(tmp)
        elif line[0] == "H":
            print(*sorted(yes.difference(no)))

