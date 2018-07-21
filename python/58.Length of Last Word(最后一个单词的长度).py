"""
<p>Given a string <i>s</i> consists of upper/lower-case alphabets and empty space characters <code>' '</code>, return the length of last word in the string.</p>

<p>If the last word does not exist, return 0.</p>

<p><b>Note:</b> A word is defined as a character sequence consists of non-space characters only.</p>

<p><b>Example:</b>
<pre>
<b>Input:</b> "Hello World"
<b>Output:</b> 5
</pre>
</p><p>给定一个仅包含大小写字母和空格&nbsp;<code>&#39; &#39;</code>&nbsp;的字符串，返回其最后一个单词的长度。</p>

<p>如果不存在最后一个单词，请返回 0&nbsp;。</p>

<p><strong>说明：</strong>一个单词是指由字母组成，但不包含任何空格的字符串。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> &quot;Hello World&quot;
<strong>输出:</strong> 5
</pre>
<p>给定一个仅包含大小写字母和空格&nbsp;<code>&#39; &#39;</code>&nbsp;的字符串，返回其最后一个单词的长度。</p>

<p>如果不存在最后一个单词，请返回 0&nbsp;。</p>

<p><strong>说明：</strong>一个单词是指由字母组成，但不包含任何空格的字符串。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> &quot;Hello World&quot;
<strong>输出:</strong> 5
</pre>
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        