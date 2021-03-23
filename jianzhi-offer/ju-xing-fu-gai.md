# 2x1矩形覆盖

## Problem

我们可以用2\*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2\*1的小矩形无重叠地覆盖一个2\*n的大矩形，总共有多少种方法？

## Solution

```python
class Solution:
    def rectCover(self,number):
        seq = [0,1,2]
        while number >= len(seq):
            seq.append(seq[-1]+seq[-2])
        return seq[number]
```

用递归其实思路更简单，但是python递归太慢了，OJ会判超时。

$$f(0) = 0\\ f(1) = 1 \\ f(2) = 2 \\f(3) =f(2) + f(1) \\…\\f(n) = f(n-1) + f(n-2)$$

其实是一个Fibonacci sequence。对于一个2\*n的大矩形，

1. 第一块**竖着**摆剩下的有$f\(n-1\)$种情况，
2. 第一块**横着**摆剩下的有$f\(n-2\)$种情况。

