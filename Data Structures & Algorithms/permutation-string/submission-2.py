class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
            
        mainCount = [0] * 26
        count = [0] * 26
        for i in range(len(s1)):
            mainCount[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] += 1

        r = len(s1) - 1
        l = 0

        while r < len(s2):
            if count == mainCount:
                return True 
            count[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1   
            if r < len(s2):
                count[ord(s2[r]) - ord('a')] += 1
     

        return False
        