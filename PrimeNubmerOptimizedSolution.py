# This one has less comparisons
num_1 = int(input("Enter the Number: "))
i = 1
factors = 0
while i <=(num_1**0.5):
    if num_1 % i == 0:
       factors += 1
    i += 1
if factors>1:
    print("Not Prime")
else:
    print("Prime")