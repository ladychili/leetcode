# 跳台阶2

## Problem

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

## Solution

老生常谈的斐波那契数列。

$$f(n) = f(n-1) + f(n-2)$$

```python
class Solution:
    def jumpFloor(self, number):
        lst= [0,1,2]
        while number >= len(lst):
            lst.append(lst[-1]+lst[-2])
        return lst[number]
```

