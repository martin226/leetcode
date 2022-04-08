# Reverse Integer

**Problem:** https://leetcode.com/problems/reverse-integer/

In order to reverse the integer, we simply get the one's digit of `x` by taking `x` modulo 10, multiply the answer by 10 and add the one's digit, floor divide `x` by 10 to get rid of one's digit, and repeat until `x` != 0.

In order to meet the integer overflow condition, we must also add a few additional checks.

Observe that if `ans * 10 + lastDigit` causes overflow, one of four conditions must be true:

1. `ans` > MAX_INT/10
2. `ans` = MAX_INT/10 and `lastDigit` > 7, with 7 being the last digit of MAX_INT
3. `ans` < MIN_INT/10
4. `ans` = MIN_INT/10 and `lastDigit` < -8, with -8 being the last digit of MIN_INT

Therefore to prevent overflow, we check these conditions before setting `ans` to its updated value.

This solution runs in `O(log(n))` time complexity and `O(1)` space complexity.
