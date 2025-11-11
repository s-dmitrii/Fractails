import turtle as t
from frac_1 import frac_1
from frac_2 import frac_2
from frac_4 import frac_4
from frac_6 import frac_6
from frac_7 import frac_7
from frac_8 import frac_8
from frac_9 import frac_9
from frac_10 import frac_10


def turtle():
    t.speed(8)
    t.screensize(2500, 2500)

number = int(input("Enter the number of frac: "))

if number == 1:
    turtle()
    frac_1(150)
elif number == 2:
    corner = int(input("Enter the corner: "))
    height = int(input("Enter the height: "))
    turtle()
    t.lt(90)
    frac_2(100, corner, height)
elif number == 4:
    depth = int(input("Enter the depth: "))
    turtle()
    frac_4(600, depth)
elif number == 5:
    depth = int(input("Enter the depth: "))
    turtle()
    for i in range(3):
        frac_4(300, depth)
        t.rt(120)
elif number == 6:
    depth = int(input("Enter the depth: "))
    turtle()
    frac_6(750, depth)
elif number == 7:
    depth = int(input("Enter the depth: "))
    turtle()
    frac_7(700, depth)
elif number == 8:
    depth = int(input("Enter the depth: "))
    turtle()
    frac_8(700, depth)
elif number == 9:
    depth = int(input("Enter the depth: "))
    turtle()
    frac_9(10, depth)
elif number == 10:
    turtle()
    frac_10(90, 50)
else:
    exit("Error")

t.done()