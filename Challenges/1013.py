valor = input().split(" ")

a, b, c = valor

maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print('{} eh o maior'.format('%.1i' % resultado))