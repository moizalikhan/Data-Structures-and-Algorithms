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

# problem 9: