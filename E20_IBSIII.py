import tkinter as tk
from tkinter import *
import random
top = tk.Tk()
top.geometry('2000x2000')
f = ('Times New Roman',20)
label = Label(top,text='Enter how many nucleotides you wish to read',bg='DarkSlateGray1',font=f).place(x = 350,y = 200)
def Chro1():
    

    chrs1=open("D://Uni//3rd Sem//IBS//Project//chromosome1.txt","r")
    chrs14=open("D://Uni//3rd Sem//IBS//Project//chromosome14.txt","r")
    chrs21=open("D://Uni//3rd Sem//IBS//Project//chromosome21.txt","r")
    p1=int(e1.get())
#chromosome 1, 14 and 21's genome sequence
    seq=chrs1.readline()
    seq1=chrs1.read(p1)

    seqfe=chrs14.readline()
    seq14=chrs14.read(p1)

    seqf=chrs21.readline()
    seq21=chrs21.read(p1)


#protein
    prf1=open("D://Uni//3rd Sem//IBS//Project//PSEN2_datasets//ncbi_dataset//data//gene.fna","r")
    prf14=open("D://Uni//3rd Sem//IBS//Project//PSEN1_datasets//ncbi_dataset//data//gene.fna","r")
    prf21=open("D://Uni//3rd Sem//IBS//Project//APP_datasets//ncbi_dataset//data//gene.fna","r")
#protein in chromosome 1, 14 and 21's genome sequence
    pseqa=prf1.readline()
    pseq1=prf1.read(p1)

    pseqb=prf14.readline()
    pseq14=prf14.read(p1)

    pseq=prf21.readline()
    pseq21=prf21.read(p1)

    Ls1=[]
    Ls14=[]
    Ls21=[]
    for i in seq1:
        Ls1.append(i)
    for i in seq14:
        Ls14.append(i)
    for i in seq21:
        Ls21.append(i)
    Lps1=[]
    Lps14=[]
    Lps21=[]
    for i in pseq1:
        Lps1.append(i)
    for i in pseq14:
        Lps14.append(i)
    for i in pseq21:
        Lps21.append(i)

    def mutation(s,p1):
        N=['A','C','T','G']
        v=random.randint(0,p1-5)
        print("The original sequence",s[v:v+5])
        for i in range(5):
            vv=random.randint(0,3)
            vN=N[vv]
            s[v+i]=vN
        print("The mutated sequence",s[v:v+5])
        


    def mutation_loc_fnc(s1,s2):
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                print('Mutation at Nucleotide location ',i)
                break
            else:
                i=i

    mutation(Ls1,p1)

    if Lps1!=Ls1:
        f2 = ("Times New Roman",20)
        Label(top,text='Mutation in Chromosome 1, Presenilin 2 protein',font=f2).place(x = 200,y = 400)
        mutation_loc_fnc(Lps1,Ls1)
    
    else:
        if Lps14!=Ls14:
            f2 = ("Times New Roman",20)
            Label(top,text='Mutation in Chromosome 14, Presenilin 1 protein',font=f2).place(x = 200,y = 650)
            mutation_loc_fnc(Lps14,Ls14)
        else:
            if Lps21!=Ls21:
                f2 = ("Times New Roman",20)
                Label(top,text='Mutation in Chromosome 21, APP protein',font=f2).place(x = 830,y = 400)
                mutation_loc_fnc(Lps21,Ls21)
            else:
                f2 = ("Times New Roman",20)
                Label(top,text='No mutation of Alzheimers found in your chromosomes.',font=f2).place(x = 830,y = 650)


def Chro2():
    

    chrs1=open("D://Uni//3rd Sem//IBS//Project//chromosome1.txt","r")
    chrs14=open("D://Uni//3rd Sem//IBS//Project//chromosome14.txt","r")
    chrs21=open("D://Uni//3rd Sem//IBS//Project//chromosome21.txt","r")
    p1=int(e1.get())
#chromosome 1, 14 and 21's genome sequence
    seq=chrs1.readline()
    seq1=chrs1.read(p1)

    seqfe=chrs14.readline()
    seq14=chrs14.read(p1)

    seqf=chrs21.readline()
    seq21=chrs21.read(p1)


#protein
    prf1=open("D://Uni//3rd Sem//IBS//Project//PSEN2_datasets//ncbi_dataset//data//gene.fna","r")
    prf14=open("D://Uni//3rd Sem//IBS//Project//PSEN1_datasets//ncbi_dataset//data//gene.fna","r")
    prf21=open("D://Uni//3rd Sem//IBS//Project//APP_datasets//ncbi_dataset//data//gene.fna","r")
