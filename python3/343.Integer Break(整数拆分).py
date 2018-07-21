"""
<p>
Given a positive integer <i>n</i>, break it into the sum of <b>at least</b> two positive integers and maximize the product of those integers. Return the maximum product you can get.
</p>

<p>
For example, given <i>n</i> = 2, return 1 (2 = 1 + 1); given <i>n</i> = 10, return 36 (10 = 3 + 3 + 4).
</p>

<p>
<b>Note</b>: You may assume that <i>n</i> is not less than 2 and not larger than 58.
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/discuss/user/jianchao.li.fighter">@jianchao.li.fighter</a> for adding this problem and creating all test cases.</p><p>给定一个正整数&nbsp;<em>n</em>，将其拆分为<strong>至少</strong>两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。</p>

<p>例如，给定&nbsp;<em>n</em> = 2，返回1（2 = 1 + 1）；给定 <em>n</em> = 10，返回36（10 = 3 + 3 + 4）。</p>

<p>注意：你可以假设&nbsp;<em>n&nbsp;</em>不小于2且不大于58。</p>

<p><strong>感谢：</strong><br />
特别感谢&nbsp;<a href="https://leetcode.com/discuss/user/jianchao.li.fighter">@jianchao.li.fighter</a>&nbsp;添加此问题并创建所有测试用例。</p>
<p>给定一个正整数&nbsp;<em>n</em>，将其拆分为<strong>至少</strong>两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。</p>

<p>例如，给定&nbsp;<em>n</em> = 2，返回1（2 = 1 + 1）；给定 <em>n</em> = 10，返回36（10 = 3 + 3 + 4）。</p>

<p>注意：你可以假设&nbsp;<em>n&nbsp;</em>不小于2且不大于58。</p>

<p><strong>感谢：</strong><br />
特别感谢&nbsp;<a href="https://leetcode.com/discuss/user/jianchao.li.fighter">@jianchao.li.fighter</a>&nbsp;添加此问题并创建所有测试用例。</p>
"""


class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        