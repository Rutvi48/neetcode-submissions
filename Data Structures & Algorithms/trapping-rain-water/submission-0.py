class Solution:
    def trap(self, height: List[int]) -> int:
        reversePrefix = []
        currMax = -math.inf

        for h in height[::-1]:
            currMax = max(currMax, h)
            reversePrefix.insert(0,currMax)

        currMax = height[0]

        area = 0

        for i in range(1, len(height)-1):
            area += max(min(currMax, reversePrefix[i+1]) - height[i], 0)
            currMax = max(currMax, height[i])

        return area


