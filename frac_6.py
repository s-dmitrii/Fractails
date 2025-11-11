import turtle as t


def frac_6(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        l = length / 4
        frac_6(l, depth - 1)
        t.left(90)
        frac_6(l, depth - 1)
        t.right(90)
        frac_6(l, depth - 1)
        t.right(90)
        frac_6(l, depth - 1)
        frac_6(l, depth - 1)
        t.left(90)
        frac_6(l, depth - 1)
        t.left(90)
        frac_6(l, depth - 1)
        t.right(90)
        frac_6(l, depth - 1)