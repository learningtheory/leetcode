"""
<p>
A string <code>S</code> of lowercase letters is given.  We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
</p><p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> S = "ababcbacadefegdehijhklij"
<b>Output:</b> [9,7,8]
<b>Explanation:</b>
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
</pre>
</p>

<p><b>Note:</b><br><ol>
<li><code>S</code> will have length in range <code>[1, 500]</code>.</li>
<li><code>S</code> will consist of lowercase letters (<code>'a'</code> to <code>'z'</code>) only.</li>
</ol></p><p>字符串 <code>S</code> 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> S = &quot;ababcbacadefegdehijhklij&quot;
<strong>输出:</strong> [9,7,8]
<strong>解释:</strong>
划分结果为 &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;。
每个字母最多出现在一个片段中。
像 &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; 的划分是错误的，因为划分的片段数较少。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>S</code>的长度在<code>[1, 500]</code>之间。</li>
	<li><code>S</code>只包含小写字母<code>&#39;a&#39;</code>到<code>&#39;z&#39;</code>。</li>
</ol>
<p>字符串 <code>S</code> 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> S = &quot;ababcbacadefegdehijhklij&quot;
<strong>输出:</strong> [9,7,8]
<strong>解释:</strong>
划分结果为 &quot;ababcbaca&quot;, &quot;defegde&quot;, &quot;hijhklij&quot;。
每个字母最多出现在一个片段中。
像 &quot;ababcbacadefegde&quot;, &quot;hijhklij&quot; 的划分是错误的，因为划分的片段数较少。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>S</code>的长度在<code>[1, 500]</code>之间。</li>
	<li><code>S</code>只包含小写字母<code>&#39;a&#39;</code>到<code>&#39;z&#39;</code>。</li>
</ol>
"""


class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """