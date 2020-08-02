import matplotlib.pyplot as plt
import numpy as np

print("\t\t****CGPA CALCULATOR*****")
a = input("Enter the department cse/ece/mech:")
def cgpa(dept_paper,dept_credit):
    try:
        grade = {'o':10,'a+':9,'a':8,'b+':7,'b':6,'ra':0}
        b = int(input("ENTER YOUR SEMESTER:"))
        k = 0
        li = []
        cr = 0
        for i in range(len(dept_paper[b-1])):
            print("ENTER YOUR GRADE ON",dept_paper[b-1][i])
            w = input()
            li.append(grade[w])
            if w =='' or w not in grade:
                print("PLEASE,ENTER VALID INPUT")
                break
                return
            elif w =='ra':
                pass
            else:
                
                k+= int(grade[w]*dept_credit[b-1][i])
                cr+= dept_credit[b-1][i]
        print("GPA FOR THE {} SEMESTER IS {}".format(b,k/cr))
    except:
        print("\t\t**&**TRY ANOTHER TIME**&**")
    xaxis = np.arange(len(cse_paper[b]))
    plt.xticks(xaxis,cse_paper[b-1])
    plt.bar(xaxis,li)

if a =='cse':
    cse_paper =[['MATHS-1','ENGINEERING CHEMISTRY','ENGINEERING PHYSICS','ENGINEERING GRAPHICS','PROBLEM SOLVING THROUGH PYTHON','ENGLISH-1','PYTHON LABROTARY','PHYSICS AND CHEMISTRY LABORATATY'],
               ['ENGLISH-2','PHYSICS=2','EVS','MATHS-2','PROGRAMING IN C','BASIC ELECTRIC ENGINEERING','ENGINEERNG PRACTISE LABAROTARY','C LABORARTRY'],
               ['DISCREATE MATHEMATICS','DIGITAL PRINCIPAL AND SYSTEM DEISGN','DATA STRUCTURE','OOP LAUNGUAGE','COMMUNUCATION ENGINEERING','DATA STRUCTURE LAB','OOP LAB','DIGITAL SYSTEM LAB','INTERPERSONNEL SKILL LAB'],
               ['PQT','COMPUTER ARCHITECTURE','DBMS','DAA','OS','SOFTWARE ENGINEERING','DBMS LAB','OOPS LAB','ADVANCED WRITING AND READING LAB'],[]]
    cse_credit = [[4,3,3,4,3,4,2,2],[4,3,3,4,3,3,2,2],[4,4,3,3,3,2,2,2,1],[4,3,3,3,3,3,2,2,1]]
    cgpa(cse_paper,cse_credit)
    
elif a =='ece':
    pass
elif a =='mech':
    pass
else:
    print("PLEASE,ENTER ONLY THOSE 3 DEPARTMENT")
