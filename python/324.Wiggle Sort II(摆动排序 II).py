"""
<p>Given an unsorted array <code>nums</code>, reorder it such that <code>nums[0] &lt; nums[1] &gt; nums[2] &lt; nums[3]...</code>.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input: </strong><code>nums = [1, 5, 1, 1, 6, 4]</code>
<strong>Output: </strong>One possible answer is <code>[1, 4, 1, 5, 1, 6]</code>.</pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input: </strong><code>nums = [1, 3, 2, 2, 3, 1]</code>
<strong>Output:</strong> One possible answer is <code>[2, 3, 1, 3, 1, 2]</code>.</pre>

<p><b>Note:</b><br />
You may assume all input has valid answer.</p>

<p><b>Follow Up:</b><br />
Can you do it in O(n) time and/or in-place with O(1) extra space?</p>
<p>给定一个无序的数组&nbsp;<code>nums</code>，将它重新排列成&nbsp;<code>nums[0] &lt; nums[1] &gt; nums[2] &lt; nums[3]...</code>&nbsp;的顺序。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入: </strong><code>nums = [1, 5, 1, 1, 6, 4]</code>
<strong>输出: </strong>一个可能的答案是 <code>[1, 4, 1, 5, 1, 6]</code></pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong><code>nums = [1, 3, 2, 2, 3, 1]</code>
<strong>输出:</strong> 一个可能的答案是 <code>[2, 3, 1, 3, 1, 2]</code></pre>

<p><strong>说明:</strong><br>
你可以假设所有输入都会得到有效的结果。</p>

<p><strong>进阶:</strong><br>
你能用&nbsp;O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？</p>
<p>给定一个无序的数组&nbsp;<code>nums</code>，将它重新排列成&nbsp;<code>nums[0] &lt; nums[1] &gt; nums[2] &lt; nums[3]...</code>&nbsp;的顺序。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入: </strong><code>nums = [1, 5, 1, 1, 6, 4]</code>
<strong>输出: </strong>一个可能的答案是 <code>[1, 4, 1, 5, 1, 6]</code></pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong><code>nums = [1, 3, 2, 2, 3, 1]</code>
<strong>输出:</strong> 一个可能的答案是 <code>[2, 3, 1, 3, 1, 2]</code></pre>

<p><strong>说明:</strong><br>
你可以假设所有输入都会得到有效的结果。</p>

<p><strong>进阶:</strong><br>
你能用&nbsp;O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？</p>
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        