# 跳台阶n

## Problem

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。

求该青蛙跳上一个n级的台阶总共有多少种跳法。

## Solution

**递归**问题

```python
class Solution:
    def jumpFloor(self, n):
        if n==0 or n==1:
            return 1
        else:
            return 2*self.jumpFloor(n-1)
```

第一跳有n种情况： 1. 跳1阶，剩下的n-1阶有$f\(n-1\)$种跳法 2. 跳2阶，剩下的n-2阶有$f\(n-2\)$种跳法 …… 3. 跳n-1阶，剩下1阶有$f\(1\)$中跳法 4. 跳n阶，就这一种跳法

$$f(n) = f(n-1) + f(n-2) + … + f(1) + f(0) \\ f(n) = f(n-1) + f(n-1) \\f(n) = 2 * f(n-1)$$

