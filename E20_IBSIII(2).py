import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.pipeline import Pipeline

from sklearn.ensemble import RandomForestClassifier


ds=pd.read_csv("C://Users//shrey//early_detection_Alzheimers.csv")

ds['Group'] = ds['Group'].replace(['Converted'], ['Demented'])
ds['Group'] = ds['Group'].replace(['Demented', 'Nondemented'], [1,0]) 
ds['M/F'] = ds['M/F'].replace(['M', 'F'], [1,0])
ds['Hand'] = ds['Hand'].replace(['R', 'L'], [1,0])
ds.dropna(inplace=True)
print(ds)

ds.info()

x=ds.drop(['Group'], axis=1)
y=ds['Group']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)








pipeline_lr  = Pipeline([('scalar1',StandardScaler()),
                         ('lr_classifier',LogisticRegression())])

pipeline_knn = Pipeline([('scalar2',StandardScaler()),
                          ('knn_classifier',KNeighborsClassifier())])

pipeline_svc = Pipeline([('scalar3',StandardScaler()),
                         ('svc_classifier',SVC())])

pipeline_dt = Pipeline([('dt_classifier',DecisionTreeClassifier())])
pipeline_rf = Pipeline([('rf_classifier',RandomForestClassifier(max_depth=3))])
pipelines = [pipeline_lr,
            pipeline_knn,
            pipeline_svc,
            pipeline_dt,
            pipeline_rf]
pipelines




for pipe in pipelines:
    pipe.fit(X_train,y_train)
pipe_dict = {0:'LR',
             1:'KNN',
             2:'SVC',
             3:'DT',
             4: 'RF'}
pipe_dict




for i,model in enumerate(pipelines):
    print("{} Test Accuracy:{}".format(pipe_dict[i],model.score(X_test,y_test)*100))





X = ds.drop('Group',axis=1)
y = ds['Group']




rf =RandomForestClassifier(max_depth=3)




rf.fit(X,y)




new_data = pd.DataFrame({
    'M/F':0,
    'Hand':1,
    'Age':88,
    'EDUC':18,
    'SES':3,
    'MMSE':28,
    'CDR':0,
    'eTIV':1215, 
    'nWBV':0.71},index=[0])

p = rf.predict(new_data)


if p[0] == 0:
    print('Non-demented')
else:
    print('Demented')



import joblib

joblib.dump(rf,'model_joblib_alzheimers')

model = joblib.load('model_joblib_alzheimers')



model.predict(new_data)



from tkinter import *
import joblib
import numpy as np
from sklearn import *
def show_entry_fields():
    p1=float(e1.get())
    p2=float(e2.get())
    p3=float(e3.get())
    p4=float(e4.get())
    p5=float(e5.get())
    p6=float(e6.get())
    p7=float(e7.get())
    p8=float(e8.get())
    p9=float(e9.get())
   
    model = joblib.load('model_joblib_alzheimers')
    result=model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p9]])
    
    if result == 0:
        Label(master, text="Non-Demented").grid(row=31)
    else:
        Label(master, text="Demented").grid(row=31)
    
    
master = Tk()
master.title("Alzheimer's Prediction Using Machine Learning")


label = Label(master, text = "Alzheimer's Prediction Using Machine Learning"
                          , bg = "black", fg = "white"). \
                               grid(row=0,columnspan=2)


Label(master, text="Gender").grid(row=1)
Label(master, text="Dominant Hand").grid(row=2)
Label(master, text="Enter Value of Age").grid(row=3)
Label(master, text="Enter Value of EDUC").grid(row=4)
Label(master, text="Enter Value of SES").grid(row=5)
Label(master, text="Enter Value of MMSE").grid(row=6)
Label(master, text="Enter Value of CDR").grid(row=7)
Label(master, text="Enter Value of eTIV").grid(row=8)
Label(master, text="Enter Value of nWBV").grid(row=9)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)
e7.grid(row=7, column=1)
e8.grid(row=8, column=1)
e9.grid(row=9, column=1)

Button(master, text='Predict', command=show_entry_fields).grid()

mainloop()