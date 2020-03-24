#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：字符串压缩（easy）
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。

示例1:
 输入："aabcccccaaa"
 输出："a2b1c5a3"

示例2:
 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
提示：

字符串长度在[0, 50000]范围内。
"""

class Solution:
    def compressString(self, S: str) -> str:
        """遍历一遍，时间复杂度为O（n），空间复杂度O（n）"""
        if len(S) <= 2:
            return S
        count = 0
        result = ""
        start = S[0]
        i = 0
        while i < len(S):
            cur = S[i]
            if cur != start:
                result += "".join([start, str(count)])
                start = cur
                count = 1
            else:
                count += 1
            i += 1
        result += "".join([start, str(count)])

        # judge length
        return S if len(S) <= len(result) else result

"""
Java代码

class Solution {
    public String compressString(String S) {
        if (S == null || S.length() <= 2) {
            return S;
        }
        StringBuilder sb = new StringBuilder().append(S.charAt(0));
        int cnt = 1;
        for (int i = 1; i < S.length(); i++) {
            // 如果i与i-1相同，cnt累加
            if (S.charAt(i) == S.charAt(i - 1)) {
                cnt++;
            } else { 
                // 否则拼接上i-1的次数，从i开始重新计数
                sb.append(cnt).append(S.charAt(i));
                cnt = 1;
            }
        }
        return sb.append(cnt).length() < S.length()? sb.toString(): S;
    }
}
"""

if __name__ == '__main__':
    testcase1 = "aabcccccaaa"
    testcase2 = "abbccd"
    s =Solution()
    print(s.compressString(testcase1))
    print(s.compressString(testcase2))
