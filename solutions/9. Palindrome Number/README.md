# Reverse Integer

**Problem:** https://leetcode.com/problems/palindrome-number/

If the number is negative, we return False because it cannot be a palindrome. Otherwise:

First, we reverse the given integer. To do this, we simply get the one's digit of `num` by taking `num` modulo 10, multiply the answer by 10 and add the one's digit, floor divide `x` by 10 to get rid of one's digit, and repeat until `num` != 0.

Then, we compare the reversed integer with the original integer to check if it is a palindrome.

This solution runs in `O(log(n))` time complexity and `O(1)` space complexity.
