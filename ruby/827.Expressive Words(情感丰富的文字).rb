=begin
<p>Sometimes people repeat letters to represent extra feeling, such as &quot;hello&quot; -&gt; &quot;heeellooo&quot;, &quot;hi&quot; -&gt; &quot;hiiii&quot;.&nbsp; Here, we have&nbsp;groups, of adjacent letters that are all the same character, and adjacent characters to&nbsp;the group are different.&nbsp; A group&nbsp;is extended if that group is length 3 or more, so &quot;e&quot; and &quot;o&quot; would be extended in the first example, and &quot;i&quot; would be extended in the second example.&nbsp; As another example, the groups of &quot;abbcccaaaa&quot; would be &quot;a&quot;, &quot;bb&quot;, &quot;ccc&quot;, and &quot;aaaa&quot;; and &quot;ccc&quot; and &quot;aaaa&quot; are the extended groups of that string.</p>

<p>For some given string S, a query word is <em>stretchy</em> if it can be made to be equal to S by extending some groups.&nbsp; Formally, we are allowed to repeatedly choose a group&nbsp;(as defined above) of characters <code>c</code>, and add some number of the&nbsp;same character <code>c</code> to it so that the length of the group is 3 or more.&nbsp; Note that we cannot extend a group of size one like &quot;h&quot; to a group of size two like &quot;hh&quot; - all extensions must leave the group extended - ie., at least 3 characters long.</p>

<p>Given a list of query words, return the number of words that are stretchy.&nbsp;</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> 
S = &quot;heeellooo&quot;
words = [&quot;hello&quot;, &quot;hi&quot;, &quot;helo&quot;]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 
We can extend &quot;e&quot; and &quot;o&quot; in the word &quot;hello&quot; to get &quot;heeellooo&quot;.
We can&#39;t extend &quot;helo&quot; to get &quot;heeellooo&quot; because the group &quot;ll&quot; is not extended.
</pre>

<p><strong>Notes: </strong></p>

<ul>
	<li><code>0 &lt;= len(S) &lt;= 100</code>.</li>
	<li><code>0 &lt;= len(words) &lt;= 100</code>.</li>
	<li><code>0 &lt;= len(words[i]) &lt;= 100</code>.</li>
	<li><code>S</code> and all words in <code>words</code>&nbsp;consist only of&nbsp;lowercase letters</li>
</ul>

<p>&nbsp;</p>
<p>有时候人们会用额外的字母来表示额外的情感，比如 &quot;hello&quot; -&gt; &quot;heeellooo&quot;, &quot;hi&quot; -&gt; &quot;hiii&quot;。我们将连续的相同的字母分组，并且相邻组的字母都不相同。我们将一个拥有三个或以上字母的组定义为扩张状态（extended），如第一个例子中的 &quot;e&quot; 和&quot; o&quot; 以及第二个例子中的 &quot;i&quot;。 此外，&quot;abbcccaaaa&quot; 将有分组&nbsp;&quot;a&quot; , &quot;bb&quot; , &quot;ccc&quot; , &quot;dddd&quot;；其中 &quot;ccc&quot; 和 &quot;aaaa&quot; 处于扩张状态。</p>

<p>对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。我们允许选择一个字母组（如包含字母&nbsp;<code>c</code>&nbsp;），然后往其中添加相同的字母&nbsp;<code>c</code>&nbsp;使其长度达到 3 或以上。注意，我们不能将一个只包含一个字母的字母组，如 &quot;h&quot;，扩张到一个包含两个字母的组，如 &quot;hh&quot;；所有的扩张必须使该字母组变成扩张状态（至少包含三个字母）。</p>

<p>输入一组单词，输出其中可扩张的单词数量。</p>

<pre>
<strong>示例：</strong>
<strong>输入：</strong> 
S = &quot;heeellooo&quot;
words = [&quot;hello&quot;, &quot;hi&quot;, &quot;helo&quot;]
<strong>输出：</strong>1
<strong>解释</strong>：
我们能通过扩张&quot;hello&quot;的&quot;e&quot;和&quot;o&quot;来得到&quot;heeellooo&quot;。
我们不能通过扩张&quot;helo&quot;来得到&quot;heeellooo&quot;因为&quot;ll&quot;不处于扩张状态。
</pre>

<p><strong>说明：</strong></p>

<ul>
	<li><code>0 &lt;= len(S) &lt;= 100</code>。</li>
	<li><code>0 &lt;= len(words) &lt;= 100</code>。</li>
	<li><code>0 &lt;= len(words[i]) &lt;= 100</code>。</li>
	<li><code>S</code>&nbsp;和所有在&nbsp;<code>words</code>&nbsp;中的单词都只由小写字母组成。</li>
</ul>
<p>有时候人们会用额外的字母来表示额外的情感，比如 &quot;hello&quot; -&gt; &quot;heeellooo&quot;, &quot;hi&quot; -&gt; &quot;hiii&quot;。我们将连续的相同的字母分组，并且相邻组的字母都不相同。我们将一个拥有三个或以上字母的组定义为扩张状态（extended），如第一个例子中的 &quot;e&quot; 和&quot; o&quot; 以及第二个例子中的 &quot;i&quot;。 此外，&quot;abbcccaaaa&quot; 将有分组&nbsp;&quot;a&quot; , &quot;bb&quot; , &quot;ccc&quot; , &quot;dddd&quot;；其中 &quot;ccc&quot; 和 &quot;aaaa&quot; 处于扩张状态。</p>

<p>对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。我们允许选择一个字母组（如包含字母&nbsp;<code>c</code>&nbsp;），然后往其中添加相同的字母&nbsp;<code>c</code>&nbsp;使其长度达到 3 或以上。注意，我们不能将一个只包含一个字母的字母组，如 &quot;h&quot;，扩张到一个包含两个字母的组，如 &quot;hh&quot;；所有的扩张必须使该字母组变成扩张状态（至少包含三个字母）。</p>

<p>输入一组单词，输出其中可扩张的单词数量。</p>

<pre>
<strong>示例：</strong>
<strong>输入：</strong> 
S = &quot;heeellooo&quot;
words = [&quot;hello&quot;, &quot;hi&quot;, &quot;helo&quot;]
<strong>输出：</strong>1
<strong>解释</strong>：
我们能通过扩张&quot;hello&quot;的&quot;e&quot;和&quot;o&quot;来得到&quot;heeellooo&quot;。
我们不能通过扩张&quot;helo&quot;来得到&quot;heeellooo&quot;因为&quot;ll&quot;不处于扩张状态。
</pre>

<p><strong>说明：</strong></p>

<ul>
	<li><code>0 &lt;= len(S) &lt;= 100</code>。</li>
	<li><code>0 &lt;= len(words) &lt;= 100</code>。</li>
	<li><code>0 &lt;= len(words[i]) &lt;= 100</code>。</li>
	<li><code>S</code>&nbsp;和所有在&nbsp;<code>words</code>&nbsp;中的单词都只由小写字母组成。</li>
</ul>

=end


# @param {String} s
# @param {String[]} words
# @return {Integer}
def expressive_words(s, words)
    
end