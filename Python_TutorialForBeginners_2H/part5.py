# List => mutable matlb change able 

# marks = [90, 80, 70, 60, 50,'A', 92.5]

# print(marks, type(marks))

# length  
# print(len(marks))
# index
# print(marks[-3])
# slicing a list

# print(marks[0:3])
# print(marks[-3: -1])
# print(marks[-2:])
# print(marks[:5])

# for score in marks:
#     print(score)

# Mutable => we can change the value of list once it is created. we can add, remove, update the value of list.
# marks = [90, 80, 70, 60, 50]
# marks.append(99)
# print(marks)
# marks.pop()
# print(marks) 

# marks.remove(70)
# print(marks, len(marks))
# marks.insert(2, 75)
# print(marks, len(marks))


# print(70 in marks) 
# marks.clear()
# print(marks, len(marks))





# Tuple => immutable means we can not change the value of tuple once it is created. just we can applay operations on it and create new tuple.orignal tuple will remain same.

# marks = (90, 80, 70, 60, 50,80, 90, 80, 70, 60, 50)
# print(marks, type(marks))

# print(marks[2])

# print(marks.index(80))
# print(marks.count(80))

# marks1 = marks + (100, 110, 120)
# print(marks1, type(marks1))



# Set => unique items 

# marks = {98,97, 95,80,98,95,80 }
# print(len(marks),marks) # 4

# for score in marks:
#     print(score)




# Dictionary  word => meaning {key => val}

# marks = {"Math": 99, "physics": 97, "Chemistry":98, "urdu":88}

# print(marks, type(marks))
# print(marks['physics'])
# marks["physics"] = 92
# marks['English'] = 85
# print(marks['physics'])
# print(marks['English'])

# for key in marks: 
#     print(key, marks[key])

# Exercise 5: 
# Given a list of roll number [101, 105, 102, 101, 108, 105, 110]. print all unique roll nums in the list.

# marks =  [101, 105, 102, 101, 108, 105, 110]

# unique_num = set(marks)
# print(unique_num)

# mathod 2: 

# unique_num = []
# for num in marks:
#     if num not in unique_num:
#         unique_num.append(num)
# print(unique_num)


# Given Employee records in the form of a list of tuples where each tuples contains:
# (Employee ID, Employee Name, Salary)

# Example [
#     (101, 'Alice', 50000),
#     (102, 'Bob', 55000),
#     (103, 'Charlie', 60000),
    
# ]
# ask user to enter Employyee ID & search it inside records 

# employees = [
#     (101, 'Alice', 50000),
#     (102, 'Bob', 55000),
#     (103, 'Charlie', 60000),
# ]
# search_id = int(input("Enter Employ ID: "))
# found = False

# for employee in employees:
#     if employee[0] == search_id:
#         print("Employee Found!")
#         print("ID:", employee[0])
#         print("Name:", employee[1])
#         print("Salary:", employee[2])
#         found = True
#         break

# # If not found 
# if found == False:
#     print("Employee not found.")