"""
<p>
Given scores of <b>N</b> athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [5, 4, 3, 2, 1]
<b>Output:</b> ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
<b>Explanation:</b> The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". <br/>For the left two athletes, you just need to output their relative ranks according to their scores.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>N is a positive integer and won't exceed 10,000.</li>
<li>All the scores of athletes are guaranteed to be unique.</li>
</ol>
</p>
<p>给出&nbsp;<strong>N</strong> 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 &ldquo;金牌&rdquo;，&ldquo;银牌&rdquo; 和&ldquo; 铜牌&rdquo;（&quot;Gold Medal&quot;, &quot;Silver Medal&quot;, &quot;Bronze Medal&quot;）。</p>

<p>(注：分数越高的选手，排名越靠前。)</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [5, 4, 3, 2, 1]
<strong>输出:</strong> [&quot;Gold Medal&quot;, &quot;Silver Medal&quot;, &quot;Bronze Medal&quot;, &quot;4&quot;, &quot;5&quot;]
<strong>解释:</strong> 前三名运动员的成绩为前三高的，因此将会分别被授予 &ldquo;金牌&rdquo;，&ldquo;银牌&rdquo;和&ldquo;铜牌&rdquo; (&quot;Gold Medal&quot;, &quot;Silver Medal&quot; and &quot;Bronze Medal&quot;).
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。</pre>

<p><strong>提示:</strong></p>

<ol>
	<li>N 是一个正整数并且不会超过&nbsp;10000。</li>
	<li>所有运动员的成绩都不相同。</li>
</ol>
<p>给出&nbsp;<strong>N</strong> 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 &ldquo;金牌&rdquo;，&ldquo;银牌&rdquo; 和&ldquo; 铜牌&rdquo;（&quot;Gold Medal&quot;, &quot;Silver Medal&quot;, &quot;Bronze Medal&quot;）。</p>

<p>(注：分数越高的选手，排名越靠前。)</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [5, 4, 3, 2, 1]
<strong>输出:</strong> [&quot;Gold Medal&quot;, &quot;Silver Medal&quot;, &quot;Bronze Medal&quot;, &quot;4&quot;, &quot;5&quot;]
<strong>解释:</strong> 前三名运动员的成绩为前三高的，因此将会分别被授予 &ldquo;金牌&rdquo;，&ldquo;银牌&rdquo;和&ldquo;铜牌&rdquo; (&quot;Gold Medal&quot;, &quot;Silver Medal&quot; and &quot;Bronze Medal&quot;).
余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。</pre>

<p><strong>提示:</strong></p>

<ol>
	<li>N 是一个正整数并且不会超过&nbsp;10000。</li>
	<li>所有运动员的成绩都不相同。</li>
</ol>
"""


class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        