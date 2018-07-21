"""
<p>
In a given array <code>nums</code> of positive integers, find three non-overlapping subarrays with maximum sum.
</p>
<p>
Each subarray will be of size <code>k</code>, and we want to maximize the sum of all <code>3*k</code> entries.
</p>
<p>
Return the result as a list of indices representing the starting position of each interval (0-indexed).  If there are multiple answers, return the lexicographically smallest one.
</p>
<p><b>Example:</b><br />
<pre>
<b>Input:</b> [1,2,1,2,6,7,5,1], 2
<b>Output:</b> [0, 3, 5]
<b>Explanation:</b> Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
</pre>
</p>

<p><b>Note:</b><br />
<li><code>nums.length</code> will be between 1 and 20000.</li>
<li><code>nums[i]</code> will be between 1 and 65535.</li>
<li><code>k</code> will be between 1 and floor(nums.length / 3).</li>
</p><p>给定数组&nbsp;<code>nums</code>&nbsp;由正整数组成，找到三个互不重叠的子数组的最大和。</p>

<p>每个子数组的长度为<code>k</code>，我们要使这<code>3*k</code>个项的和最大化。</p>

<p>返回每个区间起始索引的列表（索引从 0 开始）。如果有多个结果，返回字典序最小的一个。</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> [1,2,1,2,6,7,5,1], 2
<strong>输出:</strong> [0, 3, 5]
<strong>解释:</strong> 子数组 [1, 2], [2, 6], [7, 5] 对应的起始索引为 [0, 3, 5]。
我们也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>nums.length</code>的范围在<code>[1, 20000]</code>之间。</li>
	<li><code>nums[i]</code>的范围在<code>[1, 65535]</code>之间。</li>
	<li><code>k</code>的范围在<code>[1, floor(nums.length / 3)]</code>之间。</li>
</ul>
<p>给定数组&nbsp;<code>nums</code>&nbsp;由正整数组成，找到三个互不重叠的子数组的最大和。</p>

<p>每个子数组的长度为<code>k</code>，我们要使这<code>3*k</code>个项的和最大化。</p>

<p>返回每个区间起始索引的列表（索引从 0 开始）。如果有多个结果，返回字典序最小的一个。</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> [1,2,1,2,6,7,5,1], 2
<strong>输出:</strong> [0, 3, 5]
<strong>解释:</strong> 子数组 [1, 2], [2, 6], [7, 5] 对应的起始索引为 [0, 3, 5]。
我们也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>nums.length</code>的范围在<code>[1, 20000]</code>之间。</li>
	<li><code>nums[i]</code>的范围在<code>[1, 65535]</code>之间。</li>
	<li><code>k</code>的范围在<code>[1, floor(nums.length / 3)]</code>之间。</li>
</ul>
"""


class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        