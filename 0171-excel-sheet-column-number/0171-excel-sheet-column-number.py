class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        count=0
        for x in columnTitle:
            calc=ord(x)-ord('A')+1
            count=26*count+calc
        return count
        