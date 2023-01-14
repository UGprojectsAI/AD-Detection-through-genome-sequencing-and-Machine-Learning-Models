import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import metrics,neighbors,svm
from sklearn.metrics import confusion_matrix, precision_score,recall_score, f1_score, accuracy_score





ds=pd.read_csv("C://Users//shrey//early_detection_Alzheimers.csv")
ds['Group'] = ds['Group'].replace(['Converted'], ['Demented']) # Target variable
ds['Group'] = ds['Group'].replace(['Demented', 'Nondemented'], [1,0]) # Target variable
ds['M/F'] = ds['M/F'].replace(['M', 'F'], [1,0])
ds['Hand'] = ds['Hand'].replace(['R', 'L'], [1,0])
ds.dropna(inplace=True)
print(ds)


ds.info()
x=ds.drop(['Group'], axis=1)
y=ds.Group





x_tr, x_te, y_tr, y_te = train_test_split(x, y, test_size=0.2, random_state=1)
model = DecisionTreeClassifier(criterion="entropy", max_depth=3)#hyper parameter
model = model.fit(x_tr,y_tr)
y_pred = model.predict(x_te)
dt_cm=confusion_matrix(y_te,y_pred)
dt_ac=metrics.accuracy_score(y_te, y_pred)*100
dt_ps=metrics.precision_score(y_te, y_pred)*100
dt_rs=metrics.recall_score(y_te, y_pred)*100
dt_f1s=metrics.f1_score(y_te, y_pred)*100





Knn=neighbors.KNeighborsClassifier()
Knn.fit(x_tr,y_tr)
Y_knn=Knn.predict(x_te)
knn_ac=metrics.accuracy_score(y_te,Y_knn)*100
knn_ps=metrics.precision_score(y_te,Y_knn)*100
knn_rs=metrics.recall_score(y_te,Y_knn)*100
knn_f1s=metrics.f1_score(y_te,Y_knn)*100




SVM=svm.SVC()
SVM.fit(x_tr,y_tr)
Y_SVM=SVM.predict(x_te)
svm_ac=metrics.accuracy_score(y_te,Y_SVM)*100
svm_ps=metrics.precision_score(y_te, y_pred)*100
svm_rs=metrics.recall_score(y_te, y_pred)*100
svm_f1s=metrics.f1_score(y_te, y_pred)*100

model=LogisticRegression(multi_class='multinomial',random_state=42,solver='newton-cg')  #creating an object to train
model.fit(x_tr,y_tr)
y_LR= model.predict(x_te)
lr_ac=metrics.accuracy_score(y_te,y_LR)*100
lr_ps=metrics.precision_score(y_te,y_LR)*100
lr_rs=metrics.recall_score(y_te,y_LR)*100
lr_f1s=metrics.f1_score(y_te,y_LR)*100



knn_ac=metrics.accuracy_score(y_te,Y_knn)*100
svm_ac=metrics.accuracy_score(y_te,Y_SVM)*100
dt_ac=metrics.accuracy_score(y_te,y_pred)*100
lr_ac=metrics.accuracy_score(y_te,y_LR)*100

root=tk.Tk()


def Acc():
    data1 ={'x':['KNN','SVM','DT','LR']
    ,'y':[knn_ac,svm_ac,dt_ac,lr_ac]}
    df1 = pd.DataFrame(data1)
    root=tk.Tk()
    figure1 = plt.Figure(figsize=(6, 5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, root)
    bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df1 = df1[['x', 'y']].groupby('x').sum()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_title('SVM VS KNN VS DT VS LR (ACCURACY)')

def Prec():
    data2 ={'x':['KNN','SVM','DT','LR']
    ,'y':[knn_ps,svm_ps,dt_ps,lr_ps]}
    df2 = pd.DataFrame(data2)
    root=tk.Tk()
    figure2 = plt.Figure(figsize=(6, 5), dpi=100)
    ax2 = figure2.add_subplot(111)
    bar2 = FigureCanvasTkAgg(figure2, root)
    bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df2 = df2[['x', 'y']].groupby('x').sum()
    df2.plot(kind='bar', legend=True, ax=ax2)
    ax2.set_title('SVM VS KNN VS DT VS LR (PRECISION)')

def Rec():
    data3 ={'x':['KNN','SVM','DT','LR']
    ,'y':[knn_rs,svm_rs,dt_rs,lr_rs]}
    df3 = pd.DataFrame(data3)
    root=tk.Tk()
    figure3 = plt.Figure(figsize=(6, 5), dpi=100)
    ax3 = figure3.add_subplot(111)
    bar3 = FigureCanvasTkAgg(figure3, root)
    bar3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df3 = df3[['x', 'y']].groupby('x').sum()
    df3.plot(kind='bar', legend=True, ax=ax3)
    ax3.set_title('SVM VS KNN VS DT VS LR (RECALL SCORE)')
    

def f1():
    data4 ={'x':['KNN','SVM','DT','LR']
    ,'y':[knn_f1s,svm_f1s,dt_f1s,lr_f1s]}
    df4 = pd.DataFrame(data4)
    root=tk.Tk()
    figure4 = plt.Figure(figsize=(6, 5), dpi=100)
    ax4 = figure4.add_subplot(111)
    bar4 = FigureCanvasTkAgg(figure4, root)
    bar4.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    df4 = df4[['x', 'y']].groupby('x').sum()
    df4.plot(kind='bar', legend=True, ax=ax4)
    ax4.set_title('SVM VS KNN VS DT VS LR (F1 SCORE)')
    


    
b1 = Button(root,text='ACCURACY',height = 5,width = 30,command=Acc,bg = 'pink',fg='black').place(x=650,y=200)  

b2 = Button(root,text='PRECISION',height = 5,width = 30,command=Prec,bg = 'orange',fg='black').place(x=650,y=350)

b3 = Button(root,text='RECALL',height = 5,width = 30,command=Rec,bg = 'yellow',fg='black').place(x=650,y=500)

b4 = Button(root,text='F1',height = 5,width = 30,command=f1,bg = 'cyan',fg='black').place(x=650,y=650)

root.geometry('2500x2500')
root.config(background = 'black')
picture = Image.open("C://Users//shrey//Downloads//bio_im2.png")


picture = picture.resize((300,300))
my = ImageTk.PhotoImage(picture)
Label(image = my).pack(side=LEFT)

picture1 = Image.open("C://Users//shrey//Downloads//bio_im1.png")


picture1 = picture1.resize((300,300))
my1 = ImageTk.PhotoImage(picture1)
Label(image = my1).pack(side=RIGHT)
My_font = ('Lucida',58,'bold')
title_label=Label(text="ALZHEIMER'S DISEASE",font = My_font,width = 20,fg = 'white',bg='black')


title_label.pack()


root.mainloop()