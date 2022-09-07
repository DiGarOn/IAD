mas_1 = list(map(int,input().split()))
mas_2 = list(map(int,input().split()))

mas_1.sort()
mas_2.sort()

count = 0

while(len(mas_1) != 0 and len(mas_2) != 0):
    if(mas_1[0] < mas_2[0]):
        mas_1.pop(0)
    else:
        count += 1
        mas_1.pop(0)
        mas_2.pop(0)
print(count)
