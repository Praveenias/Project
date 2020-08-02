import pandas as pd
import matplotlib.pyplot as plt

print('******CGPA CALCULATOR*****')
a = input("Enter the department:")

def cgpa(c):
    try:
        l = []
        k = 0
        cr= 0
        grade = {'o':10,'a+':9,'a':8,'b+':7,'b':6,'ra':0}
        b = int(input("ENTER YOUR SEMESTER:"))
        if b:
            h = b-1
            for i in range(h*8,b*8):
                print("Enter marks for",c['SUB_CODE'][i],"-",c['SUBJECT_NAME'][i],":")
                w = input()
                if w not in grade :
                    print("Enter Valid Input")
                    return
                else:
                    l.append(grade[w])
                    k+= int(grade[w]*c['CREDITS'][i])
                    cr+= c['CREDITS'][i]
            print("GPA FOR THE {} SEMESTER IS {}".format(b,k/cr))
            plt.bar(c['SUB_CODE'][h*8:b*8],l)
            plt.xlabel("Subjects")
            plt.ylabel("Marks out of 10")
    except:
        print('**Sorry,Try another time***')
        
                
if a == "cse":
    c = pd.read_excel(r"C:\Users\PRAVEEN\Documents\PYthon_Praveen\CSE.xlsx",sheet_name='CSE')
    cgpa(c)
elif a== "ece":
    c = pd.read_excel(r"C:\Users\PRAVEEN\Documents\PYthon_Praveen\CSE.xlsx",sheet_name='ECE')
    cgpa(c)
elif a=="mech":
    c = pd.read_excel(r"C:\Users\PRAVEEN\Documents\PYthon_Praveen\CSE.xlsx",sheet_name='MECH')
    cgpa(c)
else:
    print("Enter only cse/ece/mech Departments")
    
