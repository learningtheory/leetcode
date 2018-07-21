/**
<p>
Given a string S, find the number of different non-empty palindromic subsequences in S, and <b>return that number modulo <code>10^9 + 7</code>.</b>
</p><p>
A subsequence of a string S is obtained by deleting 0 or more characters from S.
</p><p>
A sequence is palindromic if it is equal to the sequence reversed.
</p><p>
Two sequences <code>A_1, A_2, ...</code> and <code>B_1, B_2, ...</code> are different if there is some <code>i</code> for which <code>A_i != B_i</code>.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
S = 'bccb'
<b>Output:</b> 6
<b>Explanation:</b> 
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
<b>Output:</b> 104860361
<b>Explanation:</b> 
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>S</code> will be in the range <code>[1, 1000]</code>.</li>
<li>Each character <code>S[i]</code> will be in the set <code>{'a', 'b', 'c', 'd'}</code>.</li>
</p><p>给定一个字符串 S，找出 S 中不同的非空回文子字符串个数，并<strong>返回该数字与 <code>10^9 + 7 </code>的模。</strong></p>

<p>通过从 S 中删除 0 个或多个字符来获得子字符串。</p>

<p>如果一个字符串字符序列与它的反转字符串字符序列一致，那么它是回文字符串。</p>

<p>如果对于某个&nbsp;<code>i</code>， <code>A_i != B_i</code>，那么<code>A_1, A_2, ...</code> 和&nbsp;<code>B_1, B_2, ...</code> 这两个字符串是不同的。</p>

<p><strong>示例1:</strong></p>

<pre><strong>输入:</strong> 
S = &#39;bccb&#39;
<strong>输出:</strong> 6
<strong>解释:</strong> 
6个不同的非空回文子字符串分别为： &#39;b&#39;, &#39;c&#39;, &#39;bb&#39;, &#39;cc&#39;, &#39;bcb&#39;, &#39;bccb&#39;。
注意： &#39;bcb&#39; 虽然出现两次但仅计数一次。
</pre>

<p>&nbsp;</p>

<p><strong>样例2:</strong></p>

<pre><strong>输入:</strong> 
S = &#39;abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba&#39;
<strong>输出:</strong> 104860361
<strong>解释:</strong> 
共有 3104860382 个不同的非空回文子字符串，对 10^9 + 7 取模为 104860361。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>字符串&nbsp;<code>S</code>&nbsp;的长度将在<code>[1, 1000]</code>范围内。</li>
	<li>每个字符<code>S[i]</code>将会是集合&nbsp;<code>{&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;}</code>&nbsp;中的某一个。</li>
</ul>

<p>&nbsp;</p>
<p>给定一个字符串 S，找出 S 中不同的非空回文子字符串个数，并<strong>返回该数字与 <code>10^9 + 7 </code>的模。</strong></p>

<p>通过从 S 中删除 0 个或多个字符来获得子字符串。</p>

<p>如果一个字符串字符序列与它的反转字符串字符序列一致，那么它是回文字符串。</p>

<p>如果对于某个&nbsp;<code>i</code>， <code>A_i != B_i</code>，那么<code>A_1, A_2, ...</code> 和&nbsp;<code>B_1, B_2, ...</code> 这两个字符串是不同的。</p>

<p><strong>示例1:</strong></p>

<pre><strong>输入:</strong> 
S = &#39;bccb&#39;
<strong>输出:</strong> 6
<strong>解释:</strong> 
6个不同的非空回文子字符串分别为： &#39;b&#39;, &#39;c&#39;, &#39;bb&#39;, &#39;cc&#39;, &#39;bcb&#39;, &#39;bccb&#39;。
注意： &#39;bcb&#39; 虽然出现两次但仅计数一次。
</pre>

<p>&nbsp;</p>

<p><strong>样例2:</strong></p>

<pre><strong>输入:</strong> 
S = &#39;abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba&#39;
<strong>输出:</strong> 104860361
<strong>解释:</strong> 
共有 3104860382 个不同的非空回文子字符串，对 10^9 + 7 取模为 104860361。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>字符串&nbsp;<code>S</code>&nbsp;的长度将在<code>[1, 1000]</code>范围内。</li>
	<li>每个字符<code>S[i]</code>将会是集合&nbsp;<code>{&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;}</code>&nbsp;中的某一个。</li>
</ul>

<p>&nbsp;</p>
**/


class Solution {
    public int countPalindromicSubsequences(String S) {
        
    }
}