/**
<p>On the first row, we write a <code>0</code>. Now in every subsequent row, we look at the previous row and replace each occurrence of <code>0</code> with <code>01</code>, and each occurrence of <code>1</code> with <code>10</code>.</p>

<p>Given row <code>N</code> and index <code>K</code>, return the <code>K</code>-th indexed symbol in row <code>N</code>. (The values of <code>K</code> are 1-indexed.) (1 indexed).</p>

<pre>
<strong>Examples:</strong>
<strong>Input:</strong> N = 1, K = 1
<strong>Output:</strong> 0

<strong>Input:</strong> N = 2, K = 1
<strong>Output:</strong> 0

<strong>Input:</strong> N = 2, K = 2
<strong>Output:</strong> 1

<strong>Input:</strong> N = 4, K = 5
<strong>Output:</strong> 1

<strong>Explanation:</strong>
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>N</code> will be an integer in the range <code>[1, 30]</code>.</li>
	<li><code>K</code> will be an integer in the range <code>[1, 2^(N-1)]</code>.</li>
</ol><p>在第一行我们写上一个 <code>0</code>。接下来的每一行，将前一行中的<code>0</code>替换为<code>01</code>，<code>1</code>替换为<code>10</code>。</p>

<p>给定行数&nbsp;<code>N</code>&nbsp;和序数 <code>K</code>，返回第 <code>N</code> 行中第 <code>K</code>个字符。（<code>K</code>从1开始）</p>

<p><br>
<strong>例子:</strong></p>

<pre><strong>输入:</strong> N = 1, K = 1
<strong>输出:</strong> 0

<strong>输入:</strong> N = 2, K = 1
<strong>输出:</strong> 0

<strong>输入:</strong> N = 2, K = 2
<strong>输出:</strong> 1

<strong>输入:</strong> N = 4, K = 5
<strong>输出:</strong> 1

<strong>解释:</strong>
第一行: 0
第二行: 01
第三行: 0110
第四行: 01101001
</pre>

<p><br>
<strong>注意：</strong></p>

<ol>
	<li><code>N</code>&nbsp;的范围&nbsp;<code>[1, 30]</code>.</li>
	<li><code>K</code>&nbsp;的范围&nbsp;<code>[1, 2^(N-1)]</code>.</li>
</ol>
<p>在第一行我们写上一个 <code>0</code>。接下来的每一行，将前一行中的<code>0</code>替换为<code>01</code>，<code>1</code>替换为<code>10</code>。</p>

<p>给定行数&nbsp;<code>N</code>&nbsp;和序数 <code>K</code>，返回第 <code>N</code> 行中第 <code>K</code>个字符。（<code>K</code>从1开始）</p>

<p><br>
<strong>例子:</strong></p>

<pre><strong>输入:</strong> N = 1, K = 1
<strong>输出:</strong> 0

<strong>输入:</strong> N = 2, K = 1
<strong>输出:</strong> 0

<strong>输入:</strong> N = 2, K = 2
<strong>输出:</strong> 1

<strong>输入:</strong> N = 4, K = 5
<strong>输出:</strong> 1

<strong>解释:</strong>
第一行: 0
第二行: 01
第三行: 0110
第四行: 01101001
</pre>

<p><br>
<strong>注意：</strong></p>

<ol>
	<li><code>N</code>&nbsp;的范围&nbsp;<code>[1, 30]</code>.</li>
	<li><code>K</code>&nbsp;的范围&nbsp;<code>[1, 2^(N-1)]</code>.</li>
</ol>
**/


object Solution {
    def kthGrammar(N: Int, K: Int): Int = {
        
    }
}