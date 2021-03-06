"""
<p>
Your task is to calculate <i>a</i><sup><i>b</i></sup> mod 1337 where <i>a</i> is a positive integer and <i>b</i> is an extremely large positive integer given in the form of an array.
</p>

<p><b>Example1:</b>
<pre>
a = 2
b = [3]

Result: 8
</pre>
</p>

<p><b>Example2:</b>
<pre>
a = 2
b = [1,0]

Result: 1024
</pre>
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/stomach_ache">@Stomach_ache</a> for adding this problem and creating all test cases.</p><p>你的任务是计算&nbsp;<em>a</em><sup><em>b</em></sup>&nbsp;对&nbsp;1337 取模，<em>a</em> 是一个正整数，<em>b</em> 是一个非常大的正整数且会以数组形式给出。</p>

<p><strong>示例 1:</strong></p>

<pre>
a = 2
b = [3]

结果: 8
</pre>

<p><strong>示例 2:</strong></p>

<pre>
a = 2
b = [1,0]

结果: 1024
</pre>

<p><strong>致谢：</strong></p>

<p>特别感谢&nbsp;<a href="https://leetcode.com/stomach_ache">@Stomach_ache</a>&nbsp;添加这道题并创建所有测试用例。</p>
<p>你的任务是计算&nbsp;<em>a</em><sup><em>b</em></sup>&nbsp;对&nbsp;1337 取模，<em>a</em> 是一个正整数，<em>b</em> 是一个非常大的正整数且会以数组形式给出。</p>

<p><strong>示例 1:</strong></p>

<pre>
a = 2
b = [3]

结果: 8
</pre>

<p><strong>示例 2:</strong></p>

<pre>
a = 2
b = [1,0]

结果: 1024
</pre>

<p><strong>致谢：</strong></p>

<p>特别感谢&nbsp;<a href="https://leetcode.com/stomach_ache">@Stomach_ache</a>&nbsp;添加这道题并创建所有测试用例。</p>
"""


class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        