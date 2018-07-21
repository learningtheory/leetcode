"""
<p>There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the <b>minimum length</b> of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
<b>Output:</b> [[1,1],[2,0],[4,2],[3,3],[2,4]]
<b>Explanation:</b>
<img src="/static/images/problemset/erect_the_fence_1.png" width = "30%" />
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [[1,2],[2,2],[4,2]]
<b>Output:</b> [[1,2],[2,2],[4,2]]
<b>Explanation:</b>
<img src="/static/images/problemset/erect_the_fence_2.png" width = "30%" />
Even you only have trees in a line, you need to use rope to enclose them. 
</pre>
</p>

<p> Note: 
<ol>
<li>All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.</li>
<li>All input integers will range from 0 to 100. </li>
<li>The garden has at least one tree. </li>
<li>All coordinates are distinct. </li>
<li>Input points have <b>NO</b> order. No order required for output.</li>
</ol>
</p><p>在一个二维的花园中，有一些用 (x,y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用<strong>最短</strong>的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
<strong>输出:</strong> [[1,1],[2,0],[4,2],[3,3],[2,4]]
<strong>解释:</strong>
<img src="/static/images/problemset/erect_the_fence_1.png" style="width:30%" />
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [[1,2],[2,2],[4,2]]
<strong>输出:</strong> [[1,2],[2,2],[4,2]]
<strong>解释:</strong>
<img src="/static/images/problemset/erect_the_fence_2.png" style="width:30%" />
即使树都在一条直线上，你也需要先用绳子包围它们。
</pre>

<p>注意:</p>

<ol>
	<li>所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。</li>
	<li>输入的整数在 0 到 100 之间。</li>
	<li>花园至少有一棵树。</li>
	<li>所有树的坐标都是不同的。</li>
	<li>输入的点<strong>没有</strong>顺序。输出顺序也没有要求。</li>
</ol>
<p>在一个二维的花园中，有一些用 (x,y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用<strong>最短</strong>的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
<strong>输出:</strong> [[1,1],[2,0],[4,2],[3,3],[2,4]]
<strong>解释:</strong>
<img src="/static/images/problemset/erect_the_fence_1.png" style="width:30%" />
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [[1,2],[2,2],[4,2]]
<strong>输出:</strong> [[1,2],[2,2],[4,2]]
<strong>解释:</strong>
<img src="/static/images/problemset/erect_the_fence_2.png" style="width:30%" />
即使树都在一条直线上，你也需要先用绳子包围它们。
</pre>

<p>注意:</p>

<ol>
	<li>所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。</li>
	<li>输入的整数在 0 到 100 之间。</li>
	<li>花园至少有一棵树。</li>
	<li>所有树的坐标都是不同的。</li>
	<li>输入的点<strong>没有</strong>顺序。输出顺序也没有要求。</li>
</ol>
"""


class Solution:
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        