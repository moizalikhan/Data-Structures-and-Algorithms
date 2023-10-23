# Problem 1:
# Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# Problem 2:
# sum of elemnts with target:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousmap = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in previousmap:
                return [previousmap[difference], i]
            previousmap[n] = i

# Problem 3:
# is palindrome by two pointers:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s)-1
        while l<r:
            while l < r and not self.alpnum(s[l]):
                l = l+1                
            while r>l and not self.alpnum(s[r]):
                r = r-1
            if s[l].lower() != s[r].lower():
                return False
            l , r = l+1, r-1
        return True
    def alpnum(self, c):
        return (ord("A") <= ord(c) <=ord("Z")or
        (ord("a") <= ord(c) <=ord("z"))or 
        (ord("0") <= ord(c) <=ord("9")))

# Problem 4:
# when to buy and sell a stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        Maxprofit = 0
        while r < len(prices):
            if prices[l]<prices[r]:
                profit = prices[r]-prices[l]
                Maxprofit = max(profit,Maxprofit)
            else:
                l = r
            r += 1
        return Maxprofit

# Problem 5:
# Array rotation
def rotateLeft(d, arr):
    # Write your code here
    rotations = (d % len(arr))+1
    reversed_arr =arr[rotations:] + arr[:rotations]
    return reversed_arr
arr = [1,2,3,4,5,6,7]
d  = 3
print(f"{rotateLeft(d,arr)} is the rotated one")

# Problem 6:
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

# Problem 7:
# max elements of an array
arr = [1,2,3,4,5]
i = 0
max_element = 0
while i <len(arr):
    if max_element < arr[i]:
        max_element = arr[i]
    i +=1
print(max_element)

# Problem 8:
# reverse of an array
arr = [1,2,3,4,5]
left_pointer = 0
right_pointer = len(arr)-1
while left_pointer <= right_pointer:
    arr[left_pointer], arr[right_pointer] = arr[right_pointer],arr[left_pointer]
    left_pointer +=1
    right_pointer -=1
print(arr)

# Problem 9:
# Contains not Duplicate in a sorted array
arr = [1,1,2,2,3,4,4,5,5]
l, r = 0,1
while l < len(arr) and r < len(arr):
    if arr[l] != arr[r]:
        one_time = arr[l]
        print(one_time)
        break
    l= l + 2
    r= r + 2

# Problem 10:
# Top K Frequent Elements
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}
        bucket_sort = [[] for i in range(len(nums)+1)]
        
        for n in nums:
            track[n] = 1+ track.get(n,0)
        for n, count in track.items():
            bucket_sort[count].append(n)

        result = []
        for i in range(len(bucket_sort)-1,0,-1):
            for n in bucket_sort[i]:
                result.append(n)
                if len(result) == k:
                    return result

# Problem 11:
#  longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_set = set()
        l = 0
        result = 0
        for r in range(len(s)):
            while s[r] in c_set:
                c_set.remove(s[l])
                l += 1
            c_set.add(s[r])
            result = max(result,r-l+1)
        return result

# Problem 13:
#  longest substring without repeating characters.