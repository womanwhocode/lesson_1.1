from geom2d.point import *

l1 = [Point(0, 0), Point(1, 2), Point(2, 1)]


l = [Point(i, i*i) for i in range(-5, 6)]
l = list(map(lambda i: Point(i, i*i), range(-5, 6)))
l2 = list(filter(lambda p: p.x > 0, l))



print(l2)
