/**
<p>Given a paragraph&nbsp;and a list of banned words, return the most frequent word that is not in the list of banned words.&nbsp; It is guaranteed there is at least one word that isn&#39;t banned, and that the answer is unique.</p>

<p>Words in the list of banned words are given in lowercase, and free of punctuation.&nbsp; Words in the paragraph are not case sensitive.&nbsp; The answer is in lowercase.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> 
paragraph = &quot;Bob hit a ball, the hit BALL flew far after it was hit.&quot;
banned = [&quot;hit&quot;]
<strong>Output:</strong> &quot;ball&quot;
<strong>Explanation:</strong> 
&quot;hit&quot; occurs 3 times, but it is a banned word.
&quot;ball&quot; occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as &quot;ball,&quot;), 
and that &quot;hit&quot; isn&#39;t the answer even though it occurs more because it is banned.
</pre>

<p>&nbsp;</p>

<p><strong>Note: </strong></p>

<ul>
	<li><code>1 &lt;= paragraph.length &lt;= 1000</code>.</li>
	<li><code>1 &lt;= banned.length &lt;= 100</code>.</li>
	<li><code>1 &lt;= banned[i].length &lt;= 10</code>.</li>
	<li>The answer is unique, and written in lowercase (even if its occurrences in <code>paragraph</code>&nbsp;may have&nbsp;uppercase symbols, and even if it is a proper noun.)</li>
	<li><code>paragraph</code> only consists of letters, spaces, or the punctuation symbols <code>!?&#39;,;.</code></li>
	<li>Different words in&nbsp;<code>paragraph</code>&nbsp;are always separated by a space.</li>
	<li>There are no hyphens or hyphenated words.</li>
	<li>Words only consist of letters, never apostrophes or other punctuation symbols.</li>
</ul>

<p>&nbsp;</p><p>给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。题目保证至少有一个词不在禁用列表中，而且答案唯一。</p>

<p>禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> 
paragraph = &quot;Bob hit a ball, the hit BALL flew far after it was hit.&quot;
banned = [&quot;hit&quot;]
<strong>输出:</strong> &quot;ball&quot;
<strong>解释:</strong> 
&quot;hit&quot; 出现了3次，但它是一个禁用的单词。
&quot;ball&quot; 出现了2次 (同时没有其他单词出现2次)，所以它是段落里出现次数最多的，且不在禁用列表中的单词。 
注意，所有这些单词在段落里不区分大小写，标点符号需要忽略（即使是紧挨着单词也忽略， 比如 &quot;ball,&quot;）， 
&quot;hit&quot;不是最终的答案，虽然它出现次数更多，但它在禁用单词列表中。
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li><code>1 &lt;= 段落长度 &lt;= 1000</code>.</li>
	<li><code>1 &lt;= 禁用单词个数 &lt;= 100</code>.</li>
	<li><code>1 &lt;= 禁用单词长度 &lt;= 10</code>.</li>
	<li>答案是唯一的, 且都是小写字母&nbsp;(即使在 <code>paragraph</code> 里是大写的，即使是一些特定的名词，答案都是小写的。)</li>
	<li><code>paragraph</code>&nbsp;只包含字母、空格和下列标点符号<code>!?&#39;,;.</code></li>
	<li><code>paragraph</code>&nbsp;里单词之间都由空格隔开。</li>
	<li>不存在没有连字符或者带有连字符的单词。</li>
	<li>单词里只包含字母，不会出现省略号或者其他标点符号。</li>
</ul>
<p>给定一个段落 (paragraph) 和一个禁用单词列表 (banned)。返回出现次数最多，同时不在禁用列表中的单词。题目保证至少有一个词不在禁用列表中，而且答案唯一。</p>

<p>禁用列表中的单词用小写字母表示，不含标点符号。段落中的单词不区分大小写。答案都是小写字母。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> 
paragraph = &quot;Bob hit a ball, the hit BALL flew far after it was hit.&quot;
banned = [&quot;hit&quot;]
<strong>输出:</strong> &quot;ball&quot;
<strong>解释:</strong> 
&quot;hit&quot; 出现了3次，但它是一个禁用的单词。
&quot;ball&quot; 出现了2次 (同时没有其他单词出现2次)，所以它是段落里出现次数最多的，且不在禁用列表中的单词。 
注意，所有这些单词在段落里不区分大小写，标点符号需要忽略（即使是紧挨着单词也忽略， 比如 &quot;ball,&quot;）， 
&quot;hit&quot;不是最终的答案，虽然它出现次数更多，但它在禁用单词列表中。
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li><code>1 &lt;= 段落长度 &lt;= 1000</code>.</li>
	<li><code>1 &lt;= 禁用单词个数 &lt;= 100</code>.</li>
	<li><code>1 &lt;= 禁用单词长度 &lt;= 10</code>.</li>
	<li>答案是唯一的, 且都是小写字母&nbsp;(即使在 <code>paragraph</code> 里是大写的，即使是一些特定的名词，答案都是小写的。)</li>
	<li><code>paragraph</code>&nbsp;只包含字母、空格和下列标点符号<code>!?&#39;,;.</code></li>
	<li><code>paragraph</code>&nbsp;里单词之间都由空格隔开。</li>
	<li>不存在没有连字符或者带有连字符的单词。</li>
	<li>单词里只包含字母，不会出现省略号或者其他标点符号。</li>
</ul>
**/


object Solution {
    def mostCommonWord(paragraph: String, banned: Array[String]): String = {
        
    }
}