class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        high = 0
        l = 0
        charSet = set()

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[i])
            high = max(high, i - l + 1)

        return high          

