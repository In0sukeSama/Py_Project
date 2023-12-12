import tkinter as tk
from tkinter import *
from tkinter import messagebox,PhotoImage
from PIL import ImageTk,Image
import mysql.connector as ms

con = ms.connect(host='localhost',user='root',password='123456')

### these are for the slider label
y = "WELCOME TO APT MANAGMENT SYSTEM"
count = 0
text = ""


x = "....."
count2 = 0
text_2 = ""

    ###SOME VARIABLES FOR INBOX()
global comment,found_reply,Input_Username
comment = ''
found_reply = False
Input_Username = ''


if con.is_connected():
  cur = con.cursor()
  query1 = "create database if not exists project"
  cur.execute(query1)
  query2 = "use project"
  cur.execute(query2)
  query3 = "create table if not exists apt(BNO INT PRIMARY KEY,BHK INT,Square_Feet int,Vacancy CHAR(15),Price INT,check(Price >= 1000000 and Price <= 9999999 and Square_Feet >= 800 and Square_Feet <= 1600))"
  cur.execute(query3)
  query4 = "create table if not exists owner(Ow_ID INT NOT NULL PRIMARY KEY,Name char(15),Phone_No BIGINT,BNO INT,CONSTRAINT FOREIGN KEY (BNO) REFERENCES apt(BNO) ON DELETE CASCADE ON UPDATE CASCADE);"
  cur.execute(query4)
  query5 = "create table if not exists complaints(C_NO INT NOT NULL PRIMARY KEY,Name char(15),Ow_ID INT,CONSTRAINT FOREIGN KEY (Ow_ID) REFERENCES owner(Ow_ID) ON DELETE CASCADE ON UPDATE CASCADE,COMPLAINT CHAR(35)) "
  cur.execute(query5)
  query6 = 'create table if not exists credentials(Username CHAR(10) NOT NULL,Password CHAR(10) NOT NULL PRIMARY KEY,Ow_ID INT UNIQUE,CONSTRAINT FOREIGN KEY (Ow_ID) REFERENCES owner(Ow_ID) ON DELETE CASCADE ON UPDATE CASCADE)'
  cur.execute(query6)
  con.commit()

  def Home_Page_user():
      def inbox():

          global Input_Username
          window2 = tk.Tk()

          a =open("Login_Username.txt","r")
          s = a.read()
          a.close()

          try:
              b = open("Reply_Username.txt","r")
              q = b.read()
              b.close()

              if s == q:

                  window2.title("YOUR INBOX")
                  window2.geometry('500x215-450+260')
                  window2.configure(bg='#f7e7ce')
                  window2.resizable(False,False)  

                  test = tk.Label(window2,
                     text='YOU HAVE AN UNREAD MESSAGE', bg='#f7e7ce',width=50, fg="#FF3399", font=("Arial", 16))
                  test.place(x=-40,y=10)
                  test1 = tk.Label(window2,
                     text='SENDER : ADMIN', bg='#f7e7ce',width=50, fg="#FF3399", font=("Arial", 16))
                  test1.place(x=-40,y=40)

                  F = open("comment.txt",'r')
                  s = F.read()

                  frame2 = tk.Frame(window2, width=410, height=175, bg='#e5fcf5')
                  frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                  frame2.place(x=40, y=115)

                  test = tk.Label(frame2,
                     text= s, bg='#e5fcf5',width=50, fg="#FF3399", font=("Arial", 16))
                  test.place(x=-100,y=0)

              else:

                  window2.title("YOUR INBOX")
                  window2.geometry('500x215-450+260')
                  window2.configure(bg='white')
                  window2.resizable(False,False)

                  test = tk.Label(window2,
                     text='YOU HAVE NO UNREAD MESSAGES', bg='white',width=50, fg="#FF3399", font=("Arial", 18))
                  test.place(x=-90,y=65)

          except FileNotFoundError:
            
              window2.title("YOUR INBOX")
              window2.geometry('500x215-450+260')
              window2.configure(bg='white')
              window2.resizable(False,False)

              test = tk.Label(window2,
                 text='YOU HAVE NO UNREAD MESSAGES', bg='white',width=50, fg="#FF3399", font=("Arial", 18))
              test.place(x=-90,y=65)

      def view_complaints():

          frame2 = tk.Frame(window2, width=400, height=400, bg='white')
          frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
          frame2.place(x=375, y=180)

                        ###QUERY TO VIEW THE TABLE CONTENTS
          query = "SELECT * FROM complaints"
          cur.execute(query)
          result = cur.fetchall()
          t = "{:<15}{:<12}{:<20}{:<5}"
          s = t.format('CNO','Name','Ow_ID', 'COMPLAINTS')
          t2 = "{:<15}{:<15}{:<20}{:<12}"
          s2 =''
          for i in result:
            s2 += t2.format(str(i[0]), str(i[1]), str(i[2]), i[3],str(i[4]))+ '\n' + '\n'

          view_label1 = tk.Label(frame2,
           text='TABLE   :    APT', bg='white',width=45, fg="#FF3399",borderwidth=1, relief="solid", font=("Arial", 16))
          view_label1.place(x=-70, y=0)
          view_label2 = tk.Label(frame2,
           text=s, bg='white',width=45, fg="#FF3399", font=("Arial", 12))
          view_label2.place(x=0, y=70)
          view_label3 = tk.Label(frame2,
           text=s2, bg='white',width=50, fg="#FF3399", font=("Arial", 12))
          view_label3.place(x=0, y=100)


          close = tk.Button(frame2,
              text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
          close.place(x = 155 , y = 350)


      def Complaints():

          try:
            global view_cred
            view_cred.place(x=1000,y=1000)
          except NameError:
            pass

          def add_complaints():

              def submit():

                  global found3,found2

                  query1 = "SELECT * FROM complaints"
                  cur.execute(query1)
                  result = cur.fetchall()
                  found = False
                  for i in result:
                      if com_NO.get().isdigit():
                          if int(com_NO.get()) == i[0]:
                              found = True
                              break
                          else:
                              pass

                  query2 = "select * from owner where Ow_ID = %s"
                  values = (com_OID.get(),)
                  cur.execute(query2,values)
                  result3 = cur.fetchall()
                  found2 = False
                  found3 = False
                  for i in result3:
                      if int(com_OID.get()) == i[0]:
                          found2 = True
                          

                      if com_Name.get().isdigit() or str(com_Name.get()) == '':
                              messagebox.showerror(title="INVALID INPUT", message= 'NAME MUST BE A STR')
                      else:
                          if com_Name.get().lower() == (str(i[1])).lower():
                              found3 = True
                              

                          else:
                              messagebox.showerror(title="INVALID INPUT", message= str(com_Name.get()) + ' IS NOT THE OWNER OF the BLD NO ' + com_OID.get())

                      if found2 == False:
                          messagebox.showerror(title="INVALID INPUT", message="WRONG OW_ID IS ENTERED")
                      
                  if found == True:
                      messagebox.showerror(title="INVALID INPUT", message="A record with the given CNO already exists")
                  else:            
                      if com_NO.get().isdigit():
                          if com_OID.get().isdigit():
                              if (len(com_COM.get()) <= 25 and len(com_COM.get()) >= 8) or com_COM.get().isdigit():
                                  if found3 == True:

                                      query1 = "insert into complaints values(%s, %s, %s, %s)"
                                      values = (int(com_NO.get()),str(com_Name.get()),int(com_OID.get()), str(com_COM.get()))
                                      cur.execute(query1,values)
                                      con.commit()

                                      messagebox.showinfo(title="COMPLAINT SUBMITED", message="You successfully submitted a complaint.")  
                                  else:
                                      messagebox.showerror(title="INVALID INPUT", message="PROPER CREDENTIALS ARE REQUIRED")
                              else:
                                  messagebox.showerror(title="INVALID INPUT", message="A COMPLAINT MUST BE A STR AND 8 <= LENGTH =< 25")
                          else:
                              messagebox.showerror(title="INVALID INPUT", message="Ow_ID MUST A DIGIT")
                      else:
                          messagebox.showerror(title="INVALID INPUT", message="COM_No MUST BE AN INTEGER")


              frame2 = tk.Frame(window2, width=400, height=400, bg='white')
              frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
              frame2.place(x=375, y=180)

              global com_entry1,com_entry2,com_entry3,com_entry5

              com_label1 = tk.Label(frame2,
                text="C_NO", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
              com_label1.place(x=-20,y=20)
              com_NO = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
              com_NO.place(x = 130,y = 20)
              com_label5 = tk.Label(frame2,
               text="Name", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
              com_label5.place(x=-20,y=70)
              com_Name = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
              com_Name.place(x = 130,y = 70)
              com_label2 = tk.Label(frame2,
                text="Ow_ID", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
              com_label2.place(x=-20,y=120)
              com_OID = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
              com_OID.place(x = 130,y = 120)
              com_label3 = tk.Label(frame2,
                text="COMPLAINT", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
              com_label3.place(x=-20,y=170)
              com_COM = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
              com_COM.place(x = 130,y = 170)

              
              com_button1 = tk.Button(frame2,
                  text="SUBMIT", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=submit)
              com_button1.place(x = 155 , y = 285)

              close = tk.Button(frame2,
                  text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
              close.place(x = 155 , y = 335)

          def view_complaints():

              frame2 = tk.Frame(window2, width=400, height=400, bg='white')
              frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
              frame2.place(x=375, y=180)

                            ###QUERY TO VIEW THE TABLE CONTENTS
              query = "SELECT * FROM complaints"
              cur.execute(query)
              result = cur.fetchall()
              t = "{:<15}{:<12}{:<20}{:<5}"
              s = t.format('CNO','Name','Ow_ID', 'COMPLAINTS')
              t2 = "{:<10}{:<15}{:<20}{:<15}"
              s2 =''
              for i in result:
                s2 += t2.format(str(i[0]), i[1], str(i[2]), i[3]) + '\n' + '\n'

              view_label1 = tk.Label(frame2,
               text='TABLE   :    APT', bg='white',width=45, fg="#FF3399",borderwidth=1, relief="solid", font=("Arial", 16))
              view_label1.place(x=-70, y=0)
              view_label2 = tk.Label(frame2,
               text=s, bg='white',width=45, fg="#FF3399", font=("Arial", 12))
              view_label2.place(x=0, y=70)
              view_label3 = tk.Label(frame2,
               text=s2, bg='white',width=50, fg="#FF3399", font=("Arial", 12))
              view_label3.place(x=0, y=100)


              close = tk.Button(frame2,
                  text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
              close.place(x = 155 , y = 350)

          global add4_button,view4_button
          add4_button = tk.Button(window2,
          text="ADD", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=add_complaints)
          add4_button.place(x = 260 , y = 300)
          global view4_button
          view4_button = tk.Button(window2,
          text="VIEW", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=view_complaints)
          view4_button.place(x = 260 , y = 350)


      def add_Cred_user():
          try:
            global add4_button
            view4_button.place(x=1000,y=1000)
            add4_button.place(x=1000,y=1000)
          except NameError:
            pass
          def view_cred2():
              frame2 = tk.Frame(window2, width=400, height=400, bg='white')
              frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
              frame2.place(x=375, y=180)

              F = open('Login_Username.txt','r')
              F2 = open('Password_Username.txt','r')
              S1 = F.read()
              S2 = F2.read()

                            ###QUERY TO VIEW THE TABLE CONTENTS
              query = "SELECT * FROM credentials where Username = %s and Password = %s"
              values = (S1,S2)
              cur.execute(query,values)
              result = cur.fetchall()
              t = "{:<15}{:<20}{:<10}"
              s = t.format('USERNAME','PASSWORD','Ow_ID')
              t2 = "{:<20}{:<30}{:<20}"
              s2 =''
              for i in result:
                if i[1] == 'None' : 
                    s2 += t2.format(str(i[0]),'NULL', str(i[2]), str(i[3]))+ '\n' + '\n'
                else:
                    s2 += t2.format(str(i[0]),str(i[1]), str(i[2]))+ '\n' + '\n'

              view_label1 = tk.Label(frame2,
               text='TABLE   :    CREDENTIALS', bg='white',width=45, fg="#FF3399",borderwidth=1, relief="solid", font=("Arial", 16))
              view_label1.place(x=-70, y=10)
              view_label2 = tk.Label(frame2,
               text=s, bg='white',width=45, fg="#FF3399", font=("Arial", 12))
              view_label2.place(x=0, y=70)
              view_label3 = tk.Label(frame2,
               text=s2, bg='white',width=50, fg="#FF3399", font=("Arial", 12))
              view_label3.place(x=0, y=100)


              close = tk.Button(frame2,
                  text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
              close.place(x = 155 , y = 350)

          global view_cred
          view_cred = tk.Button(window2,
                text="VIEW", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=view_cred2)
          view_cred.place(x = 260 , y = 430)

      window2 = tk.Tk()
      window2.title("Home Page")
      window2.geometry('900x615-250-50')
      window2.configure(bg='white')
      window2.resizable(False,False)

                        #IMAGE
      frame = tk.Frame(window2, width=900, height=815, bg='white')
      frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
      frame.place(x=0, y=0)


                      # Create an object of tk ImageTk
      global img
      img = PhotoImage(file='C:/Users/Rohit/Desktop/Dubai-PNG-Pic.png', master=window2)

                      # Create a Label Widget to display the text or Image
      label = tk.Label(frame, image=img)
      label.place(x=-400,y=-300)

      COMPLAINTS_button = tk.Button(window2,
          text="COMPLAINTS", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Complaints)
      COMPLAINTS_button.place(x = 50 , y = 350)
      CRED_but = tk.Button(window2,
        text="CREDENTIALS", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=add_Cred_user)
      CRED_but.place(x = 50 , y = 415)
      Exit_Button = tk.Button(window2,
        text="Exit", bg="#FF3399", fg="#FFFFFF",borderwidth=3, relief="raised", font=("Arial", 16), command=window2.destroy)
      Exit_Button.place(x = 800 , y = 550)
      
                    # Labels for home page
      global y
      def slider():
          global count,text,y
          if count >= len(y):
              count = 0
              text = ""
              apt_Label.config(text=text)
          else:
              text += y[count]
              apt_Label.config(text=text)
              count += 1
          apt_Label.after(200,slider)
      login_label = tk.Label(frame,
         text="HOME PAGE", fg="#FF3399", font=("Arial", 30))
      login_label.place(relx= 0.35, y = 20)
      apt_Label = tk.Label(frame,
         text= y, fg="#FF3399", font=("Arial", 30))
      apt_Label.place(relx= 0.05, y = 75)
      slider()


                    #Buttons for Home Page
      
      event_button = tk.Button(window2,
          text="COMPLAINTS", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Complaints)
      event_button.place(x = 50 , y = 350)
      Amenities_but = tk.Button(window2,
        text="CREDENTIALS", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=add_Cred_user)
      Amenities_but.place(x = 50 , y = 415)
      inbox_button = tk.Button(window2,
          text="INBOX", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=inbox)
      inbox_button.place(x = 40 , y = 535)
      Exit_Button = tk.Button(window2,
        text="Exit", bg="#FF3399", fg="#FFFFFF",borderwidth=3, relief="raised", font=("Arial", 16), command=lambda:[window2.withdraw(), First()])
      Exit_Button.place(x = 800 , y = 550)

  def Home_Page():
                   ### ALL FUNTIONS FOR BUTTONS IN HOME PAGE
    def APT():

      def ADD():

          def add_records():
              query = "SELECT * FROM apt"
              cur.execute(query)
              result = cur.fetchall()
              found = False
              for i in result:
                  if apt_entry1.get().isdigit():
                      if int(apt_entry1.get()) == i[0]:
                          found = True                      
              if found == True:
                  messagebox.showerror(title="INVALID INPUT", message="A record with the given BLD_No already exists")
              else:            
                  if apt_entry1.get().isdigit():
                      if apt_entry3.get().isdigit():
                          if int(apt_entry3.get()) > 799 and int(apt_entry3.get()) < 1701:
                              s = ['VACANT','OWNER','vacant','owned','Vacant','Owned']
                              if add_apt_entry2.get() in s:
                                  if apt_entry4.get().isdigit():
                                      if int(apt_entry4.get()) > 999999 and int(apt_entry4.get()) < 10000000:
                                          if apt_entry5.get().isdigit():

                                              query1 = "insert into apt values(%s, %s, %s, %s,%s)"
                                              values = (int(apt_entry1.get()),int(apt_entry5.get()),int(apt_entry3.get()), str(add_apt_entry2.get()), int(apt_entry4.get()))
                                              cur.execute(query1, values)
                                              con.commit()

                                              messagebox.showinfo(title="RECORD ADDED", message="You successfully added a record.")
                                          else:
                                              messagebox.showerror(title="INVALID INPUT", message="BHK MUST BE A DIGIT ")
                                      else:
                                          messagebox.showerror(title="INVALID INPUT", message="PRICE MUST BE WITHIN RANGE")     
                                  else:
                                      messagebox.showerror(title="INVALID INPUT", message="PRICE MUST BE A DIGIT")
                              else:
                                  messagebox.showerror(title="INVALID INPUT", message="VACANY MUST BE 'VACANT' OR 'OWNED'")
                          else:
                              messagebox.showerror(title="INVALID INPUT", message="Square_Feet MUST BE WITHIN 800 and 1600 ")
                      else:
                          messagebox.showerror(title="INVALID INPUT", message="Square_Feet MUST A DIGIT")
                  else:
                      messagebox.showerror(title="INVALID INPUT", message="BLD_No MUST BE AN INTEGER")

                          #A FRAME TO SHOW WHAT AND ALL YOU CAN DO WHEN U PRESS APT BUTTON
          
          frame2 = tk.Frame(window2, width=400, height=400, bg='white')
          frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
          frame2.place(x=375, y=200)


          global apt_entry1,add_apt_entry2,apt_entry3,apt_entry4

          apt_label1 = tk.Label(frame2,
           text="Bldg_No", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label1.place(x=-20,y=20)
          apt_entry1 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          apt_entry1.place(x = 130,y = 20)
          apt_label5 = tk.Label(frame2,
           text="BHK", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label5.place(x=-20,y=70)
          apt_entry5 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          apt_entry5.place(x = 130,y = 70)
          apt_label3 = tk.Label(frame2,
            text="SQ_Feet", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label3.place(x=-20,y=120)
          apt_entry3 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          apt_entry3.place(x = 130,y = 120)
          add_apt_label2 = tk.Label(frame2,
            text="Vacancy", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          add_apt_label2.place(x=-20,y=170)
          add_apt_entry2 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          add_apt_entry2.place(x = 130,y = 170)
          apt_label4 = tk.Label(frame2,
            text="Price", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label4.place(x=-20,y=220)
          apt_entry4 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          apt_entry4.place(x = 130,y = 220)

          apt_button1 = tk.Button(frame2,
              text="ADD RECORD", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=add_records)
          apt_button1.place(x = 120 , y = 285)

          close = tk.Button(frame2,
              text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
          close.place(x = 155 , y = 335)



      def update():
          def update_records():
              query = "SELECT * FROM apt"
              cur.execute(query)
              result = cur.fetchall()
              found = False
              for i in result:
                  if apt_entry1.get().isdigit():
                      if int(apt_entry1.get()) == i[0]:
                          found = True                      
              if found == False:
                  messagebox.showerror(title="INVALID INPUT", message="A record with the given BLD_No does not exists")
              else:            
                  if apt_entry1.get().isdigit():
                      if apt_entry3.get().isdigit():
                          if int(apt_entry3.get()) > 799 and int(apt_entry3.get()) < 1701:
                              s = ['VACANT','OWNER','vacant','owned','Vacant','Owned']
                              if add_apt_entry2.get() in s:
                                  if apt_entry4.get().isdigit():
                                      if int(apt_entry4.get()) > 999999 and int(apt_entry4.get()) < 10000000:
                                          if apt_entry5.get().isdigit():

                                              query1 = "update apt set BHK = %s,Square_Feet = %s,Vacancy = %s,Price = %s where BNO = %s"
                                              values = (int(apt_entry5.get()),int(apt_entry3.get()),str(add_apt_entry2.get()), int(apt_entry4.get()), int(apt_entry1.get()))
                                              cur.execute(query1, values)
                                              con.commit()

                                              messagebox.showinfo(title="RECORD ADDED", message="You successfully updated a record.")
                                          else:
                                              messagebox.showerror(title="INVALID INPUT", message="BHK MUST BE A DIGIT")
                                      else:
                                          messagebox.showerror(title="INVALID INPUT", message="PRICE MUST BE WITHIN '10,000,000' AND '99,999,999'")
                                  else:
                                      messagebox.showerror(title="INVALID INPUT", message="PRICE MUST BE A DIGIT ")
                              else:
                                  messagebox.showerror(title="INVALID INPUT", message="VACANY MUST BE 'VACANT' OR 'OWNED'")
                          else:
                              messagebox.showerror(title="INVALID INPUT", message="Square_Feet MUST BE WITHIN 800 and 1600 ")
                      else:
                          messagebox.showerror(title="INVALID INPUT", message="Square_Feet MUST A DIGIT")
                  else:
                      messagebox.showerror(title="INVALID INPUT", message="BLD_No MUST BE AN INTEGER") 

                  #A FRAME TO SHOW WHAT AND ALL YOU CAN DO WHEN U PRESS APT BUTTON
          frame2 = tk.Frame(window2, width=400, height=400, bg='white')
          frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
          frame2.place(x=375, y=200)

          
          apt_label1 = tk.Label(frame2,
           text="Bldg_No", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label1.place(x=-20,y=20)
          apt_entry1 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          apt_entry1.place(x = 130,y = 20)
          apt_label5 = tk.Label(frame2,
           text="BHK", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label5.place(x=-20,y=70)
          apt_entry5 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          apt_entry5.place(x = 130,y = 70)
          apt_label3 = tk.Label(frame2,
            text="SQ_Feet", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label3.place(x=-20,y=120)
          apt_entry3 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          apt_entry3.place(x = 130,y = 120)
          apt_label2 = tk.Label(frame2,
            text="Vacancy", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label2.place(x=-20,y=170)
          add_apt_entry2 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          add_apt_entry2.place(x = 130,y = 170)
          apt_label4 = tk.Label(frame2,
            text="Price", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label4.place(x=-20,y=220)
          apt_entry4 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          apt_entry4.place(x = 130,y = 220)

          apt_button1 = tk.Button(frame2,
              text="UPDATE RECORD", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=update_records)
          apt_button1.place(x = 120 , y = 285)

          close = tk.Button(frame2,
              text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
          close.place(x = 150 , y = 335)
          
      def delete():
          def delete_records():

              query = "SELECT * FROM apt"
              cur.execute(query)
              result = cur.fetchall()
              for i in result:
                  if int(apt_entry.get()) != i[0]:
                      found = False
                  else:
                      found = True
                      break
              if found == True:
                  query1 = "delete from apt where BNo = %s "
                  values = (int(apt_entry.get()),)
                  cur.execute(query1, values)
                  con.commit()
                  messagebox.showinfo(title="RECORD DELETED", message="successfully delete the record.")
              else:
                  messagebox.showerror(title="INVALID INPUT", message="BLD_No DOES NOT EXIST IN TABLE")

                  #A FRAME TO SHOW WHAT AND ALL YOU CAN DO WHEN U PRESS APT BUTTON
          frame2 = tk.Frame(window2, width=400, height=400, bg='white')
          frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
          frame2.place(x=375, y=200)

          apt_label1 = tk.Label(frame2,
           text="ENTER BLDG DETAILS OF ", bg='white',width=25, fg="#FF3399", font=("Arial", 15))
          apt_label1.place(x=60,y=20)
          apt_label3 = tk.Label(frame2,
           text=" RECORD TO BE DELETED", bg='white',width=30, fg="#FF3399", font=("Arial", 15))
          apt_label3.place(x=30,y=60)
          apt_label2 = tk.Label(frame2,
           text="Bldg_No", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label2.place(x = -5 , y = 150)
          apt_entry = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          apt_entry.place(x = 130,y = 150)

          apt_button1 = tk.Button(frame2,
              text="DELETE RECORD", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=delete_records)
          apt_button1.place(x = 100 , y = 275)

          close = tk.Button(frame2,
              text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
          close.place(x = 155 , y = 325)
      def VIEW():
          frame2 = tk.Frame(window2, width=420, height=410, bg='white')
          frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
          frame2.place(x=375, y=180)

                        ###QUERY TO VIEW THE TABLE CONTENTS
          query = "SELECT * FROM APT"
          cur.execute(query)
          result = cur.fetchall()
          t = "{:<7}{:<10}{:<20}{:<20}{:<8}"
          s = t.format('BNo','BHK','Sq_Feet', 'VACANCY', 'PRICE')
          t2 = "{:<15}{:<15}{:<20}{:<20}{:<20}"
          s2 =''
          for i in result:
            s2 += t2.format(str(i[0]), str(i[1]), str(i[2]), i[3],str(i[4]))+ '\n' + '\n'

          view_label1 = tk.Label(frame2,
           text='TABLE   :    APT', bg='white',width=45, fg="#FF3399",borderwidth=1, relief="solid", font=("Arial", 16))
          view_label1.place(x=-70, y=0)
          view_label2 = tk.Label(frame2,
           text=s, bg='white',width=45, fg="#FF3399", font=("Arial", 12))
          view_label2.place(x=0, y=70)
          view_label3 = tk.Label(frame2,
           text=s2, bg='white',width=50, fg="#FF3399", font=("Arial", 12))
          view_label3.place(x=0, y=100)


          close = tk.Button(frame2,
              text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
          close.place(x = 155 , y = 350)
          
      global apt_button1,apt_button2,apt_button3,apt_button4

      apt_button1 = tk.Button(window2,
        text="ADD", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=ADD)
      apt_button1.place(x = 260 , y = 280)
      
      apt_button2 = tk.Button(window2,
        text="UPDATE", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=update)
      apt_button2.place(x = 250 , y =330)
      
      apt_button3 = tk.Button(window2,
        text="DELETE", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=delete)
      apt_button3.place(x = 250 , y = 380)
      
      apt_button4 = tk.Button(window2,
        text="VIEW", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=VIEW)
      apt_button4.place(x = 260 , y = 430)

    def owner():
        
        def ADD1():

            def add_records1():
                ###CHECKING VACANCY
                Vacancy = []
                B_N_O = []

                query1 = "select vacancy from apt where BNO = %s;"
                values1 = (int(apt_entry3.get()),)
                cur.execute(query1,values1)
                result1 = cur.fetchone()           
                if result1 is None:
                    messagebox.showerror(title="INVALID INPUT", message="A RECORD WITH THE GIVEN BNO DOES NOT EXIST")
                    B_N_O = [-1]

                elif result1[0].lower() == 'vacant' :
                    Vacancy = [-1]
                else:
                    pass

                query = "SELECT * FROM owner"
                cur.execute(query)
                result = cur.fetchall()
                found1 = False
                for i in result:
                    if apt_entry1.get().isdigit():
                        if int(apt_entry1.get()) == i[0]:
                            found1 = True                      
                if found1 == True:
                    messagebox.showerror(title="INVALID INPUT", message="A record with the given Ow_ID already exists")
                else:           
                    if B_N_O != [-1]: 
                        if apt_entry1.get().isdigit():
                            if apt_entry2.get().isdigit() and len(str(apt_entry2.get())) == 10:
                                if apt_entry3.get().isdigit():
                                    if apt_entry5.get().isalpha() or str(apt_entry5.get()) == '':
                                        if apt_entry1.get() == apt_entry3.get():
                                            if Vacancy == [-1]:

                                                messagebox.showerror(title="RECORD NOT ADDED", message="Can't Have an OWNER for a VACANT APT")

                                            else:
                                                if str(apt_entry5.get()) == '':
                                                    messagebox.showerror(title="INVALID INPUT", message="MUST HAVE AN OWNER FOR A OWNED APT")
                                                else:
                                                    query1 = "insert into owner values(%s, %s, %s,%s)"
                                                    values = (int(apt_entry1.get()),str(apt_entry5.get()),int(apt_entry2.get()), int(apt_entry3.get()))
                                                    cur.execute(query1,values)
                                                    con.commit()

                                                    messagebox.showinfo(title="RECORD ADDED", message="You successfully added a record.")
                                        else:
                                            messagebox.showerror(title = 'INVALID INPUT', message = "OW_ID MUST BE EQAUAL TO BNO")
                                    else:
                                        messagebox.showerror(title="INVALID INPUT", message="NAME MUST A STRING")
                                else:
                                    messagebox.showerror(title="INVALID INPUT", message="BNO MUST BE AN INTEGER")
                            else:
                                messagebox.showerror(title="INVALID INPUT", message="PHONE NO MUST BE AN INTEGER" + "\n" + 'AND MUST BE 10 DIGITS LONG')
                        else:
                            messagebox.showerror(title="INVALID INPUT", message="BLD_No MUST BE AN INTEGER")

                            #A FRAME TO SHOW WHAT AND ALL YOU CAN DO WHEN U PRESS APT BUTTON
            
            frame2 = tk.Frame(window2, width=400, height=400, bg='white')
            frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
            frame2.place(x=375, y=200)

            global apt_entry1,apt_entry2,apt_entry3,apt_entry4

            apt_label1 = tk.Label(frame2,
             text="Ow_ID", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            apt_label1.place(x=-20,y=20)
            apt_entry1 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            apt_entry1.place(x = 130,y = 20)
            apt_label5 = tk.Label(frame2,
             text="Name", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            apt_label5.place(x=-20,y=70)
            apt_entry5 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            apt_entry5.place(x = 130,y = 70)
            apt_label2 = tk.Label(frame2,
              text="Phone_NO", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            apt_label2.place(x=-20,y=120)
            apt_entry2 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            apt_entry2.place(x = 130,y = 120)
            apt_label3 = tk.Label(frame2,
              text="BNO", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            apt_label3.place(x=-20,y=170)
            apt_entry3 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            apt_entry3.place(x = 130,y = 170)

            
            apt_button1 = tk.Button(frame2,
                text="ADD RECORD", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=add_records1)
            apt_button1.place(x = 120 , y = 285)

            close = tk.Button(frame2,
                text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
            close.place(x = 155 , y = 335)


        def update1():
            def update_records1():

              ###CHECKING VACANCY
                Vacancy = []

                query1 = "select vacancy from apt where BNO = %s;"
                values1 = (str(apt_entry3.get()),)
                cur.execute(query1,values1)
                result1 = cur.fetchone()
                B_N_O = []
                if result1 is None:
                    messagebox.showerror(title="INVALID INPUT", message="A RECORD WITH THE GIVEN BNO DOES NOT EXIST") 
                    B_N_O = [-1]

                elif result1[0].lower() == 'vacant' :
                    Vacancy = [-1]
                else:
                    pass

                query = "SELECT * FROM owner"
                cur.execute(query)
                result = cur.fetchall()
                found = False
                
                if B_N_O != [-1]: 
                    if apt_entry1.get().isdigit():
                        if apt_entry2.get().isdigit() and len(str(apt_entry2.get())) == 10:
                            if apt_entry3.get().isdigit():
                                if apt_entry5.get().isalpha() or str(apt_entry5.get()) == '':
                                    if apt_entry1.get() == apt_entry3.get():
                                
                                        if Vacancy == [-1]:

                                            messagebox.showerror(title="INVALID INPUT", message="CANT UPDATE OWNER RECORD WHERE OWNER DOES NOT EXIST")

                                        else:
                                        
                                            query1 = "update owner set Ow_ID = %s, Name = %s,Phone_NO = %s where BNO = %s"
                                            values = (int(apt_entry1.get()),str(apt_entry5.get()),int(apt_entry2.get()), int(apt_entry3.get()))
                                            cur.execute(query1,values)
                                            con.commit()

                                            messagebox.showinfo(title="RECORD ADDED", message="You successfully updated a record.")
                                    else:
                                        messagebox.showerror(title = 'INVALID INPUT', message = "OW_ID MUST BE EQAUAL TO BNO")
                               
                                else:
                                    messagebox.showerror(title="INVALID INPUT", message="NAME MUST A STRING")
                            else:
                                messagebox.showerror(title="INVALID INPUT", message="BNO MUST BE AN INTEGER")
                        else:
                            messagebox.showerror(title="INVALID INPUT", message="PHONE NO MUST BE AN INTEGER" + "\n" + 'AND MUST BE 10 DIGITS LONG')
                    else:
                        messagebox.showerror(title="INVALID INPUT", message="BLD_No MUST BE AN INTEGER")

                            #A FRAME TO SHOW WHAT AND ALL YOU CAN DO  WHEN U PRESS APT BUTTON


            frame2 = tk.Frame(window2, width=400, height=400, bg='white')
            frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
            frame2.place(x=375, y=200)

            global apt_entry1,apt_entry2,apt_entry3,apt_entry4

            apt_label1 = tk.Label(frame2,
             text="Ow_ID", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            apt_label1.place(x=-20,y=20)
            apt_entry1 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            apt_entry1.place(x = 130,y = 20)
            apt_label5 = tk.Label(frame2,
             text="Name", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            apt_label5.place(x=-20,y=70)
            apt_entry5 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            apt_entry5.place(x = 130,y = 70)
            apt_label2 = tk.Label(frame2,
              text="Phone_NO", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            apt_label2.place(x=-20,y=120)
            apt_entry2 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            apt_entry2.place(x = 130,y = 120)
            apt_label3 = tk.Label(frame2,
              text="BNO", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            apt_label3.place(x=-20,y=170)
            apt_entry3 = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            apt_entry3.place(x = 130,y = 170)

            
            apt_button1 = tk.Button(frame2,
                text="UPDATE RECORD", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=update_records1)
            apt_button1.place(x = 120 , y = 285)

            close = tk.Button(frame2,
                text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
            close.place(x = 155 , y = 335)


        def delete1():
            def delete_records1():
                query = "SELECT * FROM owner"
                cur.execute(query)
                result = cur.fetchall()
                for i in result:
                    if int(apt_entry.get()) != i[0]:
                        found = False
                    else:
                        found = True
                        break
                if found == True:
                    query1 = "delete from owner where Ow_ID = %s "
                    values = (int(apt_entry.get()),)
                    cur.execute(query1, values)
                    con.commit()
                    messagebox.showinfo(title="RECORD DELETED", message="successfully delete the record.")
                else:
                    messagebox.showerror(title="INVALID INPUT", message="Ow_ID DOES NOT EXIST IN TABLE")

                  #A FRAME TO SHOW WHAT AND ALL YOU CAN DO WHEN U PRESS APT BUTTON
            frame2 = tk.Frame(window2, width=400, height=400, bg='white')
            frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
            frame2.place(x=375, y=200)

            apt_label1 = tk.Label(frame2,
             text="ENTER OWNER DETAILS OF ", bg='white',width=25, fg="#FF3399", font=("Arial", 15))
            apt_label1.place(x=60,y=20)
            apt_label3 = tk.Label(frame2,
             text=" RECORD TO BE DELETED", bg='white',width=30, fg="#FF3399", font=("Arial", 15))
            apt_label3.place(x=30,y=60)
            apt_label2 = tk.Label(frame2,
             text="Ow_ID", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            apt_label2.place(x = -5 , y = 150)
            apt_entry = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            apt_entry.place(x = 130,y = 150)

            apt_button1 = tk.Button(frame2,
                text="DELETE RECORD", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=delete_records1)
            apt_button1.place(x = 100 , y = 275)

            close = tk.Button(frame2,
                text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
            close.place(x = 155 , y = 325)


        def VIEW1():
            
            frame2 = tk.Frame(window2, width=400, height=400, bg='white')
            frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
            frame2.place(x=375, y=180)

                          ###QUERY TO VIEW THE TABLE CONTENTS
            query = "SELECT * FROM owner"
            cur.execute(query)
            result = cur.fetchall()
            t = "{:<15}{:<12}{:<20}{:<5}"
            s = t.format('Ow_ID','Name','Phone_No', 'BNO')
            t2 = "{:<15}{:<15}{:<20}{:<12}"
            s2 =''
            for i in result:
              if i[1] == 'None' : 
                  s2 += t2.format(str(i[0]),'NULL', str(i[2]), str(i[3]))+ '\n' + '\n'
              else:
                  s2 += t2.format(str(i[0]),str(i[1]), str(i[2]), str(i[3]))+ '\n' + '\n'

            view_label1 = tk.Label(frame2,
             text='TABLE   :    OWNER', bg='white',width=45, fg="#FF3399",borderwidth=1, relief="solid", font=("Arial", 16))
            view_label1.place(x=-70, y=10)
            view_label2 = tk.Label(frame2,
             text=s, bg='white',width=45, fg="#FF3399", font=("Arial", 12))
            view_label2.place(x=0, y=70)
            view_label3 = tk.Label(frame2,
             text=s2, bg='white',width=50, fg="#FF3399", font=("Arial", 12))
            view_label3.place(x=0, y=100)


            close = tk.Button(frame2,
                text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
            close.place(x = 155 , y = 350)
                      ## THE MAIN BUTTONS
        global owner_button1          
        owner_button1 = tk.Button(window2,
          text="ADD", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=ADD1)
        owner_button1.place(x = 260 , y = 280)
        
        apt_button2 = tk.Button(window2,
          text="UPDATE", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=update1)
        apt_button2.place(x = 250 , y =330)
        global owner_button3
        owner_button3 = tk.Button(window2,
          text="DELETE", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=delete1)
        owner_button3.place(x = 250 , y = 380)
        
        apt_button4 = tk.Button(window2,
          text="VIEW", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=VIEW1)
        apt_button4.place(x = 260 , y = 430)
    def Credentials():
        
        try:
          owner_button3.place(x=1000,y=1000)
          complaints_button3.place(x= 1000,y=1000)
          apt_button3.place(x = 1000,y=1000)
        except NameError:
          pass
        def delete_cred():

            def delete_CREDENTIALS():

                global Ow_ID_creddentials

                if Ow_ID_creddentials.get() == None:
                    messagebox.showerror(title="INVALID INPUT", message="Ow_ID CANNOT BE EMPTY")
                else:
                    query = 'select * from credentials where Ow_ID = %s'
                    values = (Ow_ID_creddentials.get(),)
                    cur.execute(query,values)
                    result = cur.fetchall()
                    if result == []:
                        messagebox.showerror(title="INVALID INPUT", message="Ow_ID DOES NOT EXIST IN TABLE")
                    else:
                        query = 'delete from credentials where Ow_ID = %s'
                        values = (Ow_ID_creddentials.get(),)
                        cur.execute(query,values)
                        con.commit()

                        messagebox.showinfo(title="RECORD DELETED", message="CREDENTIALS SUCCESSFULLY DELETED")


            frame2 = tk.Frame(window2, width=400, height=400, bg='white')
            frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
            frame2.place(x=375, y=180)

            apt_label1 = tk.Label(frame2,
              text="ENTER Ow_ID DETAILS OF ", bg='white',width=25, fg="#FF3399", font=("Arial", 15))
            apt_label1.place(x=60,y=20)
            apt_label3 = tk.Label(frame2,
             text=" CREDENTIALS TO BE DELETED", bg='white',width=30, fg="#FF3399", font=("Arial", 15))
            apt_label3.place(x=30,y=60)
            apt_label2 = tk.Label(frame2,
             text="Ow_ID", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            apt_label2.place(x = -15 , y = 150)
            global Ow_ID_creddentials
            Ow_ID_creddentials = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            Ow_ID_creddentials.place(x = 130,y = 150)

            apt_button1 = tk.Button(frame2,
                text="DELETE CREDENTIALS", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=delete_CREDENTIALS)
            apt_button1.place(x = 100 , y = 275)

            close = tk.Button(frame2,
                text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
            close.place(x = 155 , y = 325)

        def view_cred():

            frame2 = tk.Frame(window2, width=400, height=400, bg='white')
            frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
            frame2.place(x=375, y=180)

                          ###QUERY TO VIEW THE TABLE CONTENTS
            query = "SELECT * FROM credentials"
            cur.execute(query)
            result = cur.fetchall()
            t = "{:<15}{:<20}{:<10}"
            s = t.format('USERNAME','PASSWORD','Ow_ID')
            t2 = "{:<20}{:<30}{:<20}"
            s2 =''
            for i in result:
              if i[1] == 'None' : 
                  s2 += t2.format(str(i[0]),'NULL', str(i[2]), str(i[3]))+ '\n' + '\n'
              else:
                  s2 += t2.format(str(i[0]),str(i[1]), str(i[2]))+ '\n' + '\n'

            view_label1 = tk.Label(frame2,
             text='TABLE   :    CREDENTIALS', bg='white',width=45, fg="#FF3399",borderwidth=1, relief="solid", font=("Arial", 16))
            view_label1.place(x=-70, y=10)
            view_label2 = tk.Label(frame2,
             text=s, bg='white',width=45, fg="#FF3399", font=("Arial", 12))
            view_label2.place(x=0, y=70)
            view_label3 = tk.Label(frame2,
             text=s2, bg='white',width=50, fg="#FF3399", font=("Arial", 12))
            view_label3.place(x=0, y=100)


            close = tk.Button(frame2,
                text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
            close.place(x = 155 , y = 350)

        delete_cred= tk.Button(window2,
          text="DELETE", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=delete_cred)
        delete_cred.place(x = 250 , y = 380)

        view_cred = tk.Button(window2,
              text="VIEW", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=view_cred)
        view_cred.place(x = 260 , y = 430)

        def update_cred():

            global username_user,password_user,Ow_ID_cred

            frame2 = tk.Frame(window2, width=400, height=400, bg='white')
            frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
            frame2.place(x=375, y=180)


            title =  tk.Label(frame2,
                text=" ENTER NEW CREDENTIALS", bg='white',width=20, fg="#FF3399", font=("Arial", 16))
            title.place(x=80,y=20)
            title2 = tk.Label(frame2,
                text="OF USER", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            title2.place(x = 100,y = 60)

            username = tk.Label(frame2,
                text="USERNAME", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            username.place(x=-20,y=110)
            username_user = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            username_user.place(x = 150,y = 110)
            password = tk.Label(frame2,
                text="PASSWORD", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            password.place(x=-20,y=170)
            password_user = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            password_user.place(x = 150,y = 170)
            o_ID = tk.Label(frame2,
                text="Ow_ID", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            o_ID.place(x=-20,y=220)
            Ow_ID_cred = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            Ow_ID_cred.place(x = 150,y = 220)

            def update_credentials():

                if Ow_ID_cred.get() == '':
                    messagebox.showerror(title="INVALID INPUT", message=" BNO CANT BE EMPTY")
                else:

                    query = 'select * from owner where Ow_ID = %s '
                    values = (int(Ow_ID_cred.get()),)
                    cur.execute(query,values)
                    result = cur.fetchall()

                    found1 = False
                    for i in result:
                          if Ow_ID_cred.get().isdigit():
                                if int(Ow_ID_cred.get()) == i[0]:
                                      found1 = True 
                                      break
                          else:
                                messagebox.showerror(title="INVALID INPUT", message=" BNO MUST BE AN INT")
                    if found1 != True:
                          messagebox.showerror(title="INVALID INPUT", message="A RECORD WITH THE GIVEN BNO DOES NOT EXIST")
                    else:
                        if str(username_user.get()) != '' and len(str(username_user.get())) == 8:
                            if str(password_user.get()) != '' and len(str(password_user.get())) == 10:

                                query = "update credentials set Username = %s,Password = %s where Ow_ID = %s "
                                values = (username_user.get(),password_user.get(),str(Ow_ID_cred.get()))
                                cur.execute(query,values)
                                con.commit()

                                messagebox.showinfo(title="SAVED SUCCESSFULLY", message="CREDENTIALS OF USER HAVE BEEN UPDATED")
                            else:
                                messagebox.showerror(title="INVALID INPUT", message="PASSWORD MUST BE 10 CHARECTERS LONG")
                        else:
                          messagebox.showerror(title="INVALID INPUT", message="USERNAME MUST BE 8 CHARECTERS LONG")


            save = tk.Button(frame2,
                text="UPDATE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=update_credentials)
            save.place(x=100,y=300)

            close = tk.Button(frame2,
                text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
            close.place(x = 225 , y = 300)


        apt_button1 = tk.Button(window2,
            text="UPDATE", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command= update_cred)
        apt_button1.place(x = 250 , y = 330)

        def add_cred():
            global username_user,password_user,Ow_ID_cred

            frame2 = tk.Frame(window2, width=400, height=400, bg='white')
            frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
            frame2.place(x=375, y=180)


            title =  tk.Label(frame2,
                text=" ENTER CREDENTIALS", bg='white',width=20, fg="#FF3399", font=("Arial", 16))
            title.place(x=80,y=20)
            title2 = tk.Label(frame2,
                text="OF USER", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            title2.place(x = 100,y = 60)

            username = tk.Label(frame2,
                text="USERNAME", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            username.place(x=-20,y=110)
            username_user = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            username_user.place(x = 150,y = 110)
            password = tk.Label(frame2,
                text="PASSWORD", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            password.place(x=-20,y=170)
            password_user = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            password_user.place(x = 150,y = 170)
            o_ID = tk.Label(frame2,
                text="Ow_ID", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
            o_ID.place(x=-20,y=220)
            Ow_ID_cred = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
            Ow_ID_cred.place(x = 150,y = 220)

            def save():

                query = 'select * from owner'
                cur.execute(query)
                result = cur.fetchall()

                query = 'select * from credentials where Ow_ID = %s'
                values = (Ow_ID_cred.get(),)
                cur.execute(query,values)
                result1 = cur.fetchall()
                found = False
                if result1 == []:
                  found = True

                found1 = False

                if Ow_ID_cred.get() == '':
                    messagebox.showerror(title="INVALID INPUT", message=" BNO CANT BE EMPTY")
                else:

                    for i in result:
                          if Ow_ID_cred.get().isdigit():
                                if int(Ow_ID_cred.get()) == i[0]:
                                      found1 = True 
                                      break
                          else:
                                messagebox.showerror(title="INVALID INPUT", message=" BNO MUST BE AN INT")
                    if found1 != True:
                          messagebox.showerror(title="INVALID INPUT", message="A RECORD WITH THE GIVEN BNO DOES NOT EXIST")
                    else:
                        if found == True:
                            if str(username_user.get()) != '' and len(str(username_user.get())) == 8:
                                if str(password_user.get()) != '' and len(str(password_user.get())) == 10:
                                    try:
                                        query = "insert into credentials values(%s, %s, %s)"
                                        values = (username_user.get(),password_user.get(),str(Ow_ID_cred.get()))
                                        cur.execute(query,values)
                                        con.commit()

                                        messagebox.showinfo(title="SAVED SUCCESSFULLY", message="CREDENTIALS OF USER HAVE BEEN SAVED")
                                    except ms.errors.IntegrityError:
                                        messagebox.showerror(title="ERROR", message="DUPLICATE CREDENTIALS CANNOT BE ASSIGNED")
                                else:
                                    messagebox.showerror(title="INVALID INPUT", message="PASSWORD MUST BE 10 CHARECTERS LONG")
                            else:
                              messagebox.showerror(title="INVALID INPUT", message="USERNAME MUST BE 8 CHARECTERS LONG")
                        else:
                            messagebox.showerror(title="INVALID INPUT", message="OWNER CREDENTIALS ALREADY EXIST")


            save = tk.Button(frame2,
                text="SAVE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=save)
            save.place(x=100,y=300)

            close = tk.Button(frame2,
                text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
            close.place(x = 225 , y = 300)

        global credentials_button1
        credentials_button1 = tk.Button(window2,
            text="ADD", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=add_cred)
        credentials_button1.place(x = 260 , y = 280)


    def Complaints():
      try:
        credentials_button1.place(x=1000,y=1000)
      except NameError:
        pass
      def REPLY():


                           # FRAME TO SHOW WHAT AND ALL YOU CAN DO WHEN U PRESS APT BUTTON

          frame2 = tk.Frame(window2, width=400, height=400, bg='white')
          frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
          frame2.place(x=375, y=200)


          def get_input():

              global value_ID,Input_Oid,Input_Username

              comment = my_text_box.get("1.0","end-1c")
              if comment == '' or len(comment) < 8:
                  messagebox.showerror(title="INVALID INPUT", message="REPLY MUST BE ATLEAST 8 CHARECTERS")
              else:

                  f = open("comment.txt",'w')
                  f.write(comment)
                  f.close

                  query = "SELECT * FROM complaints"
                  cur.execute(query)
                  result = cur.fetchall()
                  for i in result:
                      if str(apt_entry.get()) == '':
                          messagebox.showerror(title="INVALID INPUT", message="COMPLAINT NO CAN NOT BE EMPTY")
                          break
                      else:
                          if int(apt_entry.get()) != i[0]:
                              pass
                          else:
                              found_reply = True
                              break
                  try:

                      if found_reply == True:
                          query = 'select Ow_ID from complaints where C_NO = %s'
                          x = (int(apt_entry.get()),)
                          cur.execute(query,x)
                          y = cur.fetchall()
                          Input_Oid = y[0][0]
                          query = 'select username from credentials where Ow_ID = %s'
                          z = (Input_Oid,)
                          cur.execute(query,z)
                          a = cur.fetchall()
                          Input_Username = a[0][0]

                          K = open("Reply_Username.txt","w")
                          K.write(Input_Username)
                          K.close()

                          K2 = open("Reply_Username.txt","r")
                          q = K2.read()
                          K2.close()

                          messagebox.showinfo(title="REPLY SENT", message="MSG SENT SUCCESSFULLY")
                      else:
                          messagebox.showerror(title="INVALID INPUT", message="COMPLAINT DOES NOT EXIST IN TABLE")

                  except UnboundLocalError:
                      messagebox.showerror(title="INVALID INPUT", message="COMPLAINT WITH GIVEN COM_NO DOES NOT EXIST IN TABLE")

          apt_label1 = tk.Label(frame2,
           text="ENTER COM_NO OF", bg='white',width=25, fg="#FF3399", font=("Arial", 15))
          apt_label1.place(x=60,y=20)
          apt_label3 = tk.Label(frame2,
           text=" COMPLAINT TO REPLY", bg='white',width=30, fg="#FF3399", font=("Arial", 15))
          apt_label3.place(x=30,y=60)
          apt_label2 = tk.Label(frame2,
           text="COMP_NO", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label2.place(x = -15 , y = 130)
          apt_entry = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          apt_entry.place(x = 130,y = 130)

          apt_label4 = tk.Label(frame2,
           text=" MESSAGE ", bg='white',width=30, fg="#FF3399", font=("Arial", 15))
          apt_label4.place(x=35,y=175)

          #Creating a text box widget
          my_text_box=Text(frame2, height=5, width=30,font=("Arial", 14),fg="#800000", bg = '#e5fcf5')
          my_text_box.place(x = 30,y = 210)

          #Create a button for Comment
          comment= Button(frame2,text="SEND", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=lambda: get_input())

          #command=get_input() will wait for the key to press and displays the entered text
          comment.place(x=100,y=340)

          close = tk.Button(frame2,
              text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
          close.place(x = 225 , y = 340)

      def delete_complaints_adm():

          def delete_records():

              query = "SELECT * FROM complaints"
              cur.execute(query)
              result = cur.fetchall()
              found = False
              for i in result:
                  if int(apt_entry.get()) != i[0]:
                      pass
                  else:
                      found = True
                      break
              if found == True:
                  query1 = "delete from complaints where C_NO = %s "
                  values = (int(apt_entry.get()),)
                  cur.execute(query1, values)
                  con.commit()
                  messagebox.showinfo(title="RECORD DELETED", message="successfully delete the complaint.")
              else:
                  messagebox.showerror(title="INVALID INPUT", message="COMPLAINT DOES NOT EXIST IN TABLE")

                  #A FRAME TO SHOW WHAT AND ALL YOU CAN DO WHEN U PRESS APT BUTTON
          frame2 = tk.Frame(window2, width=400, height=400, bg='white')
          frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
          frame2.place(x=375, y=200)

          apt_label1 = tk.Label(frame2,
           text="ENTER COM_NO DETAILS OF ", bg='white',width=25, fg="#FF3399", font=("Arial", 15))
          apt_label1.place(x=60,y=20)
          apt_label3 = tk.Label(frame2,
           text=" COMPLAINT TO BE DELETED", bg='white',width=30, fg="#FF3399", font=("Arial", 15))
          apt_label3.place(x=30,y=60)
          apt_label2 = tk.Label(frame2,
           text="COMP_NO", bg='white',width=15, fg="#FF3399", font=("Arial", 16))
          apt_label2.place(x = -15 , y = 150)
          apt_entry = tk.Entry(frame2,fg="#FF3399", font=("Arial", 16))
          apt_entry.place(x = 130,y = 150)

          apt_button1 = tk.Button(frame2,
              text="DELETE COMPLAINT", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=delete_records)
          apt_button1.place(x = 100 , y = 275)

          close = tk.Button(frame2,
              text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
          close.place(x = 155 , y = 325)
      def view_complaints_adm():

          frame2 = tk.Frame(window2, width=400, height=400, bg='white')
          frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
          frame2.place(x=375, y=180)

                      ###QUERY TO VIEW THE TABLE CONTENTS
          query = "SELECT * FROM complaints"
          cur.execute(query)
          result = cur.fetchall()
          t = "{:<15}{:<12}{:<20}{:<5}"
          s = t.format('CNO','Name','Ow_ID','COMPLAINTS')
          t2 = "{:<15}{:<15}{:<20}{:<12}"
          s2 =''
          for i in result:
            s2 += t2.format(str(i[0]), i[1], str(i[2]), i[3]) + '\n' + '\n'

          view_label1 = tk.Label(frame2,
           text='TABLE   :    APT', bg='white',width=45, fg="#FF3399",borderwidth=1, relief="solid", font=("Arial", 16))
          view_label1.place(x=-70, y=0)
          view_label2 = tk.Label(frame2,
           text=s, bg='white',width=45, fg="#FF3399", font=("Arial", 12))
          view_label2.place(x=0, y=70)
          view_label3 = tk.Label(frame2,
           text=s2, bg='white',width=50, fg="#FF3399", font=("Arial", 12))
          view_label3.place(x=0, y=100)


          close = tk.Button(frame2,
              text="CLOSE", bg="#FF3399", fg="#FFFFFF",  borderwidth=3, relief="raised",font=("Arial", 16), command=frame2.destroy)
          close.place(x = 155 , y = 350)

      global owner_button1,apt_button1

      try:
        owner_button1.place(x=1000,y=1000)
        apt_button1.place(x=1000,y=1000)
      except NameError:
        pass
      
      apt_button2 = tk.Button(window2,
        text=" REPLY ", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=REPLY)
      apt_button2.place(x = 250 , y =330)
      global complaints_button3
      complaints_button3 = tk.Button(window2,
        text="DELETE", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=delete_complaints_adm)
      complaints_button3.place(x = 250 , y = 380)
      
      apt_button4 = tk.Button(window2,
        text="VIEW", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=view_complaints_adm)
      apt_button4.place(x = 260 , y = 430)

    def clear_table():

        def clear_apt():

            def Yes():
                apt_clear.place(x = -500,y=-500)
                query = 'delete from apt'
                cur.execute(query)
                messagebox.showinfo(title="DATA CLEARED", message="APT TABLE CLEARED")
                con.commit()
                window3.destroy()
            def No():
                apt_clear.place(x = -500,y=-500)
                window3.destroy()

            window3 = tk.Tk()
            window3.eval('tk::PlaceWindow . center')
            window3.title("CHECKING...")
            window3.geometry('300x300+420+280')
            window3.configure(bg='#FF3399')
            window3.resizable(False,False)

            login_label = tk.Label(window3,
               text="ARE YOU SURE YOU WANT", fg="#FF3399", font=("Arial", 15))
            login_label.place(x =20, y = 50)
            login_label1 = tk.Label(window3,
               text=" TO CLEAR ALL DATA ???", fg="#FF3399", font=("Arial", 15))
            login_label1.place(x = 25, y = 90)

            Yes_button = tk.Button(window3,
                text="YES", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Yes)
            Yes_button.place(x = 50 , y = 200)

            No_button = tk.Button(window3,
                text="No", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=No)
            No_button.place(x = 175 , y = 200)
        global apt_clear
            
        apt_clear = tk.Button(window2,
            text="APT", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=clear_apt)
        apt_clear.place(x = 180 , y = 480)

        def clear_owner():

            def Yes1():
                owner_clear.place(x = -500,y=-500)
                query = 'delete from owner'
                cur.execute(query)
                messagebox.showinfo(title="DATA CLEARED", message="OWNER TABLE CLEARED")
                con.commit()
                window3.destroy()
            def No1():
                owner_clear.place(x = -500,y=-500)
                window3.destroy()

            window3 = tk.Tk()
            window3.eval('tk::PlaceWindow . center')
            window3.title("CHECKING...")
            window3.geometry('300x300+420+280')
            window3.configure(bg='#FF3399')
            window3.resizable(False,False)

            login_label = tk.Label(window3,
               text="ARE YOU SURE YOU WANT", fg="#FF3399", font=("Arial", 15))
            login_label.place(x =20, y = 50)
            login_label1 = tk.Label(window3,
               text=" TO CLEAR ALL DATA ???", fg="#FF3399", font=("Arial", 15))
            login_label1.place(x = 25, y = 90)

            Yes_button = tk.Button(window3,
                text="YES", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Yes1)
            Yes_button.place(x = 50 , y = 200)

            No_button = tk.Button(window3,
                text="No", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=No1)
            No_button.place(x = 175 , y = 200)
        global owner_clear
            
        owner_clear = tk.Button(window2,
            text="OWNER", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=clear_apt)
        apt_clear.place(x = 180 , y = 520)


              # Creating another window for HOME PAGE
    window2 = tk.Tk()
    window2.title("Home Page")
    window2.geometry('900x615-250-50')
    window2.configure(bg='white')
    window2.resizable(False,False)

                      #IMAGE
    frame = tk.Frame(window2, width=900, height=815, bg='white')
    frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                    ##This is to place the frame of the image on the window2
    frame.place(x=0, y=0)


                    # Create an object of tk ImageTk
    global img
    img = PhotoImage(file='C:/Users/Rohit/Desktop/Dubai-PNG-Pic.png', master=window2)

                    # Create a Label Widget to display the text or Image
    label = tk.Label(frame, image=img)
    label.place(x=-400,y=-300)


    
                  # Labels for home page
    global y
    def slider():
        global count,text,y
        if count >= len(y):
            count = 0
            text = ""
            apt_Label.config(text=text)
        else:
            text += y[count]
            apt_Label.config(text=text)
            count += 1
        apt_Label.after(200,slider)
    login_label = tk.Label(frame,
       text="HOME PAGE", fg="#FF3399", font=("Arial", 30))
    login_label.place(relx= 0.35, y = 20)
    apt_Label = tk.Label(frame,
       text= y, fg="#FF3399", font=("Arial", 30))
    apt_Label.place(relx= 0.05, y = 75)
    slider()


                  #Buttons for Home Page
    apt_button = tk.Button(window2,
        text="APARTMENTS", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=APT)
    apt_button.place(x = 50 , y = 200)
    event_button = tk.Button(window2,
        text="COMPLAINTS", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Complaints)
    event_button.place(x = 50 , y = 350)
    Owner_button = tk.Button(window2,
        text="OWNER", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=owner)
    Owner_button.place(x = 75 , y = 280)
    Amenities_but = tk.Button(window2,
      text="CREDENTIALS", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Credentials)
    Amenities_but.place(x = 50 , y = 415)
    clear = tk.Button(window2,
      text="CLEAR", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=clear_table)
    clear.place(x = 75 , y = 480)
    Exit_Button = tk.Button(window2,
      text="Exit", bg="#FF3399", fg="#FFFFFF",borderwidth=3, relief="raised", font=("Arial", 16), command=lambda:[window2.withdraw(), First()])
    Exit_Button.place(x = 800 , y = 550)



  def Admin():
      
      def login_adm():
        
          username = ""
          password = ""
         
          if username_entry.get()==username and password_entry.get()==password:
              messagebox.showinfo(title="Login Success", message="You successfully logged in.")
              Home_Page()
              window1.destroy()
              
          else:
              messagebox.showerror(title="Error", message="Unathorised Access")


                  #Forgot Password
      def forgot_pass():
        messagebox.showinfo(title="Forgot_Pass", message="Username => Jagath \n\nPassword => 123456")


      window_start.destroy()

      window1 = tk.Tk()
      window1.title("Login Page")
      window1.geometry('390x440+435+175')
      window1.configure(bg='#333333')
      window1.resizable(False,False)

                  #IMAGE FOR LOGIN PAGE
      frame = tk.Frame(window1, width=390, height=440, bg='white')
      frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                        ##This is to place the frame of the image on the window2
      frame.place(x=0, y=0)

      global img
      img = PhotoImage(file='C:/Users/Rohit/Desktop/lovepik-apartment-building-png-image_401530275_wh1200.png', master=window1)

                        # Create a Label Widget to display the text or Image
      label = tk.Label(frame, image=img)
      label.place(x=-250,y=-100)

      login_label = tk.Label(
          window1, text="Login", bg='white', fg="#FF3399", font=("Arial", 30))
      username_label = tk.Label(
          window1, text="Username", bg='white', fg="#FF3399", font=("Arial", 16))
      username_entry = tk.Entry(window1,fg="#FF3399", font=("Arial", 16))
      password_entry = tk.Entry(window1, show="*", font=("Arial", 16))
      password_entry.bind('<Return>', lambda event: login_adm())
      password_label = tk.Label(
          window1, text="Password", bg='white', fg="#FF3399", font=("Arial", 16))
      login_button = tk.Button(
          window1, text="Login", bg="white", fg="#FF3399", font=("Arial", 16), command=login_adm)
      Forgot_Cred = tk.Button(
          window1, text="Forgot password", bg="white", fg="#FF3399", font=("Arial", 10), command=forgot_pass)
      Forgot_Cred.place(x = 140,y = 275)

      login_label.place(x=140, y=0)
      username_label.place(x=25, y=100)
      username_entry.place(x=125, y=100)
      password_label.place(x=25, y=150)
      password_entry.place(x=125, y=150)
      login_button.place(x=155, y=225)

  def User():

      global result_credential,U,P,password_user_entry,username_user_entry

      query = 'select * from credentials'
      cur.execute(query)
      result_credential = cur.fetchall()


      def login_user():
          U = []
          P = []
          for i in result_credential:
              U.append(i[0])
              P.append(i[1])
            
          Name = str(username_user_entry.get())

          if username_user_entry.get() in U and password_user_entry.get() in P:
              F = open("Login_Username.txt","w")
              F3 = open('Password_Username.txt','w')
              F.write(username_user_entry.get())
              F3.write(password_user_entry.get())
              F.close()
              F2 = open("Login_Username.txt","r")
              s = F2.read()
              F2.close()

              messagebox.showinfo(title="Login Success", message="  WELCOME  "+ Name.upper())
              Home_Page_user()
              window.destroy()
              
          else:
              messagebox.showerror(title="Error", message="Unathorised Access")


                  #Forgot Password
      def forgot_pass():


          def yo():
              query = 'select * from owner'
              cur.execute(query)
              result = cur.fetchall()

              temp_found1 = False

              if Verify_ID_entry.get() == '':
                   messagebox.showerror(title="INVALID INPUT", message=" BNO CANT BE EMPTY")
              else:

                  for i in result:
                      if Verify_ID_entry.get().isdigit():
                          if int(Verify_ID_entry.get()) == i[0]:
                              temp_found1 = True 
                              break
                      else:
                          messagebox.showerror(title="INVALID INPUT", message=" BNO MUST BE AN INT")
                  if temp_found1 != True:
                        messagebox.showerror(title="INVALID INPUT", message="A RECORD WITH THE GIVEN BNO DOES NOT EXIST")
                  else:
                      query = 'select * from owner'
                      cur.execute(query)
                      result = cur.fetchall()

                      temp_found2 = False

                      if Verify_Name_entry.get() == '':
                           messagebox.showerror(title="INVALID INPUT", message=" NAME CANT BE EMPTY")
                      else:

                          for i in result:
                              if Verify_Name_entry.get().isalpha():
                                  if str(Verify_Name_entry.get()) == i[1]:
                                      temp_found2 = True 
                                      break

                          if temp_found2 == True:
                              query = 'select * from credentials where Ow_ID = %s'
                              value = (int(Verify_ID_entry.get()),)
                              cur.execute(query,value)
                              result = cur.fetchall() 

                              for i in result:
                                  name = i[0]
                                  pas = i[1]

                              messagebox.showinfo(title="Forgot_Pass", message="Username => "+name+" \n\nPassword => "+pas)
                          else:
                              messagebox.showerror(title="Forgot_Pass", message="NAME DOES NOT MATCH OWNER NAME")

                              window.destroy()



          window = tk.Tk()
          window.title("Login Page")
          window.geometry('390x350+435+175')
          window.configure(bg='#30d5c8')
          window.resizable(False,False)

                      #IMAGE FOR LOGIN PAGE
          frame = tk.Frame(window, width=390, height=440, bg='#30d5c8')
          frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                            ##This is to place the frame of the image on the window2
          frame.place(x=0, y=0)

          global Verify_Name,Verify_Pass

          login_label = tk.Label(
              window, text="VERIFING CRED", bg='#30d5c8',borderwidth=3, fg="#FF3399", font=("Arial", 19))
          Verify_Name = tk.Label(
              window, text="Name", bg='#30d5c8', fg="#FF3399", font=("Arial", 18))
          Verify_Name_entry = tk.Entry(window, font=("Arial", 16))
          Verify_ID_entry = tk.Entry(window, font=("Arial", 16))
          Verify_ID = tk.Label(
              window, text="Ow_ID", bg='#30d5c8', fg="#FF3399", font=("Arial", 18))
          login_button = tk.Button(
              window, text="SUBMIT", bg="white", fg="#FF3399", font=("Arial", 16), command=yo)

          login_label.place(x=95, y=0)
          Verify_Name.place(x=45, y=100)
          Verify_Name_entry.place(x=125, y=100)
          Verify_ID.place(x=40, y=150)
          Verify_ID_entry.place(x=125, y=150)
          login_button.place(x=135, y=225)



      window_start.destroy()

      window = tk.Tk()
      window.title("Login Page")
      window.geometry('390x440+435+175')
      window.configure(bg='#333333')
      window.resizable(False,False)

                  #IMAGE FOR LOGIN PAGE
      frame = tk.Frame(window, width=390, height=440, bg='white')
      frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                        ##This is to place the frame of the image on the window2
      frame.place(x=0, y=0)

      global img
      img = PhotoImage(file='C:/Users/Rohit/Desktop/lovepik-apartment-building-png-image_401530275_wh1200.png', master=window)

                        # Create a Label Widget to display the text or Image
      label = tk.Label(frame, image=img)
      label.place(x=-250,y=-100)

      login_label = tk.Label(
          window, text="Login", bg='white', fg="#FF3399", font=("Arial", 30))
      username_label = tk.Label(
          window, text="Username", bg='white', fg="#FF3399", font=("Arial", 16))
      username_user_entry = tk.Entry(window, font=("Arial", 16))
      password_user_entry = tk.Entry(window, show="*", font=("Arial", 16))
      password_label = tk.Label(
          window, text="Password", bg='white', fg="#FF3399", font=("Arial", 16))
      login_button = tk.Button(
          window, text="Login", bg="white", fg="#FF3399", font=("Arial", 16), command=login_user)
      Forgot_Cred = tk.Button(
          window, text="Forgot password", bg="white", fg="#FF3399", font=("Arial", 10), command=forgot_pass)
      Forgot_Cred.place(x = 140,y = 275)



              # Placing Labels on the screen
      login_label.place(x=140, y=0)
      username_label.place(x=25, y=100)
      username_user_entry.place(x=125, y=100)
      password_label.place(x=25, y=150)
      password_user_entry.place(x=125, y=150)
      login_button.place(x=155, y=225)


  def First():

      global window_start


      window_start = tk.Tk()
      window_start.title("Login Page")
      window_start.geometry('950x500+250+150')
      window_start.configure(bg='#2F38F6')
      window_start.resizable(False,False)

                  #IMAGE FOR LOGIN PAGE
      frame = tk.Frame(window_start, width=1200, height=600, bg='white')
      frame.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
                        ##This is to place the frame of the image on the window2
      frame.place(x=0, y=0)

      global img1
      img1 = PhotoImage(file='C:/Users/Rohit/Desktop/Finance_a_home.png', master=window_start)

                        # Create a Label Widget to display the text or Image
      label = tk.Label(frame, image=img1)
      label.place(x=-50,y=-3)


      Adm_Button = tk.Button(window_start,
          text="  ADMIN   ", bg="#868BFF", fg="#FFFFFF", font=("Arial", 16),borderwidth=3,relief="raised", command=Admin)
      Adm_Button.place(x = 150 , y = 210)
      User_Button = tk.Button(window_start,
          text="   USER   ", bg="#868BFF", fg="#FFFFFF",borderwidth=3, relief="raised", font=("Arial", 16), command=User)
      User_Button.place(x = 150 , y = 275)


      window_start.mainloop()

  First()
