/**
<p>
An integer interval <code>[a, b]</code> (for integers <code>a < b</code>) is a set of all consecutive integers from <code>a</code> to <code>b</code>, including <code>a</code> and <code>b</code>.
</p><p>
Find the minimum size of a set S such that for every integer interval A in <code>intervals</code>, the intersection of S with A has size at least 2.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
<b>Output:</b> 3
<b>Explanation:</b>
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
<b>Output:</b> 5
<b>Explanation:</b>
An example of a minimum sized set is {1, 2, 3, 4, 5}.
</pre>
</p>

<p><b>Note:</b><br><ol>
<li><code>intervals</code> will have length in range <code>[1, 3000]</code>.</li>
<li><code>intervals[i]</code> will have length <code>2</code>, representing some integer interval.</li>
<li><code>intervals[i][j]</code> will be an integer in <code>[0, 10^8]</code>.</li>
</ol></p><p>一个整数区间&nbsp;<code>[a, b]</code>&nbsp;&nbsp;(&nbsp;<code>a &lt; b</code>&nbsp;) 代表着从&nbsp;<code>a</code>&nbsp;到&nbsp;<code>b</code>&nbsp;的所有连续整数，包括&nbsp;<code>a</code>&nbsp;和&nbsp;<code>b</code>。</p>

<p>给你一组整数区间<code>intervals</code>，请找到一个最小的集合 S，使得 S 里的元素与区间<code>intervals</code>中的每一个整数区间都至少有2个元素相交。</p>

<p>输出这个最小集合S的大小。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
<strong>输出:</strong> 3
<strong>解释:</strong>
考虑集合 S = {2, 3, 4}. S与intervals中的四个区间都有至少2个相交的元素。
且这是S最小的情况，故我们输出3。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
<strong>输出:</strong> 5
<strong>解释:</strong>
最小的集合S = {1, 2, 3, 4, 5}.
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>intervals</code>&nbsp;的长度范围为<code>[1, 3000]</code>。</li>
	<li><code>intervals[i]</code>&nbsp;长度为&nbsp;<code>2</code>，分别代表左、右边界。</li>
	<li><code>intervals[i][j]</code> 的值是&nbsp;<code>[0, 10^8]</code>范围内的整数。</li>
</ol>
<p>一个整数区间&nbsp;<code>[a, b]</code>&nbsp;&nbsp;(&nbsp;<code>a &lt; b</code>&nbsp;) 代表着从&nbsp;<code>a</code>&nbsp;到&nbsp;<code>b</code>&nbsp;的所有连续整数，包括&nbsp;<code>a</code>&nbsp;和&nbsp;<code>b</code>。</p>

<p>给你一组整数区间<code>intervals</code>，请找到一个最小的集合 S，使得 S 里的元素与区间<code>intervals</code>中的每一个整数区间都至少有2个元素相交。</p>

<p>输出这个最小集合S的大小。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
<strong>输出:</strong> 3
<strong>解释:</strong>
考虑集合 S = {2, 3, 4}. S与intervals中的四个区间都有至少2个相交的元素。
且这是S最小的情况，故我们输出3。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
<strong>输出:</strong> 5
<strong>解释:</strong>
最小的集合S = {1, 2, 3, 4, 5}.
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>intervals</code>&nbsp;的长度范围为<code>[1, 3000]</code>。</li>
	<li><code>intervals[i]</code>&nbsp;长度为&nbsp;<code>2</code>，分别代表左、右边界。</li>
	<li><code>intervals[i][j]</code> 的值是&nbsp;<code>[0, 10^8]</code>范围内的整数。</li>
</ol>
**/


object Solution {
    def intersectionSizeTwo(intervals: Array[Array[Int]]): Int = {
        
    }
}