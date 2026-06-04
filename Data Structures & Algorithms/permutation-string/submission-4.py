class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        occur = defaultdict(int)

        for c in s1:
            occur[c] += 1

        
        curr = 0

        while curr + len(s1) <= len(s2):
            print(curr)
            if s2[curr] in occur:
                freq = defaultdict(int)
                checkfreq = True
                for i in range(len(s1)):
                    if s2[curr+i] not in occur:
                        curr += i
                        checkfreq = False
                        break
                    freq[s2[curr+i]] += 1

                if checkfreq: 
                    isPerm = True
                    for key,val in occur.items():
                        if freq[key] != val:
                            isPerm = False
                            break
                    if isPerm:
                        return True
            curr += 1

        return False
                            
                    
        