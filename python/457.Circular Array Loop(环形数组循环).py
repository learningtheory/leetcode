"""
<p>You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it&#39;s negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be &quot;forward&quot; or &quot;backward&#39;.</p>

<p><b>Example 1:</b> Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -&gt; 2 -&gt; 3 -&gt; 0.</p>

<p><b>Example 2:</b> Given the array [-1, 2], there is no loop.</p>

<p><b>Note:</b> The given array is guaranteed to contain no element &quot;0&quot;.</p>

<p>Can you do it in <b>O(n)</b> time complexity and <b>O(1)</b> space complexity?</p>
<p>给定一组含有正整数和负整数的数组。如果某个索引中的 n 是正数的，则向前移动 n 个索引。相反，如果是负数(-n)，则向后移动 n 个索引。</p>

<p>假设数组首尾相接。判断数组中是否有环。环中至少包含 2 个元素。环中的元素一律&ldquo;向前&rdquo;或者一律&ldquo;向后&rdquo;。</p>

<p><strong>示例 1：</strong>给定数组&nbsp;[2, -1, 1, 2, 2], 有一个循环，从索引 0 -&gt; 2 -&gt; 3 -&gt; 0。</p>

<p><strong>示例 2：</strong>给定数组[-1, 2], 没有循环。</p>

<p><strong>注意：</strong>给定数组保证不包含元素&quot;0&quot;。</p>

<p>你能写出时间复杂度为 <strong>O(n) </strong>且空间复杂度为&nbsp;<strong>O(1)&nbsp;</strong>的算法吗？</p>
<p>给定一组含有正整数和负整数的数组。如果某个索引中的 n 是正数的，则向前移动 n 个索引。相反，如果是负数(-n)，则向后移动 n 个索引。</p>

<p>假设数组首尾相接。判断数组中是否有环。环中至少包含 2 个元素。环中的元素一律&ldquo;向前&rdquo;或者一律&ldquo;向后&rdquo;。</p>

<p><strong>示例 1：</strong>给定数组&nbsp;[2, -1, 1, 2, 2], 有一个循环，从索引 0 -&gt; 2 -&gt; 3 -&gt; 0。</p>

<p><strong>示例 2：</strong>给定数组[-1, 2], 没有循环。</p>

<p><strong>注意：</strong>给定数组保证不包含元素&quot;0&quot;。</p>

<p>你能写出时间复杂度为 <strong>O(n) </strong>且空间复杂度为&nbsp;<strong>O(1)&nbsp;</strong>的算法吗？</p>
"""


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        