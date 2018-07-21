/*
<p>
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols <code>+</code> and <code>-</code>. For each integer, you should choose one from <code>+</code> and <code>-</code> as its new symbol.
</p> 

<p>Find out how many ways to assign symbols to make sum of integers equal to target S.  
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> nums is [1, 1, 1, 1, 1], S is 3. 
<b>Output:</b> 5
<b>Explanation:</b> 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The length of the given array is positive and will not exceed 20. </li>
<li>The sum of elements in the given array will not exceed 1000.</li>
<li>Your output answer is guaranteed to be fitted in a 32-bit integer.</li>
</ol>
</p><p>给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号&nbsp;<code>+</code>&nbsp;和&nbsp;<code>-</code>。对于数组中的任意一个整数，你都可以从&nbsp;<code>+</code>&nbsp;或&nbsp;<code>-</code>中选择一个符号添加在前面。</p>

<p>返回可以使最终数组和为目标数 S 的所有添加符号的方法数。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums: [1, 1, 1, 1, 1], S: 3
<strong>输出:</strong> 5
<strong>解释:</strong> 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>数组的长度不会超过20，并且数组中的值全为正数。</li>
	<li>初始的数组的和不会超过1000。</li>
	<li>保证返回的最终结果为32位整数。</li>
</ol>
<p>给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号&nbsp;<code>+</code>&nbsp;和&nbsp;<code>-</code>。对于数组中的任意一个整数，你都可以从&nbsp;<code>+</code>&nbsp;或&nbsp;<code>-</code>中选择一个符号添加在前面。</p>

<p>返回可以使最终数组和为目标数 S 的所有添加符号的方法数。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums: [1, 1, 1, 1, 1], S: 3
<strong>输出:</strong> 5
<strong>解释:</strong> 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>数组的长度不会超过20，并且数组中的值全为正数。</li>
	<li>初始的数组的和不会超过1000。</li>
	<li>保证返回的最终结果为32位整数。</li>
</ol>
*/


/**
 * @param {number[]} nums
 * @param {number} S
 * @return {number}
 */
var findTargetSumWays = function(nums, S) {
    
};