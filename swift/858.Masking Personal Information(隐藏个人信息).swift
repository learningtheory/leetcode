/*
<p>We are given a&nbsp;personal information string <code>S</code>, which may represent&nbsp;either <strong>an email address</strong> or <strong>a phone number.</strong></p>

<p>We would like to mask this&nbsp;personal information according to the&nbsp;following rules:</p>

<p><br />
<u><strong>1. Email address:</strong></u></p>

<p>We define a&nbsp;<strong>name</strong> to be a string of <code>length &ge; 2</code> consisting&nbsp;of only lowercase letters&nbsp;<code>a-z</code> or uppercase&nbsp;letters&nbsp;<code>A-Z</code>.</p>

<p>An email address starts with a name, followed by the&nbsp;symbol <code>&#39;@&#39;</code>, followed by a name, followed by the&nbsp;dot&nbsp;<code>&#39;.&#39;</code>&nbsp;and&nbsp;followed by a name.&nbsp;</p>

<p>All email addresses are&nbsp;guaranteed to be valid and in the format of&nbsp;<code>&quot;name1@name2.name3&quot;.</code></p>

<p>To mask an email, <strong>all names must be converted to lowercase</strong> and <strong>all letters between the first and last letter of the first name</strong> must be replaced by 5 asterisks <code>&#39;*&#39;</code>.</p>

<p><br />
<u><strong>2. Phone number:</strong></u></p>

<p>A phone number is a string consisting of&nbsp;only the digits <code>0-9</code> or the characters from the set <code>{&#39;+&#39;, &#39;-&#39;, &#39;(&#39;, &#39;)&#39;, &#39;&nbsp;&#39;}.</code>&nbsp;You may assume a phone&nbsp;number contains&nbsp;10 to 13 digits.</p>

<p>The last 10 digits make up the local&nbsp;number, while the digits before those make up the country code. Note that&nbsp;the country code is optional. We want to expose only the last 4 digits&nbsp;and mask all other&nbsp;digits.</p>

<p>The local&nbsp;number&nbsp;should be formatted and masked as <code>&quot;***-***-1111&quot;,&nbsp;</code>where <code>1</code> represents the exposed digits.</p>

<p>To mask a phone number with country code like <code>&quot;+111 111 111 1111&quot;</code>, we write it in the form <code>&quot;+***-***-***-1111&quot;.</code>&nbsp; The <code>&#39;+&#39;</code>&nbsp;sign and the first <code>&#39;-&#39;</code>&nbsp;sign before the local number should only exist if there is a country code.&nbsp; For example, a 12 digit phone number mask&nbsp;should start&nbsp;with <code>&quot;+**-&quot;</code>.</p>

<p>Note that extraneous characters like <code>&quot;(&quot;, &quot;)&quot;, &quot; &quot;</code>, as well as&nbsp;extra dashes or plus signs not part of the above formatting scheme should be removed.</p>

<p>&nbsp;</p>

<p>Return the correct &quot;mask&quot; of the information provided.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>&quot;LeetCode@LeetCode.com&quot;
<strong>Output: </strong>&quot;l*****e@leetcode.com&quot;
<strong>Explanation:&nbsp;</strong>All names are converted to lowercase, and the letters between the
&nbsp;            first and last letter of the first name is replaced by 5 asterisks.
&nbsp;            Therefore, &quot;leetcode&quot; -&gt; &quot;l*****e&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;AB@qq.com&quot;
<strong>Output: </strong>&quot;a*****b@qq.com&quot;
<strong>Explanation:&nbsp;</strong>There must be 5 asterisks between the first and last letter 
&nbsp;            of the first name &quot;ab&quot;. Therefore, &quot;ab&quot; -&gt; &quot;a*****b&quot;.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>&quot;1(234)567-890&quot;
<strong>Output: </strong>&quot;***-***-7890&quot;
<strong>Explanation:</strong>&nbsp;10 digits in the phone number, which means all digits make up the local number.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>&quot;86-(10)12345678&quot;
<strong>Output: </strong>&quot;+**-***-***-5678&quot;
<strong>Explanation:</strong>&nbsp;12 digits, 2 digits for country code and 10 digits for local number. 
</pre>

<p><strong>Notes:</strong></p>

<ol>
	<li><code>S.length&nbsp;&lt;=&nbsp;40</code>.</li>
	<li>Emails have length at least 8.</li>
	<li>Phone numbers have length at least 10.</li>
</ol><p>给你一条个人信息 string <code>S</code>，它可能是一个邮箱地址，也可能是一个电话号码。</p>

<p>我们将隐藏它的隐私信息，通过如下规则:</p>

<p>1. 电子邮箱</p>

<p>定义名称 &lt;name&gt; 的长度大于2，并且只包含小写字母 a-z 和大写字母 A-Z。</p>

<p>电子邮箱地址由名称 &lt;name&gt; 开头，紧接着是符号&nbsp;<a href="mailto:'@'">&#39;@&#39;</a>，后面接着一个名称 &lt;name&gt;，再接着一个点号 &#39;.&#39;，然后是一个名称 &lt;name&gt;。</p>

<p>电子邮箱地址确定为有效的，并且格式是&quot;<a href="mailto:name1@name2.name3">name1@name2.name3</a>&quot;。</p>

<p>为了隐藏电子邮箱，所有的名称 &lt;name&gt; 必须被转换成小写的，并且第一个名称 &lt;name&gt; 的第一个字母和最后一个字母的中间的所有字母由 5 个 &#39;*&#39; 代替。</p>

<p>2. 电话号码</p>

<p>电话号码是一串包括数组 0-9，以及 {&#39;+&#39;, &#39;-&#39;, &#39;(&#39;, &#39;)&#39;, &#39;&nbsp;&#39;} 这几个字符的字符串。你可以假设电话号码包含 10 到 13 个数字。</p>

<p>电话号码的最后 10 个数字组成本地号码，在这之前的数字组成国际号码。注意，国际号码是可选的。我们只暴露最后 4 个数字并隐藏所有其他数字。</p>

<p>本地号码是有格式的，并且如 &quot;***-***-1111&quot; 这样显示，这里的 1 表示暴露的数字。</p>

<p>为了隐藏有国际号码的电话号码，像 &quot;+111 111 111 1111&quot;，我们以 &quot;+***-***-***-1111&quot; 的格式来显示。在本地号码前面的 &#39;+&#39; 号和第一个 &#39;-&#39; 号仅当电话号码中包含国际号码时存在。例如，一个 12 位的电话号码应当以 &quot;+**-&quot; 开头进行显示。</p>

<p>注意：像 &quot;(&quot;，&quot;)&quot;，&quot; &quot; 这样的不相干的字符以及不符合上述格式的额外的减号或者加号都应当被删除。</p>

<p>&nbsp;</p>

<p>最后，将提供的信息正确隐藏后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>&quot;LeetCode@LeetCode.com&quot;
<strong>输出: </strong>&quot;l*****e@leetcode.com&quot;
<strong>解释： 
</strong>所有的名称转换成小写, 第一个名称的第一个字符和最后一个字符中间由 5 个星号代替。
因此，&quot;leetcode&quot; -&gt; &quot;l*****e&quot;。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>&quot;AB@qq.com&quot;
<strong>输出: </strong>&quot;a*****b@qq.com&quot;
<strong>解释:&nbsp;
</strong>第一个名称&quot;ab&quot;的第一个字符和最后一个字符的中间必须有 5 个星号
因此，&quot;ab&quot; -&gt; &quot;a*****b&quot;。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入: </strong>&quot;1(234)567-890&quot;
<strong>输出: </strong>&quot;***-***-7890&quot;
<strong>解释:</strong>&nbsp;
10 个数字的电话号码，那意味着所有的数字都是本地号码。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入: </strong>&quot;86-(10)12345678&quot;
<strong>输出: </strong>&quot;+**-***-***-5678&quot;
<strong>解释:</strong>&nbsp;
12 位数字，2 个数字是国际号码另外 10 个数字是本地号码 。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>S.length&nbsp;&lt;=&nbsp;40</code>。</li>
	<li>邮箱的长度至少是 8。</li>
	<li>电话号码的长度至少是 10。</li>
</ol>
<p>给你一条个人信息 string <code>S</code>，它可能是一个邮箱地址，也可能是一个电话号码。</p>

<p>我们将隐藏它的隐私信息，通过如下规则:</p>

<p>1. 电子邮箱</p>

<p>定义名称 &lt;name&gt; 的长度大于2，并且只包含小写字母 a-z 和大写字母 A-Z。</p>

<p>电子邮箱地址由名称 &lt;name&gt; 开头，紧接着是符号&nbsp;<a href="mailto:'@'">&#39;@&#39;</a>，后面接着一个名称 &lt;name&gt;，再接着一个点号 &#39;.&#39;，然后是一个名称 &lt;name&gt;。</p>

<p>电子邮箱地址确定为有效的，并且格式是&quot;<a href="mailto:name1@name2.name3">name1@name2.name3</a>&quot;。</p>

<p>为了隐藏电子邮箱，所有的名称 &lt;name&gt; 必须被转换成小写的，并且第一个名称 &lt;name&gt; 的第一个字母和最后一个字母的中间的所有字母由 5 个 &#39;*&#39; 代替。</p>

<p>2. 电话号码</p>

<p>电话号码是一串包括数组 0-9，以及 {&#39;+&#39;, &#39;-&#39;, &#39;(&#39;, &#39;)&#39;, &#39;&nbsp;&#39;} 这几个字符的字符串。你可以假设电话号码包含 10 到 13 个数字。</p>

<p>电话号码的最后 10 个数字组成本地号码，在这之前的数字组成国际号码。注意，国际号码是可选的。我们只暴露最后 4 个数字并隐藏所有其他数字。</p>

<p>本地号码是有格式的，并且如 &quot;***-***-1111&quot; 这样显示，这里的 1 表示暴露的数字。</p>

<p>为了隐藏有国际号码的电话号码，像 &quot;+111 111 111 1111&quot;，我们以 &quot;+***-***-***-1111&quot; 的格式来显示。在本地号码前面的 &#39;+&#39; 号和第一个 &#39;-&#39; 号仅当电话号码中包含国际号码时存在。例如，一个 12 位的电话号码应当以 &quot;+**-&quot; 开头进行显示。</p>

<p>注意：像 &quot;(&quot;，&quot;)&quot;，&quot; &quot; 这样的不相干的字符以及不符合上述格式的额外的减号或者加号都应当被删除。</p>

<p>&nbsp;</p>

<p>最后，将提供的信息正确隐藏后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>&quot;LeetCode@LeetCode.com&quot;
<strong>输出: </strong>&quot;l*****e@leetcode.com&quot;
<strong>解释： 
</strong>所有的名称转换成小写, 第一个名称的第一个字符和最后一个字符中间由 5 个星号代替。
因此，&quot;leetcode&quot; -&gt; &quot;l*****e&quot;。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>&quot;AB@qq.com&quot;
<strong>输出: </strong>&quot;a*****b@qq.com&quot;
<strong>解释:&nbsp;
</strong>第一个名称&quot;ab&quot;的第一个字符和最后一个字符的中间必须有 5 个星号
因此，&quot;ab&quot; -&gt; &quot;a*****b&quot;。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入: </strong>&quot;1(234)567-890&quot;
<strong>输出: </strong>&quot;***-***-7890&quot;
<strong>解释:</strong>&nbsp;
10 个数字的电话号码，那意味着所有的数字都是本地号码。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入: </strong>&quot;86-(10)12345678&quot;
<strong>输出: </strong>&quot;+**-***-***-5678&quot;
<strong>解释:</strong>&nbsp;
12 位数字，2 个数字是国际号码另外 10 个数字是本地号码 。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>S.length&nbsp;&lt;=&nbsp;40</code>。</li>
	<li>邮箱的长度至少是 8。</li>
	<li>电话号码的长度至少是 10。</li>
</ol>
*/


class Solution {
    func maskPII(_ S: String) -> String {
        
    }
}