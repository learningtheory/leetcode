/**
<p>
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step: 
<ol>
<li><code>Copy All</code>: You can copy all the characters present on the notepad (partial copy is not allowed).</li>
<li><code>Paste</code>: You can paste the characters which are copied <b>last time</b>.</li>
</ol>
</p>

<p>
Given a number <code>n</code>. You have to get <b>exactly</b> <code>n</code> 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get <code>n</code> 'A'. 
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 3
<b>Output:</b> 3
<b>Explanation:</b>
Intitally, we have one character 'A'.
In step 1, we use <b>Copy All</b> operation.
In step 2, we use <b>Paste</b> operation to get 'AA'.
In step 3, we use <b>Paste</b> operation to get 'AAA'.
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>The <code>n</code> will be in the range [1, 1000].</li>
</ol>
</p><p>最初在一个记事本上只有一个字符 &#39;A&#39;。你每次可以对这个记事本进行两种操作：</p>

<ol>
	<li><code>Copy All</code> (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。</li>
	<li><code>Paste</code> (粘贴) : 你可以粘贴你<strong>上一次</strong>复制的字符。</li>
</ol>

<p>给定一个数字&nbsp;<code>n</code>&nbsp;。你需要使用最少的操作次数，在记事本中打印出<strong>恰好</strong>&nbsp;<code>n</code>&nbsp;个 &#39;A&#39;。输出能够打印出&nbsp;<code>n</code>&nbsp;个 &#39;A&#39; 的最少操作次数。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 3
<strong>输出:</strong> 3
<strong>解释:</strong>
最初, 我们只有一个字符 &#39;A&#39;。
第 1 步, 我们使用 <strong>Copy All</strong> 操作。
第 2 步, 我们使用 <strong>Paste </strong>操作来获得 &#39;AA&#39;。
第 3 步, 我们使用 <strong>Paste</strong> 操作来获得 &#39;AAA&#39;。
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li><code>n</code>&nbsp;的取值范围是 [1, 1000] 。</li>
</ol>
<p>最初在一个记事本上只有一个字符 &#39;A&#39;。你每次可以对这个记事本进行两种操作：</p>

<ol>
	<li><code>Copy All</code> (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。</li>
	<li><code>Paste</code> (粘贴) : 你可以粘贴你<strong>上一次</strong>复制的字符。</li>
</ol>

<p>给定一个数字&nbsp;<code>n</code>&nbsp;。你需要使用最少的操作次数，在记事本中打印出<strong>恰好</strong>&nbsp;<code>n</code>&nbsp;个 &#39;A&#39;。输出能够打印出&nbsp;<code>n</code>&nbsp;个 &#39;A&#39; 的最少操作次数。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 3
<strong>输出:</strong> 3
<strong>解释:</strong>
最初, 我们只有一个字符 &#39;A&#39;。
第 1 步, 我们使用 <strong>Copy All</strong> 操作。
第 2 步, 我们使用 <strong>Paste </strong>操作来获得 &#39;AA&#39;。
第 3 步, 我们使用 <strong>Paste</strong> 操作来获得 &#39;AAA&#39;。
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li><code>n</code>&nbsp;的取值范围是 [1, 1000] 。</li>
</ol>
**/


class Solution {
    fun minSteps(n: Int): Int {
        
    }
}