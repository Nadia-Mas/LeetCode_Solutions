class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result=[]
        for i in range(1,n+1):
            devisibleBy3= (i%3==0)
            devisibleBy5= (i%5==0)

            if (devisibleBy3 and devisibleBy5):
                result.append("FizzBuzz")
            elif(devisibleBy3):
                result.append("Fizz")
            elif(devisibleBy5):
                result.append("Buzz")
            else:
                result.append(str(i))
        return result