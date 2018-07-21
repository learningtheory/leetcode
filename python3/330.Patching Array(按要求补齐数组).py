"""
<p>Given a sorted positive integer array <i>nums</i> and an integer <i>n</i>, add/patch elements to the array such that any number in range <code>[1, n]</code> inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.</p>

<p><b>Example 1:</b></p>

<pre>
<strong>Input: </strong><i>nums</i> = <code>[1,3]</code>, <i>n</i> = <code>6</code>
<strong>Output: </strong>1 
<strong>Explanation:</strong>
Combinations of <i>nums</i> are <code>[1], [3], [1,3]</code>, which form possible sums of: <code>1, 3, 4</code>.
Now if we add/patch <code>2</code> to <i>nums</i>, the combinations are: <code>[1], [2], [3], [1,3], [2,3], [1,2,3]</code>.
Possible sums are <code>1, 2, 3, 4, 5, 6</code>, which now covers the range <code>[1, 6]</code>.
So we only need <code>1</code> patch.</pre>

<p><b>Example 2:</b></p>

<pre>
<strong>Input: </strong><i>nums</i> = <code>[1,5,10]</code>, <i>n</i> = <code>20</code>
<strong>Output:</strong> 2
<strong>Explanation: </strong>The two patches can be <code>[2, 4]</code>.
</pre>

<p><b>Example 3:</b></p>

<pre>
<strong>Input: </strong><i>nums</i> = <code>[1,2,2]</code>, <i>n</i> = <code>5</code>
<strong>Output:</strong> 0
</pre>
<p>给定一个已排序的正整数数组 <em>nums，</em>和一个正整数&nbsp;<em>n 。</em>从&nbsp;<code>[1, n]</code>&nbsp;区间内选取任意个数字补充到&nbsp;<em>nums&nbsp;</em>中，使得&nbsp;<code>[1, n]</code>&nbsp;区间内的任何数字都可以用&nbsp;<em>nums&nbsp;</em>中某几个数字的和来表示。请输出满足上述要求的最少需要补充的数字个数。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入: </strong><em>nums</em> = <code>[1,3]</code>, <em>n</em> = <code>6</code>
<strong>输出: </strong>1 
<strong>解释:</strong>
根据<em> nums&nbsp;</em>里现有的组合&nbsp;<code>[1], [3], [1,3]</code>，可以得出&nbsp;<code>1, 3, 4</code>。
现在如果我们将&nbsp;<code>2</code>&nbsp;添加到&nbsp;<em>nums 中，</em>&nbsp;组合变为: <code>[1], [2], [3], [1,3], [2,3], [1,2,3]</code>。
其和可以表示数字&nbsp;<code>1, 2, 3, 4, 5, 6</code>，能够覆盖&nbsp;<code>[1, 6]</code>&nbsp;区间里所有的数。
所以我们最少需要添加一个数字。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong><em>nums</em> = <code>[1,5,10]</code>, <em>n</em> = <code>20</code>
<strong>输出:</strong> 2
<strong>解释: </strong>我们需要添加&nbsp;<code>[2, 4]</code>。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre><strong>输入: </strong><em>nums</em> = <code>[1,2,2]</code>, <em>n</em> = <code>5</code>
<strong>输出:</strong> 0
</pre>
<p>给定一个已排序的正整数数组 <em>nums，</em>和一个正整数&nbsp;<em>n 。</em>从&nbsp;<code>[1, n]</code>&nbsp;区间内选取任意个数字补充到&nbsp;<em>nums&nbsp;</em>中，使得&nbsp;<code>[1, n]</code>&nbsp;区间内的任何数字都可以用&nbsp;<em>nums&nbsp;</em>中某几个数字的和来表示。请输出满足上述要求的最少需要补充的数字个数。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入: </strong><em>nums</em> = <code>[1,3]</code>, <em>n</em> = <code>6</code>
<strong>输出: </strong>1 
<strong>解释:</strong>
根据<em> nums&nbsp;</em>里现有的组合&nbsp;<code>[1], [3], [1,3]</code>，可以得出&nbsp;<code>1, 3, 4</code>。
现在如果我们将&nbsp;<code>2</code>&nbsp;添加到&nbsp;<em>nums 中，</em>&nbsp;组合变为: <code>[1], [2], [3], [1,3], [2,3], [1,2,3]</code>。
其和可以表示数字&nbsp;<code>1, 2, 3, 4, 5, 6</code>，能够覆盖&nbsp;<code>[1, 6]</code>&nbsp;区间里所有的数。
所以我们最少需要添加一个数字。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong><em>nums</em> = <code>[1,5,10]</code>, <em>n</em> = <code>20</code>
<strong>输出:</strong> 2
<strong>解释: </strong>我们需要添加&nbsp;<code>[2, 4]</code>。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre><strong>输入: </strong><em>nums</em> = <code>[1,2,2]</code>, <em>n</em> = <code>5</code>
<strong>输出:</strong> 0
</pre>
"""


class Solution:
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        