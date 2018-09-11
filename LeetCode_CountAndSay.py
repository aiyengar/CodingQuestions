class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # each string is basically formed by the count of each unique character in prev string plus the character
        # For eg. n = 4 is formed from n = 3 representation 
        # 3 represented as 2 1
        # here 2 occurs only once so countOfChar=1 and Char=2 so becomes 1 2, similarly now moving to next char in string
        # 1 occurs only once so countOfChar = 1 and Char = 2 so becomes 1 1 and the string is now 1 2 1 1.
        if n == 0:
            return ''
        
        if n == 1:
            return '1'
        
        countDict = {}
        countDict[1] = '1'
        
        for index in range (2,n+1):
            countDict[index] = ''
            prevString = countDict[index - 1]
            count = 0
            inner_index = 0
            temp = ''
            
            while inner_index < len(prevString):
                currChar = prevString[inner_index]
                
                while inner_index < len(prevString) and currChar == prevString[inner_index]:
                    count += 1
                    inner_index +=1
                
                temp = temp + str(count) + currChar
                count = 0 
            countDict[index] = temp    
        
        return countDict[n]
