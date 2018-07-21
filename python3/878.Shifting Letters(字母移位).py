"""
<p>We have a string <code>S</code> of lowercase letters, and an integer array <code>shifts</code>.</p>

<p>Call the <em>shift</em> of a letter, the next letter in the alphabet, (wrapping around so that <code>&#39;z&#39;</code> becomes <code>&#39;a&#39;</code>).&nbsp;</p>

<p>For example, <code>shift(&#39;a&#39;) = &#39;b&#39;</code>, <code>shift(&#39;t&#39;) = &#39;u&#39;</code>, and <code>shift(&#39;z&#39;) = &#39;a&#39;</code>.</p>

<p>Now for each <code>shifts[i] = x</code>, we want to shift the first <code>i+1</code>&nbsp;letters of <code>S</code>, <code>x</code> times.</p>

<p>Return the final string&nbsp;after all such shifts to <code>S</code> are applied.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = &quot;abc&quot;, shifts = [3,5,9]
<strong>Output: </strong>&quot;rpl&quot;
<strong>Explanation: </strong>
We start with &quot;abc&quot;.
After shifting the first 1 letters of S by 3, we have &quot;dbc&quot;.
After shifting the first 2 letters of S by 5, we have &quot;igc&quot;.
After shifting the first 3 letters of S by 9, we have &quot;rpl&quot;, the answer.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= S.length = shifts.length &lt;= 20000</code></li>
	<li><code>0 &lt;= shifts[i] &lt;= 10 ^ 9</code></li>
</ol><p>有一个由小写字母组成的字符串 <code>S</code>，和一个整数数组 <code>shifts</code>。</p>

<p>我们将字母表中的下一个字母称为原字母的 <em>移位</em>（由于字母表是环绕的， <code>&#39;z&#39;</code>&nbsp;将会变成&nbsp;<code>&#39;a&#39;</code>）。</p>

<p>例如&middot;，<code>shift(&#39;a&#39;) = &#39;b&#39;</code>，&nbsp;<code>shift(&#39;t&#39;) = &#39;u&#39;</code>,， 以及&nbsp;<code>shift(&#39;z&#39;) = &#39;a&#39;</code>。</p>

<p>对于每个&nbsp;<code>shifts[i] = x</code>&nbsp;， 我们会将 <code>S</code>&nbsp;中的前&nbsp;<code>i+1</code>&nbsp;个字母移位&nbsp;<code>x</code>&nbsp;次。</p>

<p>返回将所有这些移位都应用到 <code>S</code> 后最终得到的字符串。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>S = &quot;abc&quot;, shifts = [3,5,9]
<strong>输出：</strong>&quot;rpl&quot;
<strong>解释： </strong>
我们以 &quot;abc&quot; 开始。
将 S 中的第 1 个字母移位 3 次后，我们得到 &quot;dbc&quot;。
再将 S 中的前 2 个字母移位 5 次后，我们得到 &quot;igc&quot;。
最后将 S 中的这 3 个字母移位 9 次后，我们得到答案 &quot;rpl&quot;。
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= S.length = shifts.length &lt;= 20000</code></li>
	<li><code>0 &lt;= shifts[i] &lt;= 10 ^ 9</code></li>
</ol>
<p>有一个由小写字母组成的字符串 <code>S</code>，和一个整数数组 <code>shifts</code>。</p>

<p>我们将字母表中的下一个字母称为原字母的 <em>移位</em>（由于字母表是环绕的， <code>&#39;z&#39;</code>&nbsp;将会变成&nbsp;<code>&#39;a&#39;</code>）。</p>

<p>例如&middot;，<code>shift(&#39;a&#39;) = &#39;b&#39;</code>，&nbsp;<code>shift(&#39;t&#39;) = &#39;u&#39;</code>,， 以及&nbsp;<code>shift(&#39;z&#39;) = &#39;a&#39;</code>。</p>

<p>对于每个&nbsp;<code>shifts[i] = x</code>&nbsp;， 我们会将 <code>S</code>&nbsp;中的前&nbsp;<code>i+1</code>&nbsp;个字母移位&nbsp;<code>x</code>&nbsp;次。</p>

<p>返回将所有这些移位都应用到 <code>S</code> 后最终得到的字符串。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>S = &quot;abc&quot;, shifts = [3,5,9]
<strong>输出：</strong>&quot;rpl&quot;
<strong>解释： </strong>
我们以 &quot;abc&quot; 开始。
将 S 中的第 1 个字母移位 3 次后，我们得到 &quot;dbc&quot;。
再将 S 中的前 2 个字母移位 5 次后，我们得到 &quot;igc&quot;。
最后将 S 中的这 3 个字母移位 9 次后，我们得到答案 &quot;rpl&quot;。
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= S.length = shifts.length &lt;= 20000</code></li>
	<li><code>0 &lt;= shifts[i] &lt;= 10 ^ 9</code></li>
</ol>
"""


class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        