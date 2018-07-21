"""
<p>A sentence <code>S</code> is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.</p>

<p>We would like to convert the sentence to &quot;<em>Goat Latin&quot;</em>&nbsp;(a made-up language similar to Pig Latin.)</p>

<p>The rules of Goat Latin are as follows:</p>

<ul>
	<li>If a word begins with a vowel (a, e, i, o, or u), append <code>&quot;ma&quot;</code>&nbsp;to the end of the word.<br />
	For example, the word &#39;apple&#39; becomes &#39;applema&#39;.<br />
	&nbsp;</li>
	<li>If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add <code>&quot;ma&quot;</code>.<br />
	For example, the word <code>&quot;goat&quot;</code>&nbsp;becomes <code>&quot;oatgma&quot;</code>.<br />
	&nbsp;</li>
	<li>Add one letter <code>&#39;a&#39;</code>&nbsp;to the end of each word per its word index in the sentence, starting with 1.<br />
	For example,&nbsp;the first word gets <code>&quot;a&quot;</code> added to the end, the second word gets <code>&quot;aa&quot;</code> added to the end and so on.</li>
</ul>

<p>Return the&nbsp;final sentence representing the conversion from <code>S</code>&nbsp;to Goat&nbsp;Latin.&nbsp;</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>&quot;I speak Goat Latin&quot;
<strong>Output: </strong>&quot;Imaa peaksmaaa oatGmaaaa atinLmaaaaa&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;The quick brown fox jumped over the lazy dog&quot;
<strong>Output: </strong>&quot;heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa&quot;
</pre>

<p>&nbsp;</p>

<p>Notes:</p>

<ul>
	<li><code>S</code> contains only uppercase, lowercase and spaces.&nbsp;Exactly one space between each word.</li>
	<li><code>1 &lt;= S.length &lt;= 150</code>.</li>
</ul><p>给定一个由空格分割单词的句子&nbsp;<code>S</code>。每个单词只包含大写或小写字母。</p>

<p>我们要将句子转换为&nbsp;<em>&ldquo;Goat Latin&rdquo;</em>（一种类似于 猪拉丁文&nbsp;- Pig Latin 的虚构语言）。</p>

<p>山羊拉丁文的规则如下：</p>

<ul>
	<li>如果单词以元音开头（a, e, i, o, u），在单词后添加<code>&quot;ma&quot;</code>。<br />
	例如，单词<code>&quot;apple&quot;</code>变为<code>&quot;applema&quot;</code>。</li>
	<br />
	<li>如果单词以辅音字母开头（即非元音字母），移除第一个字符并将它放到末尾，之后再添加<code>&quot;ma&quot;</code>。<br />
	例如，单词<code>&quot;goat&quot;</code>变为<code>&quot;oatgma&quot;</code>。</li>
	<br />
	<li>根据单词在句子中的索引，在单词最后添加与索引相同数量的字母<code>&#39;a&#39;</code>，索引从1开始。<br />
	例如，在第一个单词后添加<code>&quot;a&quot;</code>，在第二个单词后添加<code>&quot;aa&quot;</code>，以此类推。</li>
</ul>

<p>返回将&nbsp;<code>S</code>&nbsp;转换为山羊拉丁文后的句子。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>&quot;I speak Goat Latin&quot;
<strong>输出: </strong>&quot;Imaa peaksmaaa oatGmaaaa atinLmaaaaa&quot;
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>&quot;The quick brown fox jumped over the lazy dog&quot;
<strong>输出: </strong>&quot;heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa&quot;
</pre>

<p><strong>说明:</strong></p>

<ul>
	<li><code>S</code>&nbsp;中仅包含大小写字母和空格。单词间有且仅有一个空格。</li>
	<li><code>1 &lt;= S.length &lt;= 150</code>。</li>
</ul>
<p>给定一个由空格分割单词的句子&nbsp;<code>S</code>。每个单词只包含大写或小写字母。</p>

<p>我们要将句子转换为&nbsp;<em>&ldquo;Goat Latin&rdquo;</em>（一种类似于 猪拉丁文&nbsp;- Pig Latin 的虚构语言）。</p>

<p>山羊拉丁文的规则如下：</p>

<ul>
	<li>如果单词以元音开头（a, e, i, o, u），在单词后添加<code>&quot;ma&quot;</code>。<br />
	例如，单词<code>&quot;apple&quot;</code>变为<code>&quot;applema&quot;</code>。</li>
	<br />
	<li>如果单词以辅音字母开头（即非元音字母），移除第一个字符并将它放到末尾，之后再添加<code>&quot;ma&quot;</code>。<br />
	例如，单词<code>&quot;goat&quot;</code>变为<code>&quot;oatgma&quot;</code>。</li>
	<br />
	<li>根据单词在句子中的索引，在单词最后添加与索引相同数量的字母<code>&#39;a&#39;</code>，索引从1开始。<br />
	例如，在第一个单词后添加<code>&quot;a&quot;</code>，在第二个单词后添加<code>&quot;aa&quot;</code>，以此类推。</li>
</ul>

<p>返回将&nbsp;<code>S</code>&nbsp;转换为山羊拉丁文后的句子。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>&quot;I speak Goat Latin&quot;
<strong>输出: </strong>&quot;Imaa peaksmaaa oatGmaaaa atinLmaaaaa&quot;
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>&quot;The quick brown fox jumped over the lazy dog&quot;
<strong>输出: </strong>&quot;heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa&quot;
</pre>

<p><strong>说明:</strong></p>

<ul>
	<li><code>S</code>&nbsp;中仅包含大小写字母和空格。单词间有且仅有一个空格。</li>
	<li><code>1 &lt;= S.length &lt;= 150</code>。</li>
</ul>
"""


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        