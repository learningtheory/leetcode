"""
<p>
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
note can be constructed from the magazines ; otherwise, it will return false. 
</p>
<p>
Each letter in the magazine string can only be used once in your ransom note.
</p>

<p><b>Note:</b><br />
You may assume that both strings contain only lowercase letters.
</p>

<pre>
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
</pre>
<p>给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。</p>

<p>(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)</p>

<p><strong>注意：</strong></p>

<p>你可以假设两个字符串均只含有小写字母。</p>

<pre>
canConstruct(&quot;a&quot;, &quot;b&quot;) -&gt; false
canConstruct(&quot;aa&quot;, &quot;ab&quot;) -&gt; false
canConstruct(&quot;aa&quot;, &quot;aab&quot;) -&gt; true
</pre>
<p>给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。</p>

<p>(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)</p>

<p><strong>注意：</strong></p>

<p>你可以假设两个字符串均只含有小写字母。</p>

<pre>
canConstruct(&quot;a&quot;, &quot;b&quot;) -&gt; false
canConstruct(&quot;aa&quot;, &quot;ab&quot;) -&gt; false
canConstruct(&quot;aa&quot;, &quot;aab&quot;) -&gt; true
</pre>
"""


class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        