class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mainCount = [0] * 26

        for i in range(len(s1)):
            mainCount[ord(s1[i]) - ord('a')] += 1

        for i in range(len(s2) - len(s1) + 1):
            count = [0] * 26

            for j in range(len(s1)):
                count[ord(s2[i + j]) - ord('a')] += 1

            if count == mainCount:
                return True

        return False
        