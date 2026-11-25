class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        re = defaultdict(list)

        for word in strs:
            count = 26 * [0]
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            re[tuple(count)].append(word)
        
        return list(re.values())
        