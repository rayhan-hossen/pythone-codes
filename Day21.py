l = [3,5,6]
print(l)
print(type(l))

marks = [3,5,6, "NayanTara" , True]
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])

print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

if "NayanTara" in marks:
    print("true")

else:
    print("False")


if "Tara" in "NayanTara":
    print("Yes")

lst = [ i*i for i in range(5)]
print(lst)


lst = [ i*i for i in range(10) if i%2==0]
print(lst)