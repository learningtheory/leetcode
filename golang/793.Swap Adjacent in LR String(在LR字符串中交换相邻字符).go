/*
<p>In a string composed of <code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>, and <code>&#39;X&#39;</code> characters, like <code>&quot;RXXLRXRXL&quot;</code>, a move consists of either replacing one occurrence of <code>&quot;XL&quot;</code> with <code>&quot;LX&quot;</code>, or replacing one occurrence of <code>&quot;RX&quot;</code> with <code>&quot;XR&quot;</code>. Given the starting string <code>start</code> and the ending string <code>end</code>, return <code>True</code> if and only if there exists a sequence of moves to transform one string to the other.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> start = &quot;RXXLRXRXL&quot;, end = &quot;XRLXXRRLX&quot;
<strong>Output:</strong> True
<strong>Explanation:</strong>
We can transform start to end following these steps:
RXXLRXRXL -&gt;
XRXLRXRXL -&gt;
XRLXRXRXL -&gt;
XRLXXRRXL -&gt;
XRLXXRRLX
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= len(start) = len(end) &lt;= 10000</code>.</li>
	<li>Both start and end will only consist of characters in <code>{&#39;L&#39;, &#39;R&#39;, &#39;X&#39;}</code>.</li>
</ol><p>在一个由 <code>&#39;L&#39;</code> , <code>&#39;R&#39;</code> 和 <code>&#39;X&#39;</code> 三个字符组成的字符串（例如<code>&quot;RXXLRXRXL&quot;</code>）中进行移动操作。一次移动操作指用一个<code>&quot;LX&quot;</code>替换一个<code>&quot;XL&quot;</code>，或者用一个<code>&quot;XR&quot;</code>替换一个<code>&quot;RX&quot;</code>。现给定起始字符串<code>start</code>和结束字符串<code>end</code>，请编写代码，当且仅当存在一系列移动操作使得<code>start</code>可以转换成<code>end</code>时， 返回<code>True</code>。</p>

<p><strong>示例 :</strong></p>

<pre>
<strong>输入:</strong> start = &quot;RXXLRXRXL&quot;, end = &quot;XRLXXRRLX&quot;
<strong>输出:</strong> True
<strong>解释:</strong>
我们可以通过以下几步将start转换成end:
RXXLRXRXL -&gt;
XRXLRXRXL -&gt;
XRLXRXRXL -&gt;
XRLXXRRXL -&gt;
XRLXXRRLX
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>1 &lt;= len(start) = len(end) &lt;= 10000</code>。</li>
	<li><code>start</code>和<code>end</code>中的字符串仅限于<code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>和<code>&#39;X&#39;</code>。</li>
</ol>
<p>在一个由 <code>&#39;L&#39;</code> , <code>&#39;R&#39;</code> 和 <code>&#39;X&#39;</code> 三个字符组成的字符串（例如<code>&quot;RXXLRXRXL&quot;</code>）中进行移动操作。一次移动操作指用一个<code>&quot;LX&quot;</code>替换一个<code>&quot;XL&quot;</code>，或者用一个<code>&quot;XR&quot;</code>替换一个<code>&quot;RX&quot;</code>。现给定起始字符串<code>start</code>和结束字符串<code>end</code>，请编写代码，当且仅当存在一系列移动操作使得<code>start</code>可以转换成<code>end</code>时， 返回<code>True</code>。</p>

<p><strong>示例 :</strong></p>

<pre>
<strong>输入:</strong> start = &quot;RXXLRXRXL&quot;, end = &quot;XRLXXRRLX&quot;
<strong>输出:</strong> True
<strong>解释:</strong>
我们可以通过以下几步将start转换成end:
RXXLRXRXL -&gt;
XRXLRXRXL -&gt;
XRLXRXRXL -&gt;
XRLXXRRXL -&gt;
XRLXXRRLX
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>1 &lt;= len(start) = len(end) &lt;= 10000</code>。</li>
	<li><code>start</code>和<code>end</code>中的字符串仅限于<code>&#39;L&#39;</code>, <code>&#39;R&#39;</code>和<code>&#39;X&#39;</code>。</li>
</ol>
*/


func canTransform(start string, end string) bool {
    
}