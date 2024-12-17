from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from menu import Menu
import time

# Dashed Line
def draw_dashed_line():
    line = Turtle()
    line.speed(0)
    line.color("white")
    line.penup()
    line.goto(0, 300)
    line.setheading(270)

    # Dash length and gap length
    dash_length = 15
    gap_length = 10

    for _ in range(50):
        line.pendown()
        line.forward(dash_length)
        line.penup()
        line.forward(gap_length)

    line.hideturtle()

# Start Game
def start_game():
    screen.clear()
    screen.bgcolor("black")
    screen.title("Pong Arcade Game by WLQ")
    screen.tracer(0)

    draw_dashed_line()

    paddle1 = Paddle(350)
    paddle2 = Paddle(-350)
    ball = Ball()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkeypress(paddle1.up, "Up")
    screen.onkeypress(paddle2.up, "w")
    screen.onkeypress(paddle1.down, "Down")
    screen.onkeypress(paddle2.down, "s")

    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with wall and bounce off
        if ball.ycor() > 260 or ball.ycor() < -260:
            ball.bounce_y()

        # Detect collision with paddle
        if (
            ball.xcor() > 335
            and ball.distance(paddle1) < 50
            and ball.x_move > 0
            or ball.xcor() < -335
            and ball.distance(paddle2) < 50
            and ball.x_move < 0
        ):
            ball.bounce_x()

        # Detect if paddle misses the ball and update score
        if ball.xcor() > 380:
            scoreboard.l_point()
            scoreboard.update_scoreboard()
            ball.reset()

        if ball.xcor() < -380:
            scoreboard.r_point()
            scoreboard.update_scoreboard()
            ball.reset()

        if scoreboard.l_score >= 5:
            game_is_on = False
            scoreboard.game_over(
                "Left Player", f"{scoreboard.l_score} - {scoreboard.r_score}"
            )
        elif scoreboard.r_score >= 5:
            game_is_on = False
            scoreboard.game_over(
                "Right Player", f"{scoreboard.l_score} - {scoreboard.r_score}"
            )

    # Return to the menu after the game ends
    show_main_menu()

# Instructions
def show_instructions():
    menu.show_instructions()
    screen.listen()
    screen.onkeypress(show_main_menu, "b")  # Go back to the main menu
    screen.onkeypress(exit_game, "e")  # Ensure exit works here too

# Exit Game
def exit_game():
    screen.clear()
    menu.writer.goto(0, 0)
    menu.writer.write("Thanks for playing!", align="center", font=("Courier", 18, "bold"))
    screen.update()  # Update the screen to show the message
    time.sleep(2)
    screen.bye()

# Show Main Menu
def show_main_menu():
    menu.show_main_menu()
    screen.listen()
    screen.onkeypress(start_game, "s")  # Bind start game
    screen.onkeypress(show_instructions, "i")  # Bind instructions
    screen.onkeypress(exit_game, "e")  # Bind exit game

# Main Screen Setup
screen = Screen()
screen.setup(width=800, height=580)
screen.title("Pong Arcade Game by WLQ")
menu = Menu(screen)

# Initialize with the Main Menu
show_main_menu()
screen.mainloop()
