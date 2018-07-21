/**
<p>There is an <b>m</b> by <b>n</b> grid with a ball. Given the start coordinate <b>(i,j)</b> of the ball, you can move the ball to <b>adjacent</b> cell or cross the grid boundary in four directions (up, down, left, right). However, you can <b>at most</b> move <b>N</b> times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 10<sup>9</sup> + 7.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>m = 2, n = 2, N = 2, i = 0, j = 0
<b>Output:</b> 6
<b>Explanation:</b>
<img src="/static/images/problemset/out_of_boundary_paths_1.png" width = "40%" />
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>m = 1, n = 3, N = 3, i = 0, j = 1
<b>Output:</b> 12
<b>Explanation:</b>
<img src="/static/images/problemset/out_of_boundary_paths_2.png" width = "37%" />
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>Once you move the ball out of boundary, you cannot move it back.</li>
<li>The length and height of the grid is in range [1,50].</li>
<li>N is in range [0,50].</li>
</ol>
</p><p>给定一个 <strong>m &times; n </strong>的网格和一个球。球的起始坐标为&nbsp;<strong>(i,j)</strong>&nbsp;，你可以将球移到<strong>相邻</strong>的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，你<strong>最多</strong>可以移动&nbsp;<strong>N&nbsp;</strong>次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 10<sup>9</sup>&nbsp;+ 7 的值。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>m = 2, n = 2, N = 2, i = 0, j = 0
<strong>输出:</strong> 6
<strong>解释:</strong>
<img src="/static/images/problemset/out_of_boundary_paths_1.png" style="width:40%" />
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>m = 1, n = 3, N = 3, i = 0, j = 1
<strong>输出:</strong> 12
<strong>解释:</strong>
<img src="/static/images/problemset/out_of_boundary_paths_2.png" style="width:37%" />
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>球一旦出界，就不能再被移动回网格内。</li>
	<li>网格的长度和高度在 [1,50] 的范围内。</li>
	<li>N 在 [0,50] 的范围内。</li>
</ol>
<p>给定一个 <strong>m &times; n </strong>的网格和一个球。球的起始坐标为&nbsp;<strong>(i,j)</strong>&nbsp;，你可以将球移到<strong>相邻</strong>的单元格内，或者往上、下、左、右四个方向上移动使球穿过网格边界。但是，你<strong>最多</strong>可以移动&nbsp;<strong>N&nbsp;</strong>次。找出可以将球移出边界的路径数量。答案可能非常大，返回 结果 mod 10<sup>9</sup>&nbsp;+ 7 的值。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>m = 2, n = 2, N = 2, i = 0, j = 0
<strong>输出:</strong> 6
<strong>解释:</strong>
<img src="/static/images/problemset/out_of_boundary_paths_1.png" style="width:40%" />
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>m = 1, n = 3, N = 3, i = 0, j = 1
<strong>输出:</strong> 12
<strong>解释:</strong>
<img src="/static/images/problemset/out_of_boundary_paths_2.png" style="width:37%" />
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>球一旦出界，就不能再被移动回网格内。</li>
	<li>网格的长度和高度在 [1,50] 的范围内。</li>
	<li>N 在 [0,50] 的范围内。</li>
</ol>
**/


class Solution {
    public int findPaths(int m, int n, int N, int i, int j) {
        
    }
}