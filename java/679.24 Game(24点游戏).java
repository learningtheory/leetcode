/**
<p>
You have 4 cards each containing a number from 1 to 9.  You need to judge whether they could operated through <code>*</code>, <code>/</code>, <code>+</code>, <code>-</code>, <code>(</code>, <code>)</code> to get the value of 24.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [4, 1, 8, 7]
<b>Output:</b> True
<b>Explanation:</b> (8-4) * (7-1) = 24
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1, 2, 1, 2]
<b>Output:</b> False
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The division operator <code>/</code> represents real division, not integer division.  For example, 4 / (1 - 2/3) = 12.</li>
<li>Every operation done is between two numbers.  In particular, we cannot use <code>-</code> as a unary operator.  For example, with <code>[1, 1, 1, 1]</code> as input, the expression <code>-1 - 1 - 1 - 1</code> is not allowed.</li>
<li>You cannot concatenate numbers together.  For example, if the input is <code>[1, 2, 1, 2]</code>, we cannot write this as 12 + 12.</li>
</ol>
</p>
</p><p>你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过&nbsp;<code>*</code>，<code>/</code>，<code>+</code>，<code>-</code>，<code>(</code>，<code>)</code>&nbsp;的运算得到 24。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [4, 1, 8, 7]
<strong>输出:</strong> True
<strong>解释:</strong> (8-4) * (7-1) = 24
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [1, 2, 1, 2]
<strong>输出:</strong> False
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>除法运算符&nbsp;<code>/</code>&nbsp;表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。</li>
	<li>每个运算符对两个数进行运算。特别是我们不能用&nbsp;<code>-</code>&nbsp;作为一元运算符。例如，<code>[1, 1, 1, 1]</code>&nbsp;作为输入时，表达式&nbsp;<code>-1 - 1 - 1 - 1</code>&nbsp;是不允许的。</li>
	<li>你不能将数字连接在一起。例如，输入为&nbsp;<code>[1, 2, 1, 2]</code>&nbsp;时，不能写成 12 + 12 。</li>
</ol>
<p>你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过&nbsp;<code>*</code>，<code>/</code>，<code>+</code>，<code>-</code>，<code>(</code>，<code>)</code>&nbsp;的运算得到 24。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [4, 1, 8, 7]
<strong>输出:</strong> True
<strong>解释:</strong> (8-4) * (7-1) = 24
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [1, 2, 1, 2]
<strong>输出:</strong> False
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>除法运算符&nbsp;<code>/</code>&nbsp;表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。</li>
	<li>每个运算符对两个数进行运算。特别是我们不能用&nbsp;<code>-</code>&nbsp;作为一元运算符。例如，<code>[1, 1, 1, 1]</code>&nbsp;作为输入时，表达式&nbsp;<code>-1 - 1 - 1 - 1</code>&nbsp;是不允许的。</li>
	<li>你不能将数字连接在一起。例如，输入为&nbsp;<code>[1, 2, 1, 2]</code>&nbsp;时，不能写成 12 + 12 。</li>
</ol>
**/


class Solution {
    public boolean judgePoint24(int[] nums) {
        
    }
}