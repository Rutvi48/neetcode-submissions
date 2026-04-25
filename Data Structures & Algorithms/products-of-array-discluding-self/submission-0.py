class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        hadZero = False

        for num in nums:
            if num == 0 and not hadZero:
                hadZero = True
            else:
                product *= num

        productExceptSelf = []


        for num in nums:
            if num == 0:
                productExceptSelf.append(product)
            elif hadZero:
                productExceptSelf.append(0)
            else:
                productExceptSelf.append(product//num)

        return productExceptSelf
