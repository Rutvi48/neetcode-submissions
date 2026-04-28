class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1

        if len(nums) == 1 and nums[0] != target:
            return -1

        mid = len(nums)//2

        
            
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.search(nums[:mid], target)
        
        rightIndex = self.search(nums[mid+1:], target)
        if rightIndex != -1:
            return mid + rightIndex + 1

        return rightIndex
        