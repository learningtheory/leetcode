"""
<p>Given a string, find the length of the <b>longest substring</b> without repeating characters.</p>

<p><b>Examples:</b></p>

<p>Given <code>"abcabcbb"</code>, the answer is <code>"abc"</code>, which the length is 3.</p>

<p>Given <code>"bbbbb"</code>, the answer is <code>"b"</code>, with the length of 1.</p>

<p>Given <code>"pwwkew"</code>, the answer is <code>"wke"</code>, with the length of 3. Note that the answer must be a <b>substring</b>, <code>"pwke"</code> is a <i>subsequence</i> and not a substring.</p><p>给定一个字符串，找出不含有重复字符的<strong>最长子串</strong>的长度。</p>

<p><strong>示例：</strong></p>

<p>给定&nbsp;<code>&quot;abcabcbb&quot;</code>&nbsp;，没有重复字符的最长子串是&nbsp;<code>&quot;abc&quot;</code>&nbsp;，那么长度就是3。</p>

<p>给定&nbsp;<code>&quot;bbbbb&quot;</code>&nbsp;，最长的子串就是&nbsp;<code>&quot;b&quot;</code>&nbsp;，长度是1。</p>

<p>给定&nbsp;<code>&quot;pwwkew&quot;</code>&nbsp;，最长子串是&nbsp;<code>&quot;wke&quot;</code>&nbsp;，长度是3。请注意答案必须是一个<strong>子串</strong>，<code>&quot;pwke&quot;</code>&nbsp;是&nbsp;<em>子序列&nbsp;&nbsp;</em>而不是子串。</p>
<p>给定一个字符串，找出不含有重复字符的<strong>最长子串</strong>的长度。</p>

<p><strong>示例：</strong></p>

<p>给定&nbsp;<code>&quot;abcabcbb&quot;</code>&nbsp;，没有重复字符的最长子串是&nbsp;<code>&quot;abc&quot;</code>&nbsp;，那么长度就是3。</p>

<p>给定&nbsp;<code>&quot;bbbbb&quot;</code>&nbsp;，最长的子串就是&nbsp;<code>&quot;b&quot;</code>&nbsp;，长度是1。</p>

<p>给定&nbsp;<code>&quot;pwwkew&quot;</code>&nbsp;，最长子串是&nbsp;<code>&quot;wke&quot;</code>&nbsp;，长度是3。请注意答案必须是一个<strong>子串</strong>，<code>&quot;pwke&quot;</code>&nbsp;是&nbsp;<em>子序列&nbsp;&nbsp;</em>而不是子串。</p>
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        