class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        s = z[len(z):0:-1] + z[0]
        print(s,z)
        return True if s == z else False
        