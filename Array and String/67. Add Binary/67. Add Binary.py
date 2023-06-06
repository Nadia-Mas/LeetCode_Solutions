class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #Approach01: Using In-built Function
        
        # sum = bin(int(a, 2) + int(b, 2))
        # return(sum[2:])
        
        
        #Approach02: Using lamda both time and space complexities are O(1)
        binary_sum = lambda a,b : bin(int(a, 2) + int(b, 2))
     
        
        return(binary_sum(a,b)[2:])