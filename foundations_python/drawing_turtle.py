import turtle

def draw_j(initials):
    initials.forward(200)
    initials.backward(100)
    initials.right(90)
    initials.forward(150)
    initials.right(90)
    initials.forward(70)
    initials.right(90)
    initials.forward(70)
    initials.backward(70)

def draw_o(initials):
    initials.right(90)
    initials.forward(200)

    for i in range(1,5):
        initials.left(90)
        initials.forward(60)

def draw_e(initials):
    initials.forward(200)
    initials.backward(100)
    initials.left(90)
    initials.forward(30)
    initials.right(90)
    initials.forward(100)
    initials.backward(100)
    initials.left(90)
    initials.foward(30)
    initials.right(90)
    initials.forward(100)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    initials = turtle.Turtle()
    initials.speed(1)
    draw_j(initials)
    draw_o(initials)
    draw_e(initials)

    window.exitonclick()

draw_art()
