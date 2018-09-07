class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCodeList = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
                         "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dictWordsAndMorseCode = {}
        
        for word in words:
            morse = ''
            for char in word:
                morse += morseCodeList[ord(char) - ord('a')]
            
            if word not in dictWordsAndMorseCode:
                dictWordsAndMorseCode[word] = morse
        
        listWords = list(set(dictWordsAndMorseCode.values()))
        return len(listWords)
