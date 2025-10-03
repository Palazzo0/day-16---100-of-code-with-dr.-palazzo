from turtle import Turtle
POSITIONS = [(0, 0),(-5, 0), (-10, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_squares = []
        self.create_snake()
        self.head = self.all_squares[0]

    def create_snake(self):
        for square in POSITIONS:
            self.add_square(square)

    def add_square(self, square):
       each_square = Turtle("square")
       each_square.color("white")
       each_square.penup()
       each_square.goto(square)
       self.all_squares.append(each_square)

    def extend_snake(self):
        self.add_square(self.all_squares[-1].position())

    def reset_pos(self):
        for s in self.all_squares:
            s.goto(1000,1000)
        self.all_squares.clear()
        self.create_snake()
        self.head = self.all_squares[0]





    def move(self):
        for sq_num in range(len(self.all_squares) - 1, 0, -1):
            new_x_pos = self.all_squares[sq_num - 1].xcor()
            new_y_pos = self.all_squares[sq_num - 1].ycor()
            self.all_squares[sq_num].goto(new_x_pos, new_y_pos)
        self.head.forward(DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)