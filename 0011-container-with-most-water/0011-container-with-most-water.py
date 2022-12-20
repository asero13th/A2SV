class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        max_area = 0
        while r > l:
            min_height = min(height[r],height[l])
            area = min_height*(r - l)
            if area > max_area:
                max_area = area
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_area