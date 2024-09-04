# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        mapped_char = set()
        for i in range(len(s)):
            char = s[i]
            if char not in dic:
                if t[i] in mapped_char:
                    return False  # If t[i] is already mapped by another character
                dic[char] = t[i]
                mapped_char.add(t[i])
            elif dic[char] != t[i]:
                return False  # If current mapping doesn't match, return False
        return True

def longestConsecutive(self, nums: List[int]) -> int:
    max_len = 0
    nums_set = set()
    for i in range(len(nums)):
        ele = nums[i]
        if ele - 1 in nums_set:
            continue
        length = 1
        while ele + 1 in nums_set:
            length += 1
            ele = ele + 1
        max_len = max(max_len, length)
    return max_len
