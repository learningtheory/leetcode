"""
<p>
The set <code>S</code> originally contains numbers from 1 to <code>n</code>. But unfortunately, due to the data error, one of the numbers in the set got duplicated to <b>another</b> number in the set, which results in repetition of one number and loss of another number. 
</p>

<p>
Given an array <code>nums</code> representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> nums = [1,2,2,4]
<b>Output:</b> [2,3]
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The given array size will in the range [2, 10000].</li>
<li>The given array's numbers won't have any order.</li>
</ol>
</p><p>集合 <code>S</code> 包含从1到&nbsp;<code>n</code>&nbsp;的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。</p>

<p>给定一个数组 <code>nums</code> 代表了集合 <code>S</code> 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,2,4]
<strong>输出:</strong> [2,3]
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>给定数组的长度范围是&nbsp;[2, 10000]。</li>
	<li>给定的数组是无序的。</li>
</ol>
<p>集合 <code>S</code> 包含从1到&nbsp;<code>n</code>&nbsp;的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。</p>

<p>给定一个数组 <code>nums</code> 代表了集合 <code>S</code> 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,2,4]
<strong>输出:</strong> [2,3]
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>给定数组的长度范围是&nbsp;[2, 10000]。</li>
	<li>给定的数组是无序的。</li>
</ol>
"""


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        