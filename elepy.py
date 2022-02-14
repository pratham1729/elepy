import mysql.connector as mc
from tkinter import *  
from PIL import ImageTk, Image
from functools import partial
conn=mc.connect(host='localhost',user='root',passwd='root')
mycursor=conn.cursor()
def createdatabase():
    mycursor.execute("show databases")
    db=mycursor.fetchall()
    if "chem" not in db[0]:
        mycursor.execute("create database chem")
    mycursor.execute("use chem")
createdatabase()
mycursor.execute("show tables")
tables=mycursor.fetchall()
def createtable():
    sql='''create table if not exists elements(
    atno int primary key,
    name varchar(50) unique,
    symbol varchar(3) unique,
    mass float,
    period varchar(2),
    grp varchar(2))'''
    mycursor.execute(sql)
createtable()    
def addvalues(d):
    for i in d:    
        sql="insert into elements values({},'{}','{}',{},'{}','{}')".format(d[i][1],d[i][0],i,d[i][2],d[i][3],d[i][4])
        mycursor.execute(sql)
    conn.commit()
data={
"H":["Hydrogen",1,1.0,1,1], #symbol name atno mass period grp
"He":["Helium",2,4.0,1,18],
"Li":["Lithium",3,7.0,2,1],
"Be":["Beryllium",4,9.0,2,2],
"B":["Boron",5,10.8,2,13],
"C":["Carbon",6,12.0,2,14],
"N":["Nitrogen",7,14.0,2,15],
"O":["Oxygen",8,16.0,2,16],
"F":["Fluorine",9,19.0,2,17],
"Ne":["Neon",10,20.2,2,18],
"Na":["Sodium",11,23.0,3,1],
"Mg":["Magnesium",12,24.3,3,2],
"Al":["Aluminium",13,27.0,3,13],
"Si":["Silicon",14,28.0,3,14],
"P":["Phosphorus",15,31.0,3,15],
"S":["Sulphur",16,32.0,3,16],
"Cl":["Chlorine",17,35.5,3,17],
"Ar":["Argon",18,40.0,3,18],
"K":["Potassium",19,39.0,4,1],
"Ca":['Calcium',20,40.0,4,2],
"Sc":['Scandium',21,45.0,4,3],
"Ti":['Titanium',22,47.9,4,4],
"V":['Vanadium',23,50.9,4,5],
"Cr":['Chromium',24,51.9,4,6],
"Mn":['Manganese',25,54.9,4,7],
"Fe":['Iron',26,55.8,4,8],
"Ni":['Nickel',28,58.7,4,9],
"Co":['Cobalt',27,58.9,4,10],
"Cu":['Copper',29,63.5,4,11],
"Zn":['Zinc',30,65.3,4,12],
"Ga":['Gallium',31,69.7,4,13],
"Ge":['Germanium',32,72.5,4,14],
"As":['Arsenic',33,74.9,4,15],
"Se":['Selenium',34,79.0,4,16],
"Br":['Bromine',35,79.9,4,17],
"Kr":['Krypton',36,83.8,4,18],
"Rb":['Rubidium',37,85.5,5,1],
"Sr":['Strontium',38,87.6,5,2],
"Y":['Yttrium',39,88.9,5,3],
"Zr":['Zirconium',40,91.2,5,4],
"Nb":['Niobium',41,92.9,5,5],
"Mo":['Molybdenum',42,95.9,5,6],
"Tc":['Technitium',43,98.0,5,7],
"Ru":['Ruthenium',44,101.0,5,8],
"Rh":['Rhodium',45,102.9,5,9],
"Pd":['Palladium',46,106.4,5,10],
"Ag":['Silver',47,107.9,5,11],
"Cd":['Cadmium',48,112.4,5,12],
"In":['Indium',49,114.82,5,13],
"Sn":['Tin',50,118.7,5,14],
"Sb":['Antimony',51,121.8,5,15],
"I":['Iodine',53,126.9,5,17],
"Te":['Tellurium',52,127.6,5,16],
"Xe":['Xenon',54,131.3,5,18],
"Cs":['Cesium',55,132.9,6,1],
"Ba":['Barium',56,137.3,6,2],
"La":['Lanthanum',57,138.9,6,3],
"Ce":['Cerium',58,140.1,'f1','f'],
"Pr":['Praseodymium',59,140.9,'f1','f'],
"Nd":['Neodymium',60,144.2,'f1','f'],
"Pm":['Promethium',61,145.0,'f1','f'],
"Sm":['Samarium',62,150.4,'f1','f'],
"Eu":['Europium',63,152.0,'f1','f'],
"Gd":['Gadolinium',64,157.3,'f1','f'],
"Tb":['Terbium',65,158.9,'f1','f'],
"Dy":['Dysprosium',66,162.5,'f1','f'],
"Ho":['Holmium',67,164.9,'f1','f'],
"Er":['Erbium',68,167.3,'f1','f'],
"Tm":['Thulium',69,168.9,'f1','f'],
"Yb":['Ytterbium',70,173.0,'f1','f'],
"Lu":['Lutetium',71,175.0,'f1','f'],
"Hf":['Hafnium',72,178.5,6,4],
"Ta":['Tantalum',73,180.9,6,5],
"W":['Tungsten',74,183.9,6,6],
"Re":['Rhenium',75,186.2,6,7],
"Os":['Osmium',76,190.2,6,8],
"Ir":['Iridium',77,192.2,6,9],
"Pt":['Platinum',78,195.0,6,10],
"Au":['Gold',79,197.0,6,11],
"Hg":['Mercury',80,200.6,6,12],
"Tl":['Thallium',81,204.4,6,13],
"Pb":['Lead',82,207.2,6,14],
"Bi":['Bismuth',83,209.0,6,15],
"Po":['Polonium',84,209.0,6,16],
"At":['Astatine',85,210.0,6,17],
"Rn":['Radon',86,222.0,6,18],
"Fr":['Francium',87,223.0,7,1],
"Ra":['Radium',88,226.0,7,2],
"Ac":['Actinium',89,227.0,7,3],
"Pa":['Protactinium',91,231.0,'f2','f'],
"Th":['Thorium',90,232.0,'f2','f'],
"Np":['Neptunium',93,237.0,'f2','f'],
"U":['Uranium',92,238.0,'f2','f'],
"Pu":['Plutonium',94,242.0,'f2','f'],
"Am":['Americium',95,243.0,'f2','f'],
"Bk":['Berkelium',97,247.0,'f2','f'],
"Cm":['Curium',96,247.0,'f2','f'],
"No":['Nobelium',102,250.0,'f2','f'],
"Cf":['Californium',98,251.0,'f2','f'],
"Es":['Einsteinium',99,252.0,'f2','f'],
"Hs":['Hassium',108,255.0,7,8],
"Mt":['Meitnerium',109,256.0,7,9],
"Fm":['Fermium',100,257.0,'f2','f'],
"Md":['Mendelevium',101,258.0,'f2','f'],
"Lr":['Lawrencium',103,260.0,'f2','f'],
"Rf":['Rutherfordium',104,261.0,7,4],
"Bh":['Bohrium',107,262.0,7,7],
"Db":['Dubnium',105,262.0,7,5],
"Sg":['Seaborgium',106,263.0,7,6],
"Ds":['Dysporium',110,269.0,7,10],
"Rg":['Roentgenium',111,272.0,7,11],
"Cn":['Copernicium',112,277.0,7,12],
"Fl":['Flerovium',114,289.0,7,14],
"Nh":['Nihonium',113,286.0,7,13],
"Mc":['Moscovium',115,288.0,7,15],
"Lv":['Livermorium',116,292.0,7,16],
"Ts":['Tennessine',117,294.0,7,17],
"Og":['Oganesson',118,294.0,7,18]}
mycursor.execute("select * from elements")
y=mycursor.fetchall()
if y==[]:
    addvalues(data)
