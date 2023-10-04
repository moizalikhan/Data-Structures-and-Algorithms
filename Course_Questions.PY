# # problem 1:
number= list((input("enter")))
target = 3
i = 0
minimum = int(number[0])
for i in range(len(number)-1):
    if int(number[i])<minimum:
        minimum = int(number[i])
    i +=1
print(minimum)

# # problem 2:
number= [
    [2,8,3],
    [3,4,5],
    [6,7,8]
]
minimum = number[0][0]
for i in number:
    for j in i:
        if j <minimum:
            minimum = j
print(minimum)

# # problem 3:
number= [1,22,333,4444,55555,666666]
count_ofintegers = 0
for i in number:
    count = 0
    while i>0:
        i = i//10
        count +=1
    if count%2==0:
        count_ofintegers += 1
print(count_ofintegers)
# # or
strings= ['a','bb','ccc','dddd','eeeee','ffffff']
count_ofintegers = 0
for i in strings:
    length = len(i)
    if length%2==0:
        count_ofintegers += 1
print(count_ofintegers)

# # problem 4:
number = 123456789
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10
print(reversed_number)
# # or
string = "abcdefghi"
reversed_string = ""
index = len(string) - 1  # Start from the last character
while index >= 0:
    reversed_string += string[index]
    index -= 1
print(reversed_string)