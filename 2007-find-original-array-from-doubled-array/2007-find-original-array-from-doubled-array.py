class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        queue = []
        changed.sort()
        answer  = []
        
        for i in range(len(changed)):
            if queue and queue[0] * 2 == changed[i]:
                answer.append(queue.pop(0))
            else:
                queue.append(changed[i])
        return answer if not queue else []
        