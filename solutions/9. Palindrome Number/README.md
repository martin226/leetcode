# Palindrome Number

**Problem:** https://leetcode.com/problems/palindrome-number/

If the number is negative, we return False because it cannot be a palindrome. Otherwise:

Let `temp` denote the variable that will contain the reversed value of `num`, initialized at 0.

First, we reverse the given integer. To do this, we simply get the one's digit of `num` by taking `num` modulo 10, multiply `temp` by 10 and add the one's digit, floor divide `x` by 10 to get rid of the one's digit, and repeat until `num` != 0.

Then, we compare `temp` with `num` to check if it is a palindrome.

This solution runs in `O(|n|)` time complexity and `O(1)` space complexity.
