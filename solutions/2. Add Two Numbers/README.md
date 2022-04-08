# Add Two Numbers

**Problem:** https://leetcode.com/problems/add-two-numbers/

We begin by initializing an empty ListNode with two pointers: `root` and `cur`. The `root` pointer will always point to the zero<sub>th</sub> element in the Linked List, while the `cur` pointer will always point to the last element. We will also maintain a `carry` variable initialized with a value of 0, which will hold the value that should be carried on to the next node.

While `l1`, `l2`, and `carry` still exist, we add the values of `l1` and `l2` to `carry`. Then, we set the next node of `cur` to the one's digit of `carry`, which is simply `carry % 10`. We also floor divide `carry` by 10 to get rid of its one's digit. Afterwards, we set the `cur` pointer to `cur.next` to move on to the next digit.

Finally, we return `root.next` which is simply the pointer to the first digit of our answer.

This solution runs in `O(max(|l1|, |l2|))` time complexity and `O(max(|l1|, |l2|))` space complexity.
