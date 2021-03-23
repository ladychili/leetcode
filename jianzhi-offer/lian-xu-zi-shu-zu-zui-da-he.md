# 连续子数组的最大和

## Problem

计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？

例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8\(从第0个开始,到第3个为止\)。给一个数组，返回它的最大连续子序列的和。\(子向量的长度至少是1\)

## Solution

```python
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        max_sum = float("-inf")
        now_sum = 0
        for i in range(len(array)):
            now_sum += array.pop()
            max_sum = max(now_sum, max_sum)
            now_sum = max(0, now_sum)      
        return max_sum
```

1. 遍历array的每一个元素
2. 若某一环加上新元素得到的now\_sum为负值，直接舍弃，从0开始；正值则继续保留，哪怕比前一环小。

