/*
<p>
There is a strange printer with the following two special requirements:

<ol>
<li>The printer can only print a sequence of the same character each time.</li>
<li>At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.</li>
</ol>

</p>

<p>
Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "aaabbb"
<b>Output:</b> 2
<b>Explanation:</b> Print "aaa" first and then print "bbb".
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "aba"
<b>Output:</b> 2
<b>Explanation:</b> Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
</pre>
</p>

<p><b>Hint</b>: Length of the given string will not exceed 100.</p><p>有台奇怪的打印机有以下两个特殊要求：</p>

<ol>
	<li>打印机每次只能打印同一个字符序列。</li>
	<li>每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。</li>
</ol>

<p>给定一个只包含小写英文字母的字符串，你的任务是计算这个打印机打印它需要的最少次数。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> &quot;aaabbb&quot;
<strong>输出:</strong> 2
<strong>解释:</strong> 首先打印 &quot;aaa&quot; 然后打印 &quot;bbb&quot;。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> &quot;aba&quot;
<strong>输出:</strong> 2
<strong>解释:</strong> 首先打印 &quot;aaa&quot; 然后在第二个位置打印 &quot;b&quot; 覆盖掉原来的字符 &#39;a&#39;。</pre>

<p><strong>提示</strong>: 输入字符串的长度不会超过 100。</p>
<p>有台奇怪的打印机有以下两个特殊要求：</p>

<ol>
	<li>打印机每次只能打印同一个字符序列。</li>
	<li>每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。</li>
</ol>

<p>给定一个只包含小写英文字母的字符串，你的任务是计算这个打印机打印它需要的最少次数。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> &quot;aaabbb&quot;
<strong>输出:</strong> 2
<strong>解释:</strong> 首先打印 &quot;aaa&quot; 然后打印 &quot;bbb&quot;。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> &quot;aba&quot;
<strong>输出:</strong> 2
<strong>解释:</strong> 首先打印 &quot;aaa&quot; 然后在第二个位置打印 &quot;b&quot; 覆盖掉原来的字符 &#39;a&#39;。</pre>

<p><strong>提示</strong>: 输入字符串的长度不会超过 100。</p>
*/


class Solution {
    func strangePrinter(_ s: String) -> Int {
        
    }
}