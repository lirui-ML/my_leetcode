#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

class SortMethod:

    def QuickSort(self, array: list):
        """快速排序, 非原地排序版本"""
        # 递归终止条件：当只有一个或没有元素时
        if len(array) <= 1:
            return array
        left, right, mid = [], [], []
        # 选择分区点
        pivot = self.partition(array)
        #
        for number in array:
            if number == pivot:
                mid.append(number)
            elif number < pivot:
                left.append(number)
            else:
                right.append(number)

        return self.QuickSort(left) + mid + self.QuickSort(right)

    @staticmethod
    def partition(arr):
        """分区函数"""
        pivot = random.choice(arr)
        return pivot

    def QuickSort2(self, array: list, first: int, last: int):
        """快速排序, 原地排序版本"""
        if first >= last:
            return
        mid_value = array[first]
        low = first
        high = last
        while low < high:
            while low < high and array[high] >= mid_value:
                high -= 1
            array[low] = array[high]
            while low < high and array[low] < mid_value:
                low += 1
            array[high] = array[low]
        array[low] = mid_value

        self.QuickSort2(array, first, low - 1)
        self.QuickSort2(array, low + 1, last)

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
    test = [1, 4, 2, 3, 6, -1, 0, 25, -34, 8, 9, 20, 15]
    m = SortMethod()
    # print(m.MergeSort(test))

    # print(m.QuickSort(test))

    # m.QuickSort2(test, 0, len(test) - 1)
    # print(test)