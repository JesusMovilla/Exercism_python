def equilateral(sides):
    x = sides[0]
    y = sides[1]
    z = sides[2]
    if x == 0 and y == 0 and z == 0:
        return False
    if (x+y) < z or (x+z) < y or (y+z) < x:
        return False
    if x == y and x == z and y == z:
        return True
    else:
        return False


def isosceles(sides):
    x = sides[0]
    y = sides[1]
    z = sides[2]
    if x == 0 and y == 0 and z == 0:
        return False
    if (x+y) < z or (x+z) < y or (y+z) < x:
        return False
    if x == y or z == y or x == z:
        return True
    else:
        return False


def scalene(sides):
    x = sides[0]
    y = sides[1]
    z = sides[2]
    if x == 0 and y == 0 and z == 0:
        return False
    if (x+y) < z or (x+z) < y or (y+z) < x:
        return False
    if x != y and x != z and y != z:
        return True
    else:
        return False
