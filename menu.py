from turtle import Screen, Turtle

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.writer = Turtle()
        self.writer.color("white")
        self.writer.penup()
        self.writer.hideturtle()

    def show_main_menu(self):
        self.screen.clear()
        self.writer.clear()
        self.screen.bgcolor("black")
        self.writer.goto(0, 100)
        self.writer.write("PONG ARCADE GAME", align="center", font=("Courier", 24, "bold"))
        self.writer.goto(0, 50)
        self.writer.write("Press 'S' to Start", align="center", font=("Courier", 18, "normal"))
        self.writer.goto(0, 20)
        self.writer.write("Press 'I' for Instructions", align="center", font=("Courier", 18, "normal"))
        self.writer.goto(0, -10)
        self.writer.write("Press 'E' to Exit", align="center", font=("Courier", 18, "normal"))

    def show_instructions(self):
        self.writer.clear()
        self.screen.clear()
        self.screen.bgcolor("black")
        self.writer.goto(0, 50)
        self.writer.write("Instructions:", align="center", font=("Courier", 18, "bold"))
        self.writer.goto(0, 20)
        self.writer.write("Player 1 (Right Paddle): Up Arrow, Down Arrow", align="center", font=("Courier", 14, "normal"))
        self.writer.goto(0, -10)
        self.writer.write("Player 2 (Left Paddle): W, S", align="center", font=("Courier", 14, "normal"))
        self.writer.goto(0, -50)
        self.writer.write("Press 'B' to go back to the menu", align="center", font=("Courier", 14, "normal"))
