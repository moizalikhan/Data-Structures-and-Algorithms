# Level-1 Questions
# problem 1:
i = 1
while i <= 10:
    print(i)
    i +=1

# problem 2:
n = int(input("enter the number :" ))
i = 0
while i <= n:
    print(i)
    i= i+1

# problem 3:
n = int(input("enter a number starting point: "))
a = int(input("enter a number stoping point: "))
while n >=a:
    print(n)
    n -= 1

# problem 4:
number = 3
sum_of_num = 0
i = 0
while i<= number:
    sum_of_num +=i
    i +=1
print(sum_of_num)

# problem 5:
number = 3
sum_of_num = 0
i = 0
while i<= number:
    a = i*i
    sum_of_num += a
    i +=1
print(sum_of_num)

# problem 6:
num_1 = int(input("enter the number: "))
i = 0
while i <= num_1:
    if i % 2 == 0:
        print(i)
    i += 1

# problem 7:
num_1 = int(input("enter the number: "))
sum_of_even, i = 0,0
while i <= num_1:
    if i % 2 == 0:
        print(i)
        sum_of_even +=i
    i += 1
print(f"sum of the even numbers are: {sum_of_even}")

# problem 8:
num_1 = int(input("enter the number: "))
count,sum_of_even, i = 0,0,0
while count < num_1:
    if i % 2 == 0:
        print(i)
        sum_of_even +=i
        count += 1
    i += 1
print(f"sum of the even numbers are: {sum_of_even}")

# Level-2
# problem 9 Sum of digits of a given number:
num_1 = list(input("enter the number: "))
i = 0
sum_1 =0
for i in range(len(num_1)):
    sum_1 += int(num_1[i])
print(sum_1)
# OR
# problem 9 Sum of digits of a given number:
num_1 = input("enter the number: ")
sum_1 =0
for i in range(len(num_1)):
    sum_1 = sum_1 +int(num_1) % 10
    num_1 = int(num_1)// 10
print(sum_1)

# problem 10 Sum of square of digits of a given number:
num_1 = list(input("enter the number: "))
i = 0
sum_1 =0
for i in range(len(num_1)):
    sum_1 += int(num_1[i])*int(num_1[i])
print(sum_1)
# OR
# problem 9 Sum of digits of a given number:
num_1 = input("enter the number: ")
sum_1 =0
for i in range(len(num_1)):
    digit_1 = int(num_1) % 10
    sum_1 = sum_1 +(digit_1*digit_1)
    num_1 = int(num_1)// 10
print(sum_1)

# problem 11 a given number is armstrong or not:
num_1 = int(input("enter the no for armstrong or not?"))
original_no = num_1
i = 0
a = 0
armstrong_check = 0
while num_1>0:
    digit_1 = num_1 % 10
    cube_ofnum = digit_1**3
    armstrong_check += cube_ofnum
    num_1 = num_1//10
if armstrong_check == original_no:
    print("yes")
else:
    print("no")

# problem 12 a product of given num:
num_1 = 123
product = 1
while num_1 > 0:
    Digit_ = int(num_1) % 10
    product = product * Digit_
    num_1 = int(num_1) // 10
print(product)

# problem 13 sum of even and product of odd:
num_1 =  int(input("enter the no "))
sum_, prod_ = 0,1
while num_1>0:
    digit_ = num_1 % 10
    if digit_ % 2 == 0:
        sum_ += digit_
    else:
        prod_ *= digit_
    num_1 = num_1 // 10
print(f"sum : {sum_} and product: {prod_}")

# problem 13 reverse a number:
num_1 =  int(input("enter the no "))
while num_1>0:
    digit_ = num_1%10
    print(digit_, end='')
    num_1 = num_1//10

# problem 14 reverse a string:
string_1 =  input("enter the no ")
index = len(string_1)-1
reverse_ = ""
while index>=0:
    reverse_ += string_1[index]
    index -=1
print(reverse_)

# problem 15 palindrome a number:
num_1 =  int(input("enter the no "))
number_1=num_1
rev = 0
while num_1 > 0:
    digit_ = num_1 %10
    rev = rev*10 + digit_
    num_1 = num_1//10
if rev == number_1:
    print("yes")
else:
    print("no")
# OR 
string_1 = "tenet"
index = len(string_1) - 1
reverse =""
while index>=0:
    reverse += string_1[index]
    index -=1
if reverse == string_1:
    print("yes")
else:
    print("no")

# problem 16 prime number:
num_1 =  int(input("enter the no "))
i = 1
count = 0
while i <=num_1:
    if num_1%i==0:
       count += 1
    i +=1
if count == 2:
    print(f"{num_1} is prime no")

# problem 17 factorial of number:
num_1 = int(input("Enter the number: "))
i = 0
factorial_ = 1
while i<num_1:
    digit_ = num_1 -i
    factorial_ *= digit_
    i +=1
if num_1 == 0:
    print(1)
else:
    print(factorial_)

# problem 18 fibonacci series:
num_1 = int(input("Enter the number"))
a, b, c = 0,1,0
while c <= num_1:
    print(c)
    a = b
    b = c
    c = a+b

# problem 18 sum of elements of a list:
input_number = input("Enter an integer: ")
digit_list = list(input_number)
sum_of_list = 0
for i in digit_list:
    sum_of_list += int(i)
print("Sum of numbers:", sum_of_list)

# problem 18 sum of elements of a list:
input_number = list(input("Enter an integer: "))
odd_of_list = 0
even_of_list = 0
for i in input_number:
    if int(i) % 2 == 0:
        even_of_list +=1 
    else:
        odd_of_list +=1
print(even_of_list)
print(odd_of_list)

# problem 19 frequency of elements in a list:
input_number = list(input("Enter an integer: "))
element_count = {}
for element in input_number:
    if element in element_count:
        element_count[element] +=1
    else:
        element_count[element] = 1
for element in element_count:
    count = element_count[element]
    print(f"{element}: {count}")
