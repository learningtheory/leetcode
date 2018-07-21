"""
<p>
In a N x N <code>grid</code> representing a field of cherries, each cell is one of three possible integers.
</p><p>
<li>0 means the cell is empty, so you can pass through;</li>
<li>1 means the cell contains a cherry, that you can pick up and pass through;</li>
<li>-1 means the cell contains a thorn that blocks your way.</li>
</p><p>
Your task is to collect maximum number of cherries possible by following the rules below:
</p><p>
<li>Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);</li>
<li>After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;</li>
<li>When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);</li>
<li>If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.</li>
</p><p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
<b>Output:</b> 5
<b>Explanation:</b> 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
</pre>
</p>

<p><b>Note:</b>
<li><code>grid</code> is an <code>N</code> by <code>N</code> 2D array, with <code>1 <= N <= 50</code>.</li>
<li>Each <code>grid[i][j]</code> is an integer in the set <code>{-1, 0, 1}</code>.</li>
<li>It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.<li>
</p><p>一个N x N的网格<code>(grid)</code>&nbsp;代表了一块樱桃地，每个格子由以下三种数字的一种来表示：</p>

<ul>
	<li>0 表示这个格子是空的，所以你可以穿过它。</li>
	<li>1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。</li>
	<li>-1 表示这个格子里有荆棘，挡着你的路。</li>
</ul>

<p>你的任务是在遵守下列规则的情况下，尽可能的摘到最多樱桃：</p>

<ul>
	<li>从位置&nbsp;(0, 0) 出发，最后到达 (N-1, N-1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为0或者1的格子）；</li>
	<li>当到达 (N-1, N-1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；</li>
	<li>当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为0）；</li>
	<li>如果在 (0, 0) 和 (N-1, N-1) 之间不存在一条可经过的路径，则没有任何一个樱桃能被摘到。</li>
</ul>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
<strong>输出:</strong> 5
<strong>解释：</strong> 
玩家从（0,0）点出发，经过了向下走，向下走，向右走，向右走，到达了点(2, 2)。
在这趟单程中，总共摘到了4颗樱桃，矩阵变成了[[0,1,-1],[0,0,-1],[0,0,0]]。
接着，这名玩家向左走，向上走，向上走，向左走，返回了起始点，又摘到了1颗樱桃。
在旅程中，总共摘到了5颗樱桃，这是可以摘到的最大值了。
</pre>

<p><strong>说明:</strong></p>

<ul>
	<li><code>grid</code> 是一个&nbsp;<code>N</code> * <code>N</code> 的二维数组，N的取值范围是<code>1 &lt;= N &lt;= 50</code>。</li>
	<li>每一个&nbsp;<code>grid[i][j]</code> 都是集合&nbsp;<code>{-1, 0, 1}</code>其中的一个数。</li>
	<li>可以保证起点&nbsp;<code>grid[0][0]</code>&nbsp;和终点&nbsp;<code>grid[N-1][N-1]</code>&nbsp;的值都不会是 -1。</li>
</ul>
<p>一个N x N的网格<code>(grid)</code>&nbsp;代表了一块樱桃地，每个格子由以下三种数字的一种来表示：</p>

<ul>
	<li>0 表示这个格子是空的，所以你可以穿过它。</li>
	<li>1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。</li>
	<li>-1 表示这个格子里有荆棘，挡着你的路。</li>
</ul>

<p>你的任务是在遵守下列规则的情况下，尽可能的摘到最多樱桃：</p>

<ul>
	<li>从位置&nbsp;(0, 0) 出发，最后到达 (N-1, N-1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为0或者1的格子）；</li>
	<li>当到达 (N-1, N-1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；</li>
	<li>当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为0）；</li>
	<li>如果在 (0, 0) 和 (N-1, N-1) 之间不存在一条可经过的路径，则没有任何一个樱桃能被摘到。</li>
</ul>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
<strong>输出:</strong> 5
<strong>解释：</strong> 
玩家从（0,0）点出发，经过了向下走，向下走，向右走，向右走，到达了点(2, 2)。
在这趟单程中，总共摘到了4颗樱桃，矩阵变成了[[0,1,-1],[0,0,-1],[0,0,0]]。
接着，这名玩家向左走，向上走，向上走，向左走，返回了起始点，又摘到了1颗樱桃。
在旅程中，总共摘到了5颗樱桃，这是可以摘到的最大值了。
</pre>

<p><strong>说明:</strong></p>

<ul>
	<li><code>grid</code> 是一个&nbsp;<code>N</code> * <code>N</code> 的二维数组，N的取值范围是<code>1 &lt;= N &lt;= 50</code>。</li>
	<li>每一个&nbsp;<code>grid[i][j]</code> 都是集合&nbsp;<code>{-1, 0, 1}</code>其中的一个数。</li>
	<li>可以保证起点&nbsp;<code>grid[0][0]</code>&nbsp;和终点&nbsp;<code>grid[N-1][N-1]</code>&nbsp;的值都不会是 -1。</li>
</ul>
"""


class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        