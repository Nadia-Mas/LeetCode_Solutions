class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.split()
        i , j = 0 , len(s)-1
        
        #this:
        while i<j:
            s[i], s[j] = s[j], s[i]
            i +=1
            j -=1
            
        #or:
        #s.reverse()
            
        return(" ".join(s))