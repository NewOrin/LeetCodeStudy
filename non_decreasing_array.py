# code=utf-8
"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
题意：给定一个数组，最多只能修改一次元素，判断修改后数组是否为有序的
思路：有两种情况，array[i]可以被修改，array[i+1]也可以被修改
"""


class Solution(object):
    def checkPossibility(self, nums):
        """

        :param nums: List[int]
        :return: bool
        """
        # nums[:]返回所有元素
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                print("第", i, "次执行")
                break
        print(one, "排序后", sorted(one), "\n")
        print(two, "排序后", sorted(two))
        return one == sorted(one) or two == sorted(two)


test_array = [1, 3, 4, 8, 7, 6]
s = Solution()
print(s.checkPossibility(test_array))
