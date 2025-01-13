import datetime

current_time = datetime.datetime.now()

# print(current_time)

print(current_time.strftime("%m/%d/%y"))

print(current_time.strftime("%B, %e, %Y"))

print(current_time.strftime("%B, %e, %Y %I:%M %p"))