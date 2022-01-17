from turtle import Turtle

ALIGNMENT = "center"
FONT_SCORE = ("Consolas", 16, "bold")
FONT_GAME_OVER = ("Consolas", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 290)
        self.hideturtle()
        
        self.score = 0
        self.write_score()
        
    
    def write_score(self):
        self.clear()
        text_to_write = "Score: " + str(self.score)
        self.write(text_to_write, align=ALIGNMENT, font=FONT_SCORE)
        
        
    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        text_to_write = "GAME OVER"
        self.write(text_to_write, align=ALIGNMENT, font=FONT_GAME_OVER)
        
        
    def increment_score(self):
        self.score += 1
        self.write_score()