"""
<p>Given an array of integers, return <strong>indices</strong> of the two numbers such that they add up to a specific target.</p>

<p>You may assume that each input would have <strong><em>exactly</em></strong> one solution, and you may not use the <em>same</em> element twice.</p>

<p><strong>Example:</strong></p>

<pre>
Given nums = [2, 7, 11, 15], target = 9,

Because nums[<strong>0</strong>] + nums[<strong>1</strong>] = 2 + 7 = 9,
return [<strong>0</strong>, <strong>1</strong>].
</pre>

<p>&nbsp;</p>
<p>给定一个整数数组和一个目标值，找出数组中和为目标值的<strong>两个</strong>数。</p>

<p>你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。</p>

<p><strong>示例:</strong></p>

<pre>给定 nums = [2, 7, 11, 15], target = 9

因为 nums[<strong>0</strong>] + nums[<strong>1</strong>] = 2 + 7 = 9
所以返回 [<strong>0, 1</strong>]
</pre>
<p>给定一个整数数组和一个目标值，找出数组中和为目标值的<strong>两个</strong>数。</p>

<p>你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。</p>

<p><strong>示例:</strong></p>

<pre>给定 nums = [2, 7, 11, 15], target = 9

因为 nums[<strong>0</strong>] + nums[<strong>1</strong>] = 2 + 7 = 9
所以返回 [<strong>0, 1</strong>]
</pre>
"""


class Solution:
    def twoSum(self, nums: list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            c = target - num
            if dic.get(c) is not None:
                return [nums.index(c), i]
            else:
                dic[num] = i

        raise Exception('No two sum solution')

    def twoSum1(self, nums: list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            c = target - num
            if c in nums and nums.index(c) != i:
                return [nums.index(c), i]

        raise Exception('No two sum solution')


if __name__ == '__main__':
    # 出现相同的元素
    lis = [3, 3, 3, 3, 44, 5, 3]
    tar = 6

    # [3, 2, 4]
    # 6
    # 在使用索引实现位置的时候要注意了，in的使用会出现 [0,0]
    print(Solution().twoSum(lis, tar))
