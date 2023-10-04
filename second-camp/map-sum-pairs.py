class MapSum:

    def __init__(self):
        self.holder = defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:
        self.holder[key] = val

        

    def sum(self, prefix: str) -> int:
        ans = 0
        for key in self.holder:
            if key[:len(prefix)] == prefix:
                ans += self.holder[key]
        return ans
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)