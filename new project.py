import tkinter as tk
from tkinter import messagebox,PhotoImage
from PIL import ImageTk,Image
import mysql.connector as ms

con = ms.connect(host='localhost',user='root',password='123456')

### these are for the slider label
y = "WELCOME TO APT MANAGMENT SYSTEM"
count = 0
text = ""




if con.is_connected():
  cur = con.cursor()
  query1 = "create database if not exists project"
  cur.execute(query1)
  query2 = "use project"
  cur.execute(query2)
  query3 = "create table if not exists apt(BNO INT PRIMARY KEY,BHK INT,Square_Feet int,Vacancy CHAR(15),Price INT,check(Price >= 1000000 and Price <= 9999999 and Square_Feet >= 800 and Square_Feet <= 1600))"
  cur.execute(query3)
  query4 = "create table if not exists owner(Ow_ID INT NOT NULL PRIMARY KEY,Name char(15),Phone_No char(10),BNO INT,CONSTRAINT FOREIGN KEY (BNO) REFERENCES apt(BNO) ON DELETE CASCADE ON UPDATE CASCADE);"
  cur.execute(query4)
  con.commit()
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

                query1 = "select vacancy from apt where BNO = %s;"
                values1 = (int(apt_entry1.get()),)
                cur.execute(query1,values1)
                result1 = cur.fetchone()              
                if result1[0].lower() == 'vacant':
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
                    if apt_entry1.get().isdigit():
                        if apt_entry2.get().isdigit() and len(str(apt_entry2.get())) == 10:
                            if apt_entry3.get().isdigit():
                                if apt_entry5.get().isalpha() or str(apt_entry5.get()) == '':
                                    if Vacancy == [-1]:

                                        query2 = "insert into owner(Ow_ID,Phone_No,BNO) values(%s,%s,%s)"
                                        values = (int(apt_entry1.get()),str(apt_entry2.get()),int(apt_entry3.get()))
                                        cur.execute(query2,values)
                                        con.commit()

                                        if str(apt_entry5.get()) == '':
                                            messagebox.showinfo(title="RECORD ADDED", message="You successfully added a record.")
                                        else:
                                            messagebox.showinfo(title="RECORD ADDED BUT...", message="Can't Have an owner for a VACANT APT")

                                    else:
                                        if str(apt_entry5.get()) == '':
                                            messagebox.showinfo(title="INVALID INPUT", message="MUST HAVE AN OWNER FOR A OWNED APT")
                                        else:
                                            query1 = "insert into owner values(%s, %s, %s,%s)"
                                            values = (int(apt_entry1.get()),str(apt_entry5.get()),str(apt_entry2.get()), int(apt_entry3.get()))
                                            cur.execute(query1, values)
                                            con.commit()

                                            messagebox.showerror(title="RECORD ADDED", message="You successfully added a record.")
                                       
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
                values1 = (int(apt_entry3.get()),)
                cur.execute(query1,values1)
                result1 = cur.fetchone()
                print(result1[0].lower() + 'hello')
                if result1[0].lower() == 'vacant':

                    Vacancy = [-1]

                query = "SELECT * FROM owner"
                cur.execute(query)
                result = cur.fetchall()
                found = False
                for i in result:
                    if apt_entry3.get().isdigit():
                        if int(apt_entry3.get()) == i[3]:
                            found = True                      
                if found == False:
                    messagebox.showerror(title="INVALID INPUT", message="A record with the given BNO does not exists")
                else:            
                    if apt_entry1.get().isdigit():
                          if apt_entry2.get().isdigit():
                              if apt_entry3.get().isdigit():
                                  if apt_entry5.get().isalpha() or str(apt_entry5.get()) == '':
                                      if Vacancy == [-1]:

                                          query2 = "update owner set Ow_ID = %s,Phone_NO = %s  where BNO = &s"
                                          values = (int(apt_entry1.get()),int(apt_entry2.get()), int(apt_entry3.get()))
                                          cur.execute(query2,values)
                                          con.commit()

                                          if str(apt_entry5.get()) == '':
                                              messagebox.showinfo(title="RECORD ADDED", message="You successfully added a record.")
                                          else:
                                              messagebox.showinfo(title="RECORD ADDED BUT...", message="Can't Have an owner for a VACANT APT")

                                      else:
                                      
                                          query1 = "update owner set Ow_ID = %s,Name = %s,Phone_NO = %s where BNO = &s"
                                          values = (int(apt_entry1.get()),str(apt_entry5.get()),int(apt_entry2.get()), int(apt_entry3.get()))
                                          cur.execute(query1, values)
                                          con.commit()

                                          messagebox.showinfo(title="RECORD ADDED", message="You successfully added a record.")
                                     
                                  else:
                                      messagebox.showerror(title="INVALID INPUT", message="NAME MUST A STRING")
                              else:
                                  messagebox.showerror(title="INVALID INPUT", message="BNO MUST BE AN INTEGER")
                          else:
                              messagebox.showerror(title="INVALID INPUT", message="PHONE NO MUST BE AN INTEGER")
                    else:
                          messagebox.showerror(title="INVALID INPUT", message="Ow_ID MUST BE AN INTEGER")



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
            
            frame2 = tk.Frame(window2, width=420, height=410, bg='white')
            frame2.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
            frame2.place(x=375, y=180)

                          ###QUERY TO VIEW THE TABLE CONTENTS
            query = "SELECT * FROM owner"
            cur.execute(query)
            result = cur.fetchall()
            t = "{:<15}{:<15}{:<25}{:<15}"
            s = t.format('Ow_ID','Name','Phone_No', 'BNO')
            t2 = "{:<15}{:<15}{:<25}{:<15}"
            s2 =''
            for i in result:
              if i[1] == 'None' : 
                  s2 += t2.format(str(i[0]),'NULL', str(i[2]), str(i[3]))+ '\n' + '\n'
              else:
                  s2 += t2.format(str(i[0]),str(i[1]), str(i[2]), str(i[3]))+ '\n' + '\n'

            view_label1 = tk.Label(frame2,
             text='TABLE   :    OWNER', bg='white',width=45, fg="#FF3399",borderwidth=1, relief="solid", font=("Arial", 16))
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
                      ## THE MAIN BUTTONS
        apt_button1 = tk.Button(window2,
          text="ADD", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=ADD1)
        apt_button1.place(x = 260 , y = 280)
        
        apt_button2 = tk.Button(window2,
          text="UPDATE", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=update1)
        apt_button2.place(x = 250 , y =330)
        
        apt_button3 = tk.Button(window2,
          text="DELETE", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=delete1)
        apt_button3.place(x = 250 , y = 380)
        
        apt_button4 = tk.Button(window2,
          text="VIEW", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=VIEW1)
        apt_button4.place(x = 260 , y = 430)

    def event():
      pass
    def Amenities():
      pass
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
        text="EVENTS", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=event)
    event_button.place(x = 50 , y = 350)
    Owner_button = tk.Button(window2,
        text="OWNER", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=owner)
    Owner_button.place(x = 50 , y = 280)
    Amenities_but = tk.Button(window2,
      text="Amenities", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=Amenities)
    Amenities_but.place(x = 50 , y = 415)
    clear = tk.Button(window2,
      text="CLEAR", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=clear_table)
    clear.place(x = 50 , y = 480)
    Exit_Button = tk.Button(window2,
      text="Exit", bg="#FF3399", fg="#FFFFFF",borderwidth=3, relief="raised", font=("Arial", 16), command=window2.destroy)
    Exit_Button.place(x = 800 , y = 550)



          #Button to HOME PAGE
  def login():
      username = "a"
      password = "a"
     
      if username_entry.get()==username and password_entry.get()==password:
          messagebox.showinfo(title="Login Success", message="You successfully logged in.")
          Home_Page()
          window.destroy()
          
      else:
          messagebox.showerror(title="Error", message="Unathorised Access")


              #Forgot Password
  def forgot_pass():
    messagebox.showinfo(title="Forgot_Pass", message="Username => Jagath \n\nPassword => 123456")

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
  username_entry = tk.Entry(window,fg="#FF3399", font=("Arial", 16))
  password_entry = tk.Entry(window, show="*", font=("Arial", 16))
  password_entry.bind('<Return>', lambda event: login())
  password_label = tk.Label(
      window, text="Password", bg='white', fg="#FF3399", font=("Arial", 16))
  login_button = tk.Button(
      window, text="Login", bg="white", fg="#FF3399", font=("Arial", 16), command=login)
  Forgot_Cred = tk.Button(
      window, text="Forgot password", bg="white", fg="#FF3399", font=("Arial", 10), command=forgot_pass)
  Forgot_Cred.place(x = 140,y = 275)





          # Placing Labels on the screen
  login_label.place(x=140, y=0)
  username_label.place(x=25, y=100)
  username_entry.place(x=125, y=100)
  password_label.place(x=25, y=150)
  password_entry.place(x=125, y=150)
  login_button.place(x=155, y=225)


  window.mainloop()

