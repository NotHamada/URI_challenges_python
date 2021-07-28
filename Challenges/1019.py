time = int(input())
secs = time
hours = minutes = seconds = 0

if (secs / 3600) >= 1:
    hours = int(secs / 3600)
    secs -= hours * 3600
if (secs / 60) >= 1:
    minutes = int(secs / 60)
    secs -= minutes * 60

seconds = secs

print('{}:{}:{}'.format(hours, minutes, seconds))