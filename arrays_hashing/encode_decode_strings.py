from typing import List

# - Encode list of strings to single string
# - Decode back to original list
# - Handle special characters
# - Need length information
# - Choose proper delimiter
# - Empty strings case

class Solution:
    def encode(self, strs: List[str]) -> str:
        delimiter = '#'
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + delimiter + s
        return encoded_str

    def decode(self, encoded_str: str) -> List[str]:
        decoded_str = []
        i = 0 
        while (i < len(encoded_str)):
            j = i
            while(encoded_str[j] != '#'):
                j += 1
            str_len = int(encoded_str[i:j])
            decoded_str.append(encoded_str[j+1 : j + 1 + str_len])
            i = j + 1 + str_len
        return decoded_str

# Test Cases
sol = Solution()

# Normal case
encoded = sol.encode(["hello","world","leetcode"])
print(encoded)  # "5#hello5#world8#leetcode"
print(sol.decode(encoded))  # ["hello","world","leetcode"]

# Empty strings case
encoded = sol.encode(["","",""])
print(encoded)  # "0##0##0#"
print(sol.decode(encoded))  # ["","",""]

# Special characters case
encoded = sol.encode(["#hello#","wor#ld","leet###code"])
print(encoded)  # "7##hello#6#wor#ld9#leet###code"
print(sol.decode(encoded))  # ["#hello#","wor#ld","leet###code"]

# Mixed case
encoded = sol.encode(["a","bc","def","ghij"])
print(encoded)  # "1#a2#bc3#def4#ghij"
print(sol.decode(encoded))  # ["a","bc","def","ghij"]

# LEARNED:
# - Time: O(n) both encode/decode
# - Space: O(n) for encoded string
# - Length prefix crucial for decoding
# - Delimiter choice important
# - Handles empty strings correctly
# - Works with special characters
# - Robust against embedded delimiters
# - Simple but effective serialization
# - No escaping needed due to length prefix
# - Decoding requires careful pointer management