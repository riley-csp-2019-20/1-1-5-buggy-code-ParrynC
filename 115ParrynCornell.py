#   a115_buggy_image.py
import turtle as trtl

dot = trtl.Turtle()
drawer = trtl.Turtle()
dot.pensize(40)
dot.circle(20)

# making the spider
legs = 8
length = 110
legSpacing = 360/ legs
dot.pensize(10)
drawer.pencolor("black")
count = 0

# other calculations for creating the spider
while (count < legs):
  dot.goto(0,20)
  dot.setheading(legSpacing*count)
  dot.forward(length)
  count = count + 1
dot.hideturtle()

# Eyes of the spider
drawer.pencolor("crimson")
drawer.pensize(5)
drawer.right(-80)
drawer.circle(10)

drawer.pencolor("crimson")
drawer.pensize(5)
drawer.right(160)
drawer.circle(10)

spaceline = trtl.Screen()
spaceline.mainloop()