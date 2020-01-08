#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
描述：
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
class Solution:
    def generateParenthesis(self, n: int):
        #
        
        
    def is_True_Parenthesis(self, s: str) -> bool:
        # 判断是否是有效的括号
        if s[0] == ")":
            return False
        stack = []
        for i in s:
            if i ==  "(":
                stack.append(i)
            elif i == ")":
                if len(stack) > 0: 
                    end = stack.pop()
                    if end != "(":
                        return False
                else:
                    return False
                
        return len(stack) == 0
                

if __name__=="__main__":
    ss = Solution()
    sample1 = "()()()"
    sample2 = ")(())("
    sample3 = "(())()"
    print(ss.is_True_Parenthesis(sample3))
    
    