/**
<p>Given a non-empty array of non-negative integers <code>nums</code>, the <b>degree</b> of this array is defined as the maximum frequency of any one of its elements.</p>
<p>Your task is to find the smallest possible length of a (contiguous) subarray of <code>nums</code>, that has the same degree as <code>nums</code>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1, 2, 2, 3, 1]
<b>Output:</b> 2
<b>Explanation:</b> 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1,2,2,3,1,4,2]
<b>Output:</b> 6
</pre>
</p>

<p><b>Note:</b>
<li><code>nums.length</code> will be between 1 and 50,000.</li>
<li><code>nums[i]</code> will be an integer between 0 and 49,999.</li>
</p><p>给定一个非空且只包含非负数的整数数组&nbsp;<code>nums</code>, 数组的度的定义是指数组里任一元素出现频数的最大值。</p>

<p>你的任务是找到与&nbsp;<code>nums</code>&nbsp;拥有相同大小的度的最短连续子数组，返回其长度。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [1, 2, 2, 3, 1]
<strong>输出:</strong> 2
<strong>解释:</strong> 
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [1,2,2,3,1,4,2]
<strong>输出:</strong> 6
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>nums.length</code>&nbsp;在1到50,000区间范围内。</li>
	<li><code>nums[i]</code>&nbsp;是一个在0到49,999范围内的整数。</li>
</ul>
<p>给定一个非空且只包含非负数的整数数组&nbsp;<code>nums</code>, 数组的度的定义是指数组里任一元素出现频数的最大值。</p>

<p>你的任务是找到与&nbsp;<code>nums</code>&nbsp;拥有相同大小的度的最短连续子数组，返回其长度。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [1, 2, 2, 3, 1]
<strong>输出:</strong> 2
<strong>解释:</strong> 
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [1,2,2,3,1,4,2]
<strong>输出:</strong> 6
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>nums.length</code>&nbsp;在1到50,000区间范围内。</li>
	<li><code>nums[i]</code>&nbsp;是一个在0到49,999范围内的整数。</li>
</ul>
**/


object Solution {
    def findShortestSubArray(nums: Array[Int]): Int = {
        
    }
}