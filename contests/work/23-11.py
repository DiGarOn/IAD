from pandas import *
d = {'kg':[86,55,92,79], 'm':[1.7,1.58,2,1.78]}

df = DataFrame(data=d,index = ["Michael", "Anne", "John", "Harry"])
print(df)

bmi = {'bmi': [round(d['kg'][i]/(d['m'][i]**2), 2) for i in range(4)]}
print(bmi)
df['bmi'] = bmi['bmi']

print(df)

def check(i):
    if i < 18.5:
        return "недостаточная масса тела"
    elif (i>= 18.5 and i <= 24.99):
        return "норма"
    else:
        return "избыточная масса тела"

bmi_category = [check(bmi['bmi'][i]) for i in range(4)]
df["bmi_category"] = bmi_category

print(df)

df.to_csv("people.csv", encoding = 'utf-16', index = False)
print(df[df["bmi_category"] == "норма"])
print(len(df[df["bmi_category"] == "норма"]))