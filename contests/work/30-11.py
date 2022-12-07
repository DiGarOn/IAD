import pandas as pd
import numpy as np
students = pd.read_csv("/Users/dmitriygarkin/Documents/PL/IAD/ESS8-9.csv")
students = students.drop("Unnamed: 9", axis=1)
students = students.drop("Unnamed: 10", axis=1)
students = students.drop("Unnamed: 11", axis=1)
print(students.head())
#1:
print(students.shape)
# 9 x 56591

#2:
print(students.isna().sum())
#yes in inwyys, rlgdnm

#3:
print("unic cntry:", students["cntry"].nunique())
#31
print("unic rlgdnm:", students["rlgdnm"].nunique())
#8

#4:
print(students["rlgdnm"].value_counts().idxmax())
# 1

#5:
if(students["nwspol"].mean() > students["netustm"].mean()):
    print("nwspol")
else:
    print("netustm")
#netustm

#6:
print(students.describe()["nwspol"]["75%"])
#90.0

#7:
print(students["cntry"].corr(students["lrscale"]))

#9:
print(students[["lrscale", 'gndr']].groupby('gndr').mean())
#1

#10:
students["lrevg"] = students["lrscale"] < students["lrscale"].mean()
print(students.head())

#11:
students.sort_values("netustm", axis = 0, ascending = False, na_position='last', inplace = True)
students.to_csv("new_ESS8-9.csv", encoding = 'utf-16', index = False)