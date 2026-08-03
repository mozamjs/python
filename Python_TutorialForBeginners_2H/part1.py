# putputo
print("hello world--!")

# variable and data types
name = "shradha" #string
age = 27         #integer
cgpa = 9.6       #float
isStudent = True #boolean

# print(name, age) 
print(type(name))
print(type(age))
print(type(cgpa))
print(type(isStudent))

# Userinput

# name = input("Enter your name: ")

print("Welcome",name)
print("Welcome " + name) #concatenation

# Exercise 1: 

first_name = input("Enter your first name: ")
last_name = input("Enter your last name:")
age = input("Enter your age: ")
height = input("Enter your height:")
superhero = input("Enter your superhero name: ")

print(first_name+last_name +" is a " + superhero + ". whos age is " + age + " and height is " + height)
print(f"{first_name} {last_name} is a {superhero}. whos age is {age} and height is {height}")