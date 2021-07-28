values = input().split(" ")

a, b, c = values

triangle = (float(a) * float(c)) / 2
circle = 3.14159 * (float(c) * float(c))
trapeze = ((float(a) + float(b)) * float(c)) / 2
square = float(b) * float(b)
rectangle = float(a) * float(b)

print('TRIANGULO: {}'.format('%.3f' % triangle))
print('CIRCULO: {}'.format('%.3f' % circle))
print('TRAPEZIO: {}'.format('%.3f' % trapeze))
print('QUADRADO: {}'.format('%.3f' % square))
print('RETANGULO: {}'.format('%.3f' % rectangle))