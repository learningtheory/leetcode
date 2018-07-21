"""
Given two strings <b>s1</b> and <b>s2</b>, write a function to return true if <b>s2</b> contains the permutation of <b>s1</b>. In other words, one of the first string's permutations is the <b>substring</b> of the second string.

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>s1 = "ab" s2 = "eidbaooo"
<b>Output:</b>True
<b>Explanation:</b> s2 contains one permutation of s1 ("ba").
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>s1= "ab" s2 = "eidboaoo"
<b>Output:</b> False
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The input strings only contain lower case letters.</li>
<li>The length of both given strings is in range [1, 10,000].</li>
</ol>
</p><p>给定两个字符串&nbsp;<strong>s1</strong>&nbsp;和&nbsp;<strong>s2</strong>，写一个函数来判断 <strong>s2</strong> 是否包含 <strong>s1&nbsp;</strong>的排列。</p>

<p>换句话说，第一个字符串的排列之一是第二个字符串的子串。</p>

<p><strong>示例1:</strong></p>

<pre>
<strong>输入: </strong>s1 = &quot;ab&quot; s2 = &quot;eidbaooo&quot;
<strong>输出: </strong>True
<strong>解释:</strong> s2 包含 s1 的排列之一 (&quot;ba&quot;).
</pre>

<p>&nbsp;</p>

<p><strong>示例2:</strong></p>

<pre>
<strong>输入: </strong>s1= &quot;ab&quot; s2 = &quot;eidboaoo&quot;
<strong>输出:</strong> False
</pre>

<p>&nbsp;</p>

<p><strong>注意：</strong></p>

<ol>
	<li>输入的字符串只包含小写字母</li>
	<li>两个字符串的长度都在 [1, 10,000] 之间</li>
</ol>
<p>给定两个字符串&nbsp;<strong>s1</strong>&nbsp;和&nbsp;<strong>s2</strong>，写一个函数来判断 <strong>s2</strong> 是否包含 <strong>s1&nbsp;</strong>的排列。</p>

<p>换句话说，第一个字符串的排列之一是第二个字符串的子串。</p>

<p><strong>示例1:</strong></p>

<pre>
<strong>输入: </strong>s1 = &quot;ab&quot; s2 = &quot;eidbaooo&quot;
<strong>输出: </strong>True
<strong>解释:</strong> s2 包含 s1 的排列之一 (&quot;ba&quot;).
</pre>

<p>&nbsp;</p>

<p><strong>示例2:</strong></p>

<pre>
<strong>输入: </strong>s1= &quot;ab&quot; s2 = &quot;eidboaoo&quot;
<strong>输出:</strong> False
</pre>

<p>&nbsp;</p>

<p><strong>注意：</strong></p>

<ol>
	<li>输入的字符串只包含小写字母</li>
	<li>两个字符串的长度都在 [1, 10,000] 之间</li>
</ol>
"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        