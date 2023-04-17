import pandas as pd
import plotly.express as px

raw = pd.read_csv('Grenoble_raw.csv')
info = pd.read_csv('Grenoble.csv')

valid = False # min  age filter
while (valid == False):
    age_min = input("please enter the min age you want data for (leave blank for no limit): ") #getting filters
    if (age_min.isdigit() == True or age_min == ""):

        valid = True
    else:
        print("that value is not valid please enter a number")
        continue

valid = False #max age filter
while (valid == False):
    age_max = input("please enter the max age you want data for (leave blank for no limit): ")
    if (age_max.isdigit() == True or age_max == ""):
        if (age_max.isdigit() == True and age_min.isdigit() == True and age_max < age_min):
            print("that value is smaller than your min. This is impossible")
        else:
            valid = True
    else:
        print("that value is not valid please enter a number")
        continue


valid = False #min bmi filter
while (valid == False):
    bmi_min = input("please enter the min BMI you want data for (leave blank for no limit): ")
    if (bmi_min.isdigit() == True or bmi_min == ""):
        valid = True
    else:
        print("that value is not valid please enter a number")
        continue


valid = False # max bmi filter
while (valid == False):
    bmi_max = input("please enter the max BMI you want data for (leave blank for no limit): ")
    if (bmi_max.isdigit() == True or bmi_max == ""):
        if (bmi_max.isdigit() == True and bmi_min.isdigit()== True and bmi_max < bmi_min):
            print("that value is smaller than your min. This is impossible")
        else:
            valid = True
    else:
        print("that value is not valid please enter a number")
        continue

valid = False # sex filter
while (valid == False):
    sex = input("Which sex would you like to see data for (M/F) (leave blank for any): ")
    sex = sex.upper()
    if (sex == "M" or sex == "F" or sex == ""):
        valid = True
    else:
        print(sex + " is not a valid sex please enter M/F (leave blank for any) ")

valid = False # Smokers filter
while (valid == False):
    smoke = input("Would you like to see data for smokers Yes/No (leave blank for any): ")
    smoke = smoke.lower()
    if (smoke == "yes" or smoke == "no" or smoke == ""):
        valid = True
    else:
        print(smoke + " is not a valid answer please enter yes or no (leave blank for any) ")


if (age_min.isdigit() == True):
    age_min = int(age_min)#convert string input to int
if (age_max.isdigit() == True):
    age_max = int(age_max)
if (bmi_min.isdigit() == True):
    bmi_min = int(bmi_min)
if (bmi_max.isdigit() == True):
    bmi_max = int(bmi_max)


if (age_min != ""):# applying filters
    info = info[info['Age__years_'] >= age_min] #filtering csv file using user input filters
if (age_max != ""):
    info = info[info['Age__years_'] <= age_max]
if (bmi_min != ""):
    info = info[info['VAR15'] >= bmi_min]
if (bmi_max != ""):
    info = info[info['VAR15'] <= bmi_max]
if (sex != ""):
    info = info[info['VAR3'] == sex]
if (smoke != ""):
    info = info[info['Smoking_behavior___current_smoki'] == smoke]



patients = []
id = info['UnID']
for i in id: #fill array of IDs
    patients.append(i)



valid = False
while (valid == False):
    choice = input("which graph would you like (HR/DBP/SBP): ")
    choice = choice.upper()
    if (choice == "HR" or choice == "DBP" or choice == "SBP" ):
        valid = True
    else:
        print("Please enter the abbreviation of the stat you want to graph. " + choice + " is invalid")



temp = 0
for i in id: #print array of IDs
    print( (str(temp + 1)) + ". " + patients[temp])
    temp += 1



if (choice == "HR"):

    fig = px.line(title='Heart rate')
    temp = 0
    for i in patients:
        df1 = raw[raw['UNID'] == patients[temp]]
        df2 = df1[df1['HR'] != 0]
        fig.add_scatter(x=df2['RID'], y=df2['HR'])
        temp += 1
    fig.show()

if (choice == "SBP"  ):
    fig = px.line(title='SBP')
    temp = 0
    for i in patients:
        df1 = raw[raw['UNID'] == patients[temp]]
        df2 = df1[df1['HR'] != 0]
        fig.add_scatter(x=df2['RID'], y=df2['SBP'])
        temp += 1
    fig.show()

if (choice == "DBP"  ):
    fig = px.line(title='DBP')
    temp = 0
    for i in patients:
        df1 = raw[raw['UNID'] == patients[temp]]
        df2 = df1[df1['HR'] != 0]
        fig.add_scatter(x=df2['RID'], y=df2['DBP'])
        temp += 1
    fig.show() # displaying the graph object


