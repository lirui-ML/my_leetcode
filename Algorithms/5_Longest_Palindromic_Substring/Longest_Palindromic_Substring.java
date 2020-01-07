/*
描述：最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
 */
public class Longest_Palindromic_Substring{
	public static void main(String[] args) {
		Solution ss= new Solution();
		String sample = "babad";
		String sample2 = "cbbd";
		System.out.println(ss.longestPalindrome(sample)+'\n'+ss.longestPalindrome(sample2));
	}
}

class Solution {
    public String longestPalindrome(String s) {
    	//暴力破解
    	String ans = "";
    	int max = 0;
    	int len = s.length();
    	for (int i = 0;i < len;i++) {
    		for(int j = i + 1;j <= len;j++) {
    			String test = s.substring(i, j);
    			if(isPalindromic(test) && test.length() > max)
    				ans = test;
    				max = Math.max(max, ans.length());
    		}
    	}
    	return ans;
    }
    private boolean isPalindromic(String text) {
		//判断回文字符串函数
		int len = text.length();
		for(int i = 0;i < len / 2;i++) {
			if(text.charAt(i) != text.charAt(len - i - 1))
				return false;
		}
		return true;
	}
    public String longestPalindrome2(String s) {
    	//动态规划
    	if(s == null || s.length() <= 1) {
			return s;
		}
		int n = s.length();
		int maxlen = 1;
		String res = s.substring(0, 1);
		for(int i = 0;i < n - 1;i++) {
			for (int j = i + 1;j < n;j++) {
				if(j - i + 1 > maxlen && valid(s,i,j)){
					maxlen = j - i + 1;
					res = s.substring(i, j + 1);
				}
			}
		}
		return res;
    }
    private boolean valid(String s,int left, int right) {
		while(left < right) {
			if (s.charAt(left) != s.charAt(right)) {
				return false;
			}
			left++;
			right--;
		}
		return true;
    }
}