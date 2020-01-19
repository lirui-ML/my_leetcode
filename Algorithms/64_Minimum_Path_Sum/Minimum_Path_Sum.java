/*
描述：最小路径和 （难度：中等）
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

class Solution {
    public int minPathSum(int[][] grid) {
        //动态规划，时间和空间复杂度为O(m*n),二维数组
        int m = grid.length;
        int n = grid[0].length;
        if(m <=0 || n <= 0){
            return 0;
        }
        int[][] dp = new int[m][n];
        dp[0][0] = grid[0][0];
        for(int i = 1;i < m;i++){
            dp[i][0] = dp[i - 1][0] + grid[i][0];
        }
        for(int j = 1;j < n;j++){
            dp[0][j] = dp[0][j - 1] + grid[0][j];
        }
        for(int i = 1;i < m;i++){
            for(int j = 1;j < n;j++){
                dp[i][j] = Math.min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
            }
        }
        return dp[m - 1][n - 1];
    }

    public int minPathSum2(int[][] grid) {
        //优化动态规划，时间复杂度为O(m*n), 空间复杂度为0(n), 一维数组
        int m = grid.length;
        int n = grid[0].length;
        if(m <=0 || n <= 0){
            return 0;
        }
        int[] dp = new int[n];
        dp[0] = grid[0][0];
        for (int i = 1;i < n;i++){
            dp[i] = dp[i - 1] + grid[0][i];
        }
        for (int i = 1;i < m;i++){
            dp[0] = dp[0] + grid[i][0];
            for (int j = 1;j < n;j++){
                dp[j] = Math.min(dp[j - 1], dp[j]) + grid[i][j];
            }
        }
        return dp[n - 1];
}