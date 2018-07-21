/*
<p>A character is unique in string <code>S</code> if it occurs exactly once in it.</p>

<p>For example, in string <code>S = &quot;LETTER&quot;</code>, the only unique characters are <code>&quot;L&quot;</code> and <code>&quot;R&quot;</code>.</p>

<p>Let&#39;s define <code>UNIQ(S)</code> as the number of unique characters in string <code>S</code>.</p>

<p>For example, <code>UNIQ(&quot;LETTER&quot;) =&nbsp; 2</code>.</p>

<p>Given a string S, calculate the sum of <code>UNIQ(substring)</code> over all non-empty substrings of <code>S</code>.</p>

<p>If there are two or more equal substrings at different positions in <code>S</code>, we consider them different.</p>

<p>Since the answer can be very large, retrun the answer&nbsp;modulo&nbsp;<code>10 ^ 9 + 7</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>&quot;ABC&quot;
<strong>Output: </strong>10
<strong>Explanation: </strong>All possible substrings are: &quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;AB&quot;,&quot;BC&quot; and &quot;ABC&quot;.
Evey substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;ABA&quot;
<strong>Output: </strong>8
<strong>Explanation: </strong>The same as example 1, except uni(&quot;ABA&quot;) = 1.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong> <code>0 &lt;= S.length &lt;= 10000</code>.</p><p>如果一个字符在字符串&nbsp;<code>S</code>&nbsp;中有且仅有出现一次，那么我们称其为独特字符。</p>

<p>例如，在字符串&nbsp;<code>S = &quot;LETTER&quot;</code>&nbsp;中，<code>&quot;L&quot;</code>&nbsp;和&nbsp;<code>&quot;R&quot;</code>&nbsp;可以被称为独特字符。</p>

<p>我们再定义&nbsp;<code>UNIQ(S)</code>&nbsp;作为字符串&nbsp;<code>S</code>&nbsp;中独特字符的个数。</p>

<p>那么，在&nbsp;<code>S = &quot;LETTER&quot;</code>&nbsp;中，&nbsp;<code>UNIQ(&quot;LETTER&quot;) =&nbsp; 2</code>。</p>

<p>对于给定字符串&nbsp;<code>S</code>，计算其所有非空子串的独特字符的个数，即&nbsp;<code>UNIQ(substring)</code>。</p>

<p>如果出现两个或者多个相同的子串，将其认为是不同的两个子串。</p>

<p>考虑到答案可能会非常大，规定返回格式为：结果 mod&nbsp;<code>10 ^ 9 + 7</code>。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>&quot;ABC&quot;
<strong>输出: </strong>10
<strong>解释:</strong> 所有可能的子串为：&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;AB&quot;,&quot;BC&quot; 和 &quot;ABC&quot;。
     其中，每一个子串都由独特字符构成。
     所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>&quot;ABA&quot;
<strong>输出: </strong>8
<strong>解释: </strong>除了子串 UNIQ(&#39;ABA&#39;) = 1，其余与示例1相同。
</pre>

<p><strong>说明:</strong> <code>0 &lt;= S.length &lt;= 10000</code>。</p>
<p>如果一个字符在字符串&nbsp;<code>S</code>&nbsp;中有且仅有出现一次，那么我们称其为独特字符。</p>

<p>例如，在字符串&nbsp;<code>S = &quot;LETTER&quot;</code>&nbsp;中，<code>&quot;L&quot;</code>&nbsp;和&nbsp;<code>&quot;R&quot;</code>&nbsp;可以被称为独特字符。</p>

<p>我们再定义&nbsp;<code>UNIQ(S)</code>&nbsp;作为字符串&nbsp;<code>S</code>&nbsp;中独特字符的个数。</p>

<p>那么，在&nbsp;<code>S = &quot;LETTER&quot;</code>&nbsp;中，&nbsp;<code>UNIQ(&quot;LETTER&quot;) =&nbsp; 2</code>。</p>

<p>对于给定字符串&nbsp;<code>S</code>，计算其所有非空子串的独特字符的个数，即&nbsp;<code>UNIQ(substring)</code>。</p>

<p>如果出现两个或者多个相同的子串，将其认为是不同的两个子串。</p>

<p>考虑到答案可能会非常大，规定返回格式为：结果 mod&nbsp;<code>10 ^ 9 + 7</code>。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>&quot;ABC&quot;
<strong>输出: </strong>10
<strong>解释:</strong> 所有可能的子串为：&quot;A&quot;,&quot;B&quot;,&quot;C&quot;,&quot;AB&quot;,&quot;BC&quot; 和 &quot;ABC&quot;。
     其中，每一个子串都由独特字符构成。
     所以其长度总和为：1 + 1 + 1 + 2 + 2 + 3 = 10
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>&quot;ABA&quot;
<strong>输出: </strong>8
<strong>解释: </strong>除了子串 UNIQ(&#39;ABA&#39;) = 1，其余与示例1相同。
</pre>

<p><strong>说明:</strong> <code>0 &lt;= S.length &lt;= 10000</code>。</p>
*/


func uniqueLetterString(S string) int {
    
}