=begin
<p>Given an array of integers <code>nums</code>, write a method that returns the "pivot" index of this array.
</p><p>
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
</p><p>
If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
nums = [1, 7, 3, 6, 5, 6]
<b>Output:</b> 3
<b>Explanation:</b> 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
nums = [1, 2, 3]
<b>Output:</b> -1
<b>Explanation:</b> 
There is no index that satisfies the conditions in the problem statement.
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>nums</code> will be in the range <code>[0, 10000]</code>.</li>
<li>Each element <code>nums[i]</code> will be an integer in the range <code>[-1000, 1000]</code>.</li>
</p><p>给定一个整数类型的数组&nbsp;<code>nums</code>，请编写一个能够返回数组<strong>&ldquo;中心索引&rdquo;</strong>的方法。</p>

<p>我们是这样定义数组<strong>中心索引</strong>的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。</p>

<p>如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
nums = [1, 7, 3, 6, 5, 6]
<strong>输出:</strong> 3
<strong>解释:</strong> 
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
nums = [1, 2, 3]
<strong>输出:</strong> -1
<strong>解释:</strong> 
数组中不存在满足此条件的中心索引。</pre>

<p><strong>说明:</strong></p>

<ul>
	<li><code>nums</code> 的长度范围为&nbsp;<code>[0, 10000]</code>。</li>
	<li>任何一个&nbsp;<code>nums[i]</code> 将会是一个范围在&nbsp;<code>[-1000, 1000]</code>的整数。</li>
</ul>
<p>给定一个整数类型的数组&nbsp;<code>nums</code>，请编写一个能够返回数组<strong>&ldquo;中心索引&rdquo;</strong>的方法。</p>

<p>我们是这样定义数组<strong>中心索引</strong>的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。</p>

<p>如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
nums = [1, 7, 3, 6, 5, 6]
<strong>输出:</strong> 3
<strong>解释:</strong> 
索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
同时, 3 也是第一个符合要求的中心索引。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
nums = [1, 2, 3]
<strong>输出:</strong> -1
<strong>解释:</strong> 
数组中不存在满足此条件的中心索引。</pre>

<p><strong>说明:</strong></p>

<ul>
	<li><code>nums</code> 的长度范围为&nbsp;<code>[0, 10000]</code>。</li>
	<li>任何一个&nbsp;<code>nums[i]</code> 将会是一个范围在&nbsp;<code>[-1000, 1000]</code>的整数。</li>
</ul>

=end


# @param {Integer[]} nums
# @return {Integer}
def pivot_index(nums)
    
end