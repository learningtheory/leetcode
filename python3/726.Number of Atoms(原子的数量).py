"""
<p>Given a chemical <code>formula</code> (given as a string), return the count of each atom.
</p><p>
An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
</p><p>
1 or more digits representing the count of that element may follow if the count is greater than 1.  If the count is 1, no digits will follow.  For example, H2O and H2O2 are possible, but H1O2 is impossible.
</p><p>
Two formulas concatenated together produce another formula.  For example, H2O2He3Mg4 is also a formula.  
</p><p>
A formula placed in parentheses, and a count (optionally added) is also a formula.  For example, (H2O2) and (H2O2)3 are formulas.
</p><p>
Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
formula = "H2O"
<b>Output:</b> "H2O"
<b>Explanation:</b> 
The count of elements are {'H': 2, 'O': 1}.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
formula = "Mg(OH)2"
<b>Output:</b> "H2MgO2"
<b>Explanation:</b> 
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> 
formula = "K4(ON(SO3)2)2"
<b>Output:</b> "K4N2O14S4"
<b>Explanation:</b> 
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
</pre>
</p>

<p><b>Note:</b>
<li>All atom names consist of lowercase letters, except for the first character which is uppercase.</li>
<li>The length of <code>formula</code> will be in the range <code>[1, 1000]</code>.</li>
<li><code>formula</code> will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.</li>
</p><p>给定一个化学式<code>formula</code>（作为字符串），返回每种原子的数量。</p>

<p>原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。</p>

<p>如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。</p>

<p>两个化学式连在一起是新的化学式。例如&nbsp;H2O2He3Mg4 也是化学式。</p>

<p>一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。</p>

<p>给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
formula = &quot;H2O&quot;
<strong>输出:</strong> &quot;H2O&quot;
<strong>解释:</strong> 
原子的数量是 {&#39;H&#39;: 2, &#39;O&#39;: 1}。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
formula = &quot;Mg(OH)2&quot;
<strong>输出:</strong> &quot;H2MgO2&quot;
<strong>解释:</strong> 
原子的数量是 {&#39;H&#39;: 2, &#39;Mg&#39;: 1, &#39;O&#39;: 2}。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> 
formula = &quot;K4(ON(SO3)2)2&quot;
<strong>输出:</strong> &quot;K4N2O14S4&quot;
<strong>解释:</strong> 
原子的数量是 {&#39;K&#39;: 4, &#39;N&#39;: 2, &#39;O&#39;: 14, &#39;S&#39;: 4}。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li>所有原子的第一个字母为大写，剩余字母都是小写。</li>
	<li><code>formula</code>的长度在<code>[1, 1000]</code>之间。</li>
	<li><code>formula</code>只包含字母、数字和圆括号，并且题目中给定的是合法的化学式。</li>
</ul>
<p>给定一个化学式<code>formula</code>（作为字符串），返回每种原子的数量。</p>

<p>原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。</p>

<p>如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。</p>

<p>两个化学式连在一起是新的化学式。例如&nbsp;H2O2He3Mg4 也是化学式。</p>

<p>一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。</p>

<p>给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
formula = &quot;H2O&quot;
<strong>输出:</strong> &quot;H2O&quot;
<strong>解释:</strong> 
原子的数量是 {&#39;H&#39;: 2, &#39;O&#39;: 1}。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
formula = &quot;Mg(OH)2&quot;
<strong>输出:</strong> &quot;H2MgO2&quot;
<strong>解释:</strong> 
原子的数量是 {&#39;H&#39;: 2, &#39;Mg&#39;: 1, &#39;O&#39;: 2}。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> 
formula = &quot;K4(ON(SO3)2)2&quot;
<strong>输出:</strong> &quot;K4N2O14S4&quot;
<strong>解释:</strong> 
原子的数量是 {&#39;K&#39;: 4, &#39;N&#39;: 2, &#39;O&#39;: 14, &#39;S&#39;: 4}。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li>所有原子的第一个字母为大写，剩余字母都是小写。</li>
	<li><code>formula</code>的长度在<code>[1, 1000]</code>之间。</li>
	<li><code>formula</code>只包含字母、数字和圆括号，并且题目中给定的是合法的化学式。</li>
</ul>
"""


class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        