"""
<p>You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The five points are show in the figure below. The red triangle is the largest.
</pre>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png" style="height:328px; width:400px" /></p>

<p><strong>Notes: </strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 50</code>.</li>
	<li>No points will be duplicated.</li>
	<li>&nbsp;<code>-50 &lt;= points[i][j] &lt;= 50</code>.</li>
	<li>Answers within&nbsp;<code>10^-6</code>&nbsp;of the true value will be accepted as correct.</li>
</ul>

<p>&nbsp;</p><p>给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
<strong>输出:</strong> 2
<strong>解释:</strong> 
这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
</pre>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png" style="height:328px; width:400px" /></p>

<p><strong>注意: </strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 50</code>.</li>
	<li>不存在重复的点。</li>
	<li>&nbsp;<code>-50 &lt;= points[i][j] &lt;= 50</code>.</li>
	<li>结果误差值在&nbsp;<code>10^-6</code>&nbsp;以内都认为是正确答案。</li>
</ul>
<p>给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
<strong>输出:</strong> 2
<strong>解释:</strong> 
这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
</pre>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png" style="height:328px; width:400px" /></p>

<p><strong>注意: </strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 50</code>.</li>
	<li>不存在重复的点。</li>
	<li>&nbsp;<code>-50 &lt;= points[i][j] &lt;= 50</code>.</li>
	<li>结果误差值在&nbsp;<code>10^-6</code>&nbsp;以内都认为是正确答案。</li>
</ul>
"""


class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        