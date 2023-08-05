class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        hashmap = {
            "++X" : 1,
            "X++" : 1,
            "--X": -1,
            "X--": -1
            }
        
        num = 0
        for op in operations:
            num += hashmap[op]
        return num