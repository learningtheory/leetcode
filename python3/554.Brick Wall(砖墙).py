"""
<p>There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the <b>top</b> to the <b>bottom</b> and cross the <b>least</b> bricks. </p>

<p>
The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right. 
</p>

<p>If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks. </p>

<p><b>You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks. </b></p>

<p><b>Example:</b><br />
<pre>
<b>Input:</b> 
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
<b>Output:</b> 2
<b>Explanation:</b> 
<img src="/static/images/problemset/brick_wall.png" width = "30%" />
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The width sum of bricks in different rows are the same and won't exceed INT_MAX.</li>
<li>The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000. </li>
</ol>
</p><p>你的面前有一堵方形的、由多行砖块组成的砖墙。&nbsp;这些砖块高度相同但是宽度不同。你现在要画一条<strong>自顶向下</strong>的、穿过<strong>最少</strong>砖块的垂线。</p>

<p>砖墙由行的列表表示。 每一行都是一个代表从左至右每块砖的宽度的整数列表。</p>

<p>如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。你需要找出怎样画才能使这条线穿过的砖块数量最少，并且返回穿过的砖块数量。</p>

<p><strong>你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。</strong></p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入:</strong> 
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
<strong>输出:</strong> 2
<strong>解释:</strong> 
<img src="/static/images/problemset/brick_wall.png" style="width: 30%;">
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>每一行砖块的宽度之和应该相等，并且不能超过 INT_MAX。</li>
	<li>每一行砖块的数量在&nbsp;[1,10,000] 范围内，&nbsp;墙的高度在&nbsp;[1,10,000] 范围内，&nbsp;总的砖块数量不超过 20,000。</li>
</ol>

<p>&nbsp;</p>
<p>你的面前有一堵方形的、由多行砖块组成的砖墙。&nbsp;这些砖块高度相同但是宽度不同。你现在要画一条<strong>自顶向下</strong>的、穿过<strong>最少</strong>砖块的垂线。</p>

<p>砖墙由行的列表表示。 每一行都是一个代表从左至右每块砖的宽度的整数列表。</p>

<p>如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。你需要找出怎样画才能使这条线穿过的砖块数量最少，并且返回穿过的砖块数量。</p>

<p><strong>你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。</strong></p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入:</strong> 
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
<strong>输出:</strong> 2
<strong>解释:</strong> 
<img src="/static/images/problemset/brick_wall.png" style="width: 30%;">
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>每一行砖块的宽度之和应该相等，并且不能超过 INT_MAX。</li>
	<li>每一行砖块的数量在&nbsp;[1,10,000] 范围内，&nbsp;墙的高度在&nbsp;[1,10,000] 范围内，&nbsp;总的砖块数量不超过 20,000。</li>
</ol>

<p>&nbsp;</p>
"""


class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        