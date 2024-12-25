from math import sin, cos, tan, radians
a = float(input('Digite o angiulo em º'))
r = radians(a)
s = sin(r)
c = cos(r)
t = tan(r)
print (f'O resultado é:\n sen = {s:.2f}\n cos = {c:.2f}\n tan = {t:.2f}')