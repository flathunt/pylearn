from math import pi, tan, cos

g = 9.81
y = 1
x = 0.5
thd = 80
v = 44

thr = thd * (pi/180)

h = y + (x * tan(thr)) - ((g * x**2) / (2 * (v * cos(thr))**2))

print(h)