/*
<p>Some people will make friend requests. The&nbsp;list of their ages is given and&nbsp;<code>ages[i]</code>&nbsp;is the age of the&nbsp;ith person.&nbsp;</p>

<p>Person A will NOT friend request person B (B != A) if any of the following conditions are true:</p>

<ul>
	<li><code>age[B]&nbsp;&lt;= 0.5 * age[A]&nbsp;+ 7</code></li>
	<li><code>age[B]&nbsp;&gt; age[A]</code></li>
	<li><code>age[B]&nbsp;&gt; 100 &amp;&amp;&nbsp;age[A]&nbsp;&lt; 100</code></li>
</ul>

<p>Otherwise, A will friend request B.</p>

<p>Note that if&nbsp;A requests B, B does not necessarily request A.&nbsp; Also, people will not friend request themselves.</p>

<p>How many total friend requests are made?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[16,16]
<strong>Output: </strong>2
<strong>Explanation: </strong>2 people friend request each other.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[16,17,18]
<strong>Output: </strong>2
<strong>Explanation: </strong>Friend requests are made 17 -&gt; 16, 18 -&gt; 17.</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>[20,30,100,110,120]
<strong>Output: </strong>
<strong>Explanation: </strong>Friend requests are made 110 -&gt; 100, 120 -&gt; 110, 120 -&gt; 100.
</pre>

<p>&nbsp;</p>

<p>Notes:</p>

<ul>
	<li><code>1 &lt;= ages.length&nbsp;&lt;= 20000</code>.</li>
	<li><code>1 &lt;= ages[i] &lt;= 120</code>.</li>
</ul><p>人们会互相发送好友请求，现在给定一个包含有他们年龄的数组，<code>ages[i]</code>&nbsp;表示第 i 个人的年龄。</p>

<p>当满足以下条件时，A 不能给 B（A、B不为同一人）发送好友请求：</p>

<ul>
	<li><code>age[B]&nbsp;&lt;= 0.5 * age[A]&nbsp;+ 7</code></li>
	<li><code>age[B]&nbsp;&gt; age[A]</code></li>
	<li><code>age[B]&nbsp;&gt; 100 &amp;&amp;&nbsp;age[A]&nbsp;&lt; 100</code></li>
</ul>

<p>否则，A 可以给 B 发送好友请求。</p>

<p>注意如果 A 向 B 发出了请求，不等于 B 接受了 A 的请求。而且，人们不会给自己发送好友请求。&nbsp;</p>

<p>求总共会发出多少份好友请求?</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>[16,16]
<strong>输出: </strong>2
<strong>解释: 二人可以互发好友申请。</strong>
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>[16,17,18]
<strong>输出: </strong>2
<strong>解释: 好友请求可产生于</strong> 17 -&gt; 16, 18 -&gt; 17.</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>[20,30,100,110,120]
<strong>输出: 3</strong>
<strong>解释: 好友请求可产生于</strong> 110 -&gt; 100, 120 -&gt; 110, 120 -&gt; 100.
</pre>

<p><strong>说明:</strong></p>

<ul>
	<li><code>1 &lt;= ages.length&nbsp;&lt;= 20000</code>.</li>
	<li><code>1 &lt;= ages[i] &lt;= 120</code>.</li>
</ul>
<p>人们会互相发送好友请求，现在给定一个包含有他们年龄的数组，<code>ages[i]</code>&nbsp;表示第 i 个人的年龄。</p>

<p>当满足以下条件时，A 不能给 B（A、B不为同一人）发送好友请求：</p>

<ul>
	<li><code>age[B]&nbsp;&lt;= 0.5 * age[A]&nbsp;+ 7</code></li>
	<li><code>age[B]&nbsp;&gt; age[A]</code></li>
	<li><code>age[B]&nbsp;&gt; 100 &amp;&amp;&nbsp;age[A]&nbsp;&lt; 100</code></li>
</ul>

<p>否则，A 可以给 B 发送好友请求。</p>

<p>注意如果 A 向 B 发出了请求，不等于 B 接受了 A 的请求。而且，人们不会给自己发送好友请求。&nbsp;</p>

<p>求总共会发出多少份好友请求?</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入: </strong>[16,16]
<strong>输出: </strong>2
<strong>解释: 二人可以互发好友申请。</strong>
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>[16,17,18]
<strong>输出: </strong>2
<strong>解释: 好友请求可产生于</strong> 17 -&gt; 16, 18 -&gt; 17.</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>[20,30,100,110,120]
<strong>输出: 3</strong>
<strong>解释: 好友请求可产生于</strong> 110 -&gt; 100, 120 -&gt; 110, 120 -&gt; 100.
</pre>

<p><strong>说明:</strong></p>

<ul>
	<li><code>1 &lt;= ages.length&nbsp;&lt;= 20000</code>.</li>
	<li><code>1 &lt;= ages[i] &lt;= 120</code>.</li>
</ul>
*/


int numFriendRequests(int* ages, int agesSize) {
    
}