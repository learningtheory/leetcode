"""
<p>Given <em>n</em> non-negative integers representing the histogram&#39;s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.</p>

<p><img src="https://leetcode.com/static/images/problemset/histogram.png" /><br />
<small>Above is a histogram where width of each bar is 1, given height = <code>[2,1,5,6,2,3]</code>.</small></p>

<p>&nbsp;</p>

<p><img src="https://leetcode.com/static/images/problemset/histogram_area.png" /><br />
<small>The largest rectangle is shown in the shaded area, which has area = <code>10</code> unit.</small></p>

<p>&nbsp;</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [2,1,5,6,2,3]
<strong>Output:</strong> 10
</pre>
<p>给定 <em>n</em> 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。</p>

<p>求在该柱状图中，能够勾勒出来的矩形的最大面积。</p>

<p><img src="/static/images/problemset/histogram.png"></p>

<p><small>以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为&nbsp;<code>[2,1,5,6,2,3]</code>。</small></p>

<p><img src="/static/images/problemset/histogram_area.png"></p>

<p><small>图中阴影部分为所能勾勒出的最大矩形面积，其面积为&nbsp;<code>10</code>&nbsp;个单位。</small></p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [2,1,5,6,2,3]
<strong>输出:</strong> 10</pre>
<p>给定 <em>n</em> 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。</p>

<p>求在该柱状图中，能够勾勒出来的矩形的最大面积。</p>

<p><img src="/static/images/problemset/histogram.png"></p>

<p><small>以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为&nbsp;<code>[2,1,5,6,2,3]</code>。</small></p>

<p><img src="/static/images/problemset/histogram_area.png"></p>

<p><small>图中阴影部分为所能勾勒出的最大矩形面积，其面积为&nbsp;<code>10</code>&nbsp;个单位。</small></p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [2,1,5,6,2,3]
<strong>输出:</strong> 10</pre>
"""


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        