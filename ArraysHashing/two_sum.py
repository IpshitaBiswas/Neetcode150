from typing import List, Dict

# - Array of numbers
# - Find two that add to target
# - Return their indices
# - Can't use same element twice
# - Exactly one solution exists
# - Need efficient lookup

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in hashmap:
                return [hashmap[comp], i]
            hashmap[num] = i

# Test Cases
print(Solution().twoSum([2,7,11,15], 9))    # [0, 1]
print(Solution().twoSum([3,2,4], 6))        # [1, 2]
print(Solution().twoSum([3,3], 6))          # [0, 1]
print(Solution().twoSum([-1,-2,-3,-4], -6)) # [1, 3]
print(Solution().twoSum([0,4,3,0], 0))      # [0, 3]


# LEARNED:
# - Time: O(n) - single pass through array
# - Space: O(n) - hashmap storage
# - Trade space for time efficiency
# - Hashmap provides O(1) lookups
# - enumerate() for index tracking
# - Works with negative numbers
# - Handles duplicate values correctly
# - Edge case: same element can't be used twice
# - Guaranteed solution exists (no error handling needed)
