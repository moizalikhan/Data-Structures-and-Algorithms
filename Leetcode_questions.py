# Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

# sum of elemnts with target:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousmap = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in previousmap:
                return [previousmap[difference], i]
            previousmap[n] = i

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