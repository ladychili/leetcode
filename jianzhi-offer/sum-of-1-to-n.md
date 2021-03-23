# 求1至n的和

## Problem

求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

## Solution

```python
class Solution:
    def Sum_Solution(self,n):
        return n and n+self.Sum_Solution(n-1)
```

一个简单的递归，n=0时终止。

* a非0时，`a and n = n`
* a为0时，`a and n = 0`

