import turtle as t

def frac_8(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        new_len = length / 2
        frac_8(new_len, depth - 1)
        t.left(120)
        frac_8(new_len / 2, depth - 1)
        t.left(180)
        frac_8(new_len / 2, depth - 1)
        t.left(120)
        frac_8(new_len / 2, depth - 1)
        t.left(180)
        frac_8(new_len / 2, depth - 1)
        t.left(120)
        frac_8(new_len, depth - 1)