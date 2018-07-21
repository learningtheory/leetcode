"""
<p>Additive number is a string whose digits can form additive sequence.</p>

<p>A valid additive sequence should contain <b>at least</b> three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.</p>

<p>Given a string containing only digits <code>&#39;0&#39;-&#39;9&#39;</code>, write a function to determine if it&#39;s an additive number.</p>

<p><b>Note:</b> Numbers in the additive sequence <b>cannot</b> have leading zeros, so sequence <code>1, 2, 03</code> or <code>1, 02, 3</code> is invalid.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>&quot;112358&quot;</code>
<b>Output:</b> true 
<strong>Explanation: </strong>The digits can form an additive sequence: <code>1, 1, 2, 3, 5, 8</code>. 
&nbsp;            1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <code>&quot;199100199&quot;</code>
<b>Output:</b> true 
<strong>Explanation: </strong>The additive sequence is: <code>1, 99, 100, 199</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">.</span>&nbsp;
&nbsp;            1 + 99 = 100, 99 + 100 = 199</pre>

<p><b>Follow up:</b><br />
How would you handle overflow for very large input integers?</p><p>累加数是一个字符串，组成它的数字可以形成累加序列。</p>

<p>一个有效的累加序列必须<strong>至少</strong>包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。</p>

<p>给定一个只包含数字&nbsp;<code>&#39;0&#39;-&#39;9&#39;</code>&nbsp;的字符串，编写一个算法来判断给定输入是否是累加数。</p>

<p><strong>说明:&nbsp;</strong>累加序列里的数不会以 0 开头，所以不会出现&nbsp;<code>1, 2, 03</code> 或者&nbsp;<code>1, 02, 3</code>&nbsp;的情况。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> <code>&quot;112358&quot;</code>
<strong>输出:</strong> true 
<strong>解释: </strong>累加序列为: <code>1, 1, 2, 3, 5, 8 </code>。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> <code>&quot;199100199&quot;</code>
<strong>输出:</strong> true 
<strong>解释: </strong>累加序列为: <code>1, 99, 100, 199。</code>1 + 99 = 100, 99 + 100 = 199</pre>

<p><strong>进阶:</strong><br>
你如何处理一个溢出的过大的整数输入?</p>
<p>累加数是一个字符串，组成它的数字可以形成累加序列。</p>

<p>一个有效的累加序列必须<strong>至少</strong>包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。</p>

<p>给定一个只包含数字&nbsp;<code>&#39;0&#39;-&#39;9&#39;</code>&nbsp;的字符串，编写一个算法来判断给定输入是否是累加数。</p>

<p><strong>说明:&nbsp;</strong>累加序列里的数不会以 0 开头，所以不会出现&nbsp;<code>1, 2, 03</code> 或者&nbsp;<code>1, 02, 3</code>&nbsp;的情况。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> <code>&quot;112358&quot;</code>
<strong>输出:</strong> true 
<strong>解释: </strong>累加序列为: <code>1, 1, 2, 3, 5, 8 </code>。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> <code>&quot;199100199&quot;</code>
<strong>输出:</strong> true 
<strong>解释: </strong>累加序列为: <code>1, 99, 100, 199。</code>1 + 99 = 100, 99 + 100 = 199</pre>

<p><strong>进阶:</strong><br>
你如何处理一个溢出的过大的整数输入?</p>
"""


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """