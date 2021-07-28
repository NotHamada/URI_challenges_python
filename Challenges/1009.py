name = str(input())
s_fixed = float(input())
sold = float(input())

salary = s_fixed + (sold * 0.15)

print('TOTAL = R$ {}'.format('%.2f' % salary))