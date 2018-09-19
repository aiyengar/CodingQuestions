class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        returnList = []
        
        if not nums:
            return []
        
        hashSumIndexTable = {}
        
        for index in range(len(nums)):
            if target - nums[index] in hashSumIndexTable:
                returnList.append(hashSumIndexTable[(target -nums[index])])
                returnList.append(index)
                return returnList
                
            hashSumIndexTable[nums[index]] = index
            
        return returnList
        
