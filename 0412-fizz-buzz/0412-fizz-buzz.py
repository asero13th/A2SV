class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #n = 7
        #1 2 3 4 5 6 7
        #arr = ["1", "2","Fizz", "4", "Buzz", "Fizz", "7", . . .. ."FizzBuzz"]
        arr = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                arr.append("FizzBuzz")
                
            elif i % 3 == 0:
                arr.append("Fizz")
            
            elif  i % 5 == 0:
                arr.append("Buzz")
            
            else:
                arr.append(str(i))
            
        return arr