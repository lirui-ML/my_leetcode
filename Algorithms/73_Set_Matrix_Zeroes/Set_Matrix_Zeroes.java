import java.util.HashSet;
import java.util.Set;

/*
描述：矩阵置0，难度（medium）
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:
输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:
输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/set-matrix-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

class Solution {
    public void setZeroes(int[][] matrix) {
      //O（m*n）时间复杂度，O（m+n）空间复杂度
        if (matrix == null || matrix.length == 0) {
          return;
        }
        int m  = matrix.length;
        int n = matrix[0].length;
        Set<Integer> rows = new HashSet<Integer>();
        Set<Integer> cols = new HashSet<Integer>();
        
        for (int i = 0; i < m; i++) {
          for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
              rows.add(i);
              cols.add(j);
            }
          }
        }
        for (int i = 0; i < m; i++) {
          for (int j = 0; j < n; j++) {
            if (rows.contains(i) || cols.contains(j)) {
              matrix[i][j] = 0;
            }
          }
        }  
    }
    
    public void setZeroes_2(int[][] matrix) {
      //"""设置虚拟值，O（1）的额外空间"""
      int MODIFIED = -1000000;
      int R = matrix.length;
      int C = matrix[0].length;

      for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
          if (matrix[r][c] == 0) {
            // We modify the corresponding rows and column elements in place.
            // Note, we only change the non zeroes to MODIFIED
            for (int k = 0; k < C; k++) {
              if (matrix[r][k] != 0) {
                matrix[r][k] = MODIFIED;
              }
            }
            for (int k = 0; k < R; k++) {
              if (matrix[k][c] != 0) {
                matrix[k][c] = MODIFIED;
              }
            }
          }
        }
      }

      for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
          // Make a second pass and change all MODIFIED elements to 0 """
          if (matrix[r][c] == MODIFIED) {
            matrix[r][c] = 0;
          }
        }
      }
    }
}