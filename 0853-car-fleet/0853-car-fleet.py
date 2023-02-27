class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[position[i],speed[i]] for i in range(len(speed))]
        pair.sort()
        stack = []
        for pos, speed in pair:
            time = (target - pos)/speed

            while  stack and time >= stack[-1]:
                stack.pop() 
            stack.append(time)

        return len(stack)