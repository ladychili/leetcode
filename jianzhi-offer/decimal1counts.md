# 十进制数中1的个数

## Problem

求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

## Solution 1

思路：

把一个数如`abcde`分为3份。以百位c为例，百位出现1的次数：

1. `c=0`时，有`ab*100`次。  e.g. 12045百位出现1的次数为 `12*100`
2. `c=1`时，有`ab*100 + de+1`次。 e.g. 12145百位出现1的次数为 `12*100+(45+1)`
3. `c>1`时，有`(ab+1)*100`次。  e.g. 12345百位出现1的次数为 `(12+1)*100`

其他位同理。从个位循环到最高位，次数求和即可。

代码：

```python
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        i = 1
        cnt = 0
        while (n//i) != 0:
            now = n//i%10        #当前位
            left = n//(i*10)     #高位
            right = n%i          #低位
            if now == 0:
                cnt+= left*i
            elif now == 1:
                cnt+= left*i + right+1
            else:
                cnt+= (left+1)*i
            i = i*10
        return(cnt)
```

## Solution 2 \(Python抖机灵版\)

人生苦短...

```python
def NumberOf1Between1AndN_Solution(self, n):
    n = int(n)
    s = ""
    for i in range(1,n+1):
        s+=str(i)
    return(s.count('1'))
```

