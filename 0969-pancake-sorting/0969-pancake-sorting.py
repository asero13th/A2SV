class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
            def flip(end):
                start = 0
                while start < end:
                    arr[start],arr[end] = arr[end],arr[start]
                    start += 1
                    end -= 1
            n = len(arr)
            answer = []
            for i in range(n - 1,-1,-1):
                maximum = i
                for j in range(i,-1,-1):
                    if arr[j] > arr[maximum]:
                        maximum = j

                if maximum != i:
                    flip(maximum)
                    flip(i)
                    answer.append(maximum + 1)
                    answer.append(i+1)
            return answer
