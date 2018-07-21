"""
<p>You are given a string, <strong>s</strong>, and a list of words, <strong>words</strong>, that are all of the same length. Find all starting indices of substring(s) in <strong>s</strong> that is a concatenation of each word in <strong>words</strong> exactly once and without any intervening characters.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:
  s =</strong> &quot;barfoothefoobarman&quot;,
<strong>  words = </strong>[&quot;foo&quot;,&quot;bar&quot;]
<strong>Output:</strong> <code>[0,9]</code>
<strong>Explanation:</strong> Substrings starting at index 0 and 9 are &quot;barfoor&quot; and &quot;foobar&quot; respectively.
The output order does not matter, returning [9,0] is fine too.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:
  s =</strong> &quot;wordgoodstudentgoodword&quot;,
<strong>  words = </strong>[&quot;word&quot;,&quot;student&quot;]
<strong>Output:</strong> <code>[]</code>
</pre>
<p>给定一个字符串&nbsp;<strong>s&nbsp;</strong>和一些长度相同的单词&nbsp;<strong>words。</strong>在<strong> s </strong>中找出可以恰好串联&nbsp;<strong>words&nbsp;</strong>中所有单词的子串的起始位置。</p>

<p>注意子串要与&nbsp;<strong>words </strong>中的单词完全匹配，中间不能有其他字符，但不需要考虑&nbsp;<strong>words&nbsp;</strong>中单词串联的顺序。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:
  s =</strong> &quot;barfoothefoobarman&quot;,
<strong>  words = </strong>[&quot;foo&quot;,&quot;bar&quot;]
<strong>输出:</strong> <code>[0,9]</code>
<strong>解释:</strong> 从索引 0 和 9 开始的子串分别是 &quot;barfoor&quot; 和 &quot;foobar&quot; 。
输出的顺序不重要, [9,0] 也是有效答案。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:
  s =</strong> &quot;wordgoodstudentgoodword&quot;,
<strong>  words = </strong>[&quot;word&quot;,&quot;student&quot;]
<strong>输出:</strong> <code>[]</code>
</pre>
<p>给定一个字符串&nbsp;<strong>s&nbsp;</strong>和一些长度相同的单词&nbsp;<strong>words。</strong>在<strong> s </strong>中找出可以恰好串联&nbsp;<strong>words&nbsp;</strong>中所有单词的子串的起始位置。</p>

<p>注意子串要与&nbsp;<strong>words </strong>中的单词完全匹配，中间不能有其他字符，但不需要考虑&nbsp;<strong>words&nbsp;</strong>中单词串联的顺序。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:
  s =</strong> &quot;barfoothefoobarman&quot;,
<strong>  words = </strong>[&quot;foo&quot;,&quot;bar&quot;]
<strong>输出:</strong> <code>[0,9]</code>
<strong>解释:</strong> 从索引 0 和 9 开始的子串分别是 &quot;barfoor&quot; 和 &quot;foobar&quot; 。
输出的顺序不重要, [9,0] 也是有效答案。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:
  s =</strong> &quot;wordgoodstudentgoodword&quot;,
<strong>  words = </strong>[&quot;word&quot;,&quot;student&quot;]
<strong>输出:</strong> <code>[]</code>
</pre>
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        