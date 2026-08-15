# Range 0 to range   range(5) => [0,1,2,3,4]

# range (start=0, stop=5, step=1)  => [0,1,2,3,4]

# nums = range(5)
# print(nums)

# nums1 = range (1, 6)
# print(nums1)



# LOOPS => any iterable object can be looped over using for loop and while loop

# while loop
# count = 1

# while count <= 5:
#     print(count * '*')
#     count += 1 

# i = 5

# while i > 0:
#     print(i * '*')
#     i -= 1

# for loop

# num = range(5)

# for i in range(1, 5001):
#     print(i)

# for i in range(1,11):
#     if i % 2 == 0:
#         print(i, "is even")
#     else:
#         print(i, "is odd")

# for i in range (2, 11 , 2):
#     print(i)

# break & continue 

# i want to print all the multiples  of 3 =>  [1 to 30]  but stop at 21



# for i in range(1, 31):
#     if i ==21: 
#         break

#     if(i % 3 == 0): 
#         print(i)

# for i in range(1, 31):
#     if i ==21: 
#         continue

#     if(i % 3 == 0): 
#         print(i)

# Exercise: 4 
# print all odd numbers from 1 to 20 

# for i in range(1, 21):
#     if i % 2 != 0:
#         print(i)

# print the table of 57 

# num = 57

# for i in range (1,11):
#     print (num, "x", i, '=', num*i)

# print all multiples of 3 from 1 to 50 but skip 15

# for i in range(1,51):
#     if i == 15:
#         continue
#     if i % 3 == 0:
#         print(i)

# take two integer a and b as input 
# Find and print the first number between 1 and 1000 that is divisible by both numbers.

# a = int(input ("Enter 1st number: "))
# b = int(input ("Enter 2nd number: "))

# for i in range (1, 1001):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break