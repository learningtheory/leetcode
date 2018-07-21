"""
<p>
    Given a list of <b>unique</b> words, find all pairs of <b><i>distinct</i></b> indices <code>(i, j)</code> in the given list, so that the concatenation of the two words, i.e. <code>words[i] + words[j]</code> is a palindrome.
</p>

<p>
    <b>Example 1:</b><br/>
    Given <code>words</code> = <code>["bat", "tab", "cat"]</code><br/>
    Return <code>[[0, 1], [1, 0]]</code><br/>
    The palindromes are <code>["battab", "tabbat"]</code><br/>
</p>
<p>
    <b>Example 2:</b><br/>
    Given <code>words</code> = <code>["abcd", "dcba", "lls", "s", "sssll"]</code><br/>
    Return <code>[[0, 1], [1, 0], [3, 2], [2, 4]]</code><br/>
    The palindromes are <code>["dcbaabcd", "abcddcba", "slls", "llssssll"]</code><br/>
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/discuss/user/dietpepsi">@dietpepsi</a> for adding this problem and creating all test cases.</p><p>给定一组<strong>唯一</strong>的单词， 找出所有<strong><em>不同&nbsp;</em></strong>的索引对<code>(i, j)</code>，使得列表中的两个单词，&nbsp;<code>words[i] + words[j]</code>&nbsp;，可拼接成回文串。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>[&quot;abcd&quot;,&quot;dcba&quot;,&quot;lls&quot;,&quot;s&quot;,&quot;sssll&quot;]
<strong>输出: </strong>[[0,1],[1,0],[3,2],[2,4]] 
<strong>解释: </strong>可拼接成的回文串为 <code>[&quot;dcbaabcd&quot;,&quot;abcddcba&quot;,&quot;slls&quot;,&quot;llssssll&quot;]</code>
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>[&quot;bat&quot;,&quot;tab&quot;,&quot;cat&quot;]
<strong>输出: </strong>[[0,1],[1,0]] 
<strong>解释: </strong>可拼接成的回文串为 <code>[&quot;battab&quot;,&quot;tabbat&quot;]</code></pre>
<p>给定一组<strong>唯一</strong>的单词， 找出所有<strong><em>不同&nbsp;</em></strong>的索引对<code>(i, j)</code>，使得列表中的两个单词，&nbsp;<code>words[i] + words[j]</code>&nbsp;，可拼接成回文串。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>[&quot;abcd&quot;,&quot;dcba&quot;,&quot;lls&quot;,&quot;s&quot;,&quot;sssll&quot;]
<strong>输出: </strong>[[0,1],[1,0],[3,2],[2,4]] 
<strong>解释: </strong>可拼接成的回文串为 <code>[&quot;dcbaabcd&quot;,&quot;abcddcba&quot;,&quot;slls&quot;,&quot;llssssll&quot;]</code>
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>[&quot;bat&quot;,&quot;tab&quot;,&quot;cat&quot;]
<strong>输出: </strong>[[0,1],[1,0]] 
<strong>解释: </strong>可拼接成的回文串为 <code>[&quot;battab&quot;,&quot;tabbat&quot;]</code></pre>
"""


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        