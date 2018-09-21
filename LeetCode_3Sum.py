class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        hashTable = {}
        returnOuterList = []
        
        
    
        if not nums or len(nums)<3:
            return []
        
        nums.sort()
        index_start = 0

        
        for index_start in range(len(nums)):
            index_mid = index_start + 1
            index_end = len(nums) - 1
            while index_mid < index_end:
                sumResult = nums[index_start] + nums[index_mid] + nums[index_end]
                
                if sumResult == 0:
                    returnInnerList = []
                    returnInnerList.append(nums[index_start])
                    returnInnerList.append(nums[index_mid])
                    returnInnerList.append(nums[index_end])
                    
                    if returnInnerList not in returnOuterList:
                        returnOuterList.append(returnInnerList)
                    index_mid += 1
                    index_end -= 1
                
                elif sumResult < 0:
                    index_mid += 1
                
                else:
                    index_end -= 1
        
        return returnOuterList
                  
