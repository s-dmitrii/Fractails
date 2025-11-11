import turtle as t

def frac_9(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        t.left(45)
        frac_9(length, depth - 1)
        t.right(90)
        frac_9(length, depth - 1)
        t.left(45)
