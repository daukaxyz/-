from math import sqrt, pi, log10, atan, ceil

def f(s):
    if abs(s)<3:
        print(abs(ceil((s/5) - 3)))
    elif 3<=abs(s)<=4:
        print(log10(sqrt(pi) + abs(s/4)))
    else:
        print(atan(s/3) + (1/((2*s) - 9)))
f(s=float(input()))

    # vtoroe
halfOfSide = 8
side = 16
Ax_center = 3
Ay_center = 4
Bx_center = -1
By_center = -4
radius1 = 4
radius2 = 10
x = float(input())
y = float(input())

A = False
if (Ax_center - halfOfSide) < x and x < (Ax_center + halfOfSide) and (Ay_center - halfOfSide) < y and y < (Ay_center + halfOfSide):
    A = True
else:
    A = False
B = False
distanceFromCenter = ((Bx_center - x)**2) + ((By_center - y)**2)
if radius1 <= sqrt(distanceFromCenter) <= radius2:
    B = True
else:
    B = False
C = False
if A and B:
    C = True
else:
    C = False