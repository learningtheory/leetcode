"""
<p>We are given a list of (axis-aligned)&nbsp;<code>rectangles</code>.&nbsp; Each&nbsp;<code>rectangle[i] = [x1, y1, x2, y2]&nbsp;</code>, where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the <code>i</code>th rectangle.</p>

<p>Find the total area covered by all <code>rectangles</code> in the plane.&nbsp; Since the answer&nbsp;may be too large, <strong>return it modulo 10^9 + 7</strong>.</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png" style="width: 480px; height: 360px;" /></p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[0,0,2,2],[1,0,2,3],[1,0,3,1]]
<strong>Output: </strong>6
<strong>Explanation: </strong>As illustrated in the picture.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[[0,0,1000000000,1000000000]]
<strong>Output: </strong>49
<strong>Explanation: </strong>The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= rectangles.length &lt;= 200</code></li>
	<li><code><font face="monospace">rectanges[i].length = 4</font></code></li>
	<li><code>0 &lt;= rectangles[i][j] &lt;= 10^9</code></li>
	<li>The total area covered by all rectangles will never exceed&nbsp;<code>2^63 - 1</code>&nbsp;and thus will fit in a 64-bit signed integer.</li>
</ul><p>我们给出了一个（轴对齐的）矩形列表&nbsp;<code>rectangles</code>&nbsp;。 对于&nbsp;<code>rectangle[i] = [x1, y1, x2, y2]</code>，其中（x1，y1）是矩形&nbsp;<code>i</code>&nbsp;左下角的坐标，（x2，y2）是该矩形右上角的坐标。</p>

<p>找出平面中所有矩形叠加覆盖后的总面积。 由于答案可能太大，<strong>请返回它对 10 ^ 9 + 7 取模的结果</strong>。</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png" style="height: 360px; width: 480px;"></p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[[0,0,2,2],[1,0,2,3],[1,0,3,1]]
<strong>输出：</strong>6
<strong>解释：</strong>如图所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[[0,0,1000000000,1000000000]]
<strong>输出：</strong>49
<strong>解释：</strong>答案是 10^18 对 (10^9 + 7) 取模的结果， 即 (10^9)^2 &rarr; (-7)^2 = 49 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rectangles.length &lt;= 200</code></li>
	<li><code>rectanges[i].length = 4</code></li>
	<li><code>0 &lt;= rectangles[i][j] &lt;= 10^9</code></li>
	<li>矩形叠加覆盖后的总面积不会超越&nbsp;<code>2^63 - 1</code>&nbsp;，这意味着可以用一个&nbsp;64 位有符号整数来保存面积结果。</li>
</ul>
<p>我们给出了一个（轴对齐的）矩形列表&nbsp;<code>rectangles</code>&nbsp;。 对于&nbsp;<code>rectangle[i] = [x1, y1, x2, y2]</code>，其中（x1，y1）是矩形&nbsp;<code>i</code>&nbsp;左下角的坐标，（x2，y2）是该矩形右上角的坐标。</p>

<p>找出平面中所有矩形叠加覆盖后的总面积。 由于答案可能太大，<strong>请返回它对 10 ^ 9 + 7 取模的结果</strong>。</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/06/rectangle_area_ii_pic.png" style="height: 360px; width: 480px;"></p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[[0,0,2,2],[1,0,2,3],[1,0,3,1]]
<strong>输出：</strong>6
<strong>解释：</strong>如图所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[[0,0,1000000000,1000000000]]
<strong>输出：</strong>49
<strong>解释：</strong>答案是 10^18 对 (10^9 + 7) 取模的结果， 即 (10^9)^2 &rarr; (-7)^2 = 49 。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rectangles.length &lt;= 200</code></li>
	<li><code>rectanges[i].length = 4</code></li>
	<li><code>0 &lt;= rectangles[i][j] &lt;= 10^9</code></li>
	<li>矩形叠加覆盖后的总面积不会超越&nbsp;<code>2^63 - 1</code>&nbsp;，这意味着可以用一个&nbsp;64 位有符号整数来保存面积结果。</li>
</ul>
"""


class Solution:
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        