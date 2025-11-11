import turtle as t

def frac_7(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        new_len = length / 2
        frac_7(new_len, depth - 1)
        t.left(90)
        frac_7(new_len / 2, depth - 1)
        t.right(180)
        frac_7(new_len / 2, depth - 1)
        t.left(90)
        frac_7(new_len, depth - 1)