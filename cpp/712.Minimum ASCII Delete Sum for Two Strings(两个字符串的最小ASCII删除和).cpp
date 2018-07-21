/*
<p>Given two strings <code>s1, s2</code>, find the lowest ASCII sum of deleted characters to make two strings equal.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> s1 = "sea", s2 = "eat"
<b>Output:</b> 231
<b>Explanation:</b> Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> s1 = "delete", s2 = "leet"
<b>Output:</b> 403
<b>Explanation:</b> Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
</pre>
</p>

<p><b>Note:</b>
<li><code>0 < s1.length, s2.length <= 1000</code>.</li>
<li>All elements of each string will have an ASCII value in <code>[97, 122]</code>.</li> 
</p><p>给定两个字符串<code>s1, s2</code>，找到使两个字符串相等所需删除字符的ASCII值的最小和。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> s1 = &quot;sea&quot;, s2 = &quot;eat&quot;
<strong>输出:</strong> 231
<strong>解释:</strong> 在 &quot;sea&quot; 中删除 &quot;s&quot; 并将 &quot;s&quot; 的值(115)加入总和。
在 &quot;eat&quot; 中删除 &quot;t&quot; 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> s1 = &quot;delete&quot;, s2 = &quot;leet&quot;
<strong>输出:</strong> 403
<strong>解释:</strong> 在 &quot;delete&quot; 中删除 &quot;dee&quot; 字符串变成 &quot;let&quot;，
将 100[d]+101[e]+101[e] 加入总和。在 &quot;leet&quot; 中删除 &quot;e&quot; 将 101[e] 加入总和。
结束时，两个字符串都等于 &quot;let&quot;，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 &quot;lee&quot; 或 &quot;eet&quot;，我们会得到 433 或 417 的结果，比答案更大。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>0 &lt; s1.length, s2.length &lt;= 1000</code>。</li>
	<li>所有字符串中的字符ASCII值在<code>[97, 122]</code>之间。</li>
</ul>
<p>给定两个字符串<code>s1, s2</code>，找到使两个字符串相等所需删除字符的ASCII值的最小和。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> s1 = &quot;sea&quot;, s2 = &quot;eat&quot;
<strong>输出:</strong> 231
<strong>解释:</strong> 在 &quot;sea&quot; 中删除 &quot;s&quot; 并将 &quot;s&quot; 的值(115)加入总和。
在 &quot;eat&quot; 中删除 &quot;t&quot; 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> s1 = &quot;delete&quot;, s2 = &quot;leet&quot;
<strong>输出:</strong> 403
<strong>解释:</strong> 在 &quot;delete&quot; 中删除 &quot;dee&quot; 字符串变成 &quot;let&quot;，
将 100[d]+101[e]+101[e] 加入总和。在 &quot;leet&quot; 中删除 &quot;e&quot; 将 101[e] 加入总和。
结束时，两个字符串都等于 &quot;let&quot;，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 &quot;lee&quot; 或 &quot;eet&quot;，我们会得到 433 或 417 的结果，比答案更大。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>0 &lt; s1.length, s2.length &lt;= 1000</code>。</li>
	<li>所有字符串中的字符ASCII值在<code>[97, 122]</code>之间。</li>
</ul>
*/


class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        
    }
};