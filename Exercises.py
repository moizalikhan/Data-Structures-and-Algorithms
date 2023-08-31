
num_1, num_2 ,num_3 = input("Gave me 3 numbers: ").split(",")
average = (int(num_1)+int(num_2)+int(num_3))/3  
print(average)

name = input("enter your name : ")
print(name[::-1])

name, character = input("Enter name and character: ").split(",")
print(f"length of the character is {len(name)}")
print(f"Character Count is : {name.count(character)}")