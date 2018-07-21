"""
<p>Given a list <code>accounts</code>, each element <code>accounts[i]</code> is a list of strings, where the first element <code>accounts[i][0]</code> is a <i>name</i>, and the rest of the elements are <i>emails</i> representing emails of the account.</p>

<p>Now, we would like to merge these accounts.  Two accounts definitely belong to the same person if there is some email that is common to both accounts.  Note that even if two accounts have the same name, they may belong to different people as people could have the same name.  A person can have any number of accounts initially, but all of their accounts definitely have the same name.</p>

<p>After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails <b>in sorted order</b>.  The accounts themselves can be returned in any order.</p>

<p><b>Example 1:</b><br />
<pre style="white-space: pre-wrap">
<b>Input:</b> 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
<b>Output:</b> [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
<b>Explanation:</b> 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>accounts</code> will be in the range <code>[1, 1000]</code>.</li>
<li>The length of <code>accounts[i]</code> will be in the range <code>[1, 10]</code>.</li>
<li>The length of <code>accounts[i][j]</code> will be in the range <code>[1, 30]</code>.</li>
</p><p>给定一个列表 <code>accounts</code>，每个元素 <code>accounts[i]</code>&nbsp;是一个字符串列表，其中第一个元素 <code>accounts[i][0]</code>&nbsp;是&nbsp;<em>名称 (name)</em>，其余元素是 <em>emails </em>表示该帐户的邮箱地址。</p>

<p>现在，我们想合并这些帐户。如果两个帐户都有一些共同的邮件地址，则两个帐户必定属于同一个人。请注意，即使两个帐户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的帐户，但其所有帐户都具有相同的名称。</p>

<p>合并帐户后，按以下格式返回帐户：每个帐户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。accounts 本身可以以任意顺序返回。</p>

<p><strong>例子 1:</strong></p>

<pre>
<strong>Input:</strong> 
accounts = [[&quot;John&quot;, &quot;johnsmith@mail.com&quot;, &quot;john00@mail.com&quot;], [&quot;John&quot;, &quot;johnnybravo@mail.com&quot;], [&quot;John&quot;, &quot;johnsmith@mail.com&quot;, &quot;john_newyork@mail.com&quot;], [&quot;Mary&quot;, &quot;mary@mail.com&quot;]]
<strong>Output:</strong> [[&quot;John&quot;, &#39;john00@mail.com&#39;, &#39;john_newyork@mail.com&#39;, &#39;johnsmith@mail.com&#39;],  [&quot;John&quot;, &quot;johnnybravo@mail.com&quot;], [&quot;Mary&quot;, &quot;mary@mail.com&quot;]]
<strong>Explanation:</strong> 
  第一个和第三个 John 是同一个人，因为他们有共同的电子邮件 &quot;johnsmith@mail.com&quot;。 
  第二个 John 和 Mary 是不同的人，因为他们的电子邮件地址没有被其他帐户使用。
  我们可以以任何顺序返回这些列表，例如答案[[&#39;Mary&#39;，&#39;mary@mail.com&#39;]，[&#39;John&#39;，&#39;johnnybravo@mail.com&#39;]，
  [&#39;John&#39;，&#39;john00@mail.com&#39;，&#39;john_newyork@mail.com&#39;，&#39;johnsmith@mail.com&#39;]]仍然会被接受。

</pre>

<p><strong>注意：</strong></p>

<ul>
	<li><code>accounts</code>的长度将在<code>[1，1000]</code>的范围内。</li>
	<li><code>accounts[i]</code>的长度将在<code>[1，10]</code>的范围内。</li>
	<li><code>accounts[i][j]</code>的长度将在<code>[1，30]</code>的范围内。</li>
</ul>
<p>给定一个列表 <code>accounts</code>，每个元素 <code>accounts[i]</code>&nbsp;是一个字符串列表，其中第一个元素 <code>accounts[i][0]</code>&nbsp;是&nbsp;<em>名称 (name)</em>，其余元素是 <em>emails </em>表示该帐户的邮箱地址。</p>

<p>现在，我们想合并这些帐户。如果两个帐户都有一些共同的邮件地址，则两个帐户必定属于同一个人。请注意，即使两个帐户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的帐户，但其所有帐户都具有相同的名称。</p>

<p>合并帐户后，按以下格式返回帐户：每个帐户的第一个元素是名称，其余元素是按顺序排列的邮箱地址。accounts 本身可以以任意顺序返回。</p>

<p><strong>例子 1:</strong></p>

<pre>
<strong>Input:</strong> 
accounts = [[&quot;John&quot;, &quot;johnsmith@mail.com&quot;, &quot;john00@mail.com&quot;], [&quot;John&quot;, &quot;johnnybravo@mail.com&quot;], [&quot;John&quot;, &quot;johnsmith@mail.com&quot;, &quot;john_newyork@mail.com&quot;], [&quot;Mary&quot;, &quot;mary@mail.com&quot;]]
<strong>Output:</strong> [[&quot;John&quot;, &#39;john00@mail.com&#39;, &#39;john_newyork@mail.com&#39;, &#39;johnsmith@mail.com&#39;],  [&quot;John&quot;, &quot;johnnybravo@mail.com&quot;], [&quot;Mary&quot;, &quot;mary@mail.com&quot;]]
<strong>Explanation:</strong> 
  第一个和第三个 John 是同一个人，因为他们有共同的电子邮件 &quot;johnsmith@mail.com&quot;。 
  第二个 John 和 Mary 是不同的人，因为他们的电子邮件地址没有被其他帐户使用。
  我们可以以任何顺序返回这些列表，例如答案[[&#39;Mary&#39;，&#39;mary@mail.com&#39;]，[&#39;John&#39;，&#39;johnnybravo@mail.com&#39;]，
  [&#39;John&#39;，&#39;john00@mail.com&#39;，&#39;john_newyork@mail.com&#39;，&#39;johnsmith@mail.com&#39;]]仍然会被接受。

</pre>

<p><strong>注意：</strong></p>

<ul>
	<li><code>accounts</code>的长度将在<code>[1，1000]</code>的范围内。</li>
	<li><code>accounts[i]</code>的长度将在<code>[1，10]</code>的范围内。</li>
	<li><code>accounts[i][j]</code>的长度将在<code>[1，30]</code>的范围内。</li>
</ul>
"""


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        