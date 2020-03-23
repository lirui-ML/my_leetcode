#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：一次编辑（medium）

字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

示例 1:
输入:
first = "pale"
second = "ple"
输出: True


示例 2:
输入:
first = "pales"
second = "pal"
输出: False
"""

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        ## 根据题意，只有一次或零次编辑机会，故两个字符串长度之差不能超过1
        if abs(len(first) - len(second)) > 1:
            return False

        # 固定first比second的长度长
        if len(first) < len(second):
            first, second = second, first
        # 双指针遍历，寻找差异处个数
        diff = 0
        first_point = 0
        second_point = 0
        while first_point < len(first) and second_point < len(second):
            if first[first_point] == second[second_point]:
                first_point += 1
                second_point += 1
            else:
                if len(first) == len(second):
                    diff += 1
                    first_point += 1
                    second_point += 1
                else:
                    diff += 1
                    first_point += 1
        return diff <= 1

"""
Java代码

class Solution {
    public boolean oneEditAway(String first, String second) {
        int len1 = Math.max(first.length(), second.length());
        int len2 = Math.min(first.length(), second.length());
        if (len1 - len2 > 1)
            return false;

        //first为长字符串，second为短字符串
        if (len1 != first.length()){
            String tmp = first;
            first = second;
            second = tmp;
        }

        int count=0;
        //分两种情况
        if(len1==len2){
            for (int i=0;i<len1;i++){
                if(first.charAt(i)!=second.charAt(i))
                    count++;
                if(count>1)return false;
            }
        }else {
            for(int i=0,j=0;i<len2;j++){
                if(count>1)return false;
                if(first.charAt(j)!=second.charAt(i)){
                    //不相同只移动长字符串的指针，把for改成while循环应该好些
                    count++;
                    continue;
                }
                i++;
            }
        }
        return true;
    }
}
"""


if __name__ == '__main__':
    testcase1 = ("pale", "ple")
    testcase2 = ("pales", "pal")
    s = Solution()
    print(s.oneEditAway(testcase1[0], testcase1[1]))
    print(s.oneEditAway(testcase2[0], testcase2[1]))