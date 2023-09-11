import time

timestamp= time.strftime('%H:%M:%S')
print(timestamp)
timestamp= time.strftime('%H')
print(timestamp)
timestamp= time.strftime('%M')
print(timestamp)
timestamp= time.strftime('%S')
print(timestamp)




print("Please Enter 24 hour Format Time")
t=int(input("Enter the exact time :"))
if(t>5 and t<12):
    print("Good Morning Sir")
elif(t>12 and t<16):
    print("Good Noon sir")
elif(t>16 and t<19):
    print("Good evening Sir")
else:
    print("Good Night Sir")