#protein in chromosome 1, 14 and 21's genome sequence
    pseqa=prf1.readline()
    pseq1=prf1.read(p1)

    pseqb=prf14.readline()
    pseq14=prf14.read(p1)

    pseq=prf21.readline()
    pseq21=prf21.read(p1)

    Ls1=[]
    Ls14=[]
    Ls21=[]
    for i in seq1:
        Ls1.append(i)
    for i in seq14:
        Ls14.append(i)
    for i in seq21:
        Ls21.append(i)
    Lps1=[]
    Lps14=[]
    Lps21=[]
    for i in pseq1:
        Lps1.append(i)
    for i in pseq14:
        Lps14.append(i)
    for i in pseq21:
        Lps21.append(i)

    def mutation(s,p1):
        N=['A','C','T','G']
        v=random.randint(0,p1-5)
        print("The original sequence",s[v:v+5])
        for i in range(5):
            vv=random.randint(0,3)
            vN=N[vv]
            s[v+i]=vN
        print("The mutated sequence",s[v:v+5])
        


    def mutation_loc_fnc(s1,s2):
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                print('Mutation at Nucleotide location ',i)
                break
            else:
                i=i

    mutation(Ls14,p1)

    if Lps1!=Ls1:
        f2 = ("Times New Roman",20)
        Label(top,text='Mutation in Chromosome 1, Presenilin 2 protein',font=f2).place(x = 200,y = 400)
        mutation_loc_fnc(Lps1,Ls1)
    
    else:
        if Lps14!=Ls14:
            f2 = ("Times New Roman",20)
            Label(top,text='Mutation in Chromosome 14, Presenilin 1 protein',font=f2).place(x = 200,y = 650)
            mutation_loc_fnc(Lps14,Ls14)
        else:
            if Lps21!=Ls21:
                f2 = ("Times New Roman",20)
                Label(top,text='Mutation in Chromosome 21, APP protein',font=f2).place(x = 830,y = 400)
                mutation_loc_fnc(Lps21,Ls21)
            else:
                f2 = ("Times New Roman",20)
                Label(top,text='No mutation of Alzheimers found in your chromosomes.',font=f2).place(x = 830,y = 650)

def app():
    

    chrs1=open("D://Uni//3rd Sem//IBS//Project//chromosome1.txt","r")
    chrs14=open("D://Uni//3rd Sem//IBS//Project//chromosome14.txt","r")
    chrs21=open("D://Uni//3rd Sem//IBS//Project//chromosome21.txt","r")
    p1=int(e1.get())
#chromosome 1, 14 and 21's genome sequence
    seq=chrs1.readline()
    seq1=chrs1.read(p1)

    seqfe=chrs14.readline()
    seq14=chrs14.read(p1)

    seqf=chrs21.readline()
    seq21=chrs21.read(p1)


#protein
    prf1=open("D://Uni//3rd Sem//IBS//Project//PSEN2_datasets//ncbi_dataset//data//gene.fna","r")
    prf14=open("D://Uni//3rd Sem//IBS//Project//PSEN1_datasets//ncbi_dataset//data//gene.fna","r")
    prf21=open("D://Uni//3rd Sem//IBS//Project//APP_datasets//ncbi_dataset//data//gene.fna","r")
#protein in chromosome 1, 14 and 21's genome sequence
    pseqa=prf1.readline()
    pseq1=prf1.read(p1)

    pseqb=prf14.readline()
    pseq14=prf14.read(p1)

    pseq=prf21.readline()
    pseq21=prf21.read(p1)

    Ls1=[]
    Ls14=[]
    Ls21=[]
    for i in seq1:
        Ls1.append(i)
    for i in seq14:
        Ls14.append(i)
    for i in seq21:
        Ls21.append(i)
    Lps1=[]
    Lps14=[]
    Lps21=[]
    for i in pseq1:
        Lps1.append(i)
    for i in pseq14:
        Lps14.append(i)
    for i in pseq21:
        Lps21.append(i)

    def mutation(s,p1):
        N=['A','C','T','G']
        v=random.randint(0,p1-5)
        print("The original sequence",s[v:v+5])
        for i in range(5):
            vv=random.randint(0,3)
            vN=N[vv]
            s[v+i]=vN
        print("The mutated sequence",s[v:v+5])
        


    def mutation_loc_fnc(s1,s2):
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                print('Mutation at Nucleotide location ',i)
                break
            else:
                i=i

    mutation(Ls21,p1)

    if Lps1!=Ls1:
        f2 = ("Times New Roman",20)
        Label(top,text='Mutation in Chromosome 1, Presenilin 2 protein',font=f2).place(x = 200,y = 400)
        mutation_loc_fnc(Lps1,Ls1)
    
    else:
        if Lps14!=Ls14:
            f2 = ("Times New Roman",20)
            Label(top,text='Mutation in Chromosome 14, Presenilin 1 protein',font=f2).place(x = 200,y = 650)
            mutation_loc_fnc(Lps14,Ls14)
        else:
            if Lps21!=Ls21:
                f2 = ("Times New Roman",20)
                Label(top,text='Mutation in Chromosome 21, APP protein',font=f2).place(x = 830,y = 400)
                mutation_loc_fnc(Lps21,Ls21)
            else:
                f2 = ("Times New Roman",20)
                Label(top,text='No mutation of Alzheimers found in your chromosomes.',font=f2).place(x = 830,y = 650)

