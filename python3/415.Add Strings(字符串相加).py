"""
<p>Given two non-negative integers <code>num1</code> and <code>num2</code> represented as string, return the sum of <code>num1</code> and <code>num2</code>.</p>

<p><b>Note:</b>
<ol>
<li>The length of both <code>num1</code> and <code>num2</code> is < 5100.</li>
<li>Both <code>num1</code> and <code>num2</code> contains only digits <code>0-9</code>.</li>
<li>Both <code>num1</code> and <code>num2</code> does not contain any leading zero.</li>
<li>You <b>must not use any built-in BigInteger library</b> or <b>convert the inputs to integer</b> directly.</li>
</ol>
</p><p>给定两个字符串形式的非负整数&nbsp;<code>num1</code> 和<code>num2</code>&nbsp;，计算它们的和。</p>

<p><strong>注意：</strong></p>

<ol>
	<li><code>num1</code> 和<code>num2</code>&nbsp;的长度都小于 5100.</li>
	<li><code>num1</code> 和<code>num2</code> 都只包含数字&nbsp;<code>0-9</code>.</li>
	<li><code>num1</code> 和<code>num2</code> 都不包含任何前导零。</li>
	<li><strong>你不能使用任何內建 BigInteger 库，&nbsp;也不能直接将输入的字符串转换为整数形式。</strong></li>
</ol>
<p>给定两个字符串形式的非负整数&nbsp;<code>num1</code> 和<code>num2</code>&nbsp;，计算它们的和。</p>

<p><strong>注意：</strong></p>

<ol>
	<li><code>num1</code> 和<code>num2</code>&nbsp;的长度都小于 5100.</li>
	<li><code>num1</code> 和<code>num2</code> 都只包含数字&nbsp;<code>0-9</code>.</li>
	<li><code>num1</code> 和<code>num2</code> 都不包含任何前导零。</li>
	<li><strong>你不能使用任何內建 BigInteger 库，&nbsp;也不能直接将输入的字符串转换为整数形式。</strong></li>
</ol>
"""


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        