def datadisplay(x):
    root=Tk()
    root.title("Periodic Table")
    root.geometry("300x300")
    root.configure(bg="black")
    name=StringVar()
    sym=StringVar()
    mass=StringVar()
    period=StringVar()
    group=StringVar()
    atno=StringVar()
    sql="select * from elements where symbol='{}'".format(x)
    mycursor.execute(sql)
    y=mycursor.fetchall()
    print(y)
    name.set(y[0][1])
    sym.set(x)
    mass.set(y[0][3])
    period.set(y[0][4])
    group.set(y[0][5])
    atno.set(y[0][0])
    heading=Label(root, text=name.get(),font="Times 15 bold underline",
    fg="white",bg="black")
    ano=Label(root, text="Atomic Number:"+str(atno.get()),font="Times 12 bold ",
    fg="yellow",bg="black")
    mas=Label(root, text="Mass:"+str(mass.get()),font="Times 12 bold",
    fg="yellow",bg="black")
    symbol=Label(root, text="Symbol:"+str(sym.get()),font="Times 12 bold",
    fg="yellow",bg="black")
    per=Label(root, text="Period:"+str(period.get()),font="Times 12 bold",
    fg="yellow",bg="black")
    grp=Label(root, text="Group:"+str(group.get()),font="Times 8 bold",
    fg="yellow",bg="black")
    q=Button(root,text='QUIT',bg="GREEN",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=root.destroy)
    heading.grid(row=0,column=2,columnspan=4)
    ano.grid(row=1,column=0)
    symbol.grid(row=2,column=0)
    mas.grid(row=3,column=0)
    per.grid(row=4,column=0)
    grp.grid(row=5,column=0)
    q.grid(row=6,column=2)
    root.mainloop()
