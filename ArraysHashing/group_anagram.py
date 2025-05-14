from typing import List, DefaultDict, Tuple
from collections import defaultdict

# - List of strings
# - Group anagrams together
# - Anagrams: same chars, different order
# - Need efficient grouping key
# - Case sensitive? (assume lowercase)
# - Empty strings?

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)
        for word in strs:
            arr = [0]*26
            for char in word:
                arr[ord(char)- ord('a')] +=1
            grp[tuple(arr)].append(word)
        return list(grp.values())

# Test Cases
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [["eat","tea","ate"],["tan","nat"],["bat"]]

print(Solution().groupAnagrams([""]))
# [[""]]

print(Solution().groupAnagrams(["a"]))
# [["a"]]

print(Solution().groupAnagrams(["abc", "cba", "bac", "xyz", "zyx"]))
# [["abc","cba","bac"],["xyz","zyx"]]

print(Solution().groupAnagrams(["listen", "silent", "hello", "world"]))
# [["listen","silent"],["hello"],["world"]]

# LEARNED:
# - Time: O(n*k) - n words, k avg length
# - Space: O(n*k) - storage of all strings
# - Character count tuple as effective hash key
# - defaultdict simplifies group creation
# - ord() for ASCII value conversion
# - tuple() makes list hashable for dict key
# - Handles empty strings naturally
# - Preserves original string cases
# - More efficient than sorting each string
# - Works for Unicode with larger array