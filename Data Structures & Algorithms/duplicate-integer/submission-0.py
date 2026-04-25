class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existsBefore = set()

        for num in nums:
            if num in existsBefore:
                return True

            existsBefore.add(num)
    
        return False
