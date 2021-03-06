"""
<p>
Implement a magic directory with <code>buildDict</code>, and <code>search</code> methods.
</p>

<p>
For the method <code>buildDict</code>, you'll be given a list of non-repetitive words to build a dictionary.
</p>

<p>
For the method <code>search</code>, you'll be given a word, and judge whether if you modify <b>exactly</b> one character into <b>another</b> character in this word, the modified word is in the dictionary you just built.
</p>

<p><b>Example 1:</b><br />
<pre>
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>You may assume that all the inputs are consist of lowercase letters <code>a-z</code>.</li>
<li>For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.</li>
<li>Please remember to <b>RESET</b> your class variables declared in class MagicDictionary, as static/class variables are <b>persisted across multiple test cases</b>. Please see <a href="https://leetcode.com/faq/#different-output">here</a> for more details.</li>
</ol>
</p><p>实现一个带有<code>buildDict</code>, 以及&nbsp;<code>search</code>方法的魔法字典。</p>

<p>对于<code>buildDict</code>方法，你将被给定一串不重复的单词来构建一个字典。</p>

<p>对于<code>search</code>方法，你将被给定一个单词，并且判定能否只将这个单词中<strong>一个</strong>字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。</p>

<p><strong>示例 1:</strong></p>

<pre>
Input: buildDict([&quot;hello&quot;, &quot;leetcode&quot;]), Output: Null
Input: search(&quot;hello&quot;), Output: False
Input: search(&quot;hhllo&quot;), Output: True
Input: search(&quot;hell&quot;), Output: False
Input: search(&quot;leetcoded&quot;), Output: False
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>你可以假设所有输入都是小写字母&nbsp;<code>a-z</code>。</li>
	<li>为了便于竞赛，测试所用的数据量很小。你可以在竞赛结束后，考虑更高效的算法。</li>
	<li>请记住<strong>重置</strong>MagicDictionary类中声明的类变量，因为静态/类变量会在多个测试用例中保留。 请参阅<a href="http://leetcode.com/faq/#different-output">这里</a>了解更多详情。</li>
</ol>
<p>实现一个带有<code>buildDict</code>, 以及&nbsp;<code>search</code>方法的魔法字典。</p>

<p>对于<code>buildDict</code>方法，你将被给定一串不重复的单词来构建一个字典。</p>

<p>对于<code>search</code>方法，你将被给定一个单词，并且判定能否只将这个单词中<strong>一个</strong>字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。</p>

<p><strong>示例 1:</strong></p>

<pre>
Input: buildDict([&quot;hello&quot;, &quot;leetcode&quot;]), Output: Null
Input: search(&quot;hello&quot;), Output: False
Input: search(&quot;hhllo&quot;), Output: True
Input: search(&quot;hell&quot;), Output: False
Input: search(&quot;leetcoded&quot;), Output: False
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>你可以假设所有输入都是小写字母&nbsp;<code>a-z</code>。</li>
	<li>为了便于竞赛，测试所用的数据量很小。你可以在竞赛结束后，考虑更高效的算法。</li>
	<li>请记住<strong>重置</strong>MagicDictionary类中声明的类变量，因为静态/类变量会在多个测试用例中保留。 请参阅<a href="http://leetcode.com/faq/#different-output">这里</a>了解更多详情。</li>
</ol>
"""


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)