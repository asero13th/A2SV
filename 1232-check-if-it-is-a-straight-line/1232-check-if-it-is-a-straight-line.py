class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        slope = (y2-y1)/(x2 - x1) if x2 - x1 != 0 else None
        for i in range(len(coordinates) - 1):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i + 1]
            
            if x2 - x1 == 0:
                if slope != None:
                    return False
                else:
                    continue
            if slope != (y2 - y1)/( x2 - x1):
                return False
        return True           
            
        