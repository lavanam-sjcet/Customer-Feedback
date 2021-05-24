from tkinter import *
import pymysql
from PIL import Image,ImageTk



def on_click(i,j,event):
    global counter
    print(i,j)


def redraw():
    root = Tk()
    root.geometry("950x550")
    root.title("FORM")
    root.minsize(550,460)
    root.config(bg="#ff8201")
    image = Image.open("admin.jpg")
    image = image.resize((950, 550), Image.ANTIALIAS) ## The (550, 250) is (height, width)
    pic = ImageTk.PhotoImage(image)
##    lbl_reg=Label(root,image=pic)
##    lbl_reg.place(x=0,y=0)
    bb = Label(root, text="View Users and Approve")
    bb.place(x=15, y=15)
    fr = Frame(root)
    fr.place(x=20,y=80)
    db=pymysql.connect("localhost","root","","customersatisfaction")
    cursor=db.cursor()
    sql="select first_nm,last_nm,dob,age,email,phno,gender,addr,username from registration"
    print (sql)
    try:
        cursor.execute(sql)
        res=cursor.fetchall()
        print(res)
    except:
        pass
    newres=[]
    for i in res:
        t= i+tuple(['Approve User'])
        newres.append(t)
    # take the data 
    lst = [('First Name', 'Last Name', 'DOB', 'Age', 'Email', 'Phone', 'Gender', 'Address', 'Username', 'Approve' ) ] + list(newres)
    for i,row in enumerate(lst):
        for j,column in enumerate(row):
            name = str(i)+str(j)
            
            if j==9 and i!=0:
                b = Button(fr, text='Click Me')
                b.grid(row=i, column=j, sticky=NSEW)
                b.bind('<Button-1>',lambda e,i=i,j=j:on_click(i,j,e))
                continue
            if j==4 or j==7:
              
                e = Entry(fr, width=20, fg='blue', 
                               font=('Arial',10,'bold')) 
            else:
                e = Entry(fr, width=10, fg='blue', 
                               font=('Arial',10,'bold'))
            
            e.grid(row=i, column=j, sticky=NSEW) 
            e.insert(END, lst[i][j])
            if i==0:
                e.config(state='disabled')
##            L = Label(gameframe,text=lst[i][j],bg= "grey" if board[i][j] == None else board[i][j])
##            L.grid(row=i,column=j,padx='3',pady='3')
##            L.bind('<Button-1>',lambda e,i=i,j=j:on_click(i,j,e))
    root.mainloop()


redraw()

