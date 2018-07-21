/*
<p>
Given two integers <code>L</code> and <code>R</code>, find the count of numbers in the range <code>[L, R]</code> (inclusive) having a prime number of set bits in their binary representation.
</p><p>
(Recall that the number of set bits an integer has is the number of <code>1</code>s present when written in binary.  For example, <code>21</code> written in binary is <code>10101</code> which has 3 set bits.  Also, 1 is not a prime.)
</p><p>

<p><b>Example 1:</b><br /><pre>
<b>Input:</b> L = 6, R = 10
<b>Output:</b> 4
<b>Explanation:</b>
6 -> 110 (2 set bits, 2 is prime)
7 -> 111 (3 set bits, 3 is prime)
9 -> 1001 (2 set bits , 2 is prime)
10->1010 (2 set bits , 2 is prime)
</pre></p>

<p><b>Example 2:</b><br /><pre>
<b>Input:</b> L = 10, R = 15
<b>Output:</b> 5
<b>Explanation:</b>
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
</pre></p>

<p><b>Note:</b><br><ol>
<li><code>L, R</code> will be integers <code>L <= R</code> in the range <code>[1, 10^6]</code>.</li>
<li><code>R - L</code> will be at most 10000.</li>
</ol></p><p>给定两个整数&nbsp;<code>L</code>&nbsp;和&nbsp;<code>R</code>&nbsp;，找到闭区间&nbsp;<code>[L, R]</code>&nbsp;范围内，计算置位位数为质数的整数个数。</p>

<p>（注意，计算置位代表二进制表示中1的个数。例如&nbsp;<code>21</code>&nbsp;的二进制表示&nbsp;<code>10101</code>&nbsp;有 3 个计算置位。还有，1 不是质数。）</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> L = 6, R = 10
<strong>输出:</strong> 4
<strong>解释:</strong>
6 -&gt; 110 (2 个计算置位，2 是质数)
7 -&gt; 111 (3 个计算置位，3 是质数)
9 -&gt; 1001 (2 个计算置位，2 是质数)
10-&gt; 1010 (2 个计算置位，2 是质数)
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> L = 10, R = 15
<strong>输出:</strong> 5
<strong>解释:</strong>
10 -&gt; 1010 (2 个计算置位, 2 是质数)
11 -&gt; 1011 (3 个计算置位, 3 是质数)
12 -&gt; 1100 (2 个计算置位, 2 是质数)
13 -&gt; 1101 (3 个计算置位, 3 是质数)
14 -&gt; 1110 (3 个计算置位, 3 是质数)
15 -&gt; 1111 (4 个计算置位, 4 不是质数)
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>L, R</code>&nbsp;是&nbsp;<code>L &lt;= R</code>&nbsp;且在&nbsp;<code>[1, 10^6]</code>&nbsp;中的整数。</li>
	<li><code>R - L</code>&nbsp;的最大值为 10000。</li>
</ol>
<p>给定两个整数&nbsp;<code>L</code>&nbsp;和&nbsp;<code>R</code>&nbsp;，找到闭区间&nbsp;<code>[L, R]</code>&nbsp;范围内，计算置位位数为质数的整数个数。</p>

<p>（注意，计算置位代表二进制表示中1的个数。例如&nbsp;<code>21</code>&nbsp;的二进制表示&nbsp;<code>10101</code>&nbsp;有 3 个计算置位。还有，1 不是质数。）</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> L = 6, R = 10
<strong>输出:</strong> 4
<strong>解释:</strong>
6 -&gt; 110 (2 个计算置位，2 是质数)
7 -&gt; 111 (3 个计算置位，3 是质数)
9 -&gt; 1001 (2 个计算置位，2 是质数)
10-&gt; 1010 (2 个计算置位，2 是质数)
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> L = 10, R = 15
<strong>输出:</strong> 5
<strong>解释:</strong>
10 -&gt; 1010 (2 个计算置位, 2 是质数)
11 -&gt; 1011 (3 个计算置位, 3 是质数)
12 -&gt; 1100 (2 个计算置位, 2 是质数)
13 -&gt; 1101 (3 个计算置位, 3 是质数)
14 -&gt; 1110 (3 个计算置位, 3 是质数)
15 -&gt; 1111 (4 个计算置位, 4 不是质数)
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>L, R</code>&nbsp;是&nbsp;<code>L &lt;= R</code>&nbsp;且在&nbsp;<code>[1, 10^6]</code>&nbsp;中的整数。</li>
	<li><code>R - L</code>&nbsp;的最大值为 10000。</li>
</ol>
*/


func countPrimeSetBits(L int, R int) int {
    
}