# Two Sum

**Problem:** https://leetcode.com/problems/two-sum/

Let `v`<sub>`i`</sub> denote the `i`<sub>th</sub> value in the `nums` array.

We iterate through `nums` while maintaining a hashmap `idx` which pairs `v`<sub>`i`</sub> with `i`.

If `target` - `v`<sub>`i`</sub> is present inside `idx`, we have found the pair of numbers that add up to `target`. Therefore, we return `idx`[`target` - `v`<sub>`i`</sub>] and `i`. Otherwise, we set `idx`\[`v`<sub>`i`</sub>\] = `i` and continue our loop.

This solution runs in `O(n)` time complexity and `O(n)` space complexity.
