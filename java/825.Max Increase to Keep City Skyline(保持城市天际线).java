/**
<p>In a 2 dimensional array <code>grid</code>, each value <code>grid[i][j]</code> represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts&nbsp;can be different for different buildings). Height&nbsp;0 is considered to be a&nbsp;building&nbsp;as well.&nbsp;</p>

<p>At the end, the &quot;skyline&quot; when viewed from all four directions&nbsp;of the grid, i.e.&nbsp;top, bottom, left, and right,&nbsp;must be the same as the&nbsp;skyline of the original grid. A city&#39;s skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See&nbsp;the following example.</p>

<p>What is the maximum total sum that the height of the buildings can be increased?</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
<strong>Output:</strong> 35
<strong>Explanation:</strong> 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

</pre>

<p><strong>Notes: </strong></p>

<ul>
	<li><code>1 &lt; grid.length = grid[0].length &lt;= 50</code>.</li>
	<li>All heights <code>grid[i][j]</code> are in the range <code>[0, 100]</code>.</li>
	<li>All buildings in <code>grid[i][j]</code> occupy the entire grid cell: that is, they are a <code>1 x 1 x grid[i][j]</code> rectangular prism.</li>
</ul>
<p>在二维数组<code>grid</code>中，<code>grid[i][j]</code>代表位于某处的建筑物的高度。 我们被允许增加任何数量（不同建筑物的数量可能不同）的建筑物的高度。 高度 0 也被认为是建筑物。</p>

<p>最后，从新数组的所有四个方向（即顶部，底部，左侧和右侧）观看的&ldquo;天际线&rdquo;必须与原始数组的天际线相同。 城市的天际线是从远处观看时，由所有建筑物形成的矩形的外部轮廓。 请看下面的例子。</p>

<p>建筑物高度可以增加的最大总和是多少？</p>

<pre>
<strong>例子：</strong>
<strong>输入：</strong> grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
<strong>输出：</strong> 35
<strong>解释：</strong> 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

从数组竖直方向（即顶部，底部）看&ldquo;天际线&rdquo;是：[9, 4, 8, 7]
从水平水平方向（即左侧，右侧）看&ldquo;天际线&rdquo;是：[8, 7, 9, 3]

在不影响天际线的情况下对建筑物进行增高后，新数组如下：

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li><code>1 &lt; grid.length = grid[0].length &lt;= 50</code>。</li>
	<li>&nbsp;<code>grid[i][j]</code> 的高度范围是： <code>[0, 100]</code>。</li>
	<li>一座建筑物占据一个<code>grid[i][j]</code>：换言之，它们是 <code>1 x 1 x grid[i][j]</code> 的长方体。</li>
</ul>
<p>在二维数组<code>grid</code>中，<code>grid[i][j]</code>代表位于某处的建筑物的高度。 我们被允许增加任何数量（不同建筑物的数量可能不同）的建筑物的高度。 高度 0 也被认为是建筑物。</p>

<p>最后，从新数组的所有四个方向（即顶部，底部，左侧和右侧）观看的&ldquo;天际线&rdquo;必须与原始数组的天际线相同。 城市的天际线是从远处观看时，由所有建筑物形成的矩形的外部轮廓。 请看下面的例子。</p>

<p>建筑物高度可以增加的最大总和是多少？</p>

<pre>
<strong>例子：</strong>
<strong>输入：</strong> grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
<strong>输出：</strong> 35
<strong>解释：</strong> 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

从数组竖直方向（即顶部，底部）看&ldquo;天际线&rdquo;是：[9, 4, 8, 7]
从水平水平方向（即左侧，右侧）看&ldquo;天际线&rdquo;是：[8, 7, 9, 3]

在不影响天际线的情况下对建筑物进行增高后，新数组如下：

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li><code>1 &lt; grid.length = grid[0].length &lt;= 50</code>。</li>
	<li>&nbsp;<code>grid[i][j]</code> 的高度范围是： <code>[0, 100]</code>。</li>
	<li>一座建筑物占据一个<code>grid[i][j]</code>：换言之，它们是 <code>1 x 1 x grid[i][j]</code> 的长方体。</li>
</ul>
**/


class Solution {
    public int maxIncreaseKeepingSkyline(int[][] grid) {
        
    }
}