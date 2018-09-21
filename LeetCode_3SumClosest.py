class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return None
        
        nums.sort()
        positiveClosest = float("inf")
        negativeClosest = (float("-inf"))
        
        
        for index in range(len(nums)):
            indexStart = index + 1
            indexEnd = len(nums) - 1

            while indexStart < indexEnd:
                temp = nums[index] + nums[indexStart] + nums[indexEnd]
               
                if  temp > target:
                    indexEnd -= 1
                    if temp < positiveClosest:
                        positiveClosest = temp

                elif temp < target:
                    indexStart += 1
                    if temp > negativeClosest:
                        negativeClosest = temp

                else:
                    return target
                
        if (positiveClosest - target) > (target-negativeClosest):
            return negativeClosest
       
        else:
            return positiveClosest
            
