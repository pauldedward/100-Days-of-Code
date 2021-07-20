from turtle import Turtle

class Snake:
    def __init__(self):
        self.body = []
        for i in range (0,3):
            todd = Turtle()
            todd.penup()
            todd.color("white")
            todd.shape("square")
            todd.setx(20 - (i * 20))
            self.body.append(todd)
        self.head = self.body[0]
    
    def move(self, heading):
    
        head_heading = self.head.heading()
        if heading !=  head_heading and abs(heading - head_heading) != 180:
            self.head.setheading(heading)

        prev_x = self.head.xcor()
        prev_y = self.head.ycor()
        self.head.forward(20)
        
        for i in range(1, len(self.body)):
            current_x = self.body[i].xcor()
            current_y = self.body[i].ycor()
            self.body[i].goto(prev_x, prev_y)
            prev_x = current_x
            prev_y = current_y
