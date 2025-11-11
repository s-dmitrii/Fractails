import turtle as t


def frac_4(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        frac_4(length / 3, depth - 1)
        t.left(60)
        frac_4(length / 3, depth - 1)
        t.right(120)
        frac_4(length / 3, depth - 1)
        t.left(60)
        frac_4(length / 3, depth - 1)