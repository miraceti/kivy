from kivy.lang import Builder
from kivymd.app import MDApp
# import sqlite3
import mysql.connector

class MainApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        # create db
        # conn = sqlite3.connect('first_db.db')
        
        # define database stuf
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "1234",
            database = "second_db",
        )
        
        # create a cursor
        # c = conn.cursor()
        c = conn.cursor()
        
        # create an actual database
        c.execute("CREATE DATABASE If NOT EXISTS second_db")
        
        #  check see if database was created
        c.execute("SHOw DATABASES")
        for db in c:
            print(db)
        
        # create table
        c.execute("""CREATE TABLE if not exists customers(
            name VARCHAR(50)            
            )   
            """)
        
        # check if ta   ble created
        c.execute("SELECT * FROM customers")
        print(c.description)
        
        # commit
        # conn.commit()
        
        # # close conn
        conn.close()
        
        return Builder.load_file('kivy056.kv')
        
    def submit(self):
         # create db
        # conn = sqlite3.connect('first_db.db')
        # define database stuf
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "1234",
            database = "second_db",
        )
        
        # create a cursor
        c = conn.cursor()
        
        # add a record
        sql_command = "INSERT INTO customers (name) VALUES (%s)"
        values = (self.root.ids.word_input.text, )
        
        # execute sql
        c.execute(sql_command, values)
        
        # c.execute(" INSERT INTO customers VALUES (:first)", 
        #           {
        #               'first': self.root.ids.word_input.text,
        #           }
        #           )
        # add message
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} added'
        
        # clear input box
        self.root.ids.word_input.text =""
        
                
        # commit
        conn.commit()
        
        # close conn
        conn.close()
    
    def show_records(self):
         # create db
        # conn = sqlite3.connect('first_db.db')
        # define database stuf
        conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "1234",
            database = "second_db",
        )
        
        # create a cursor
        c = conn.cursor()
        
        # grab records from db
        c.execute("SELECT * FROM customers")
        records = c.fetchall()
        
        word = ''
        
        # loop thru records
        for record in records:
            word = f'{word} \n{record[0]}'
            self.root.ids.word_label.text = f'{word}'
        
        # commit
        # conn.commit()
        
        # close conn
        conn.close()

    
MainApp().run()