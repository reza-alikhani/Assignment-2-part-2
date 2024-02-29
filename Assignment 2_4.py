timeInterval = "1:00:00"
list = timeInterval.split(':')
hours = list[0]
minutes = list[1]
seconds = list[2]
total = (int(hours) * 3600 + int(minutes) * 60 + int(seconds))
print("total = ", total)
