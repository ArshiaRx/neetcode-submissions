class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Initialize length and adjust array size
        n = len(nums)                #  Input [1,   2, 4,  6]
        result = [1] * n             #        [1,   1, 1,  1]
                                     #        [28, 24, 12, 8]

        # loop through left
        for e in range(1, n):
            result[e] = result[e-1] * nums[e-1]

        # loop through right and multiply
        right_product = 1
        for e in range(n-1, -1, -1):
            result[e] = result[e] * right_product
            right_product = right_product * nums[e]

        return result


            
        

               