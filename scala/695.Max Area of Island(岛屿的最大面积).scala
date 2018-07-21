/**
<p><p>Given a non-empty 2D array <code>grid</code> of 0's and 1's, an <b>island</b> is a group of <code>1</code>'s (representing land) connected 4-directionally (horizontal or vertical.)  You may assume all four edges of the grid are surrounded by water.</p>
<p>
Find the maximum area of an island in the given 2D array.
(If there is no island, the maximum area is 0.)
</p>
<p><b>Example 1:</b><br />
<pre>
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,0,<b>1</b>,0,0],
 [0,1,0,0,1,1,0,0,<b>1</b>,<b>1</b>,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,0,0,0,<b>1</b>,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
</pre>
Given the above grid, return <code>6</code>.

Note the answer is not 11, because the island must be connected 4-directionally.
</p>

<p><b>Example 2:</b><br />
<pre>[[0,0,0,0,0,0,0,0]]</pre>
Given the above grid, return <code>0</code>.
</p>

<p><b>Note:</b>
The length of each dimension in the given <code>grid</code> does not exceed 50.
</p><p>给定一个包含了一些 0 和 1的非空二维数组&nbsp;<code>grid</code>&nbsp;, 一个&nbsp;<strong>岛屿</strong>&nbsp;是由四个方向 (水平或垂直) 的&nbsp;<code>1</code>&nbsp;(代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。</p>

<p>找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)</p>

<p><strong>示例 1:</strong></p>

<pre>
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,<strong>1</strong>,0,<strong>1</strong>,0,0],
 [0,1,0,0,1,1,0,0,<strong>1</strong>,<strong>1</strong>,<strong>1</strong>,0,0],
 [0,0,0,0,0,0,0,0,0,0,<strong>1</strong>,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
</pre>

<p>对于上面这个给定矩阵应返回&nbsp;<code>6</code>。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的&lsquo;1&rsquo;。</p>

<p><strong>示例 2:</strong></p>

<pre>
[[0,0,0,0,0,0,0,0]]</pre>

<p>对于上面这个给定的矩阵, 返回&nbsp;<code>0</code>。</p>

<p><strong>注意:&nbsp;</strong>给定的矩阵<code>grid</code>&nbsp;的长度和宽度都不超过 50。</p>
<p>给定一个包含了一些 0 和 1的非空二维数组&nbsp;<code>grid</code>&nbsp;, 一个&nbsp;<strong>岛屿</strong>&nbsp;是由四个方向 (水平或垂直) 的&nbsp;<code>1</code>&nbsp;(代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。</p>

<p>找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)</p>

<p><strong>示例 1:</strong></p>

<pre>
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,<strong>1</strong>,0,<strong>1</strong>,0,0],
 [0,1,0,0,1,1,0,0,<strong>1</strong>,<strong>1</strong>,<strong>1</strong>,0,0],
 [0,0,0,0,0,0,0,0,0,0,<strong>1</strong>,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
</pre>

<p>对于上面这个给定矩阵应返回&nbsp;<code>6</code>。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的&lsquo;1&rsquo;。</p>

<p><strong>示例 2:</strong></p>

<pre>
[[0,0,0,0,0,0,0,0]]</pre>

<p>对于上面这个给定的矩阵, 返回&nbsp;<code>0</code>。</p>

<p><strong>注意:&nbsp;</strong>给定的矩阵<code>grid</code>&nbsp;的长度和宽度都不超过 50。</p>
**/


object Solution {
    def maxAreaOfIsland(grid: Array[Array[Int]]): Int = {
        
    }
}