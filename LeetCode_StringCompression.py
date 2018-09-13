class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        
        if len(chars) == 1:
            return 1
        
        startpoint = 0
        traversepoint = 0
        
        while startpoint < len(chars):
            print(startpoint)
            charCur = chars[startpoint]
            countChar = 0 
            traversepoint = startpoint
            
            while traversepoint < len(chars) and charCur == chars[traversepoint]:
                countChar += 1
                traversepoint +=1
            
            startpoint += 1
            if countChar > 1:
                stringCount = str(countChar)
                
                for char in stringCount:
                    chars[startpoint] = char
                    startpoint += 1
                
                del chars[startpoint:traversepoint]
            
        return len(chars)
