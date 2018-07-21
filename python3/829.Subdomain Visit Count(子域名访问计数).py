"""
<p>A website domain like &quot;discuss.leetcode.com&quot; consists of various subdomains. At the top level, we have &quot;com&quot;, at the next level, we have &quot;leetcode.com&quot;, and at the lowest level, &quot;discuss.leetcode.com&quot;. When we visit a domain like &quot;discuss.leetcode.com&quot;, we will also visit the parent domains &quot;leetcode.com&quot; and &quot;com&quot; implicitly.</p>

<p>Now, call a &quot;count-paired domain&quot; to be a count (representing the number of visits this domain received), followed by a space, followed by the address. An example of a count-paired domain might be &quot;9001 discuss.leetcode.com&quot;.</p>

<p>We are given a list <code>cpdomains</code> of count-paired domains. We would like a list of count-paired domains, (in the same format as the input, and in any order), that explicitly counts the number of visits to each subdomain.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> 
[&quot;9001 discuss.leetcode.com&quot;]
<strong>Output:</strong> 
[&quot;9001 discuss.leetcode.com&quot;, &quot;9001 leetcode.com&quot;, &quot;9001 com&quot;]
<strong>Explanation:</strong> 
We only have one website domain: &quot;discuss.leetcode.com&quot;. As discussed above, the subdomain &quot;leetcode.com&quot; and &quot;com&quot; will also be visited. So they will all be visited 9001 times.

</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> 
[&quot;900 google.mail.com&quot;, &quot;50 yahoo.com&quot;, &quot;1 intel.mail.com&quot;, &quot;5 wiki.org&quot;]
<strong>Output:</strong> 
[&quot;901 mail.com&quot;,&quot;50 yahoo.com&quot;,&quot;900 google.mail.com&quot;,&quot;5 wiki.org&quot;,&quot;5 org&quot;,&quot;1 intel.mail.com&quot;,&quot;951 com&quot;]
<strong>Explanation:</strong> 
We will visit &quot;google.mail.com&quot; 900 times, &quot;yahoo.com&quot; 50 times, &quot;intel.mail.com&quot; once and &quot;wiki.org&quot; 5 times. For the subdomains, we will visit &quot;mail.com&quot; 900 + 1 = 901 times, &quot;com&quot; 900 + 50 + 1 = 951 times, and &quot;org&quot; 5 times.

</pre>

<p><strong>Notes: </strong></p>

<ul>
	<li>The length of <code>cpdomains</code> will not exceed&nbsp;<code>100</code>.&nbsp;</li>
	<li>The length of each domain name will not exceed <code>100</code>.</li>
	<li>Each address will have either 1 or 2 &quot;.&quot; characters.</li>
	<li>The input count&nbsp;in any count-paired domain will not exceed <code>10000</code>.</li>
	<li>The answer output can be returned in any order.</li>
</ul>
<p>一个网站域名，如&quot;discuss.leetcode.com&quot;，包含了多个子域名。作为顶级域名，常用的有&quot;com&quot;，下一级则有&quot;leetcode.com&quot;，最低的一级为&quot;discuss.leetcode.com&quot;。当我们访问域名&quot;discuss.leetcode.com&quot;时，也同时访问了其父域名&quot;leetcode.com&quot;以及顶级域名&nbsp;&quot;com&quot;。</p>

<p>给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。其格式为访问次数+空格+地址，例如：&quot;9001 discuss.leetcode.com&quot;。</p>

<p>接下来会给出一组访问次数和域名组合的列表<code>cpdomains</code>&nbsp;。要求解析出所有域名的访问次数，输出格式和输入格式相同，不限定先后顺序。</p>

<pre>
<strong>示例 1:</strong>
<strong>输入:</strong> 
[&quot;9001 discuss.leetcode.com&quot;]
<strong>输出:</strong> 
[&quot;9001 discuss.leetcode.com&quot;, &quot;9001 leetcode.com&quot;, &quot;9001 com&quot;]
<strong>说明:</strong> 
例子中仅包含一个网站域名：&quot;discuss.leetcode.com&quot;。按照前文假设，子域名&quot;leetcode.com&quot;和&quot;com&quot;都会被访问，所以它们都被访问了9001次。
</pre>

<pre>
<strong>示例 2
输入:</strong> 
[&quot;900 google.mail.com&quot;, &quot;50 yahoo.com&quot;, &quot;1 intel.mail.com&quot;, &quot;5 wiki.org&quot;]
<strong>输出:</strong> 
[&quot;901 mail.com&quot;,&quot;50 yahoo.com&quot;,&quot;900 google.mail.com&quot;,&quot;5 wiki.org&quot;,&quot;5 org&quot;,&quot;1 intel.mail.com&quot;,&quot;951 com&quot;]
<strong>说明:</strong> 
按照假设，会访问&quot;google.mail.com&quot; 900次，&quot;yahoo.com&quot; 50次，&quot;intel.mail.com&quot; 1次，&quot;wiki.org&quot; 5次。
而对于父域名，会访问&quot;mail.com&quot; 900+1 = 901次，&quot;com&quot; 900 + 50 + 1 = 951次，和 &quot;org&quot; 5 次。
</pre>

<p><strong>注意事项：</strong></p>

<ul>
	<li>&nbsp;<code>cpdomains</code>&nbsp;的长度小于&nbsp;<code>100</code>。</li>
	<li>每个域名的长度小于<code>100</code>。</li>
	<li>每个域名地址包含一个或两个&quot;.&quot;符号。</li>
	<li>输入中任意一个域名的访问次数都小于<code>10000</code>。</li>
</ul>
<p>一个网站域名，如&quot;discuss.leetcode.com&quot;，包含了多个子域名。作为顶级域名，常用的有&quot;com&quot;，下一级则有&quot;leetcode.com&quot;，最低的一级为&quot;discuss.leetcode.com&quot;。当我们访问域名&quot;discuss.leetcode.com&quot;时，也同时访问了其父域名&quot;leetcode.com&quot;以及顶级域名&nbsp;&quot;com&quot;。</p>

<p>给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。其格式为访问次数+空格+地址，例如：&quot;9001 discuss.leetcode.com&quot;。</p>

<p>接下来会给出一组访问次数和域名组合的列表<code>cpdomains</code>&nbsp;。要求解析出所有域名的访问次数，输出格式和输入格式相同，不限定先后顺序。</p>

<pre>
<strong>示例 1:</strong>
<strong>输入:</strong> 
[&quot;9001 discuss.leetcode.com&quot;]
<strong>输出:</strong> 
[&quot;9001 discuss.leetcode.com&quot;, &quot;9001 leetcode.com&quot;, &quot;9001 com&quot;]
<strong>说明:</strong> 
例子中仅包含一个网站域名：&quot;discuss.leetcode.com&quot;。按照前文假设，子域名&quot;leetcode.com&quot;和&quot;com&quot;都会被访问，所以它们都被访问了9001次。
</pre>

<pre>
<strong>示例 2
输入:</strong> 
[&quot;900 google.mail.com&quot;, &quot;50 yahoo.com&quot;, &quot;1 intel.mail.com&quot;, &quot;5 wiki.org&quot;]
<strong>输出:</strong> 
[&quot;901 mail.com&quot;,&quot;50 yahoo.com&quot;,&quot;900 google.mail.com&quot;,&quot;5 wiki.org&quot;,&quot;5 org&quot;,&quot;1 intel.mail.com&quot;,&quot;951 com&quot;]
<strong>说明:</strong> 
按照假设，会访问&quot;google.mail.com&quot; 900次，&quot;yahoo.com&quot; 50次，&quot;intel.mail.com&quot; 1次，&quot;wiki.org&quot; 5次。
而对于父域名，会访问&quot;mail.com&quot; 900+1 = 901次，&quot;com&quot; 900 + 50 + 1 = 951次，和 &quot;org&quot; 5 次。
</pre>

<p><strong>注意事项：</strong></p>

<ul>
	<li>&nbsp;<code>cpdomains</code>&nbsp;的长度小于&nbsp;<code>100</code>。</li>
	<li>每个域名的长度小于<code>100</code>。</li>
	<li>每个域名地址包含一个或两个&quot;.&quot;符号。</li>
	<li>输入中任意一个域名的访问次数都小于<code>10000</code>。</li>
</ul>
"""


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        