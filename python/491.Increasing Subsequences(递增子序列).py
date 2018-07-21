"""
<p>
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .
</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> [4, 6, 7, 7]
<b>Output:</b> [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The length of the given array will not exceed 15.</li>
<li>The range of integer in the given array is [-100,100].</li>
<li>The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.</li>
</ol>
</p><p>给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> [4, 6, 7, 7]
<strong>输出:</strong> [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>给定数组的长度不会超过15。</li>
	<li>数组中的整数范围是&nbsp;[-100,100]。</li>
	<li>给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。</li>
</ol>
<p>给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> [4, 6, 7, 7]
<strong>输出:</strong> [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>给定数组的长度不会超过15。</li>
	<li>数组中的整数范围是&nbsp;[-100,100]。</li>
	<li>给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。</li>
</ol>
"""


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        