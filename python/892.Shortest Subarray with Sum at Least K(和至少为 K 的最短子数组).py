"""
<p>Return the <strong>length</strong> of the shortest, non-empty, contiguous&nbsp;subarray of <code>A</code> with sum at least <code>K</code>.</p>

<p>If there is no non-empty subarray with sum at least <code>K</code>, return <code>-1</code>.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1]</span>, K = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">1</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[1,2]</span>, K = <span id="example-input-2-2">4</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[2,-1,2]</span>, K = <span id="example-input-3-2">3</span>
<strong>Output: </strong><span id="example-output-3">3</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 50000</code></li>
	<li><code>-10 ^ 5&nbsp;&lt;= A[i] &lt;= 10 ^ 5</code></li>
	<li><code>1 &lt;= K &lt;= 10 ^ 9</code></li>
</ol>
</div>
</div>
</div><p>返回 <code>A</code> 的最短的非空连续子数组的<strong>长度</strong>，该子数组的和至少为 <code>K</code> 。</p>

<p>如果没有和至少为&nbsp;<code>K</code>&nbsp;的非空子数组，返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = [1], K = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [1,2], K = 4
<strong>输出：</strong>-1
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>A = [2,-1,2], K = 3
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 50000</code></li>
	<li><code>-10 ^ 5&nbsp;&lt;= A[i] &lt;= 10 ^ 5</code></li>
	<li><code>1 &lt;= K &lt;= 10 ^ 9</code></li>
</ol>
<p>返回 <code>A</code> 的最短的非空连续子数组的<strong>长度</strong>，该子数组的和至少为 <code>K</code> 。</p>

<p>如果没有和至少为&nbsp;<code>K</code>&nbsp;的非空子数组，返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = [1], K = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [1,2], K = 4
<strong>输出：</strong>-1
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>A = [2,-1,2], K = 3
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 50000</code></li>
	<li><code>-10 ^ 5&nbsp;&lt;= A[i] &lt;= 10 ^ 5</code></li>
	<li><code>1 &lt;= K &lt;= 10 ^ 9</code></li>
</ol>
"""


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        