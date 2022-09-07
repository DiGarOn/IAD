n, k = map(int,input().split())

mas = [0]*n

for i in range(n):
    mas[i] = list(map(int,input().split()))

for l in range(n):
    for i in range(n):
        l_insex = i
        for j in range(i+1, n):
            if(abs(k-mas[j][l]) == abs(k-mas[l_insex][l])):
                if(mas[j][l] < mas[l_insex][l]):
                    l_insex = j
            elif(abs(k-mas[j][l]) < abs(k-mas[l_insex][l])):
                l_insex = j
        mas[i][l], mas[l_insex][l] = mas[l_insex][l], mas[i][l]


for i in range(n):
    s = ""
    for j in range(n):
        s += str(mas[i][j]) + " "
    print(s)