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