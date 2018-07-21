"""
<p>Given a <b>non-empty</b> array containing <b>only positive integers</b>, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
</p>

<p><b>Note:</b><br />
<ol>
<li>Each of the array element will not exceed 100.</li>
<li>The array size will not exceed 200.</li>
</ol>
</p>

<p><b>Example 1:</b>
<pre>
Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
</pre>
</p>

<p><b>Example 2:</b>
<pre>
Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
</pre>
</p><p>给定一个<strong>只包含正整数</strong>的<strong>非空</strong>数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。</p>

<p><strong>注意:</strong></p>

<ol>
	<li>每个数组中的元素不会超过 100</li>
	<li>数组的大小不会超过 200</li>
</ol>

<p><strong>示例 1:</strong></p>

<pre>输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
</pre>

<p>&nbsp;</p>

<p><strong>示例&nbsp;2:</strong></p>

<pre>输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
</pre>

<p>&nbsp;</p>
<p>给定一个<strong>只包含正整数</strong>的<strong>非空</strong>数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。</p>

<p><strong>注意:</strong></p>

<ol>
	<li>每个数组中的元素不会超过 100</li>
	<li>数组的大小不会超过 200</li>
</ol>

<p><strong>示例 1:</strong></p>

<pre>输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
</pre>

<p>&nbsp;</p>

<p><strong>示例&nbsp;2:</strong></p>

<pre>输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.
</pre>

<p>&nbsp;</p>
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        