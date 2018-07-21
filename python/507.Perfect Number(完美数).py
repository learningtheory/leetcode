"""
<p>We define the Perfect Number is a <b>positive</b> integer that is equal to the sum of all its <b>positive</b> divisors except itself. 
</p>
Now, given an <b>integer</b> n, write a function that returns true when it is a perfect number and false when it is not.
</p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> 28
<b>Output:</b> True
<b>Explanation:</b> 28 = 1 + 2 + 4 + 7 + 14
</pre>
</p>

<p><b>Note:</b>
The input number <b>n</b> will not exceed 100,000,000. (1e8)
</p><p>对于一个&nbsp;<strong>正整数</strong>，如果它和除了它自身以外的所有正因子之和相等，我们称它为&ldquo;完美数&rdquo;。</p>

<p>给定一个&nbsp;<strong>正整数&nbsp;</strong><code>n</code>，&nbsp;如果他是完美数，返回&nbsp;<code>True</code>，否则返回&nbsp;<code>False</code></p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入:</strong> 28
<strong>输出:</strong> True
<strong>解释:</strong> 28 = 1 + 2 + 4 + 7 + 14
</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<p>输入的数字&nbsp;<strong><code>n</code></strong> 不会超过 100,000,000. (1e8)</p>
<p>对于一个&nbsp;<strong>正整数</strong>，如果它和除了它自身以外的所有正因子之和相等，我们称它为&ldquo;完美数&rdquo;。</p>

<p>给定一个&nbsp;<strong>正整数&nbsp;</strong><code>n</code>，&nbsp;如果他是完美数，返回&nbsp;<code>True</code>，否则返回&nbsp;<code>False</code></p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入:</strong> 28
<strong>输出:</strong> True
<strong>解释:</strong> 28 = 1 + 2 + 4 + 7 + 14
</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<p>输入的数字&nbsp;<strong><code>n</code></strong> 不会超过 100,000,000. (1e8)</p>
"""


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        