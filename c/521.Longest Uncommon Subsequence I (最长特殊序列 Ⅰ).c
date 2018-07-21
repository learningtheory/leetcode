/*
<p>
Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings.
The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be <b>any</b> subsequence of the other strings.
</p>

<p>
A <b>subsequence</b> is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
</p>

<p>
The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "aba", "cdc"
<b>Output:</b> 3
<b>Explanation:</b> The longest uncommon subsequence is "aba" (or "cdc"), <br/>because "aba" is a subsequence of "aba", <br/>but not a subsequence of any other strings in the group of two strings. 
</pre>
</p>

<p><b>Note:</b>
<ol>
<li>Both strings' lengths will not exceed 100.</li>
<li>Only letters from a ~ z will appear in input strings. </li>
</ol>
</p><p>给定两个字符串，你需要从这两个字符串中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。</p>

<p><strong>子序列</strong>可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。</p>

<p>输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。</p>

<p><strong>示例 :</strong></p>

<pre>
<strong>输入:</strong> &quot;aba&quot;, &quot;cdc&quot;
<strong>输出:</strong> 3
<strong>解析:</strong> 最长特殊序列可为 &quot;aba&quot; (或 &quot;cdc&quot;)
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>两个字符串长度均小于100。</li>
	<li>字符串中的字符仅含有&nbsp;&#39;a&#39;~&#39;z&#39;。</li>
</ol>
<p>给定两个字符串，你需要从这两个字符串中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。</p>

<p><strong>子序列</strong>可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。</p>

<p>输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。</p>

<p><strong>示例 :</strong></p>

<pre>
<strong>输入:</strong> &quot;aba&quot;, &quot;cdc&quot;
<strong>输出:</strong> 3
<strong>解析:</strong> 最长特殊序列可为 &quot;aba&quot; (或 &quot;cdc&quot;)
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>两个字符串长度均小于100。</li>
	<li>字符串中的字符仅含有&nbsp;&#39;a&#39;~&#39;z&#39;。</li>
</ol>
*/


int findLUSlength(char* a, char* b) {
    
}