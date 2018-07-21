/**
<p>
Given an array of integers and an integer <b>k</b>, you need to find the number of <b>unique</b> k-diff pairs in the array. Here a <b>k-diff</b> pair is defined as an integer pair (i, j), where <b>i</b> and <b>j</b> are both numbers in the array and their <a href = "https://en.wikipedia.org/wiki/Absolute_difference">absolute difference</a> is <b>k</b>.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [3, 1, 4, 1, 5], k = 2
<b>Output:</b> 2
<b>Explanation: </b>There are two 2-diff pairs in the array, (1, 3) and (3, 5).</br>Although we have two 1s in the input, we should only return the number of <b>unique</b> pairs.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>[1, 2, 3, 4, 5], k = 1
<b>Output: </b>4
<b>Explanation:</b> There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input: </b>[1, 3, 1, 5, 4], k = 0
<b>Output: </b>1
<b>Explanation:</b> There is one 0-diff pair in the array, (1, 1).
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The pairs (i, j) and (j, i) count as the same pair.</li>
<li>The length of the array won't exceed 10,000.</li>
<li>All the integers in the given input belong to the range: [-1e7, 1e7].</li>
</ol>
</p><p>给定一个整数数组和一个整数&nbsp;<strong>k</strong>, 你需要在数组里找到<strong>不同的&nbsp;</strong>k-diff 数对。这里将&nbsp;<strong>k-diff</strong>&nbsp;数对定义为一个整数对 (i, j), 其中<strong> i </strong>和<strong> j </strong>都是数组中的数字，且两数之差的绝对值是&nbsp;<strong>k</strong>.</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [3, 1, 4, 1, 5], k = 2
<strong>输出:</strong> 2
<strong>解释: </strong>数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong>[1, 2, 3, 4, 5], k = 1
<strong>输出: </strong>4
<strong>解释:</strong> 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>[1, 3, 1, 5, 4], k = 0
<strong>输出: </strong>1
<strong>解释:</strong> 数组中只有一个 0-diff 数对，(1, 1)。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>数对 (i, j) 和数对&nbsp;(j, i) 被算作同一数对。</li>
	<li>数组的长度不超过10,000。</li>
	<li>所有输入的整数的范围在&nbsp;[-1e7, 1e7]。</li>
</ol>
<p>给定一个整数数组和一个整数&nbsp;<strong>k</strong>, 你需要在数组里找到<strong>不同的&nbsp;</strong>k-diff 数对。这里将&nbsp;<strong>k-diff</strong>&nbsp;数对定义为一个整数对 (i, j), 其中<strong> i </strong>和<strong> j </strong>都是数组中的数字，且两数之差的绝对值是&nbsp;<strong>k</strong>.</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [3, 1, 4, 1, 5], k = 2
<strong>输出:</strong> 2
<strong>解释: </strong>数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong>[1, 2, 3, 4, 5], k = 1
<strong>输出: </strong>4
<strong>解释:</strong> 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>[1, 3, 1, 5, 4], k = 0
<strong>输出: </strong>1
<strong>解释:</strong> 数组中只有一个 0-diff 数对，(1, 1)。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>数对 (i, j) 和数对&nbsp;(j, i) 被算作同一数对。</li>
	<li>数组的长度不超过10,000。</li>
	<li>所有输入的整数的范围在&nbsp;[-1e7, 1e7]。</li>
</ol>
**/


class Solution {
    public int findPairs(int[] nums, int k) {
        
    }
}