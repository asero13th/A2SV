class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(number):
            for i in range(4):
                x = int(number[i])
                for d in [-1, 1]:
                    y = (x + d) % 10
                    yield number[:i] + str(y) + number[i+1:]

        if '0000' in deadends:
            return -1
        queue = deque(['0000'])
        seen = set(deadends + ['0000'])
        turns = 0
        while queue:
            size = len(queue)
            for i in range(size):
                number = queue.popleft()
                if number == target:
                    return turns
                for neighbor in neighbors(number):
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            turns += 1
        return -1
        