# Function => remove redandency
# User define function

# def sum (num1, num2):
#     print(num1 + num2)

# sum(3,5)

# def cal_gst(price):
#     new_price = price + price * 0.18
#     return new_price

# print(cal_gst(100))

# in-built Function 

# print("hello") # actually a function 
# len min max type  



# Module function -> collection of related functions 

# eg  math   
# import math
# print(dir(math))

# from math import sqrt , log2 # not complete module just one function of math module

# print(sqrt(16))
# print(log2(16)) # for finding the power to get 16 from power

# import random 
# print(random.random()) # 0 and in between 1
# print (random.randint(1,10)) # from 1 to 10

# Exercise 6

# write a function (WAF) to check if a number is odd or even 

# num = int(input("Enter the number: "))

# def func (num):
#     if num % 2 == 0:
#         return "Even number"
#     else:
#         return "Odd number"

# print(func(num))
    
# WAF to count the number of vowels in a string 


# def func (str):
#     count = 0
#     for char in str:
#         if char.lower() in "aeiou":
#             count += 1 
#     return count

# str = input("Enter your string: ")

# result = func(str)
# print("Number of vowels:", result)

# WAF to print if a number is prime or not 
# def check_prime(num):
#     if num <= 1:
#         print(num, "is not a prime number")

#     for i in range (2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             return
        
#     print(num , "is a prime number")

# number = int(input("Enter a number: "))

# check_prime(number)

# WAF to return the average marks if a list of marks is passed as parameter: 

# def average_marks(marks):
#     total = sum(marks)
#     average = total / len(marks)
#     return average

# marks = [83, 88, 90, 85, 80, 81]

# avg = average_marks(marks)
# print("Average Marks =", avg)