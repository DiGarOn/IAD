s = input()
is_first = False
is_last = False
last_id = 0
for i in range(len(s)):
    if(s[i] == "h"):
        if(is_first):
            s = s[:i] + "H" + s[i+1:]
        else:
            is_first = True
        last_id = i
s = s[:last_id] + "h" + s[last_id+1:]
print(s)
