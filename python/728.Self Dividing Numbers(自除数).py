"""
<p>
A <i>self-dividing number</i> is a number that is divisible by every digit it contains.
</p><p>
For example, 128 is a self-dividing number because <code>128 % 1 == 0</code>, <code>128 % 2 == 0</code>, and <code>128 % 8 == 0</code>.
</p><p>
Also, a self-dividing number is not allowed to contain the digit zero.
</p><p>
Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
</p>
<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
left = 1, right = 22
<b>Output:</b> [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
</pre>
</p>

<p><b>Note:</b>
<li>The boundaries of each input argument are <code>1 <= left <= right <= 10000</code>.</li>
</p><p><em>自除数&nbsp;</em>是指可以被它包含的每一位数除尽的数。</p>

<p>例如，128 是一个自除数，因为&nbsp;<code>128 % 1 == 0</code>，<code>128 % 2 == 0</code>，<code>128 % 8 == 0</code>。</p>

<p>还有，自除数不允许包含 0 。</p>

<p>给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong> 
上边界left = 1, 下边界right = 22
<strong>输出：</strong> [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
</pre>

<p><strong>注意：</strong></p>

<ul>
	<li>每个输入参数的边界满足&nbsp;<code>1 &lt;= left &lt;= right &lt;= 10000</code>。</li>
</ul>
<p><em>自除数&nbsp;</em>是指可以被它包含的每一位数除尽的数。</p>

<p>例如，128 是一个自除数，因为&nbsp;<code>128 % 1 == 0</code>，<code>128 % 2 == 0</code>，<code>128 % 8 == 0</code>。</p>

<p>还有，自除数不允许包含 0 。</p>

<p>给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong> 
上边界left = 1, 下边界right = 22
<strong>输出：</strong> [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
</pre>

<p><strong>注意：</strong></p>

<ul>
	<li>每个输入参数的边界满足&nbsp;<code>1 &lt;= left &lt;= right &lt;= 10000</code>。</li>
</ul>
"""


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        