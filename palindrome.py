class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            reversed_x = 0
            temp_x = x
            while temp_x > 0:
                reversed_x *= 10
                reversed_x += temp_x % 10
                temp_x = int(temp_x / 10)
            return reversed_x == x
