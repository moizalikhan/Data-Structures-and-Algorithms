# Array rotation
def rotateLeft(d, arr):
    # Write your code here
    rotations = d % len(arr)
    reversed_arr =arr[rotations:] + arr[:rotations]
    return reversed_arr
arr = [1,2,3,4,5]
d  = 1
print(f"{rotateLeft(d,arr)} is the rotated one")