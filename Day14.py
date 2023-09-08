a = int(input("Enter you age "))
print("Your age is", a)

# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# The space after if con is Indentetional Pyhton
if(a>18):
    print("You can drive")#Its indentation
else:
    print("You cannot Drive")
print("Yes, its not indentation")

applePrice = 250
myWallet = 230

if(applePrice <= myWallet ):
    print("Jarvis, Add Apple to Cart")
else:
    print("Jarvis, Lets Move")

applePrice = 10
myWallet = 200

if(myWallet - applePrice > 50 ):
    print("Jarvis, Add Apple to Cart")
elif (myWallet - applePrice > 70):
    print("Ok, buy it")
else:
    print("Jarvis, Lets Move")

num = int(input("enter the value of number:"))

if(num<0):
    print("Your number is negative")
elif(num==0):
    print("You number is 0")
elif(num==999):
    print("You number is special")
else:
    print("Your number is positive")

print("Nested if else")

num =18

if(num<0):
    print("Number is negative")

elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 10 and 20")
    else:
        print("Number is greater than 20")
else:
    print("number is 0")
