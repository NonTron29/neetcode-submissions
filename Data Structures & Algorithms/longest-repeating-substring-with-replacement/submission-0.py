class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = 0

        for target in set(s):
            left = 0
            count = 0

            for right in range(len(s)):
                if s[right] != target:
                    count += 1

                while count > k:
                    if s[left] != target:
                        count -= 1

                    left += 1

                m = max(m, right - left + 1)

        return m