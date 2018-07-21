/**
<p>Given a positive integer <b>n</b>, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 10<sup>9</sup> + 7.</p>

<p>A student attendance record is a string that only contains the following three characters:</p>

<p>
<ol>
<li><b>'A'</b> : Absent. </li>
<li><b>'L'</b> : Late.</li>
<li> <b>'P'</b> : Present. </li>
</ol>
</p>

<p>
A record is regarded as rewardable if it doesn't contain <b>more than one 'A' (absent)</b> or <b>more than two continuous 'L' (late)</b>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> n = 2
<b>Output:</b> 8 
<b>Explanation:</b>
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
</pre>
</p>

<p><b>Note:</b>
The value of <b>n</b> won't exceed 100,000.
</p>


<p>给定一个正整数&nbsp;<strong>n</strong>，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 10<sup>9</sup> + 7的值。</p>

<p>学生出勤记录是只包含以下三个字符的字符串：</p>

<ol>
	<li><strong>&#39;A&#39;</strong> : Absent，缺勤</li>
	<li><strong>&#39;L&#39;</strong> : Late，迟到</li>
	<li><strong>&#39;P&#39;</strong> : Present，到场</li>
</ol>

<p>如果记录不包含<strong>多于一个&#39;A&#39;（缺勤）</strong>或<strong>超过两个连续的&#39;L&#39;（迟到）</strong>，则该记录被视为可奖励的。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> n = 2
<strong>输出:</strong> 8 <strong>
解释：</strong>
有8个长度为2的记录将被视为可奖励：
&quot;PP&quot; , &quot;AP&quot;, &quot;PA&quot;, &quot;LP&quot;, &quot;PL&quot;, &quot;AL&quot;, &quot;LA&quot;, &quot;LL&quot;
只有&quot;AA&quot;不会被视为可奖励，因为缺勤次数超过一次。</pre>

<p><strong>注意：n </strong>的值不会超过100000。</p>
<p>给定一个正整数&nbsp;<strong>n</strong>，返回长度为 n 的所有可被视为可奖励的出勤记录的数量。 答案可能非常大，你只需返回结果mod 10<sup>9</sup> + 7的值。</p>

<p>学生出勤记录是只包含以下三个字符的字符串：</p>

<ol>
	<li><strong>&#39;A&#39;</strong> : Absent，缺勤</li>
	<li><strong>&#39;L&#39;</strong> : Late，迟到</li>
	<li><strong>&#39;P&#39;</strong> : Present，到场</li>
</ol>

<p>如果记录不包含<strong>多于一个&#39;A&#39;（缺勤）</strong>或<strong>超过两个连续的&#39;L&#39;（迟到）</strong>，则该记录被视为可奖励的。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> n = 2
<strong>输出:</strong> 8 <strong>
解释：</strong>
有8个长度为2的记录将被视为可奖励：
&quot;PP&quot; , &quot;AP&quot;, &quot;PA&quot;, &quot;LP&quot;, &quot;PL&quot;, &quot;AL&quot;, &quot;LA&quot;, &quot;LL&quot;
只有&quot;AA&quot;不会被视为可奖励，因为缺勤次数超过一次。</pre>

<p><strong>注意：n </strong>的值不会超过100000。</p>
**/


object Solution {
    def checkRecord(n: Int): Int = {
        
    }
}