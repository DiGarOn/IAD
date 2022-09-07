s = input()
a = s.find(";")
b = s.find(":")
is_here = True
if(a == -1):
    if(b == -1):
        print(0)
        is_here = False
    else:
        s = s[b:]
else:
    if(b == -1):
        s = s[a:]
    else:
        s = s[min(a,b):]

count_s = 0
count_m = 0
count_e = 0

count = 0
if(is_here):
    for i in range(len(s)):
        if(s[i] == ";" or s[i] == ":"):
            count_s += 1
        elif(s[i] == "-"):
            count_m += 1
        elif(s[i] == "]" or s[i] == "[" or s[i] == "(" or s[i] == ")"):
            if(count_s > 0):
                count += 1
                count_s = 0
                count_m = 0
                count_e = 0
            else:
                count_e = 0
        else:
            count_s = 0
            count_m = 0
            count_e = 0
    print(count)