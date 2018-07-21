"""
<p>
Given a list of sorted characters <code>letters</code> containing only lowercase letters, and given a target letter <code>target</code>, find the smallest element in the list that is larger than the given target.
</p><p>
Letters also wrap around.  For example, if the target is <code>target = 'z'</code> and <code>letters = ['a', 'b']</code>, the answer is <code>'a'</code>.
</p>

<p><b>Examples:</b><br />
<pre>
<b>Input:</b>
letters = ["c", "f", "j"]
target = "a"
<b>Output:</b> "c"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "c"
<b>Output:</b> "f"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "d"
<b>Output:</b> "f"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "g"
<b>Output:</b> "j"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "j"
<b>Output:</b> "c"

<b>Input:</b>
letters = ["c", "f", "j"]
target = "k"
<b>Output:</b> "c"
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>letters</code> has a length in range <code>[2, 10000]</code>.</li>
<li><code>letters</code> consists of lowercase letters, and contains at least 2 unique letters.</li>
<li><code>target</code> is a lowercase letter.</li>
</ol>
</p><p>给定一个只包含小写字母的有序数组<code>letters</code>&nbsp;和一个目标字母&nbsp;<code>target</code>，寻找有序数组里面比目标字母大的最小字母。</p>

<p>数组里字母的顺序是循环的。举个例子，如果目标字母<code>target = &#39;z&#39;</code> 并且有序数组为&nbsp;<code>letters = [&#39;a&#39;, &#39;b&#39;]</code>，则答案返回&nbsp;<code>&#39;a&#39;</code>。</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;a&quot;
<strong>输出:</strong> &quot;c&quot;

<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;c&quot;
<strong>输出:</strong> &quot;f&quot;

<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;d&quot;
<strong>输出:</strong> &quot;f&quot;

<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;g&quot;
<strong>输出:</strong> &quot;j&quot;

<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;j&quot;
<strong>输出:</strong> &quot;c&quot;

<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;k&quot;
<strong>输出:</strong> &quot;c&quot;
</pre>

<p><strong>注:</strong></p>

<ol>
	<li><code>letters</code>长度范围在<code>[2, 10000]</code>区间内。</li>
	<li><code>letters</code> 仅由小写字母组成，最少包含两个不同的字母。</li>
	<li>目标字母<code>target</code> 是一个小写字母。</li>
</ol>
<p>给定一个只包含小写字母的有序数组<code>letters</code>&nbsp;和一个目标字母&nbsp;<code>target</code>，寻找有序数组里面比目标字母大的最小字母。</p>

<p>数组里字母的顺序是循环的。举个例子，如果目标字母<code>target = &#39;z&#39;</code> 并且有序数组为&nbsp;<code>letters = [&#39;a&#39;, &#39;b&#39;]</code>，则答案返回&nbsp;<code>&#39;a&#39;</code>。</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;a&quot;
<strong>输出:</strong> &quot;c&quot;

<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;c&quot;
<strong>输出:</strong> &quot;f&quot;

<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;d&quot;
<strong>输出:</strong> &quot;f&quot;

<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;g&quot;
<strong>输出:</strong> &quot;j&quot;

<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;j&quot;
<strong>输出:</strong> &quot;c&quot;

<strong>输入:</strong>
letters = [&quot;c&quot;, &quot;f&quot;, &quot;j&quot;]
target = &quot;k&quot;
<strong>输出:</strong> &quot;c&quot;
</pre>

<p><strong>注:</strong></p>

<ol>
	<li><code>letters</code>长度范围在<code>[2, 10000]</code>区间内。</li>
	<li><code>letters</code> 仅由小写字母组成，最少包含两个不同的字母。</li>
	<li>目标字母<code>target</code> 是一个小写字母。</li>
</ol>
"""


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        