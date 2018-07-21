"""
<p>We define a harmonious array is an array where the difference between its maximum value and its minimum value is <b>exactly</b> 1.</p>

<p>Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible <a href="https://en.wikipedia.org/wiki/Subsequence">subsequences</a>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,3,2,2,5,2,3,7]
<b>Output:</b> 5
<b>Explanation:</b> The longest harmonious subsequence is [3,2,2,2,3].
</pre>
</p>

<p><b>Note:</b>
The length of the input array will not exceed 20,000.
</p>

<p>和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。</p>

<p>现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [1,3,2,2,5,2,3,7]
<strong>输出:</strong> 5
<strong>原因:</strong> 最长的和谐数组是：[3,2,2,2,3].
</pre>

<p><strong>说明:</strong> 输入的数组长度最大不超过20,000.</p>
<p>和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。</p>

<p>现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [1,3,2,2,5,2,3,7]
<strong>输出:</strong> 5
<strong>原因:</strong> 最长的和谐数组是：[3,2,2,2,3].
</pre>

<p><strong>说明:</strong> 输入的数组长度最大不超过20,000.</p>
"""


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        