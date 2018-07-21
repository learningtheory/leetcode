/**
<p>Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be <a href = "https://en.wikipedia.org/wiki/Irreducible_fraction">irreducible fraction</a>. If your final result is an integer, say <code>2</code>, you need to change it to the format of fraction that has denominator <code>1</code>. So in this case, <code>2</code> should be converted to <code>2/1</code>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>"-1/2+1/2"
<b>Output:</b> "0/1"
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>"-1/2+1/2+1/3"
<b>Output:</b> "1/3"
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b>"1/3-1/2"
<b>Output:</b> "-1/6"
</pre>
</p>

<p><b>Example 4:</b><br />
<pre>
<b>Input:</b>"5/3+1/3"
<b>Output:</b> "2/1"
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The input string only contains <code>'0'</code> to <code>'9'</code>, <code>'/'</code>, <code>'+'</code> and <code>'-'</code>. So does the output.</li>
<li>Each fraction (input and output) has format <code>±numerator/denominator</code>. If the first input fraction or the output is positive, then <code>'+'</code> will be omitted.</li>
<li>The input only contains valid <b>irreducible fractions</b>, where the <b>numerator</b> and <b>denominator</b> of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.</li> 
<li>The number of given fractions will be in the range [1,10].</li>
<li>The numerator and denominator of the <b>final result</b> are guaranteed to be valid and in the range of 32-bit int.</li>
</ol>
</p><p>给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果。&nbsp;这个结果应该是不可约分的分数，即<a href="https://baike.baidu.com/item/%E6%9C%80%E7%AE%80%E5%88%86%E6%95%B0" target="_blank">最简分数</a>。&nbsp;如果最终结果是一个整数，例如&nbsp;<code>2</code>，你需要将它转换成分数形式，其分母为&nbsp;<code>1</code>。所以在上述例子中, <code>2</code>&nbsp;应该被转换为&nbsp;<code>2/1</code>。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong>&quot;-1/2+1/2&quot;
<strong>输出:</strong> &quot;0/1&quot;
</pre>

<p><strong>&nbsp;示例 2:</strong></p>

<pre>
<strong>输入:</strong>&quot;-1/2+1/2+1/3&quot;
<strong>输出:</strong> &quot;1/3&quot;
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong>&quot;1/3-1/2&quot;
<strong>输出:</strong> &quot;-1/6&quot;
</pre>

<p><strong>示例 4:</strong></p>

<pre>
<strong>输入:</strong>&quot;5/3+1/3&quot;
<strong>输出:</strong> &quot;2/1&quot;
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>输入和输出字符串只包含&nbsp;<code>&#39;0&#39;</code> 到&nbsp;<code>&#39;9&#39;</code>&nbsp;的数字，以及&nbsp;<code>&#39;/&#39;</code>, <code>&#39;+&#39;</code> 和&nbsp;<code>&#39;-&#39;</code>。&nbsp;</li>
	<li>输入和输出分数格式均为&nbsp;<code>&plusmn;分子/分母</code>。如果输入的第一个分数或者输出的分数是正数，则&nbsp;<code>&#39;+&#39;</code>&nbsp;会被省略掉。</li>
	<li>输入只包含合法的<strong>最简分数</strong>，每个分数的<strong>分子</strong>与<strong>分母</strong>的范围是&nbsp;&nbsp;[1,10]。&nbsp;如果分母是1，意味着这个分数实际上是一个整数。</li>
	<li>输入的分数个数范围是 [1,10]。</li>
	<li><strong>最终结果</strong>的分子与分母保证是 32 位整数范围内的有效整数。</li>
</ol>
<p>给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果。&nbsp;这个结果应该是不可约分的分数，即<a href="https://baike.baidu.com/item/%E6%9C%80%E7%AE%80%E5%88%86%E6%95%B0" target="_blank">最简分数</a>。&nbsp;如果最终结果是一个整数，例如&nbsp;<code>2</code>，你需要将它转换成分数形式，其分母为&nbsp;<code>1</code>。所以在上述例子中, <code>2</code>&nbsp;应该被转换为&nbsp;<code>2/1</code>。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong>&quot;-1/2+1/2&quot;
<strong>输出:</strong> &quot;0/1&quot;
</pre>

<p><strong>&nbsp;示例 2:</strong></p>

<pre>
<strong>输入:</strong>&quot;-1/2+1/2+1/3&quot;
<strong>输出:</strong> &quot;1/3&quot;
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong>&quot;1/3-1/2&quot;
<strong>输出:</strong> &quot;-1/6&quot;
</pre>

<p><strong>示例 4:</strong></p>

<pre>
<strong>输入:</strong>&quot;5/3+1/3&quot;
<strong>输出:</strong> &quot;2/1&quot;
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>输入和输出字符串只包含&nbsp;<code>&#39;0&#39;</code> 到&nbsp;<code>&#39;9&#39;</code>&nbsp;的数字，以及&nbsp;<code>&#39;/&#39;</code>, <code>&#39;+&#39;</code> 和&nbsp;<code>&#39;-&#39;</code>。&nbsp;</li>
	<li>输入和输出分数格式均为&nbsp;<code>&plusmn;分子/分母</code>。如果输入的第一个分数或者输出的分数是正数，则&nbsp;<code>&#39;+&#39;</code>&nbsp;会被省略掉。</li>
	<li>输入只包含合法的<strong>最简分数</strong>，每个分数的<strong>分子</strong>与<strong>分母</strong>的范围是&nbsp;&nbsp;[1,10]。&nbsp;如果分母是1，意味着这个分数实际上是一个整数。</li>
	<li>输入的分数个数范围是 [1,10]。</li>
	<li><strong>最终结果</strong>的分子与分母保证是 32 位整数范围内的有效整数。</li>
</ol>
**/


class Solution {
    fun fractionAddition(expression: String): String {
        
    }
}