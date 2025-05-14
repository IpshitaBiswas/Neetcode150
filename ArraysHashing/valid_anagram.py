from typing import Dict

# - Two strings
# - Check if same characters, same counts
# - Length check first
# - Character frequency counts
# - Edge cases: empty strings, unicode, different lengths

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        for char in s:
            char_count[char] = char_count.get(char,0)+1
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        return (all(count==0 for count in char_count.values()))

# Test Cases
print(Solution().isAnagram("anagram", "nagaram"))  # True
print(Solution().isAnagram("rat", "car"))          # False
print(Solution().isAnagram("", ""))                # True
print(Solution().isAnagram("a", "a"))              # True
print(Solution().isAnagram("a", "b"))              # False
print(Solution().isAnagram("ab", "a"))             # False

# LEARNED:
# - Time: O(n) - two passes through strings
# - Space: O(1) - fixed size dict (for ASCII)
# - Alternative: sorted strings O(n log n) time
# - Edge cases: empty strings, single char
# - Early length check optimization
# - all() is clean for checking zero counts
# - Unicode handling would need larger dict
# - get() with default handles missing keys