from turtle import Turtle, xcor
STEP_SIZE = 20


class Snake:

    def __init__(self):

        self.body = []
        for i in range(0, 10):
            todd = Turtle()
            todd.penup()
            todd.color("white")
            todd.shape("square")
            todd.setx(STEP_SIZE - (i * STEP_SIZE))
            self.body.append(todd)

        self.head = self.body[0]

    def move(self, heading):

        head_heading = self.head.heading()
        if heading != head_heading and abs(heading - head_heading) != 180:
            self.head.setheading(heading)

        prev_x = self.head.xcor()
        prev_y = self.head.ycor()
        self.head.forward(STEP_SIZE)

        for i in range(1, len(self.body)):
            current_x = self.body[i].xcor()
            current_y = self.body[i].ycor()
            self.body[i].goto(prev_x, prev_y)
            prev_x = current_x
            prev_y = current_y
            
            
    def grow(self, direction):
        
        x_offset = 0
        y_offset = 0
        
        if direction == 0:
            x_offset = -STEP_SIZE
        elif direction == 180:
            x_offset = STEP_SIZE
        elif direction == 90:
            y_offset = STEP_SIZE
        elif direction == 270:
            y_offset = -STEP_SIZE
        
        x_pos = self.body[-1].xcor() + x_offset
        y_pos = self.body[-1].ycor() + y_offset
        
        todd = Turtle()
        todd.penup()
        todd.color("white")
        todd.shape("square")
        todd.goto(x_pos, y_pos)
        self.body.append(todd)
        
    def check_bitself(self):
        for i in range(1, len(self.body)):
            if self.head.xcor() == self.body[i].xcor() and self.head.ycor() == self.body[i].ycor():
                print("Game Over")
                return True
        return False
