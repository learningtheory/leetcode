"""
<p>We are given two strings, <code>A</code> and <code>B</code>.</p>

<p>A <em>shift on <code>A</code></em> consists of taking string <code>A</code> and moving the leftmost character to the rightmost position. For example, if <code>A = &#39;abcde&#39;</code>, then it will be <code>&#39;bcdea&#39;</code> after one shift on <code>A</code>. Return <code>True</code> if and only if <code>A</code> can become <code>B</code> after some number of shifts on <code>A</code>.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> A = &#39;abcde&#39;, B = &#39;cdeab&#39;
<strong>Output:</strong> true

<strong>Example 2:</strong>
<strong>Input:</strong> A = &#39;abcde&#39;, B = &#39;abced&#39;
<strong>Output:</strong> false
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>A</code> and <code>B</code> will have length at most <code>100</code>.</li>
</ul>
<p>给定两个字符串, <code>A</code>&nbsp;和&nbsp;<code>B</code>。</p>

<p><code>A</code>&nbsp;的旋转操作就是将&nbsp;<code>A</code> 最左边的字符移动到最右边。&nbsp;例如, 若&nbsp;<code>A = &#39;abcde&#39;</code>，在移动一次之后结果就是<code>&#39;bcdea&#39;</code>&nbsp;。如果在若干次旋转操作之后，<code>A</code>&nbsp;能变成<code>B</code>，那么返回<code>True</code>。</p>

<pre>
<strong>示例 1:</strong>
<strong>输入:</strong> A = &#39;abcde&#39;, B = &#39;cdeab&#39;
<strong>输出:</strong> true

<strong>示例 2:</strong>
<strong>输入:</strong> A = &#39;abcde&#39;, B = &#39;abced&#39;
<strong>输出:</strong> false</pre>

<p><strong>注意：</strong></p>

<ul>
	<li><code>A</code> 和&nbsp;<code>B</code>&nbsp;长度不超过&nbsp;<code>100</code>。</li>
</ul>
<p>给定两个字符串, <code>A</code>&nbsp;和&nbsp;<code>B</code>。</p>

<p><code>A</code>&nbsp;的旋转操作就是将&nbsp;<code>A</code> 最左边的字符移动到最右边。&nbsp;例如, 若&nbsp;<code>A = &#39;abcde&#39;</code>，在移动一次之后结果就是<code>&#39;bcdea&#39;</code>&nbsp;。如果在若干次旋转操作之后，<code>A</code>&nbsp;能变成<code>B</code>，那么返回<code>True</code>。</p>

<pre>
<strong>示例 1:</strong>
<strong>输入:</strong> A = &#39;abcde&#39;, B = &#39;cdeab&#39;
<strong>输出:</strong> true

<strong>示例 2:</strong>
<strong>输入:</strong> A = &#39;abcde&#39;, B = &#39;abced&#39;
<strong>输出:</strong> false</pre>

<p><strong>注意：</strong></p>

<ul>
	<li><code>A</code> 和&nbsp;<code>B</code>&nbsp;长度不超过&nbsp;<code>100</code>。</li>
</ul>
"""


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        