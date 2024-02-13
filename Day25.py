countries = ("spain" , "Italy", "India", "england", "Germany")

temp = list(countries)
temp.append("Russia")  #add item
temp.pop(3)            #remove item
temp[2] = "Finland"    #change item
countries= tuple(temp)
print(countries)

# If you want to add something in tuple
#Instead of amking it into list
#Make a new tuple and add them with previous tuple

country1= ("spain" , "Italy", "India")
country2= ("Albania", "Morocco")
europeAsia= country1 + country2
print(europeAsia)

# if you want to count something in tuple

tuple1= (0,2,1,0,3,5,0,1,4)
res= tuple1.count(1)
print('Count of 1 in tuple1 is:', res)

#if you want to see first appearance of a specific value in tuple

tuple1= (0,2,1,0,3,5,0,1,4)
res= tuple1.index(1)
print('First apearance of 1 in tuple1 is:', res)

#if you want to see specific limit

tuple1= (0,2,1,0,3,5,0,1,4)
res= tuple1.index(1, 3, 8,)
print('First apearance of 1 in tuple1 is:', res)