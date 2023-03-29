class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n + 1):
            one = 0
            num = i
            while num > 0:
                if  num % 2 != 0:
                    one += 1
                num = num // 2
            answer.append(one)
        return answer
                
                
        