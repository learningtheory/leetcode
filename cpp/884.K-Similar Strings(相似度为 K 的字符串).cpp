/*
<p>Strings&nbsp;<code>A</code> and <code>B</code> are <code>K</code>-similar (for some non-negative integer <code>K</code>) if we can swap the positions of two letters in <code>A</code> exactly <code>K</code>&nbsp;times so that the resulting string equals <code>B</code>.</p>

<p>Given two anagrams <code>A</code> and <code>B</code>, return the smallest <code>K</code>&nbsp;for which <code>A</code> and <code>B</code> are <code>K</code>-similar.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">&quot;ab&quot;</span>, B = <span id="example-input-1-2">&quot;ba&quot;</span>
<strong>Output: </strong><span id="example-output-1">1</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">&quot;abc&quot;</span>, B = <span id="example-input-2-2">&quot;bca&quot;</span>
<strong>Output: </strong><span id="example-output-2">2</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">&quot;abac&quot;</span>, B = <span id="example-input-3-2">&quot;baca&quot;</span>
<strong>Output: </strong><span id="example-output-3">2</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-4-1">&quot;aabc&quot;</span>, B = <span id="example-input-4-2">&quot;abca&quot;</span>
<strong>Output: </strong><span id="example-output-4">2</span></pre>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length == B.length &lt;= 20</code></li>
	<li><code>A</code> and <code>B</code> contain only lowercase letters from the set <code>{&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39;e&#39;, &#39;f&#39;}</code></li>
</ol><p>如果可以通过将 <code>A</code> 中的两个小写字母精确地交换位置 <code>K</code> 次得到与 <code>B</code> 相等的字符串，我们称字符串&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;的相似度为 <code>K</code>（<code>K</code>&nbsp;为非负整数）。</p>

<p>给定两个字母异位词&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;，返回 <code>A</code> 和 <code>B</code>&nbsp;的相似度 <code>K</code> 的最小值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = &quot;ab&quot;, B = &quot;ba&quot;
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = &quot;abc&quot;, B = &quot;bca&quot;
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>A = &quot;abac&quot;, B = &quot;baca&quot;
<strong>输出：</strong>2
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>A = &quot;aabc&quot;, B = &quot;abca&quot;
<strong>输出：</strong>2</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length == B.length &lt;= 20</code></li>
	<li><code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;只包含集合&nbsp;<code>{&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39;e&#39;, &#39;f&#39;}</code>&nbsp;中的小写字母。</li>
</ol>
<p>如果可以通过将 <code>A</code> 中的两个小写字母精确地交换位置 <code>K</code> 次得到与 <code>B</code> 相等的字符串，我们称字符串&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;的相似度为 <code>K</code>（<code>K</code>&nbsp;为非负整数）。</p>

<p>给定两个字母异位词&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;，返回 <code>A</code> 和 <code>B</code>&nbsp;的相似度 <code>K</code> 的最小值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>A = &quot;ab&quot;, B = &quot;ba&quot;
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>A = &quot;abc&quot;, B = &quot;bca&quot;
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>A = &quot;abac&quot;, B = &quot;baca&quot;
<strong>输出：</strong>2
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>A = &quot;aabc&quot;, B = &quot;abca&quot;
<strong>输出：</strong>2</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length == B.length &lt;= 20</code></li>
	<li><code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;只包含集合&nbsp;<code>{&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39;e&#39;, &#39;f&#39;}</code>&nbsp;中的小写字母。</li>
</ol>
*/


class Solution {
public:
    int kSimilarity(string A, string B) {
        
    }
};