LETTER = 'h'

s = input()
# s = "1h23h45h6"

s = s[:s.find(LETTER)] +  s[s.find(LETTER):s.rfind(LETTER)+1][::-1] + s[s.rfind(LETTER)+1:]

print(s)