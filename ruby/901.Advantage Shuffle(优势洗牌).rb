=begin
<p>Given two arrays <code>A</code> and <code>B</code> of equal size, the <em>advantage of <code>A</code> with respect to <code>B</code></em> is the number of indices <code>i</code>&nbsp;for which <code>A[i] &gt; B[i]</code>.</p>

<p>Return <strong>any</strong> permutation of <code>A</code> that maximizes its advantage with respect to <code>B</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[2,7,11,15]</span>, B = <span id="example-input-1-2">[1,10,4,11]</span>
<strong>Output: </strong><span id="example-output-1">[2,11,7,15]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[12,24,8,32]</span>, B = <span id="example-input-2-2">[13,25,32,11]</span>
<strong>Output: </strong><span id="example-output-2">[24,32,8,12]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length = B.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
	<li><code>0 &lt;= B[i] &lt;= 10^9</code></li>
</ol>
</div>
</div>
<p>给定两个大小相等的数组&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>，A 相对于 B 的<em>优势</em>可以用满足&nbsp;<code>A[i] &gt; B[i]</code>&nbsp;的索引 <code>i</code>&nbsp;的数目来描述。</p>

<p>返回&nbsp;<code>A</code>&nbsp;的<strong>任意</strong>排列，使其相对于 <code>B</code>&nbsp;的优势最大化。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = [2,7,11,15], B = [1,10,4,11]
<strong>输出：</strong>[2,11,7,15]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [12,24,8,32], B = [13,25,32,11]
<strong>输出：</strong>[24,32,8,12]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length = B.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
	<li><code>0 &lt;= B[i] &lt;= 10^9</code></li>
</ol>
<p>给定两个大小相等的数组&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>，A 相对于 B 的<em>优势</em>可以用满足&nbsp;<code>A[i] &gt; B[i]</code>&nbsp;的索引 <code>i</code>&nbsp;的数目来描述。</p>

<p>返回&nbsp;<code>A</code>&nbsp;的<strong>任意</strong>排列，使其相对于 <code>B</code>&nbsp;的优势最大化。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = [2,7,11,15], B = [1,10,4,11]
<strong>输出：</strong>[2,11,7,15]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = [12,24,8,32], B = [13,25,32,11]
<strong>输出：</strong>[24,32,8,12]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length = B.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
	<li><code>0 &lt;= B[i] &lt;= 10^9</code></li>
</ol>

=end


# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer[]}
def advantage_count(a, b)
    
end