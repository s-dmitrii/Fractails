import turtle as t


def frac_2(distance,corner, height):
    if height == 0:
        return
    t.forward(distance)
    t.right(corner)
    frac_2(distance * 0.75, corner, height - 1)
    t.left(corner * 2)
    frac_2(distance * 0.75, corner, height - 1)
    t.right(corner)
    t.back(distance)
