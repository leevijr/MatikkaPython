import numpy


print(numpy.degrees(2.493))
print(numpy.degrees(0.911))

print(numpy.radians(137.7))
print(numpy.radians(62.3))

lista=[]
for x in (30, 45, 60, 90, 120, 135, 150, 180, 270, 360):
    lista.append(numpy.radians(x))
print(lista)

print(numpy.hypot(1.6, 2.3))

print(6.4*numpy.sin(numpy.arctan(1.5)), 6.4*numpy.cos(numpy.arctan(1.5)))