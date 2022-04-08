class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT_10, MIN_INT_10 = 214748364, -214748364
        ans = 0
        while x:
            lastDigit = int(math.fmod(x, 10))
            x = int(x/10)
            if ans > MAX_INT_10 or (ans == MAX_INT_10 and lastDigit > 7):
                return 0
            if ans < MIN_INT_10 or (ans == MIN_INT_10 and lastDigit < -8):
                return 0
            ans = ans * 10 + lastDigit
        return ans
