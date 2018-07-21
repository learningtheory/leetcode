"""
<p>
Nearly every one have used the <a href="https://en.wikipedia.org/wiki/Multiplication_table">Multiplication Table</a>. But could you find out the <code>k-th</code> smallest number quickly from the multiplication table?
</p>

<p>
Given the height <code>m</code> and the length <code>n</code> of a <code>m * n</code> Multiplication Table, and a positive integer <code>k</code>, you need to return the <code>k-th</code> smallest number in this table.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> m = 3, n = 3, k = 5
<b>Output:</b> 
<b>Explanation:</b> 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> m = 2, n = 3, k = 6
<b>Output:</b> 
<b>Explanation:</b> 
The Multiplication Table:
1	2	3
2	4	6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>The <code>m</code> and <code>n</code> will be in the range [1, 30000].</li>
<li>The <code>k</code> will be in the range [1, m * n]</li>
</ol>
</p><p>几乎每一个人都用&nbsp;<a href="https://baike.baidu.com/item/%E4%B9%98%E6%B3%95%E8%A1%A8">乘法表</a>。但是你能在乘法表中快速找到第<code>k</code>小的数字吗？</p>

<p>给定高度<code>m</code>&nbsp;、宽度<code>n</code> 的一张&nbsp;<code>m * n</code>的乘法表，以及正整数<code>k</code>，你需要返回表中第<code>k</code>&nbsp;小的数字。</p>

<p><strong>例&nbsp;1：</strong></p>

<pre>
<strong>输入:</strong> m = 3, n = 3, k = 5
<strong>输出:</strong> 3
<strong>解释:</strong> 
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).
</pre>

<p><strong>例 2：</strong></p>

<pre>
<strong>输入:</strong> m = 2, n = 3, k = 6
<strong>输出:</strong> 6
<strong>解释:</strong> 
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li><code>m</code> 和&nbsp;<code>n</code>&nbsp;的范围在 [1, 30000] 之间。</li>
	<li><code>k</code> 的范围在 [1, m * n] 之间。</li>
</ol>
<p>几乎每一个人都用&nbsp;<a href="https://baike.baidu.com/item/%E4%B9%98%E6%B3%95%E8%A1%A8">乘法表</a>。但是你能在乘法表中快速找到第<code>k</code>小的数字吗？</p>

<p>给定高度<code>m</code>&nbsp;、宽度<code>n</code> 的一张&nbsp;<code>m * n</code>的乘法表，以及正整数<code>k</code>，你需要返回表中第<code>k</code>&nbsp;小的数字。</p>

<p><strong>例&nbsp;1：</strong></p>

<pre>
<strong>输入:</strong> m = 3, n = 3, k = 5
<strong>输出:</strong> 3
<strong>解释:</strong> 
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).
</pre>

<p><strong>例 2：</strong></p>

<pre>
<strong>输入:</strong> m = 2, n = 3, k = 6
<strong>输出:</strong> 6
<strong>解释:</strong> 
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li><code>m</code> 和&nbsp;<code>n</code>&nbsp;的范围在 [1, 30000] 之间。</li>
	<li><code>k</code> 的范围在 [1, m * n] 之间。</li>
</ol>
"""


class Solution:
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        