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