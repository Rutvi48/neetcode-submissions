class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charS = defaultdict(int)

        for char in s:
            charS[char] += 1

        
        charT = defaultdict(int)

        for char in t:
            charT[char] += 1

    
        for key in charS.keys():
            if charS[key] != charT[key]:
                return False

        return True
