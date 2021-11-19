from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    title = "Tic Tac Toe!"
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        
        return Builder.load_file('kivy065.kv')
    
    #define who's turn it is
    turn = "X"
    
    # keep track of win or lose
    winner = False
    
    #keep track of winners and losers
    X_win = 0
    O_win = 0
    
    # no winner
    def no_winner(self):
        if self.winner == False and \
        self.root.ids.btn1.disabled == True and \
        self.root.ids.btn2.disabled == True and \
        self.root.ids.btn3.disabled == True and \
        self.root.ids.btn4.disabled == True and \
        self.root.ids.btn5.disabled == True and \
        self.root.ids.btn6.disabled == True and \
        self.root.ids.btn7.disabled == True and \
        self.root.ids.btn8.disabled == True and \
        self.root.ids.btn9.disabled == True :
            self.root.ids.score.text = "EGALITE !"
    
    # end game
    def end_game(self, a, b, c):
        self.winner = True
        a.color = "red"
        b.color = "red"
        c.color = "red"
        
        # disable btn
        self.disable_all_buttons()
        
        # set label for winner
        self.root.ids.score.text = f'{a.text} Wins!'
        
        #keep track of winners and losers
        if a.text == "X":
            self.X_win = self.X_win + 1
        else:
            self.O_win = self.O_win + 1
            
        self.root.ids.game.text = f'X Wins: {self.X_win} |  O Wins: {self.O_win} '
    
    def disable_all_buttons(self):
        #disable buttons
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True
    
    def win(self):
        # across
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn2.text == self.root.ids.btn3.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)
        if self.root.ids.btn4.text != "" and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn6.text:
            self.end_game(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)
        if self.root.ids.btn7.text != "" and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)
        
        # down
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn4.text == self.root.ids.btn7.text:
            self.end_game(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)
        if self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn8.text:
            self.end_game(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)
        if self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.text == self.root.ids.btn9.text:
            self.end_game(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)
          
        # diagonal
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn9.text:
                self.end_game(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)
        if self.root.ids.btn7.text != "" and self.root.ids.btn7.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn3.text:
            self.end_game(self.root.ids.btn7, self.root.ids.btn5, self.root.ids.btn3)
        
        
        self.no_winner()
    
    def presser(self, btn):
        if self.turn=='X':
            btn.text = "X"
            btn.disabled= True
            self.root.ids.score.text = "O's turn!"
            self.turn = 'O'
        else:
            btn.text = 'O'
            btn.disabled = True
            self.root.ids.score.text = "X's turn!"
            self.turn = 'X'
            
        self.win()
    
    def restart(self):
        #Reset Who's Turn it is
        self.turn = 'X'
        
        #enable buttons
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False
        
        #clear buttons
        self.root.ids.btn1.text = ""
        self.root.ids.btn2.text = ""
        self.root.ids.btn3.text = ""
        self.root.ids.btn4.text = ""
        self.root.ids.btn5.text = ""
        self.root.ids.btn6.text = ""
        self.root.ids.btn7.text = ""
        self.root.ids.btn8.text = ""
        self.root.ids.btn9.text = ""
        
        # reset button colors
        self.root.ids.btn1.color = "green"
        self.root.ids.btn2.color = "green"
        self.root.ids.btn3.color = "green"
        self.root.ids.btn4.color = "green"
        self.root.ids.btn5.color = "green"
        self.root.ids.btn6.color = "green"
        self.root.ids.btn7.color = "green"
        self.root.ids.btn8.color = "green"
        self.root.ids.btn9.color = "green"
        
        self.root.ids.score.text = "X GOES FIRST!"
        
        # reset the winner variable
        self.winner = False
        
MainApp().run()
 
