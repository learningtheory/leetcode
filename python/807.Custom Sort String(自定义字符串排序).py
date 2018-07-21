"""
<p><code>S</code> and <code>T</code> are strings composed of lowercase letters. In <code>S</code>, no letter occurs more than once.</p>

<p><code>S</code> was sorted in some custom order previously. We want to permute the characters of <code>T</code> so that they match the order that <code>S</code> was sorted. More specifically, if <code>x</code> occurs before <code>y</code> in <code>S</code>, then <code>x</code> should occur before <code>y</code> in the returned string.</p>

<p>Return any permutation of <code>T</code> (as a string) that satisfies this property.</p>

<pre>
<strong>Example :</strong>
<strong>Input:</strong> 
S = &quot;cba&quot;
T = &quot;abcd&quot;
<strong>Output:</strong> &quot;cbad&quot;
<strong>Explanation:</strong> 
&quot;a&quot;, &quot;b&quot;, &quot;c&quot; appear in S, so the order of &quot;a&quot;, &quot;b&quot;, &quot;c&quot; should be &quot;c&quot;, &quot;b&quot;, and &quot;a&quot;. 
Since &quot;d&quot; does not appear in S, it can be at any position in T. &quot;dcba&quot;, &quot;cdba&quot;, &quot;cbda&quot; are also valid outputs.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>S</code> has length at most <code>26</code>, and no character is repeated in <code>S</code>.</li>
	<li><code>T</code> has length at most <code>200</code>.</li>
	<li><code>S</code> and <code>T</code> consist of lowercase letters only.</li>
</ul>
<p>字符串<code>S</code>和 <code>T</code> 只包含小写字符。在<code>S</code>中，所有字符只会出现一次。</p>

<p><code>S</code> 已经根据某种规则进行了排序。我们要根据<code>S</code>中的字符顺序对<code>T</code>进行排序。更具体地说，如果<code>S</code>中<code>x</code>在<code>y</code>之前出现，那么返回的字符串中<code>x</code>也应出现在<code>y</code>之前。</p>

<p>返回任意一种符合条件的字符串<code>T</code>。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong>
S = &quot;cba&quot;
T = &quot;abcd&quot;
<strong>输出:</strong> &quot;cbad&quot;
<strong>解释:</strong> 
S中出现了字符 &quot;a&quot;, &quot;b&quot;, &quot;c&quot;, 所以 &quot;a&quot;, &quot;b&quot;, &quot;c&quot; 的顺序应该是 &quot;c&quot;, &quot;b&quot;, &quot;a&quot;. 
由于 &quot;d&quot; 没有在S中出现, 它可以放在T的任意位置. &quot;dcba&quot;, &quot;cdba&quot;, &quot;cbda&quot; 都是合法的输出。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>S</code>的最大长度为<code>26</code>，其中没有重复的字符。</li>
	<li><code>T</code>的最大长度为<code>200</code>。</li>
	<li><code>S</code>和<code>T</code>只包含小写字符。</li>
</ul>
<p>字符串<code>S</code>和 <code>T</code> 只包含小写字符。在<code>S</code>中，所有字符只会出现一次。</p>

<p><code>S</code> 已经根据某种规则进行了排序。我们要根据<code>S</code>中的字符顺序对<code>T</code>进行排序。更具体地说，如果<code>S</code>中<code>x</code>在<code>y</code>之前出现，那么返回的字符串中<code>x</code>也应出现在<code>y</code>之前。</p>

<p>返回任意一种符合条件的字符串<code>T</code>。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong>
S = &quot;cba&quot;
T = &quot;abcd&quot;
<strong>输出:</strong> &quot;cbad&quot;
<strong>解释:</strong> 
S中出现了字符 &quot;a&quot;, &quot;b&quot;, &quot;c&quot;, 所以 &quot;a&quot;, &quot;b&quot;, &quot;c&quot; 的顺序应该是 &quot;c&quot;, &quot;b&quot;, &quot;a&quot;. 
由于 &quot;d&quot; 没有在S中出现, 它可以放在T的任意位置. &quot;dcba&quot;, &quot;cdba&quot;, &quot;cbda&quot; 都是合法的输出。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>S</code>的最大长度为<code>26</code>，其中没有重复的字符。</li>
	<li><code>T</code>的最大长度为<code>200</code>。</li>
	<li><code>S</code>和<code>T</code>只包含小写字符。</li>
</ul>
"""


class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        