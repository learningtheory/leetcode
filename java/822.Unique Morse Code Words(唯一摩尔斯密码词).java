/**
<p>International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: <code>&quot;a&quot;</code> maps to <code>&quot;.-&quot;</code>, <code>&quot;b&quot;</code> maps to <code>&quot;-...&quot;</code>, <code>&quot;c&quot;</code> maps to <code>&quot;-.-.&quot;</code>, and so on.</p>

<p>For convenience, the full table for the 26 letters of the English alphabet is given below:</p>

<pre>
[&quot;.-&quot;,&quot;-...&quot;,&quot;-.-.&quot;,&quot;-..&quot;,&quot;.&quot;,&quot;..-.&quot;,&quot;--.&quot;,&quot;....&quot;,&quot;..&quot;,&quot;.---&quot;,&quot;-.-&quot;,&quot;.-..&quot;,&quot;--&quot;,&quot;-.&quot;,&quot;---&quot;,&quot;.--.&quot;,&quot;--.-&quot;,&quot;.-.&quot;,&quot;...&quot;,&quot;-&quot;,&quot;..-&quot;,&quot;...-&quot;,&quot;.--&quot;,&quot;-..-&quot;,&quot;-.--&quot;,&quot;--..&quot;]</pre>

<p>Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, &quot;cab&quot; can be written as &quot;-.-.-....-&quot;, (which is the concatenation &quot;-.-.&quot; + &quot;-...&quot; + &quot;.-&quot;). We&#39;ll call such a concatenation, the transformation&nbsp;of a word.</p>

<p>Return the number of different transformations among all words we have.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> words = ["gin", "zen", "gig", "msg"]
<strong>Output:</strong> 2
<strong>Explanation: </strong>
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The length of <code>words</code> will be at most <code>100</code>.</li>
	<li>Each <code>words[i]</code> will have length in range <code>[1, 12]</code>.</li>
    <li><code>words[i]</code> will only consist of lowercase letters.</li>
</ul>
<p>国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串，&nbsp;比如: <code>&quot;a&quot;</code> 对应 <code>&quot;.-&quot;</code>, <code>&quot;b&quot;</code> 对应 <code>&quot;-...&quot;</code>, <code>&quot;c&quot;</code> 对应 <code>&quot;-.-.&quot;</code>, 等等。</p>

<p>为了方便，所有26个英文字母对应摩尔斯密码表如下：</p>

<pre>[&quot;.-&quot;,&quot;-...&quot;,&quot;-.-.&quot;,&quot;-..&quot;,&quot;.&quot;,&quot;..-.&quot;,&quot;--.&quot;,&quot;....&quot;,&quot;..&quot;,&quot;.---&quot;,&quot;-.-&quot;,&quot;.-..&quot;,&quot;--&quot;,&quot;-.&quot;,&quot;---&quot;,&quot;.--.&quot;,&quot;--.-&quot;,&quot;.-.&quot;,&quot;...&quot;,&quot;-&quot;,&quot;..-&quot;,&quot;...-&quot;,&quot;.--&quot;,&quot;-..-&quot;,&quot;-.--&quot;,&quot;--..&quot;]</pre>

<p>给定一个单词列表，每个单词可以写成每个字母对应摩尔斯密码的组合。例如，&quot;cab&quot; 可以写成 &quot;-.-.-....-&quot;，(即 &quot;-.-.&quot; + &quot;-...&quot; + &quot;.-&quot;字符串的结合)。我们将这样一个连接过程称作单词翻译。</p>

<p>返回我们可以获得所有词不同单词翻译的数量。</p>

<pre><strong>例如:</strong>
<strong>输入:</strong> words = [&quot;gin&quot;, &quot;zen&quot;, &quot;gig&quot;, &quot;msg&quot;]
<strong>输出:</strong> 2
<strong>解释: </strong>
各单词翻译如下:
&quot;gin&quot; -&gt; &quot;--...-.&quot;
&quot;zen&quot; -&gt; &quot;--...-.&quot;
&quot;gig&quot; -&gt; &quot;--...--.&quot;
&quot;msg&quot; -&gt; &quot;--...--.&quot;

共有 2 种不同翻译, &quot;--...-.&quot; 和 &quot;--...--.&quot;.
</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<ul>
	<li>单词列表<code>words</code>&nbsp;的长度不会超过 <code>100</code>。</li>
	<li>每个单词&nbsp;<code>words[i]</code>的长度范围为&nbsp;<code>[1, 12]</code>。</li>
	<li>每个单词&nbsp;<code>words[i]</code>只包含小写字母。</li>
</ul>
<p>国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串，&nbsp;比如: <code>&quot;a&quot;</code> 对应 <code>&quot;.-&quot;</code>, <code>&quot;b&quot;</code> 对应 <code>&quot;-...&quot;</code>, <code>&quot;c&quot;</code> 对应 <code>&quot;-.-.&quot;</code>, 等等。</p>

<p>为了方便，所有26个英文字母对应摩尔斯密码表如下：</p>

<pre>[&quot;.-&quot;,&quot;-...&quot;,&quot;-.-.&quot;,&quot;-..&quot;,&quot;.&quot;,&quot;..-.&quot;,&quot;--.&quot;,&quot;....&quot;,&quot;..&quot;,&quot;.---&quot;,&quot;-.-&quot;,&quot;.-..&quot;,&quot;--&quot;,&quot;-.&quot;,&quot;---&quot;,&quot;.--.&quot;,&quot;--.-&quot;,&quot;.-.&quot;,&quot;...&quot;,&quot;-&quot;,&quot;..-&quot;,&quot;...-&quot;,&quot;.--&quot;,&quot;-..-&quot;,&quot;-.--&quot;,&quot;--..&quot;]</pre>

<p>给定一个单词列表，每个单词可以写成每个字母对应摩尔斯密码的组合。例如，&quot;cab&quot; 可以写成 &quot;-.-.-....-&quot;，(即 &quot;-.-.&quot; + &quot;-...&quot; + &quot;.-&quot;字符串的结合)。我们将这样一个连接过程称作单词翻译。</p>

<p>返回我们可以获得所有词不同单词翻译的数量。</p>

<pre><strong>例如:</strong>
<strong>输入:</strong> words = [&quot;gin&quot;, &quot;zen&quot;, &quot;gig&quot;, &quot;msg&quot;]
<strong>输出:</strong> 2
<strong>解释: </strong>
各单词翻译如下:
&quot;gin&quot; -&gt; &quot;--...-.&quot;
&quot;zen&quot; -&gt; &quot;--...-.&quot;
&quot;gig&quot; -&gt; &quot;--...--.&quot;
&quot;msg&quot; -&gt; &quot;--...--.&quot;

共有 2 种不同翻译, &quot;--...-.&quot; 和 &quot;--...--.&quot;.
</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<ul>
	<li>单词列表<code>words</code>&nbsp;的长度不会超过 <code>100</code>。</li>
	<li>每个单词&nbsp;<code>words[i]</code>的长度范围为&nbsp;<code>[1, 12]</code>。</li>
	<li>每个单词&nbsp;<code>words[i]</code>只包含小写字母。</li>
</ul>
**/


class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        
    }
}