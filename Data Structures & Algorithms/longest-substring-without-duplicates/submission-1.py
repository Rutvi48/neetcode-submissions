class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        
        seen = set()
        start = 0

        for i in range(0,len(s)):
            if s[i] in seen:
                longest = max(longest, i-start)

                while start < i and s[start] != s[i]:
                    seen.remove(s[start])
                    start += 1
                
                start += 1

            seen.add(s[i])

        longest = max(longest, len(s)-start)

        return longest
                



