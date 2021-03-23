# 二进制数中1的个数

## Problem

输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

## Solution

```python
class Solution():
    def NumberOf1(self,n):
        if n<0:
            return (32 - bin(~n).count('1'))
        else:
            return bin(n).count('1')
```

* 负数，先按位取反`~`得到「相反数-1」，「相反数-1」里的“1”=原数补码里的“0”，32-补码里“0”的个数即得到1的个数。
* 非负，直接数1

补充: `n = n & (n-1)`相当于去掉二进制n里「从右往左第一个1」，直到n=0，迭代次数即1的个数。

```text
class Solution():
    def NumberOf1(self,n):
        cnt = 0
        while n!=0:
            n&=(n-1)
            cnt+=1
        return cnt
```

