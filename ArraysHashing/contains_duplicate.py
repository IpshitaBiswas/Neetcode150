from typing import List

# - Array of numbers
# - Any duplicates?
# - Return true/false
# - Can use set to check length
# - Edge cases: empty array, single element

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

print(Solution().containsDuplicate([1, 2, 3, 1]))  # True
print(Solution().containsDuplicate([1, 2, 3, 4]))  # False
print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
print(Solution().containsDuplicate([]))  # False
print(Solution().containsDuplicate([1]))  # False

# LEARNED:
# - Time: O(n) - set conversion is O(n)
# - Space: O(n) - worst case stores all elements
# - Alternative: sorting would be O(n log n) time, O(1) space
# - Python sets are hash-based, average O(1) lookups
# - Edge cases matter: empty/single-element arrays
# - len() is O(1) operation in Python
# - Simpler solution often better than premature optimization