#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class SortMethod:

    def QuickSort(self, array: list):
        """快速排序"""
        

    def MergeSort(self, array: list):
        """归并排序"""
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        left = self.MergeSort(left)
        right = self.MergeSort(right)

        return self.merge(left, right)

    @staticmethod
    def merge(left, right):
        """合并函数"""
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:result.append(right.pop(0))
        if left:
            result += left
        if right:
            result += right
        return result


    def bucketSort(self, array: list):
        """冒泡排序"""
        pass

    def insertSort(self, array: list):
        """插入排序"""
        pass
    
    def __repr__(self):
        pass

    def __call__(self):
        pass

if __name__=='__main__':
    test = [1, 4, 2, 3, 6, -1, 0, 25, -34, 8, 9, 1, 15]
    m = SortMethod()
    print(m.MergeSort(test))