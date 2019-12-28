#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
回溯思想

8皇后问题
我们有一个 8x8 的棋盘，希望往里放 8 个棋子（皇后），每个棋子所在的行、列、对角线都不能有另一个棋子。
"""

class QueenFeedBack:
    
    def __init__(self):
        self.result = [0 for _ in range(8)]
        
    def cal8queens(self, row: int):
        if row == 8:
            self.printQueens(self.result)
            return
        for column in range(8):
            if self.isOk(row, column):
                self.result[row] = column
                self.cal8queens(row + 1)
            
    """
    打印出一个二维矩阵
    """       
    @staticmethod
    def printQueens(result: list):  
        print("\n"+'-' * 30)
        for row in range(8):
            for column in range(8):
                if result[row] == column:
                    print("Q | ", sep="", end='')
                else:
                    print("* | ", sep="", end='')
            print("\n"+'-' * 30)
        print("\n")
    
    """
    判断row行column列放置是否合适
    """
    def isOk(self, row: int, column: int):
        leftup = column - 1
        rightup = column + 1
        # 逐行往上考察每一行
        for i in range(row - 1, -1, -1):
            if self.result[i] == column:  # 第i行的column列有棋子吗？
                return False
            if leftup >= 0: #  考察左上对角线：第i行leftup列有棋子吗？
                if self.result[i] == leftup:
                    return False
            if rightup < 8:  # 考察右上对角线：第i行rightup列有棋子吗？
                if self.result[i] == rightup:
                    return False
            leftup -= 1
            rightup += 1
            
        return True
    
"""
0-1背包问题
"""
maxW = float('inf')
n = 10
w = 100
items = [15, 25, 8, 32, 16, 29, 51, 60, 8, 18]
def fun(i , cw, items, n, w):
    """
    Args:
        i: 表示考察到哪个物品了
        cw: 表示当前已经装进去的物品的重量和
        items: 表示每个物品的重量
        n: 表示物品个数
        w: 背包重量
    """
    global maxW
    if cw == w or i == n:
        if cw > maxW:
            maxW = cw
        return
    fun(i + 1, cw, items, n, w)
    if cw + items[i] <= w:
        fun(i + 1, cw + items[i], items, n, w)
        
fun(0, 0, items, n, w)

            
if __name__=='__main__':
    s = QueenFeedBack()
    s.cal8queens(0)
                
            
