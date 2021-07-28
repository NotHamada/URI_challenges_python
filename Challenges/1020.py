value = int(input())
d = value
year = month = days = 0

if (d / 365) >= 1:
    year = int(d / 365)
    d -= year*365

if (d / 30) >= 1:
    month = int(d / 30)
    d -= month* 30

days = d

print('{} ano(s)'.format(year))
print('{} mes(es)'.format(month))
print('{} dia(s)'.format(days))