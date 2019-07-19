# 构建乘积数组

## Problem

给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]\*A[1]\*...\*A[i-1]\*A[i+1]\*...\*A[n-1]。

**不能使用除法。**

## Solution

```python
from functools import reduce
class Solution:
    def multiply(self, A):
        B = [1]*len(A)
        for i in range(len(A)):
            n = A[i]
            A[i] = 1
            B[i] = reduce((lambda x,y: x*y), A)
            A[i] = n
        return B
```

