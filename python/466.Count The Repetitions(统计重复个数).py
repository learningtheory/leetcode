"""
<p>Define <code>S = [s,n]</code> as the string S which consists of n connected strings s. For example, <code>["abc", 3]</code> ="abcabcabc". </p>
<p>On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, “abc”  can be obtained from “abdbec” based on our definition, but it can not be obtained from “acbbe”.</p>
<p>You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 &le; n1 &le; 10<sup>6</sup> and 1 &le; n2 &le; 10<sup>6</sup>. Now consider the strings S1 and S2, where <code>S1=[s1,n1]</code> and <code>S2=[s2,n2]</code>. Find the maximum integer M such that <code>[S2,M]</code> can be obtained from <code>S1</code>.</p>

<p><b>Example:</b>
<pre>
Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
</pre>
</p><p>定义由 n 个连接的字符串 s 组成字符串 S，即&nbsp;<code>S = [s,n]</code>。例如，<code>[&quot;abc&quot;, 3]</code>=&ldquo;abcabcabc&rdquo;。</p>

<p>另一方面，如果我们可以从 s<sub>2&nbsp;</sub>中删除某些字符使其变为 s<sub>1</sub>，我们称字符串 s<sub>1&nbsp;</sub>可以从字符串 s<sub>2&nbsp;</sub>获得。例如，&ldquo;abc&rdquo; 可以根据我们的定义从 &ldquo;abdbec&rdquo; 获得，但不能从 &ldquo;acbbe&rdquo; 获得。</p>

<p>现在给出两个非空字符串 S<sub>1&nbsp;</sub>和 S<sub>2</sub>（每个最多 100 个字符长）和两个整数 0 &le; N<sub>1&nbsp;</sub>&le; 10<sup>6&nbsp;</sup>和 1 &le; N<sub>2&nbsp;</sub>&le; 10<sup>6</sup>。现在考虑字符串 S<sub>1&nbsp;</sub>和 S<sub>2</sub>，其中<code>S1=[s1,n1]</code>和<code>S2=[s2,n2]</code>。找出可以使<code>[S2,M]</code>从&nbsp;<code>S1</code>&nbsp;获得的最大整数 M。</p>

<p><strong>示例：</strong></p>

<pre>输入：
s1 =&quot;acb&quot;,n1 = 4
s2 =&quot;ab&quot;,n2 = 2

返回：
2
</pre>
<p>定义由 n 个连接的字符串 s 组成字符串 S，即&nbsp;<code>S = [s,n]</code>。例如，<code>[&quot;abc&quot;, 3]</code>=&ldquo;abcabcabc&rdquo;。</p>

<p>另一方面，如果我们可以从 s<sub>2&nbsp;</sub>中删除某些字符使其变为 s<sub>1</sub>，我们称字符串 s<sub>1&nbsp;</sub>可以从字符串 s<sub>2&nbsp;</sub>获得。例如，&ldquo;abc&rdquo; 可以根据我们的定义从 &ldquo;abdbec&rdquo; 获得，但不能从 &ldquo;acbbe&rdquo; 获得。</p>

<p>现在给出两个非空字符串 S<sub>1&nbsp;</sub>和 S<sub>2</sub>（每个最多 100 个字符长）和两个整数 0 &le; N<sub>1&nbsp;</sub>&le; 10<sup>6&nbsp;</sup>和 1 &le; N<sub>2&nbsp;</sub>&le; 10<sup>6</sup>。现在考虑字符串 S<sub>1&nbsp;</sub>和 S<sub>2</sub>，其中<code>S1=[s1,n1]</code>和<code>S2=[s2,n2]</code>。找出可以使<code>[S2,M]</code>从&nbsp;<code>S1</code>&nbsp;获得的最大整数 M。</p>

<p><strong>示例：</strong></p>

<pre>输入：
s1 =&quot;acb&quot;,n1 = 4
s2 =&quot;ab&quot;,n2 = 2

返回：
2
</pre>
"""


class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        