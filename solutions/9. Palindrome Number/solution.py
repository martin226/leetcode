class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0:
            return False
        rev, temp = 0, num
        while temp:
            lastDigit = temp % 10
            temp //= 10
            rev = rev * 10 + lastDigit
        return rev == num
