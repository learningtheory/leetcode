"""
<p>Given two arrays of length <code>m</code> and <code>n</code> with digits <code>0-9</code> representing two numbers. Create the maximum number of length <code>k &lt;= m + n</code> from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the <code>k</code> digits.</p>

<p><strong>Note: </strong>You should try to optimize your time and space complexity.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input:</strong>
nums1 = <code>[3, 4, 6, 5]</code>
nums2 = <code>[9, 1, 2, 5, 8, 3]</code>
k = <code>5</code>
<strong>Output:</strong>
<code>[9, 8, 6, 5, 3]</code></pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input:</strong>
nums1 = <code>[6, 7]</code>
nums2 = <code>[6, 0, 4]</code>
k = <code>5</code>
<strong>Output:</strong>
<code>[6, 7, 6, 0, 4]</code></pre>

<p><b>Example 3:</b></p>

<pre>
<strong>Input:</strong>
nums1 = <code>[3, 9]</code>
nums2 = <code>[8, 9]</code>
k = <code>3</code>
<strong>Output:</strong>
<code>[9, 8, 9]</code>
</pre>
<p>给定长度分别为&nbsp;<code>m</code>&nbsp;和&nbsp;<code>n</code>&nbsp;的两个数组，其元素由&nbsp;<code>0-9</code>&nbsp;构成，表示两个自然数各位上的数字。现在从这两个数组中选出 <code>k (k &lt;= m + n)</code>&nbsp;个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。</p>

<p>求满足该条件的最大数。结果返回一个表示该最大数的长度为&nbsp;<code>k</code>&nbsp;的数组。</p>

<p><strong>说明: </strong>请尽可能地优化你算法的时间和空间复杂度。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong>
nums1 = <code>[3, 4, 6, 5]</code>
nums2 = <code>[9, 1, 2, 5, 8, 3]</code>
k = <code>5</code>
<strong>输出:</strong>
<code>[9, 8, 6, 5, 3]</code></pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>
nums1 = <code>[6, 7]</code>
nums2 = <code>[6, 0, 4]</code>
k = <code>5</code>
<strong>输出:</strong>
<code>[6, 7, 6, 0, 4]</code></pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong>
nums1 = <code>[3, 9]</code>
nums2 = <code>[8, 9]</code>
k = <code>3</code>
<strong>输出:</strong>
<code>[9, 8, 9]</code></pre>
<p>给定长度分别为&nbsp;<code>m</code>&nbsp;和&nbsp;<code>n</code>&nbsp;的两个数组，其元素由&nbsp;<code>0-9</code>&nbsp;构成，表示两个自然数各位上的数字。现在从这两个数组中选出 <code>k (k &lt;= m + n)</code>&nbsp;个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。</p>

<p>求满足该条件的最大数。结果返回一个表示该最大数的长度为&nbsp;<code>k</code>&nbsp;的数组。</p>

<p><strong>说明: </strong>请尽可能地优化你算法的时间和空间复杂度。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong>
nums1 = <code>[3, 4, 6, 5]</code>
nums2 = <code>[9, 1, 2, 5, 8, 3]</code>
k = <code>5</code>
<strong>输出:</strong>
<code>[9, 8, 6, 5, 3]</code></pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>
nums1 = <code>[6, 7]</code>
nums2 = <code>[6, 0, 4]</code>
k = <code>5</code>
<strong>输出:</strong>
<code>[6, 7, 6, 0, 4]</code></pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong>
nums1 = <code>[3, 9]</code>
nums2 = <code>[8, 9]</code>
k = <code>3</code>
<strong>输出:</strong>
<code>[9, 8, 9]</code></pre>
"""


class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        