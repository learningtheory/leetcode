=begin
<p>
<i>Special</i> binary strings are binary strings with the following two properties:
</p><p>
<li>The number of 0's is equal to the number of 1's.</li>
<li>Every prefix of the binary string has at least as many 1's as 0's.</li>
</p><p>
Given a special string <code>S</code>, a <i>move</i> consists of choosing two consecutive, non-empty, special substrings of <code>S</code>, and swapping them.  <i>(Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)</i>
</p><p>
At the end of any number of moves, what is the lexicographically largest resulting string possible?
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> S = "11011000"
<b>Output:</b> "11100100"
<b>Explanation:</b>
The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
</pre>
</p>

<p><b>Note:</b><ol>
<li><code>S</code> has length at most <code>50</code>.</li>
<li><code>S</code> is guaranteed to be a <i>special</i> binary string as defined above.</li>
</ol></p><p>特殊的二进制序列是具有以下两个性质的二进制序列：</p>

<ul>
	<li>0 的数量与 1 的数量相等。</li>
	<li>二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量。</li>
</ul>

<p>给定一个特殊的二进制序列&nbsp;<code>S</code>，以字符串形式表示。定义一个<em>操作 </em>为首先选择&nbsp;<code>S</code>&nbsp;的两个连续且非空的特殊的子串，然后将它们交换。（两个子串为连续的当且仅当第一个子串的最后一个字符恰好为第二个子串的第一个字符的前一个字符。)</p>

<p>在任意次数的操作之后，交换后的字符串按照字典序排列的最大的结果是什么？</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> S = &quot;11011000&quot;
<strong>输出:</strong> &quot;11100100&quot;
<strong>解释:</strong>
将子串 &quot;10&quot; （在S[1]出现） 和 &quot;1100&quot; （在S[3]出现）进行交换。
这是在进行若干次操作后按字典序排列最大的结果。
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li><code>S</code>&nbsp;的长度不超过&nbsp;<code>50</code>。</li>
	<li><code>S</code>&nbsp;保证为一个满足上述定义的<em>特殊 </em>的二进制序列。</li>
</ol>
<p>特殊的二进制序列是具有以下两个性质的二进制序列：</p>

<ul>
	<li>0 的数量与 1 的数量相等。</li>
	<li>二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量。</li>
</ul>

<p>给定一个特殊的二进制序列&nbsp;<code>S</code>，以字符串形式表示。定义一个<em>操作 </em>为首先选择&nbsp;<code>S</code>&nbsp;的两个连续且非空的特殊的子串，然后将它们交换。（两个子串为连续的当且仅当第一个子串的最后一个字符恰好为第二个子串的第一个字符的前一个字符。)</p>

<p>在任意次数的操作之后，交换后的字符串按照字典序排列的最大的结果是什么？</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> S = &quot;11011000&quot;
<strong>输出:</strong> &quot;11100100&quot;
<strong>解释:</strong>
将子串 &quot;10&quot; （在S[1]出现） 和 &quot;1100&quot; （在S[3]出现）进行交换。
这是在进行若干次操作后按字典序排列最大的结果。
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li><code>S</code>&nbsp;的长度不超过&nbsp;<code>50</code>。</li>
	<li><code>S</code>&nbsp;保证为一个满足上述定义的<em>特殊 </em>的二进制序列。</li>
</ol>

=end


# @param {String} s
# @return {String}
def make_largest_special(s)
    
end