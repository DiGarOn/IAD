l = input()
while(len(l)<4):
    l = "0" + l


if(l[0] == l[3] and l[1] == l[2]):
    print(1)
else:
    print(0)