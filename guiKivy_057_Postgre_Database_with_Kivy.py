from kivy.lang import Builder
from kivymd.app import MDApp
import psycopg2



class MainApp(MDApp):
    
    def build(self):
        self.theme_cls.theme_style= "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        conn = psycopg2.connect(
        host= "127.0.0.1",
        database= "postgresexemple",
        user= "postgres",
        password= "1234",
        port= "5432",
        
        )
        
        # create a cursor
        c = conn.cursor()
                
        # create table
        c.execute("""CREATE TABLE if not exists customersp
                  (
            name TEXT            
                    );   
            """)
        
        # check if ta   ble created
        # c.execute("SELECT * FROM customers")
        # print(c.description)
        
        # commit
        conn.commit()
        
        # # close conn
        conn.close()
        
        return Builder.load_file('kivy057.kv')
        
    def submit(self):
        
        conn = psycopg2.connect(
        host= "127.0.0.1",
        database= "postgresexemple",
        user= "postgres",
        password= "1234",
        port= "5432",
        
        )
        # create a cursor
        c = conn.cursor()
        
        # add a record
        sql_command = "INSERT INTO customersp (name) VALUES (%s)"
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
        
        conn = psycopg2.connect(
        host= "127.0.0.1",
        database= "postgresexemple",
        user= "postgres",
        password= "1234",
        port= "5432",
        
        )
        # create a cursor
        c = conn.cursor()
        
        # grab records from db
        c.execute("SELECT * FROM customersp")
        records = c.fetchall()
        
        word = ''
        
        # loop thru records
        for record in records:
            word = f'{word} \n{record[0]}'
            self.root.ids.word_label.text = f'{word}'
        
        # commit
        conn.commit()
        
        # close conn
        conn.close()

    
MainApp().run()