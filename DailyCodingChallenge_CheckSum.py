#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17, #Google

def checkSum(inputList,k):
    
    if not inputList:
        return False
    
    for element in inputList:
        if (k - element) in inputList:
            return True
    
    return False

print(checkSum([10,15,3,7],17))
print(checkSum([10,10,30,3],80))
print(checkSum([],70))