def periodictabledesign():
    root=Tk()
    root.title("Periodic Table")
    root.geometry("1140x550")
    root.configure(bg="black")   
    heading=Label(root, text="Periodic Table of Elements",
    font="Times 25 bold underline",fg="white",bg="black")
    heading.grid(row=0,column=6,columnspan=10)
    H=Button(root,text='H',bg="white",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"H"))
    Li=Button(root,text='Li',bg="#075AF5",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Li"))
    Na=Button(root,text='Na',bg="#075AF5",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Na"))
    K=Button(root,text='K',bg="#075AF5",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"K"))
    Rb=Button(root,text='Rb',bg="#075AF5",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Rb"))
    Cs=Button(root,text='Cs',bg="#075AF5",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Cs"))
    Fr=Button(root,text='Fr',bg="#075AF5",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Fr"))
    Be=Button(root,text='Be',bg="orange",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Be"))
    Mg=Button(root,text='Mg',bg="orange",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Mg"))
    Ca=Button(root,text='Ca',bg="orange",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ca"))
    Sr=Button(root,text='Sr',bg="orange",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Sr"))
    Ba=Button(root,text='Ba',bg="orange",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ba"))
    Ra=Button(root,text='Ra',bg="orange",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ra"))
    H.grid(row=3)
    Li.grid(row=4)
    Na.grid(row=5)
    K.grid(row=6)
    Rb.grid(row=7)
    Cs.grid(row=8)
    Fr.grid(row=9)
    Be.grid(row=4,column=2)
    Mg.grid(row=5,column=2)
    Ca.grid(row=6,column=2)
    Sr.grid(row=7,column=2)
    Ba.grid(row=8,column=2)
    Ra.grid(row=9,column=2)

    Sc=Button(root,text='Sc',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Sc"))
    Ti=Button(root,text='Ti',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ti"))
    V=Button(root,text='V',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"V"))
    Cr=Button(root,text='Cr',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Cr"))
    Mn=Button(root,text='Mn',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Mn"))
    Fe=Button(root,text='Fe',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Fe"))
    Co=Button(root,text='Co',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Co"))
    Ni=Button(root,text='Ni',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ni"))
    Cu=Button(root,text='Cu',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Cu"))
    Zn=Button(root,text='Zn',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Zn"))
    b1=Button(root,bg="black",width=4,bd=0)
    b1b=Button(root,bg="black",width=4,bd=0)
    b1.grid(row=6,column=3)
    Sc.grid(row=6,column=4)
    Ti.grid(row=6,column=5)
    V.grid(row=6,column=6)
    Cr.grid(row=6,column=7)
    Mn.grid(row=6,column=8)
    Fe.grid(row=6,column=9)
    Co.grid(row=6,column=10)
    Ni.grid(row=6,column=11)
    Cu.grid(row=6,column=12)
    Zn.grid(row=6,column=13)
    b1b.grid(row=6,column=14)

    Y=Button(root,text='Y',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Y"))
    Zr=Button(root,text='Zr',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Zr"))
    Nb=Button(root,text='Nb',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Nb"))
    Mo=Button(root,text='Mo',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Mo"))
    Tc=Button(root,text='Tc',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Tc"))
    Ru=Button(root,text='Ru',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ru"))
    Rh=Button(root,text='Rh',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Rh"))
    Pd=Button(root,text='Pd',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Pd"))
    Ag=Button(root,text='Ag',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ag"))
    Cd=Button(root,text='Cd',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Cd"))
    b2=Button(root,bg="black",width=4,bd=0)
    b2b=Button(root,bg="black",width=4,bd=0)
    b2.grid(row=7,column=3)
    Y.grid(row=7,column=4)
    Zr.grid(row=7,column=5)
    Nb.grid(row=7,column=6)
    Mo.grid(row=7,column=7)
    Tc.grid(row=7,column=8)
    Ru.grid(row=7,column=9)
    Rh.grid(row=7,column=10)
    Pd.grid(row=7,column=11)
    Ag.grid(row=7,column=12)
    Cd.grid(row=7,column=13)
    b2b.grid(row=7,column=14)

    Lan=Button(root,text='*',bg="black",font="Helvetica 15 bold",fg="white",
    justify="center",width=4,bd="0")
    Hf=Button(root,text='Hf',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Hf"))
    Ta=Button(root,text='Ta',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ta"))
    W=Button(root,text='W',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"W"))
    Re=Button(root,text='Re',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Re"))
    Os=Button(root,text='Os',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Os"))
    Ir=Button(root,text='Ir',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ir"))
    Pt=Button(root,text='Pt',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Pt"))
    Au=Button(root,text='Au',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Au"))
    Hg=Button(root,text='Hg',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Hg"))
    b3=Button(root,bg="black",width=4,bd=0)
    b3b=Button(root,bg="black",width=4,bd=0)
    b3.grid(row=8,column=3)
    Lan.grid(row=8,column=4)
    Hf.grid(row=8,column=5)
    Ta.grid(row=8,column=6)
    W.grid(row=8,column=7)
    Re.grid(row=8,column=8)
    Os.grid(row=8,column=9)
    Ir.grid(row=8,column=10)
    Pt.grid(row=8,column=11)
    Au.grid(row=8,column=12)
    Hg.grid(row=8,column=13)
    b3b.grid(row=8,column=14)

    Act=Button(root,text='**',bg="black",font="Helvetica 15 bold",fg="white",
    justify="center",width=4,bd="0")
    Rf=Button(root,text='Hf',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Rf"))
    Db=Button(root,text='Db',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Db"))
    Sg=Button(root,text='Sg',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Sg"))
    Bh=Button(root,text='Bh',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Bh"))
    Hs=Button(root,text='Hs',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Hs"))
    Mt=Button(root,text='Mt',bg="grey",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Mt"))
    Ds=Button(root,text='Ds',bg="grey",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ds"))
    Rg=Button(root,text='Rg',bg="grey",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Rg"))
    Cn=Button(root,text='Cn',bg="yellow",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Cn"))
    b4=Button(root,bg="black",width=4,bd=0)
    b4b=Button(root,bg="black",width=4,bd=0)
    b4.grid(row=9,column=3)
    Act.grid(row=9,column=4)
    Rf.grid(row=9,column=5)
    Db.grid(row=9,column=6)
    Sg.grid(row=9,column=7)
    Bh.grid(row=9,column=8)
    Hs.grid(row=9,column=9)
    Mt.grid(row=9,column=10)
    Ds.grid(row=9,column=11)
    Rg.grid(row=9,column=12)
    Cn.grid(row=9,column=13)
    b4b.grid(row=9,column=14)

    B=Button(root,text='B',bg="#FF33C7",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"B"))
    Al=Button(root,text='Al',bg="#07F5BC",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Al"))
    Ga=Button(root,text='Ga',bg="#07F5BC",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ga"))
    In=Button(root,text='In',bg="#07F5BC",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"In"))
    Tl=Button(root,text='Tl',bg="#07F5BC",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Tl"))
    Nh=Button(root,text='Nh',bg="grey",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Nh"))
    B.grid(row=4,column=15)
    Al.grid(row=5,column=15)
    Ga.grid(row=6,column=15)
    In.grid(row=7,column=15)
    Tl.grid(row=8,column=15)
    Nh.grid(row=9,column=15)

    C=Button(root,text='C',bg="#07F55E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"C"))
    Si=Button(root,text='Si',bg="#FF33C7",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Si"))
    Ge=Button(root,text='Ge',bg="#FF33C7",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ge"))
    Sn=Button(root,text='Sn',bg="#07F5BC",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Sn"))
    Pb=Button(root,text='Pb',bg="#07F5BC",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Pb"))
    Fl=Button(root,text='Fl',bg="grey",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Fl"))
    C.grid(row=4,column=16)
    Si.grid(row=5,column=16)
    Ge.grid(row=6,column=16)
    Sn.grid(row=7,column=16)
    Pb.grid(row=8,column=16)
    Fl.grid(row=9,column=16)

    N=Button(root,text='N',bg="#07F55E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"N"))
    P=Button(root,text='P',bg="#07F55E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"P"))
    As=Button(root,text='As',bg="#FF33C7",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"As"))
    Sb=Button(root,text='Sb',bg="#FF33C7",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Sb"))
    Bi=Button(root,text='Bi',bg="#07F5BC",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Bi"))
    Mc=Button(root,text='Mc',bg="grey",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Mc"))
    N.grid(row=4,column=17)
    P.grid(row=5,column=17)
    As.grid(row=6,column=17)
    Sb.grid(row=7,column=17)
    Bi.grid(row=8,column=17)
    Mc.grid(row=9,column=17)

    O=Button(root,text='O',bg="#07F55E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"O"))
    S=Button(root,text='S',bg="#07F55E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"S"))
    Se=Button(root,text='Se',bg="#07F55E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Se"))
    Te=Button(root,text='Te',bg="#FF33C7",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Te"))
    Po=Button(root,text='Po',bg="#07F5BC",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Po"))
    Lv=Button(root,text='Lv',bg="grey",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Lv"))
    O.grid(row=4,column=18)
    S.grid(row=5,column=18)
    Se.grid(row=6,column=18)
    Te.grid(row=7,column=18)
    Po.grid(row=8,column=18)
    Lv.grid(row=9,column=18)

    F=Button(root,text='F',bg="#07F55E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"F"))
    Cl=Button(root,text='Cl',bg="#07F55E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Cl"))
    Br=Button(root,text='Br',bg="#07F55E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Br"))
    I=Button(root,text='I',bg="#07F55E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"I"))
    At=Button(root,text='At',bg="#07F55E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"At"))
    Ts=Button(root,text='Ts',bg="grey",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ts"))
    F.grid(row=4,column=19)
    Cl.grid(row=5,column=19)
    Br.grid(row=6,column=19)
    I.grid(row=7,column=19)
    At.grid(row=8,column=19)
    Ts.grid(row=9,column=19)

    He=Button(root,text='He',bg="#EC616E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"He"))
    Ne=Button(root,text='Ne',bg="#EC616E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ne"))
    Ar=Button(root,text='Ar',bg="#EC616E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ar"))
    Kr=Button(root,text='Kr',bg="#EC616E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Kr"))
    Xe=Button(root,text='Xe',bg="#EC616E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Xe"))
    Rn=Button(root,text='Rn',bg="#EC616E",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Rn"))
    Og=Button(root,text='Og',bg="grey",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Og"))
    He.grid(row=3,column=20)
    Ne.grid(row=4,column=20)
    Ar.grid(row=5,column=20)
    Kr.grid(row=6,column=20)
    Xe.grid(row=7,column=20)
    Rn.grid(row=8,column=20)
    Og.grid(row=9,column=20)

    a1=Button(root,bg="black",width=4,bd=0)
    a2=Button(root,bg="black",width=4,bd=0)
    a3=Button(root,bg="black",width=4,bd=0)
    a4=Button(root,bg="black",width=4,bd=0)
    a5=Button(root,bg="black",width=4,bd=0)
    a6=Button(root,bg="black",width=4,bd=0)
    a7=Button(root,bg="black",width=4,bd=0)
    a8=Button(root,bg="black",width=4,bd=0)
    a9=Button(root,bg="black",width=4,bd=0)
    a10=Button(root,bg="black",width=4,bd=0)
    a11=Button(root,bg="black",width=4,bd=0)
    a12=Button(root,bg="black",width=4,bd=0)
    a13=Button(root,bg="black",width=4,bd=0)
    a14=Button(root,bg="black",width=4,bd=0)
    a15=Button(root,bg="black",width=4,bd=0)
    a16=Button(root,bg="black",width=4,bd=0)
    a1.grid(row=10,column=4)
    a2.grid(row=10,column=5)
    a3.grid(row=10,column=6)
    a4.grid(row=10,column=7)
    a5.grid(row=10,column=8)
    a6.grid(row=10,column=9)
    a7.grid(row=10,column=10)
    a8.grid(row=10,column=11)
    a9.grid(row=10,column=12)
    a10.grid(row=10,column=13)
    a11.grid(row=10,column=14)
    a12.grid(row=10,column=15)
    a13.grid(row=10,column=16)
    a14.grid(row=10,column=17)
    a15.grid(row=10,column=18)
    a16.grid(row=10,column=19)





    Lan2=Button(root,text='*',bg="black",font="Helvetica 15 bold",fg="white",
    justify="center",width=4,bd="0")
    La=Button(root,text='La',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"La"))
    Ce=Button(root,text='Ce',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ce"))
    Pr=Button(root,text='Pr',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Pr"))
    Nd=Button(root,text='Nd',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Nd"))
    Pm=Button(root,text='Pm',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Pm"))
    Sm=Button(root,text='Sm',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Sm"))
    Eu=Button(root,text='Eu',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Eu"))
    Gd=Button(root,text='Gd',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Gd"))
    Tb=Button(root,text='Tb',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Tb"))
    Dy=Button(root,text='Dy',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Dy"))
    Ho=Button(root,text='Ho',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ho"))
    Er=Button(root,text='Er',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Er"))
    Tm=Button(root,text='Tm',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Tm"))
    Yb=Button(root,text='Yb',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Yb"))
    Lu=Button(root,text='Lu',bg="#DC7633",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Lu"))
    Lan2.grid(row=11,column=4)
    La.grid(row=11,column=5)
    Ce.grid(row=11,column=6)
    Pr.grid(row=11,column=7)
    Nd.grid(row=11,column=8)
    Pm.grid(row=11,column=9)
    Sm.grid(row=11,column=10)
    Eu.grid(row=11,column=11)
    Gd.grid(row=11,column=12)
    Tb.grid(row=11,column=13)
    Dy.grid(row=11,column=14)
    Ho.grid(row=11,column=15)
    Er.grid(row=11,column=16)
    Tm.grid(row=11,column=17)
    Yb.grid(row=11,column=18)
    Lu.grid(row=11,column=19)

    Act2=Button(root,text='**',bg="black",font="Helvetica 15 bold",fg="white",
    justify="center",width=4,bd="0")
    Ac=Button(root,text='Ac',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Ac"))
    Th=Button(root,text='Th',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Th"))
    Pa=Button(root,text='Pa',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Pa"))
    U=Button(root,text='U',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"U"))
    Np=Button(root,text='Np',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Np"))
    Pu=Button(root,text='Pu',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Pu"))
    Am=Button(root,text='Am',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Am"))
    Cm=Button(root,text='Cm',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Cm"))
    Bk=Button(root,text='Bk',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Bk"))
    Cf=Button(root,text='Cf',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Cf"))
    Es=Button(root,text='Es',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Es"))
    Fm=Button(root,text='Fm',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Fm"))
    Md=Button(root,text='Md',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Md"))
    No=Button(root,text='No',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"No"))
    Lr=Button(root,text='Lr',bg="#5DADE2",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=partial(datadisplay,"Lr"))
    q=Button(root,text='QUIT',bg="GREEN",font="Helvetica 15 bold",fg="black",
    justify="center",width=4,command=root.destroy)
    Act2.grid(row=12,column=4)
    Ac.grid(row=12,column=5)
    Th.grid(row=12,column=6)
    Pa.grid(row=12,column=7)
    U.grid(row=12,column=8)
    Np.grid(row=12,column=9)
    Pu.grid(row=12,column=10)
    Am.grid(row=12,column=11)
    Cm.grid(row=12,column=12)
    Bk.grid(row=12,column=13)
    Cf.grid(row=12,column=14)
    Es.grid(row=12,column=15)
    Fm.grid(row=12,column=16)
    Md.grid(row=12,column=17)
    No.grid(row=12,column=18)
    Lr.grid(row=12,column=19)

    c1=Button(root,bg="black",width=4,bd=0)
    c1.grid(row=13,column=6)

    hydrogen=Label(root, text="Hydrogen",font="Helvetica 10 bold",
    fg="black",bg="white")
    g1=Label(root, text="Alkali Metal",font="Helvetica 10 bold",
    fg="black",bg="#075AF5")
    g2=Label(root, text="Alkali Earth Metal",font="Helvetica 10 bold",
    fg="black",bg="orange")
    transition=Label(root, text="Transition Metal",font="Helvetica 10 bold",
    fg="black",bg="yellow")
    transition2=Label(root, text="Post-Transition Metal",
    font="Helvetica 10 bold",fg="black",bg="#07F5BC")
    actinoid=Label(root, text="Actinoids",font="Helvetica 10 bold",
    fg="black",bg="#5DADE2")
    lanthanoid=Label(root, text="Lanthanoids",font="Helvetica 10 bold",
    fg="black",bg="#DC7633")
    unknown=Label(root, text="Unknown",font="Helvetica 10 bold",
    fg="black",bg="grey")
    nobelgas=Label(root, text="Nobel Gas",font="Helvetica 10 bold",
    fg="black",bg="#EC616E")
    nonmetal=Label(root, text="Non-Metal",font="Helvetica 10 bold",
    fg="black",bg="#07F55E")
    metalloid=Label(root, text="Metalloid",font="Helvetica 10 bold",
    fg="black",bg="#FF33C7")
    hydrogen.grid(row=14,column=1,columnspan=4)
    g1.grid(row=14,column=4,columnspan=4)
    g2.grid(row=14,column=7,columnspan=4)
    transition.grid(row=14,column=10,columnspan=4)
    transition2.grid(row=14,column=13,columnspan=4)
    lanthanoid.grid(row=14,column=16,columnspan=4)
    actinoid.grid(row=15,column=1,columnspan=4)
    nobelgas.grid(row=15,column=4,columnspan=4)
    nonmetal.grid(row=15,column=7,columnspan=4)
    metalloid.grid(row=15,column=10,columnspan=4)
    unknown.grid(row=15,column=13,columnspan=4)
    q.grid(row=17,column=10)
    root.mainloop()
def search():
    def SearchData():
        if(atno.get()!=""):    #This method searches record on the basis of empid provided
            ano=int(atno.get())
            if(ano):
                sql="Select * from elements where atno={}".format(ano)  
                try:
                    mycursor.execute(sql)
                    records=mycursor.fetchone()
                    print(records)
                    if(mycursor.rowcount>=1):
                        name.set(str(records[1]))
                        mass.set(str(records[3]))
                        period.set(str(records[4]))
                        group.set(str(records[5]))
                        symbol.set(str(records[2]))
                    else:
                        clearfields()
                        callpopup("Important","Data not found")
                        
                        
                except mc.errors.InternalError:
                        print("Internal error raised")
        else:
            callpopup("Error","Atomic Number cannot be empty")
            clearfields()
    root=Tk()
    root.config(bg="black")
    root.title("Search Elements")
    root.geometry("600x400") 
    root.resizable(0, 0) 
    atno=StringVar(root)
    name=StringVar(root)
    mass=StringVar(root)
    group=StringVar(root)
    period=StringVar(root)
    symbol=StringVar(root)
    label1=Label(root,text='Atomic Number',font=("Arial Bold", 14),
    fg="White",bg="Black")
    label1.grid(row=0,column=0)
    entry1=Entry(root,textvariable=atno)
    entry1.grid(row=0,column=1)
    label2=Label(root,text='Symbol',font=("Arial Bold", 14),
    fg="White",bg="Black")
    label2.grid(row=1,column=0)
    entry2=Entry(root,textvariable=symbol,width=25)
    entry2.grid(row=1,column=1)
    label3=Label(root,text='Name',font=("Arial Bold", 14),
    fg="White",bg="Black")
    label3.grid(row=2,column=0)
    entry3=Entry(root,textvariable=name)
    entry3.grid(row=2,column=1)
    label4=Label(root,text='Group',font=("Arial Bold", 14),
    fg="White",bg="Black")
    label4.grid(row=3,column=0)
    entry4=Entry(root,textvariable=group)
    entry4.grid(row=3,column=1)
    label5=Label(root,text='Period',font=("Arial Bold", 14),
    fg="White",bg="Black")
    label5.grid(row=4,column=0)
    entry5=Entry(root,textvariable=period)
    entry5.grid(row=4,column=1)
    label6=Label(root,text='Mass',font=("Arial Bold", 14),
    fg="White",bg="Black")
    label6.grid(row=5,column=0)
    entry6=Entry(root,textvariable=mass)
    entry6.grid(row=5,column=1)
    frmbtn=Frame(root)
    frmbtn.grid(row=6,column=0)
    btnExit=Button(frmbtn,text='Quit',command=root.destroy)
    btnExit.pack(side=LEFT)
    btnSearch=Button(frmbtn,text='Search',command=SearchData)
    btnSearch.pack(side=LEFT)

    
    root.mainloop()    
def callpopup(title,msg):
    popup = Tk()
    popup.wm_title(title)
    label=Label(popup, text=msg,font=("Arial Bold", 8))
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()    
def checkempty():
    if(str(atno.get())=='' or name.get()=='' or symbol.get()=='' 
    or period.get()=='' or group.get()=='' or str(mass.get())==''):
        return True
    else:
        return Fals
def clearfields():
    name.set("")
    atno.set("")
    group.set("")
    period.set('')
    mass.set("")
    symbol.set("")
def intro():
    root=Tk()
    root.configure(bg="black")
    img=ImageTk.PhotoImage(Image.open("elepy.jpg"))
    panel=Label(root, image = img)
    panel.pack(side="top",expand="yes")
    root.resizable(0,0)
    b1=Button(root,text='Open Periodic Table',bg="black",font="Helvetica 15 bold"
    ,fg="white",justify="center",width=20,command=periodictabledesign)
    b1.pack(side="left")
    b2=Button(root,text='Search',bg="black",font="Helvetica 15 bold",fg="white",
    justify="center",width=20,command=search)
    b2.pack(side="left")    
    q=Button(root,text='Exit',bg="black",font="Helvetica 15 bold",fg="white",
    justify="center",width=20,command=root.destroy)
    q.pack(side="left")    
    root.mainloop()   

intro()










