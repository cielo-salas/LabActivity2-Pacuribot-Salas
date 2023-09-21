# Prompts the user to enter a name

name1 = str(input(" Enter Full Name: "))

id1 = str(input(" Enter id#: "))

course1 = str(input(" Enter Course: "))

section1 = str(input(" Enter Section: "))


# Prompt the user to enter three numbers

number1 = eval(input(" Enter 1st Grade: "))

number2 = eval(input(" Enter 2nd Grade: "))

number3 = eval(input(" Enter 3rd Grade: "))

number4 = eval(input(" Enter 4th Grade; "))

# Compute the average of four numbers

average = (number1 + number2 + number3 + number4) / 4

# Display result

print(" The average of ", number1, number2, number3, number4, "is", average)

# This prints the user's grade average, grades, name, id#, course, section
print(name1)
print(id1)
print(course1)
print(section1)

print(number1)
print(number2)
print(number3)
print(number4)
print(average)
