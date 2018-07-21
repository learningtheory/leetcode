/*
<p>Given a string array <code>words</code>, find the maximum value of <code>length(word[i]) * length(word[j])</code> where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>[&quot;abcw&quot;,&quot;baz&quot;,&quot;foo&quot;,&quot;bar&quot;,&quot;xtfn&quot;,&quot;abcdef&quot;]</code>
<b>Output: </b><code>16 
<strong>Explanation: </strong></code>The two words can be <code>&quot;abcw&quot;, &quot;xtfn&quot;</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">.</span></pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> <code>[&quot;a&quot;,&quot;ab&quot;,&quot;abc&quot;,&quot;d&quot;,&quot;cd&quot;,&quot;bcd&quot;,&quot;abcd&quot;]</code>
<b>Output: </b><code>4 
<strong>Explanation: </strong></code>The two words can be <code>&quot;ab&quot;, &quot;cd&quot;</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">.</span></pre>

<p><b>Example 3:</b></p>

<pre>
<b>Input:</b> <code>[&quot;a&quot;,&quot;aa&quot;,&quot;aaa&quot;,&quot;aaaa&quot;]</code>
<b>Output: </b><code>0 
<strong>Explanation: </strong></code>No such pair of words.
</pre>
<p>给定一个字符串数组&nbsp;<code>words</code>，找到&nbsp;<code>length(word[i]) * length(word[j])</code>&nbsp;的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> <code>[&quot;abcw&quot;,&quot;baz&quot;,&quot;foo&quot;,&quot;bar&quot;,&quot;xtfn&quot;,&quot;abcdef&quot;]</code>
<strong>输出: </strong><code>16 
<strong>解释:</strong> 这两个单词为<strong> </strong></code><code>&quot;abcw&quot;, &quot;xtfn&quot;</code>。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> <code>[&quot;a&quot;,&quot;ab&quot;,&quot;abc&quot;,&quot;d&quot;,&quot;cd&quot;,&quot;bcd&quot;,&quot;abcd&quot;]</code>
<strong>输出: </strong><code>4 
<strong>解释: </strong></code>这两个单词为 <code>&quot;ab&quot;, &quot;cd&quot;</code>。</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> <code>[&quot;a&quot;,&quot;aa&quot;,&quot;aaa&quot;,&quot;aaaa&quot;]</code>
<strong>输出: </strong><code>0 
<strong>解释: </strong>不存在这样的两个单词。</code></pre>
<p>给定一个字符串数组&nbsp;<code>words</code>，找到&nbsp;<code>length(word[i]) * length(word[j])</code>&nbsp;的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> <code>[&quot;abcw&quot;,&quot;baz&quot;,&quot;foo&quot;,&quot;bar&quot;,&quot;xtfn&quot;,&quot;abcdef&quot;]</code>
<strong>输出: </strong><code>16 
<strong>解释:</strong> 这两个单词为<strong> </strong></code><code>&quot;abcw&quot;, &quot;xtfn&quot;</code>。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> <code>[&quot;a&quot;,&quot;ab&quot;,&quot;abc&quot;,&quot;d&quot;,&quot;cd&quot;,&quot;bcd&quot;,&quot;abcd&quot;]</code>
<strong>输出: </strong><code>4 
<strong>解释: </strong></code>这两个单词为 <code>&quot;ab&quot;, &quot;cd&quot;</code>。</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> <code>[&quot;a&quot;,&quot;aa&quot;,&quot;aaa&quot;,&quot;aaaa&quot;]</code>
<strong>输出: </strong><code>0 
<strong>解释: </strong>不存在这样的两个单词。</code></pre>
*/


/**
 * @param {string[]} words
 * @return {number}
 */
var maxProduct = function(words) {
    
};