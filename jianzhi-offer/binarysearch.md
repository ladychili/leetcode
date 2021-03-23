# 二分查找

## Problem

对于一个**有序**数组，我们通常采用二分查找的方式来定位某一元素，请编写二分查找的算法，在数组中查找指定元素。

给定一个整数数组**A**及它的大小**n**，同时给定要查找的元素**val**，请返回它在数组中的位置\(从0开始\)，若不存在该元素，返回-1。若该元素出现多次，请**返回第一次出现的位置**。

## Solution

一个无限循环的 while loop，两种情况下break

* 「向右查找」时（`val > 当前值`），「右边第一个」刚好等于val，此时最优。更新并输出val\_pos。 
* 范围缩小到两个数时 \(`左边界 == 右边阶-1`\)，break循环。左右都等于val时也要优先输出左边。

```python
class BinarySearch:
    def getPos(self, A, n, val):
        val_pos = -1
        left = 0
        right = n-1
        now_pos = (left + right)//2
        while 1:
            if A[now_pos] < val:            # 当前值 < val，
                if val == A[now_pos+1]:     # 右边第一个 = val
                    val_pos = now_pos + 1   # 更新val_pos
                    break                   # 跳出
                left = now_pos
                now_pos = (left + right)//2
            else: # A[now_pos] >= val       # 当前值 = val，仍要「向左查找」，确保找到「第一次出现的位置」
                right = now_pos
                now_pos = (left + right)//2
            if left==right-1:               # 范围缩小到两个数
                if val==A[left]:
                    val_pos = left          # 优先输出左边
                elif val==A[right]:
                    val_pos = right
                break                       # 即使左右都不符合也要break
        return(val_pos)
```

Line 13 和 line 16 其实可以合并写在 `if... else...`外，不过为了逻辑更直观还是分开写了。

