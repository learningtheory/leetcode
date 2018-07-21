"""
<p>You are given a license key represented as a string S which consists only alphanumeric character and dashes. The string is separated into N+1 groups by N dashes.</p>

<p>Given a number K, we would want to reformat the strings such that each group contains <i>exactly</i> K characters, except for the first group which could be shorter than K, but still must contain at least one character. Furthermore, there must be a dash inserted between two groups and all lowercase letters should be converted to uppercase.</p>

<p>Given a non-empty string S and a number K, format the string according to the rules described above.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> S = "5F3Z-2e-9-w", K = 4

<b>Output:</b> "5F3Z-2E9W"

<b>Explanation:</b> The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> S = "2-5g-3-J", K = 2

<b>Output:</b> "2-5G-3J"

<b>Explanation:</b> The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The length of string S will not exceed 12,000, and K is a positive integer.</li>
<li>String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).</li>
<li>String S is non-empty.</li>
</ol>
</p><p>给定一个密钥字符串S，只包含字母，数字以及 &#39;-&#39;（破折号）。N 个 &#39;-&#39; 将字符串分成了 N+1 组。给定一个数字 K，重新格式化字符串，除了第一个分组以外，每个分组要包含 K 个字符，第一个分组至少要包含 1 个字符。两个分组之间用 &#39;-&#39;（破折号）隔开，并且将所有的小写字母转换为大写字母。</p>

<p>给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>S = &quot;5F3Z-2e-9-w&quot;, K = 4

<strong>输出：</strong>&quot;5F3Z-2E9W&quot;

<strong>解释：</strong>字符串 S 被分成了两个部分，每部分 4 个字符；
&nbsp;    注意，两个额外的破折号需要删掉。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>S = &quot;2-5g-3-J&quot;, K = 2

<strong>输出：</strong>&quot;2-5G-3J&quot;

<strong>解释：</strong>字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ol>
	<li>S 的长度不超过 12,000，K 为正整数</li>
	<li>S 只包含字母数字（a-z，A-Z，0-9）以及破折号&#39;-&#39;</li>
	<li>S 非空</li>
</ol>

<p>&nbsp;</p>
<p>给定一个密钥字符串S，只包含字母，数字以及 &#39;-&#39;（破折号）。N 个 &#39;-&#39; 将字符串分成了 N+1 组。给定一个数字 K，重新格式化字符串，除了第一个分组以外，每个分组要包含 K 个字符，第一个分组至少要包含 1 个字符。两个分组之间用 &#39;-&#39;（破折号）隔开，并且将所有的小写字母转换为大写字母。</p>

<p>给定非空字符串 S 和数字 K，按照上面描述的规则进行格式化。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>S = &quot;5F3Z-2e-9-w&quot;, K = 4

<strong>输出：</strong>&quot;5F3Z-2E9W&quot;

<strong>解释：</strong>字符串 S 被分成了两个部分，每部分 4 个字符；
&nbsp;    注意，两个额外的破折号需要删掉。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>S = &quot;2-5g-3-J&quot;, K = 2

<strong>输出：</strong>&quot;2-5G-3J&quot;

<strong>解释：</strong>字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ol>
	<li>S 的长度不超过 12,000，K 为正整数</li>
	<li>S 只包含字母数字（a-z，A-Z，0-9）以及破折号&#39;-&#39;</li>
	<li>S 非空</li>
</ol>

<p>&nbsp;</p>
"""


class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        