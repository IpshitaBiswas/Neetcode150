from typing import List

# - Array is sorted but rotated at an unknown pivot
# - No duplicates (simpler case)
# - Return index of target or -1 if not found
# - Must be O(log n) time complexity
# - Edge cases: empty array, single element, target at pivot

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

print(Solution().search([4,5,6,7,0,1,2], 0))  # 4 (target at pivot)
print(Solution().search([4,5,6,7,0,1,2], 3))  # -1 (not found)
print(Solution().search([1], 0))  # -1 (single element)
print(Solution().search([], 5))  # -1 (empty array)
print(Solution().search([6,7,8,1,2,3,4,5], 8))  # 2 (target in left sorted half)
print(Solution().search([6,7,8,1,2,3,4,5], 4))  # 6 (target in right sorted half)

# LEARNED:
# - Key insight: One half of the array is always sorted
# - Check which half is sorted first (nums[left] <= nums[mid])
# - Then check if target is within the sorted half's bounds
# - Time: O(log n) - binary search
# - Space: O(1) - no extra data structures
# - Edge cases matter: empty/single-element arrays, target at pivot
# - Alternative approach: Find pivot first, then binary search (but less efficient)
# - Python's // operator floors the division (critical for mid calculation)
# - Loop condition (left <= right) ensures we check all possibilities