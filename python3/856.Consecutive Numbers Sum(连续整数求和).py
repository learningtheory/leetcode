"""
<p>Given a positive integer&nbsp;<code>N</code>, how many ways can we write it as a sum of&nbsp;consecutive positive integers?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>5
<strong>Output: </strong>2
<strong>Explanation: </strong>5 = 5 = 2 + 3</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>9
<strong>Output: </strong>3
<strong>Explanation: </strong>9 = 9 = 4 + 5 = 2 + 3 + 4</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>15
<strong>Output: </strong>4
<strong>Explanation: </strong>15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5</pre>

<p><strong>Note:</strong>&nbsp;<code>1 &lt;= N &lt;= 10 ^ 9</code>.</p><p>给定一个正整数 <code>N</code>，试求有多少组连续正整数满足所有数字之和为 <code>N</code>?</p>

<p><strong>示</strong><strong>例 1:</strong></p>

<pre>
<strong>输入: </strong>5
<strong>输出: </strong>2
<strong>解释: </strong>5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>9
<strong>输出: </strong>3
<strong>解释: </strong>9 = 9 = 4 + 5 = 2 + 3 + 4</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>15
<strong>输出: </strong>4
<strong>解释: </strong>15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5</pre>

<p><strong>说明:&nbsp;</strong><code>1 &lt;= N &lt;= 10 ^ 9</code></p>
<p>给定一个正整数 <code>N</code>，试求有多少组连续正整数满足所有数字之和为 <code>N</code>?</p>

<p><strong>示</strong><strong>例 1:</strong></p>

<pre>
<strong>输入: </strong>5
<strong>输出: </strong>2
<strong>解释: </strong>5 = 5 = 2 + 3，共有两组连续整数([5],[2,3])求和后为 5。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>9
<strong>输出: </strong>3
<strong>解释: </strong>9 = 9 = 4 + 5 = 2 + 3 + 4</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>15
<strong>输出: </strong>4
<strong>解释: </strong>15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5</pre>

<p><strong>说明:&nbsp;</strong><code>1 &lt;= N &lt;= 10 ^ 9</code></p>
"""


class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        