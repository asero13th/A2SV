class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = {}
        for i,v in enumerate(arr):
            if v ==  0:
                if v in hashmap:
                    hashmap[v].append(i)
                else:
                    hashmap[v] = [0]
            else:
                hashmap[v] = i
        for num in hashmap:
            if (num * 2) in hashmap and num != 0:
                return True
            
            if num == 0 and len(hashmap[num]) > 1:
                return True
        return False
        