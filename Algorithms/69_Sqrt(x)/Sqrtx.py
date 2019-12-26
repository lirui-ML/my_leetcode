#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分法
        if x == 0:
            return 0
        if x < 4:
            return 1
        start = 1
        end = x - 1
        while start < end:
            mid = (start + end) // 2
            if mid * mid <= x and (mid + 1) * (mid + 1) > x:
                break
            if mid * mid < x:
                start = mid
            else:
                end = mid
        return mid
    
    def mySqrt_2(self, x: int) -> int:
        # 牛顿法
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        cur = 1
        while 1:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)
            
            
if __name__=="__main__":
    ss = Solution()
    print(ss.mySqrt(9))