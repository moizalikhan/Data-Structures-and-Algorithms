# Problem 1:
# num_1, num_2 ,num_3 = input("Gave me 3 numbers: ").split(",")
# average = (int(num_1)+int(num_2)+int(num_3))/3  
# print(average)

# Problem 2:
# name = input("enter your name : ")
# print(name[::-1])

# Problem 3:
# name, character = input("Enter name and character: ").split(",")
# print(f"length of the character is {len(name)}")
# print(f"Character Count is : {name.lower().count(character.lower())}")

# Problem 4:
# import random
# b = random.randint(0,9)
# print(b)
# a = int(input("give me a number:"))
# if a == b:
#     print("you won")
# if a > b:
#     print("too high")
# else:
#     print("too low")

# Problem 5:
# name = input("name:")
# age = int(input("Age:"))
# if name[0].lower() == "a" and age > 10:
#     print("you can watch Coco Movie")
# else:
#     print("sorry, you cannot watch Coco")

# Problem 6:
# number = int(input("Enter a number for sum: :"))
# i = 1
# total = 0 
# while i <=number: 
#     total= total + i
#     i = i+1
# print(total)

# problem 7:
# number = input("Enter a Number: ")
# total = 0
# i = 0
# while i <len(number):
#     total = total + int(number[i])
#     i = i + 1
# print(total)

# Problem 8:
# name = input("Enter your name :")
# i = 0
# temp = ""
# while i < len(name):
#     if name[i] not in temp:
#         print(f"{name[i]} : {name.count(name[i])}")
#         temp = name[i]
#     i = i+1

# Problem 9:
# Problem 4 extension:
# import random
# b = random.randint(0,10)
# guess_game = False
# i = 0
# while not guess_game:
#     a = int(input("give me a number:"))
#     if a == b:
#         i = i+1
#         print(f"you won, you guessed in {i} times")
#         continue
#     if a > b:
#         i = i+1
#         print("too high")
#         continue
#     if a < b :
#         i = i+1
#         print("too low")
#         continue

# # problem 10:
# def is_even(x):
#     return x%2==0

# problem 11:
# def Greater(x,y):
#     if x>y:
#         return x 
#     return y
# a,b = input("enter: ").split(" ")
# print(Greater(a,b))

# problem 12:
# def Greater(x,y,z):
#     if x>y and x>z:
#         return x
#     if y>x and y>z:
#         return x 
#     return z
# a,b,c = input("enter: ").split(" ")
# print(Greater(a,b,c))

# Problem 13:
# def is_palindrome(string):
#     new_string = ""
#     count = len(string)
#     while count>0:
#             new_string = new_string + string[count - 1]
#             count = count - 1
#     return string == new_string
# name = input("enter the name:")
# print(is_palindrome(name))

# Problem 14:
# def Fibonacci_series(num):
#     a,b = 0,1  
#     i = 1
#     print(a,end = " ")
#     print(b,end = " ")
#     while i <= int(num)-2:
#         c = a+b
#         print(c,end = " ")
#         a = b
#         b = c
#         i += 1
# x= input("Enter a number: ")
# Fibonacci_series(x)

# Problem 15:
# 
# 
# 
# 
# 