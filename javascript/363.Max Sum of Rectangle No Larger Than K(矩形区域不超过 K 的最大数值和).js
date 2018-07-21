/*
<p>Given a non-empty 2D matrix <i>matrix</i> and an integer <i>k</i>, find the max sum of a rectangle in the <i>matrix</i> such that its sum is no larger than <i>k</i>.</p>

<p><b>Example:</b><br />
<pre>Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
</pre>
</p>

<p>The answer is <code>2</code>. Because the sum of rectangle <code>[[0, 1], [-2, 3]]</code> is 2 and 2 is the max number no larger than k (k = 2).</p>

<p><b>Note:</b><br />
<ol>
<li>The rectangle inside the matrix must have an area > 0.</li>
<li>What if the number of rows is much larger than the number of columns?</li>
</ol>
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://discuss.leetcode.com/user/fujiaozhu">@fujiaozhu</a> for adding this problem and creating all test cases.</p><p>给定一个非空二维矩阵&nbsp;<code>matrix</code>，和一个整数 k，找到这个矩阵中矩形区域不超过 k 的最大数值和。</p>

<p><strong>示例：</strong></p>

<pre>给定 matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
</pre>

<p>结果是&nbsp;<code>2</code>，因为矩形区域&nbsp;<code>[[0, 1], [-2, 3]]</code>&nbsp;的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。</p>

<p><strong>注意：</strong></p>

<ol>
	<li>矩阵内的矩形区域面积必须大于 0；</li>
	<li>如果行数远大于列数呢？</li>
</ol>
<p>给定一个非空二维矩阵&nbsp;<code>matrix</code>，和一个整数 k，找到这个矩阵中矩形区域不超过 k 的最大数值和。</p>

<p><strong>示例：</strong></p>

<pre>给定 matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
</pre>

<p>结果是&nbsp;<code>2</code>，因为矩形区域&nbsp;<code>[[0, 1], [-2, 3]]</code>&nbsp;的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。</p>

<p><strong>注意：</strong></p>

<ol>
	<li>矩阵内的矩形区域面积必须大于 0；</li>
	<li>如果行数远大于列数呢？</li>
</ol>
*/


/**
 * @param {number[][]} matrix
 * @param {number} k
 * @return {number}
 */
var maxSumSubmatrix = function(matrix, k) {
    
};