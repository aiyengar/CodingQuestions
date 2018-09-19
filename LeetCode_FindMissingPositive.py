class Solution:
    def shiftArray(self,nums):
        indexStart = 0
        indexShift = 0
        
        while indexStart < len(nums):
            if nums[indexStart] <=0:
                temp = nums[indexShift]
                nums[indexShift] = nums[indexStart]
                nums[indexStart] = temp
                indexShift +=1
            indexStart += 1
        
        return indexShift
        
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        indexShift = self.shiftArray(nums)
        nums = nums[indexShift:]
        
        for index in range(len(nums)):
            if (abs(nums[index]) - 1 < len(nums) ) and (nums[abs(nums[index]) - 1] > 0):
                nums[abs(nums[index]) - 1] = -nums[abs(nums[index]) - 1]
        
        for index in range(len(nums)):
            if nums[index] > 0:
                return index+1
                
        return(len(nums) + 1)
        
            
