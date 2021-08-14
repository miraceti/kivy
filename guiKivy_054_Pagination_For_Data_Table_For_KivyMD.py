from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class MainApp(MDApp):
    
    def build(self):
        
        #define screen
        screen = Screen()
        
        #define table
        table = MDDataTable(
            pos_hint = {'center_x':0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.6),
            check = True,
            use_pagination = True,
            rows_num = 3,
            pagination_menu_height =  '240dp',
            pagination_menu_pos = "auto",#do not work
            background_color = [1,0,0,.5], #do not work
            column_data = [
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email Adress", dp(30)),
                ("Phone number", dp(30))
                
            ],
            
            row_data = [
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345"),
                ("Jhon", "elder1","jhon1@codemy.com","12312"),
                ("john", "elder2","jho2n@codemy.com","12323"),
                ("Jhonny", "elder3","jhon3@codemy.com","12354"),
                ("Johnny", "elder4","jhon4@codemy.com","12345")
                       
                
            ]
            
            
            
        )
        
        #bind table
        table.bind(on_check_press = self.checked)
        table.bind(on_row_press =  self.row_checked)
        
        self.theme_cls.theme_style= "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # return Builder.load_file('kivy053.kv')
        
        #add table widget to screen
        screen.add_widget(table)
        
        
        
        return screen
    
    #fonction for check presses
    def checked(self, instance_table, current_row):
        print(instance_table, current_row)
    
    #fonction for row presses
    def row_checked(self, instance_table, instance_row):
        print(instance_table, instance_row )
    
MainApp().run()