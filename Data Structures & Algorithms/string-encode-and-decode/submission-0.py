class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            l = str(len(word))
            output += l + '#' + word
        
        return output



    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            num = int(s[i:j])
            i = j + 1
            j = i + num
            word = s[i:j]
            i = j 
            output.append(word)
        
        return output
                

