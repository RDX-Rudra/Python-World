import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
print(hour)
name = input("Enter your name: ")
if(hour>0 and hour<12):
    print("Good Morning ", name)
elif(hour>=12 and hour<17):
    print("Good Afternoon ", name)
else:
    print("Good Evening ", name)