def dect():
    

    chrs1=open("D://Uni//3rd Sem//IBS//Project//chromosome1.txt","r")
    chrs14=open("D://Uni//3rd Sem//IBS//Project//chromosome14.txt","r")
    chrs21=open("D://Uni//3rd Sem//IBS//Project//chromosome21.txt","r")
    p1=int(e1.get())
#chromosome 1, 14 and 21's genome sequence
    seq=chrs1.readline()
    seq1=chrs1.read(p1)

    seqfe=chrs14.readline()
    seq14=chrs14.read(p1)

    seqf=chrs21.readline()
    seq21=chrs21.read(p1)


#protein
    prf1=open("D://Uni//3rd Sem//IBS//Project//PSEN2_datasets//ncbi_dataset//data//gene.fna","r")
    prf14=open("D://Uni//3rd Sem//IBS//Project//PSEN1_datasets//ncbi_dataset//data//gene.fna","r")
    prf21=open("D://Uni//3rd Sem//IBS//Project//APP_datasets//ncbi_dataset//data//gene.fna","r")
#protein in chromosome 1, 14 and 21's genome sequence
    pseqa=prf1.readline()
    pseq1=prf1.read(p1)

    pseqb=prf14.readline()
    pseq14=prf14.read(p1)

    pseq=prf21.readline()
    pseq21=prf21.read(p1)

    Ls1=[]
    Ls14=[]
    Ls21=[]
    for i in seq1:
        Ls1.append(i)
    for i in seq14:
        Ls14.append(i)
    for i in seq21:
        Ls21.append(i)
    Lps1=[]
    Lps14=[]
    Lps21=[]
    for i in pseq1:
        Lps1.append(i)
    for i in pseq14:
        Lps14.append(i)
    for i in pseq21:
        Lps21.append(i)

    def mutation(s,p1):
        N=['A','C','T','G']
        v=random.randint(0,p1-5)
        print("The original sequence",s[v:v+5])
        for i in range(5):
            vv=random.randint(0,3)
            vN=N[vv]
            s[v+i]=vN
        print("The mutated sequence",s[v:v+5])
        


    def mutation_loc_fnc(s1,s2):
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                print('Mutation at Nucleotide location ',i)
                break
            else:
                i=i

    

    if Lps1!=Ls1:
        f2 = ("Times New Roman",20)
        Label(top,text='Mutation in Chromosome 1, Presenilin 2 protein',font=f2).place(x = 200,y = 400)
        mutation_loc_fnc(Lps1,Ls1)
    
    else:
        if Lps14!=Ls14:
            f2 = ("Times New Roman",20)
            Label(top,text='Mutation in Chromosome 14, Presenilin 1 protein',font=f2).place(x = 200,y = 650)
            mutation_loc_fnc(Lps14,Ls14)
        else:
            if Lps21!=Ls21:
                f2 = ("Times New Roman",20)
                Label(top,text='Mutation in Chromosome 21, APP protein',font=f2).place(x = 830,y = 400)
                mutation_loc_fnc(Lps21,Ls21)
            else:
                f2 = ("Times New Roman",20)
                Label(top,text='No mutation of Alzheimers found in your chromosomes.',font=f2).place(x = 830,y = 650)

my_font = ('Rockwell',55)
label1 = Label(top,text="ALZHEIMER'S MUTATIONS",font=my_font,bg='DarkSlateGray1').place(x = 300 , y =0)
button1 = Button(top,text = 'Chromosome 1',command=Chro1,height=5,width=25,bg='snow',fg='black').place(x = 430,y=300)
button2 = Button(top,text = 'Chromosome 14',command=Chro2,height=5,width=25,bg='snow',fg='black').place(x = 430,y=500)
button3 = Button(top,text='APP',command=app,height=5,width=25,bg='snow',fg='black').place(x=940,y=300)
button3 = Button(top,text='No Mutation',command=dect,height=5,width=25,bg='snow',fg='black').place(x=940,y=500)
top.config(background = 'DarkSlateGray1')
e1 = Entry(top)
e1.place(x=900,y=210)
top.mainloop()
