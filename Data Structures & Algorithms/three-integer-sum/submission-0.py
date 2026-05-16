class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()

        length= len(nums)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(temp))

        return [list(i) for i in res]

        