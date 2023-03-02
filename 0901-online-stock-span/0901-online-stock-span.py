class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        total = 1
        
        while self.stack and  self.stack[-1][0] <= price:
            p, amount = self.stack.pop()
            total += amount
        self.stack.append([price, total])
        
        return self.stack[-1][1]
                
            
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)