import turtle as t

def frac_1(distance):
    for i in range(4):
        t.forward(distance)
        t.right(90)

    t.right(10)
    t.up()
    t.forward(distance * 0.1)
    t.down()
    distance *= 0.9
    frac_1(distance)