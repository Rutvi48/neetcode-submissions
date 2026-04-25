class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        freqToChar = defaultdict(list)

        maxFreq = -1
        for c in freq:
            freqToChar[freq[c]].append(c)
            maxFreq = max(maxFreq, freq[c])

        freqKeys = list(freqToChar.keys())

        topK = []

        for i in range(maxFreq,0,-1):
            for e in freqToChar[i]:
                topK.append(e)
                if len(topK) == k:
                    return topK



       