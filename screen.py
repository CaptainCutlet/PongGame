from turtle import Turtle

class MainScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.score_1 = 0
        self.score_2 = 0
        self.show_score()

    # def draw_middle_line(self):
    #     self.speed("fastest")
    #     self.pensize(5)
    #     self.hideturtle()
    #     self.pencolor("white")
    #     self.penup()
    #     self.goto(0, 400)
    #     self.setheading(270)
    #     for _ in range(16):
    #         self.pendown()
    #         self.forward(35)
    #         self.penup()
    #         self.forward(15)

    def add_to_left(self):
        self.score_1 += 1
        self.show_score()

    def add_to_right(self):
        self.score_2 += 1
        self.show_score()

    def show_score(self):
        print(self.score_1)
        # self.draw_middle_line()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-80, 330)
        self.pendown()
        self.write(self.score_1, move=False, align="left", font=("Arial", 30, "bold"))
        self.penup()
        self.goto(60, 330)
        self.write(self.score_2, move=False, align="left", font=("Arial", 30, "bold"))
