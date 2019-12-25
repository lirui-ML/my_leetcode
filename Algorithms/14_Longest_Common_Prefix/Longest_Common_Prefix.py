#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

    输入: ["flower","flow","flight"]
    输出: "fl"
示例 2:

    输入: ["dog","racecar","car"]
    输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

"""
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
                
        return shortest
            
    def longestCommonPrefix_2(self, strs) -> str:
        # 巧妙利用zip函数
        
        # >>strs = ["flower","flow","flight"]
        # >>list(zip(*strs))
        # [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        result = ""
        for i in zip(*strs):
            if len(set(i)) == 1:
                result += i[0]
            else:
                break
        return result
    
    def longestCommonPrefix_3(self, strs) -> str:
        # 水平扫描
        result = ""
        if len(strs) == 0:
            return result
        short = min(strs, key=len)
        for index in range(len(short)):
            if all([x.startswith(short[:index]) for x in strs]):
                result = short[:index]
            else:
                break
        return result
