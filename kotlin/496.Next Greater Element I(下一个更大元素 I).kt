/**
<p>
You are given two arrays <b>(without duplicates)</b> <code>nums1</code> and <code>nums2</code> where <code>nums1</code>’s elements are subset of <code>nums2</code>. Find all the next greater numbers for <code>nums1</code>'s elements in the corresponding places of <code>nums2</code>. 
</p>

<p>
The Next Greater Number of a number <b>x</b> in <code>nums1</code> is the first greater number to its right in <code>nums2</code>. If it does not exist, output -1 for this number.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> <b>nums1</b> = [4,1,2], <b>nums2</b> = [1,3,4,2].
<b>Output:</b> [-1,3,-1]
<b>Explanation:</b>
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> <b>nums1</b> = [2,4], <b>nums2</b> = [1,2,3,4].
<b>Output:</b> [3,-1]
<b>Explanation:</b>
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>All elements in <code>nums1</code> and <code>nums2</code> are unique.</li>
<li>The length of both <code>nums1</code> and <code>nums2</code> would not exceed 1000.</li>
</ol>
</p><p>给定两个<strong>没有重复元素</strong>的数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;，其中<code>nums1</code>&nbsp;是&nbsp;<code>nums2</code>&nbsp;的子集。找到&nbsp;<code>nums1</code>&nbsp;中每个元素在&nbsp;<code>nums2</code>&nbsp;中的下一个比其大的值。</p>

<p><code>nums1</code>&nbsp;中数字&nbsp;<strong>x</strong>&nbsp;的下一个更大元素是指&nbsp;<strong>x</strong>&nbsp;在&nbsp;<code>nums2</code>&nbsp;中对应位置的右边的第一个比&nbsp;<strong>x&nbsp;</strong>大的元素。如果不存在，对应位置输出-1。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <strong>nums1</strong> = [4,1,2], <strong>nums2</strong> = [1,3,4,2].
<strong>输出:</strong> [-1,3,-1]
<strong>解释:</strong>
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> <strong>nums1</strong> = [2,4], <strong>nums2</strong> = [1,2,3,4].
<strong>输出:</strong> [3,-1]
<strong>解释:</strong>
&nbsp;   对于num1中的数字2，第二个数组中的下一个较大数字是3。
    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>nums1</code>和<code>nums2</code>中所有元素是唯一的。</li>
	<li><code>nums1</code>和<code>nums2</code>&nbsp;的数组大小都不超过1000。</li>
</ol>
<p>给定两个<strong>没有重复元素</strong>的数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;，其中<code>nums1</code>&nbsp;是&nbsp;<code>nums2</code>&nbsp;的子集。找到&nbsp;<code>nums1</code>&nbsp;中每个元素在&nbsp;<code>nums2</code>&nbsp;中的下一个比其大的值。</p>

<p><code>nums1</code>&nbsp;中数字&nbsp;<strong>x</strong>&nbsp;的下一个更大元素是指&nbsp;<strong>x</strong>&nbsp;在&nbsp;<code>nums2</code>&nbsp;中对应位置的右边的第一个比&nbsp;<strong>x&nbsp;</strong>大的元素。如果不存在，对应位置输出-1。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <strong>nums1</strong> = [4,1,2], <strong>nums2</strong> = [1,3,4,2].
<strong>输出:</strong> [-1,3,-1]
<strong>解释:</strong>
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> <strong>nums1</strong> = [2,4], <strong>nums2</strong> = [1,2,3,4].
<strong>输出:</strong> [3,-1]
<strong>解释:</strong>
&nbsp;   对于num1中的数字2，第二个数组中的下一个较大数字是3。
    对于num1中的数字4，第二个数组中没有下一个更大的数字，因此输出 -1。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>nums1</code>和<code>nums2</code>中所有元素是唯一的。</li>
	<li><code>nums1</code>和<code>nums2</code>&nbsp;的数组大小都不超过1000。</li>
</ol>
**/


class Solution {
    fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
        
    }
}