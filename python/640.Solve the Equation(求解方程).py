"""
<p>
Solve a given equation and return the value of <code>x</code> in the form of string "x=#value". The equation contains only '+', '-' operation, the variable <code>x</code> and its coefficient.
</p>

<p>
If there is no solution for the equation, return "No solution".
</p>
<p>
If there are infinite solutions for the equation, return "Infinite solutions".
</p>
<p>
If there is exactly one solution for the equation, we ensure that the value of <code>x</code> is an integer.
</p>

<p><b>Example 1:</b><br/>
<pre>
<b>Input:</b> "x+5-3+x=6+x-2"
<b>Output:</b> "x=2"
</pre>
</p>

<p><b>Example 2:</b><br/>
<pre>
<b>Input:</b> "x=x"
<b>Output:</b> "Infinite solutions"
</pre>
</p>

<p><b>Example 3:</b><br/>
<pre>
<b>Input:</b> "2x=x"
<b>Output:</b> "x=0"
</pre>
</p>

<p><b>Example 4:</b><br/>
<pre>
<b>Input:</b> "2x+3x-6x=x+2"
<b>Output:</b> "x=-1"
</pre>
</p>

<p><b>Example 5:</b><br/>
<pre>
<b>Input:</b> "x=x+2"
<b>Output:</b> "No solution"
</pre>
</p><p>求解一个给定的方程，将<code>x</code>以字符串&quot;x=#value&quot;的形式返回。该方程仅包含&#39;+&#39;，&#39; - &#39;操作，变量&nbsp;<code>x</code>&nbsp;和其对应系数。</p>

<p>如果方程没有解，请返回&ldquo;No solution&rdquo;。</p>

<p>如果方程有无限解，则返回&ldquo;Infinite solutions&rdquo;。</p>

<p>如果方程中只有一个解，要保证返回值&nbsp;<code>x</code>&nbsp;是一个整数。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> &quot;x+5-3+x=6+x-2&quot;
<strong>输出:</strong> &quot;x=2&quot;
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> &quot;x=x&quot;
<strong>输出:</strong> &quot;Infinite solutions&quot;
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> &quot;2x=x&quot;
<strong>输出:</strong> &quot;x=0&quot;
</pre>

<p><strong>示例 4:</strong></p>

<pre>
<strong>输入:</strong> &quot;2x+3x-6x=x+2&quot;
<strong>输出:</strong> &quot;x=-1&quot;
</pre>

<p><strong>示例 5:</strong></p>

<pre>
<strong>输入:</strong> &quot;x=x+2&quot;
<strong>输出:</strong> &quot;No solution&quot;
</pre>
<p>求解一个给定的方程，将<code>x</code>以字符串&quot;x=#value&quot;的形式返回。该方程仅包含&#39;+&#39;，&#39; - &#39;操作，变量&nbsp;<code>x</code>&nbsp;和其对应系数。</p>

<p>如果方程没有解，请返回&ldquo;No solution&rdquo;。</p>

<p>如果方程有无限解，则返回&ldquo;Infinite solutions&rdquo;。</p>

<p>如果方程中只有一个解，要保证返回值&nbsp;<code>x</code>&nbsp;是一个整数。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> &quot;x+5-3+x=6+x-2&quot;
<strong>输出:</strong> &quot;x=2&quot;
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> &quot;x=x&quot;
<strong>输出:</strong> &quot;Infinite solutions&quot;
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> &quot;2x=x&quot;
<strong>输出:</strong> &quot;x=0&quot;
</pre>

<p><strong>示例 4:</strong></p>

<pre>
<strong>输入:</strong> &quot;2x+3x-6x=x+2&quot;
<strong>输出:</strong> &quot;x=-1&quot;
</pre>

<p><strong>示例 5:</strong></p>

<pre>
<strong>输入:</strong> &quot;x=x+2&quot;
<strong>输出:</strong> &quot;No solution&quot;
</pre>
"""


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        