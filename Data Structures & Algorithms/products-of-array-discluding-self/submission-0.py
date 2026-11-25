class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        i = 0
        product = 1
        output[0] = 1

        for j in range(len(nums)):
            product = nums[j] * product
            if (j + 1) < len(nums):
                output[j + 1] = product


        postproduct = nums[len(nums) - 1]

        for j in range(len(nums) - 2, -1, -1):
            if j >= 0:
                output[j] = postproduct * output[j]
                postproduct = nums[j] * postproduct
            
        
        return output

        
