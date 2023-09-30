# swiping the elements of an array
arr = [1,2,3,4,5]
i = 0
index1 = 0
index2 = 2
for i in arr:
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp 
print(arr)

# max elements of an array
arr = [1,2,3,4,5]
i = 0
max_element = 0
while i <len(arr):
    if max_element < arr[i]:
        max_element = arr[i]
    i +=1
print(max_element)

# reverse of an array
arr = [1,2,3,4,5]
left_pointer = 0
right_pointer = len(arr)-1
while left_pointer <= right_pointer:
    arr[left_pointer], arr[right_pointer] = arr[right_pointer],arr[left_pointer]
    left_pointer +=1
    right_pointer -=1
print(arr)