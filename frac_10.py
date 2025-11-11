import turtle as t

def frac_10(corner, distance):
    t.forward(distance)
    t.right(corner)
    distance *= 1.001
    corner *= 0.99
    frac_10(corner, distance)
