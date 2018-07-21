"""
<p>We partition a row of numbers <code>A</code>&nbsp;into at most <code>K</code> adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?</p>

<p>Note that our partition must use every number in A, and that scores are not necessarily integers.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> 
A = [9,1,2,3,9]
K = 3
<strong>Output:</strong> 20
<strong>Explanation:</strong> 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
</pre>

<p>&nbsp;</p>

<p><strong>Note: </strong></p>

<ul>
	<li><code>1 &lt;= A.length &lt;= 100</code>.</li>
	<li><code>1 &lt;= A[i] &lt;= 10000</code>.</li>
	<li><code>1 &lt;= K &lt;= A.length</code>.</li>
	<li>Answers within <code>10^-6</code> of the correct answer will be accepted as correct.</li>
</ul>
<p>我们将给定的数组&nbsp;<code>A</code>&nbsp;分成&nbsp;<code>K</code>&nbsp;个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。</p>

<p>注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> 
A = [9,1,2,3,9]
K = 3
<strong>输出:</strong> 20
<strong>解释:</strong> 
A 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
我们也可以把 A 分成[9, 1], [2], [3, 9].
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li><code>1 &lt;= A.length &lt;= 100</code>.</li>
	<li><code>1 &lt;= A[i] &lt;= 10000</code>.</li>
	<li><code>1 &lt;= K &lt;= A.length</code>.</li>
	<li>答案误差在&nbsp;<code>10^-6</code>&nbsp;内被视为是正确的。</li>
</ul>
<p>我们将给定的数组&nbsp;<code>A</code>&nbsp;分成&nbsp;<code>K</code>&nbsp;个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。</p>

<p>注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> 
A = [9,1,2,3,9]
K = 3
<strong>输出:</strong> 20
<strong>解释:</strong> 
A 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
我们也可以把 A 分成[9, 1], [2], [3, 9].
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li><code>1 &lt;= A.length &lt;= 100</code>.</li>
	<li><code>1 &lt;= A[i] &lt;= 10000</code>.</li>
	<li><code>1 &lt;= K &lt;= A.length</code>.</li>
	<li>答案误差在&nbsp;<code>10^-6</code>&nbsp;内被视为是正确的。</li>
</ul>
"""


class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        