"""
<p>Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. </p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [0,1]
<b>Output:</b> 2
<b>Explanation:</b> [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [0,1,0]
<b>Output:</b> 2
<b>Explanation:</b> [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
</pre>
</p>

<p><b>Note:</b>
The length of the given binary array will not exceed 50,000.
</p><p>给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [0,1]
<strong>输出:</strong> 2
<strong>说明:</strong> [0, 1] 是具有相同数量0和1的最长连续子数组。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [0,1,0]
<strong>输出:</strong> 2
<strong>说明:</strong> [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。</pre>

<p><strong>注意:&nbsp;</strong>给定的二进制数组的长度不会超过50000。</p>
<p>给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [0,1]
<strong>输出:</strong> 2
<strong>说明:</strong> [0, 1] 是具有相同数量0和1的最长连续子数组。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [0,1,0]
<strong>输出:</strong> 2
<strong>说明:</strong> [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。</pre>

<p><strong>注意:&nbsp;</strong>给定的二进制数组的长度不会超过50000。</p>
"""


class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        