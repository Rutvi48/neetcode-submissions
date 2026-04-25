class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        longest = 0

        for i in nums:
            length = 1
            if i-1 not in elements:
                nextElement = i+1
                while nextElement in elements:
                    length += 1
                    nextElement += 1
            longest = max(longest, length)

        return longest
            
                

            

         

