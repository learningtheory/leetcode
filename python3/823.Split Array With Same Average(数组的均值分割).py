"""
<p>In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)</p>

<p>Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.</p>

<pre>
<strong>Example :</strong>
<strong>Input:</strong> 
[1,2,3,4,5,6,7,8]
<strong>Output:</strong> true
<strong>Explanation: </strong>We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>The length of <code>A</code> will be in the range&nbsp;[1, 30].</li>
	<li><code>A[i]</code> will be in the range of <code>[0, 10000]</code>.</li>
</ul>

<p>&nbsp;</p>
<p>给定的整数数组 A ，我们要将 A数组 中的每个元素移动到 B数组 或者 C数组中。（B数组和C数组在开始的时候都为空）</p>

<p>返回<code>true</code> ，当且仅当在我们的完成这样的移动后，可使得B数组的平均值和C数组的平均值相等，并且B数组和C数组都不为空。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> 
[1,2,3,4,5,6,7,8]
<strong>输出:</strong> true
<strong>解释: </strong>我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>A</code> 数组的长度范围为 <code>[1, 30]</code>.</li>
	<li><code>A[i]</code> 的数据范围为 <code>[0, 10000]</code>.</li>
</ul>
<p>给定的整数数组 A ，我们要将 A数组 中的每个元素移动到 B数组 或者 C数组中。（B数组和C数组在开始的时候都为空）</p>

<p>返回<code>true</code> ，当且仅当在我们的完成这样的移动后，可使得B数组的平均值和C数组的平均值相等，并且B数组和C数组都不为空。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> 
[1,2,3,4,5,6,7,8]
<strong>输出:</strong> true
<strong>解释: </strong>我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>A</code> 数组的长度范围为 <code>[1, 30]</code>.</li>
	<li><code>A[i]</code> 的数据范围为 <code>[0, 10000]</code>.</li>
</ul>
"""


class Solution:
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        