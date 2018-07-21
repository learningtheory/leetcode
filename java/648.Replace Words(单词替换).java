/**
<p>
In English, we have a concept called <code>root</code>, which can be followed by some other words to form another longer word - let's call this word <code>successor</code>. For example, the root <code>an</code>, followed by <code>other</code>, which can form another word <code>another</code>.
</p>


<p>
Now, given a dictionary consisting of many roots and a sentence. You need to replace all the <code>successor</code> in the sentence with the <code>root</code> forming it. If a <code>successor</code> has many <code>roots</code> can form it, replace it with the root with the shortest length.
</p>

<p>
You need to output the sentence after the replacement.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
<b>Output:</b> "the cat was rat by the bat"
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>The input will only have lower-case letters.</li>
<li> 1 <= dict words number <= 1000 </li>
<li> 1 <= sentence words number <= 1000  </li>
<li> 1 <= root length <= 100 </li>
<li> 1 <= sentence words length <= 1000 </li>
</ol>
</p><p>在英语中，我们有一个叫做&nbsp;<code>词根</code>(root)的概念，它可以跟着其他一些词组成另一个较长的单词&mdash;&mdash;我们称这个词为&nbsp;<code>继承词</code>(successor)。例如，词根<code>an</code>，跟随着单词&nbsp;<code>other</code>(其他)，可以形成新的单词&nbsp;<code>another</code>(另一个)。</p>

<p>现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有<code>继承词</code>用<code>词根</code>替换掉。如果<code>继承词</code>有许多可以形成它的<code>词根</code>，则用最短的词根替换它。</p>

<p>你需要输出替换之后的句子。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> dict(词典) = [&quot;cat&quot;, &quot;bat&quot;, &quot;rat&quot;]
sentence(句子) = &quot;the cattle was rattled by the battery&quot;
<strong>输出:</strong> &quot;the cat was rat by the bat&quot;
</pre>

<p><strong>注:</strong></p>

<ol>
	<li>输入只包含小写字母。</li>
	<li>1 &lt;= 字典单词数 &lt;=1000</li>
	<li>1 &lt;=&nbsp; 句中词语数&nbsp;&lt;= 1000</li>
	<li>1 &lt;= 词根长度 &lt;= 100</li>
	<li>1 &lt;= 句中词语长度&nbsp;&lt;= 1000</li>
</ol>
<p>在英语中，我们有一个叫做&nbsp;<code>词根</code>(root)的概念，它可以跟着其他一些词组成另一个较长的单词&mdash;&mdash;我们称这个词为&nbsp;<code>继承词</code>(successor)。例如，词根<code>an</code>，跟随着单词&nbsp;<code>other</code>(其他)，可以形成新的单词&nbsp;<code>another</code>(另一个)。</p>

<p>现在，给定一个由许多词根组成的词典和一个句子。你需要将句子中的所有<code>继承词</code>用<code>词根</code>替换掉。如果<code>继承词</code>有许多可以形成它的<code>词根</code>，则用最短的词根替换它。</p>

<p>你需要输出替换之后的句子。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> dict(词典) = [&quot;cat&quot;, &quot;bat&quot;, &quot;rat&quot;]
sentence(句子) = &quot;the cattle was rattled by the battery&quot;
<strong>输出:</strong> &quot;the cat was rat by the bat&quot;
</pre>

<p><strong>注:</strong></p>

<ol>
	<li>输入只包含小写字母。</li>
	<li>1 &lt;= 字典单词数 &lt;=1000</li>
	<li>1 &lt;=&nbsp; 句中词语数&nbsp;&lt;= 1000</li>
	<li>1 &lt;= 词根长度 &lt;= 100</li>
	<li>1 &lt;= 句中词语长度&nbsp;&lt;= 1000</li>
</ol>
**/


class Solution {
    public String replaceWords(List<String> dict, String sentence) {
        
    }
}