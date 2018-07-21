/*
<p>We have a grid of 1s and 0s; the 1s in a cell represent bricks.&nbsp; A brick will not drop if and only if it is directly connected to the top of the grid, or at least one of its (4-way) adjacent bricks will not drop.</p>

<p>We will do some erasures&nbsp;sequentially. Each time we want to do the erasure at the location (i, j), the brick (if it exists) on that location will disappear, and then some other bricks may&nbsp;drop because of that&nbsp;erasure.</p>

<p>Return an array representing the number of bricks that will drop after each erasure in sequence.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> 
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
<strong>Output:</strong> [2]
<strong>Explanation: </strong>
If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> 
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
<strong>Output:</strong> [0,0]
<strong>Explanation: </strong>
When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move. So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The number of rows and columns in the grid will be in the range&nbsp;[1, 200].</li>
	<li>The number of erasures will not exceed the area of the grid.</li>
	<li>It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.</li>
	<li>An erasure may refer to a location with no brick - if it does, no bricks drop.</li>
</ul>
<p>我们有一组包含1和0的网格；其中1表示砖块。&nbsp;当且仅当一块砖直接连接到网格的顶部，或者它至少连接着(4个方向)相邻的砖块之一时，它才不会落下。</p>

<p>我们会依次消除一些砖块。每当我们消除&nbsp;(i, j) 位置时， 对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这个消除而落下。</p>

<p>返回一个数组表示每次消除操作对应落下的砖块数目。</p>

<pre>
<strong>示例 1：</strong>
<strong>输入：</strong>
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
<strong>输出:</strong> [2]
<strong>解释: </strong>
如果我们消除(1, 0)位置的砖块, 在(1, 1) 和(1, 2) 的砖块会落下。所以我们应该返回2。</pre>

<pre>
<strong>示例 2：</strong>
<strong>输入：</strong>
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
<strong>输出：</strong>[0,0]
<strong>解释：</strong>
当我们消除(1, 0)的砖块时，(1, 1)的砖块已经由于上一步消除而消失了。所以每次消除操作不会造成砖块落下。注意(1, 0)砖块不会记作落下的砖块。</pre>

<p><strong>注意:</strong></p>

<ul>
	<li>网格的行数和列数的范围是[1, 200]。</li>
	<li>消除的数字不会超过网格的区域。</li>
	<li>可以保证每次的消除都不相同，并且位于网格的内部。</li>
	<li>一个消除的位置可能没有砖块，如果这样的话，就不会有砖块落下。</li>
</ul>
<p>我们有一组包含1和0的网格；其中1表示砖块。&nbsp;当且仅当一块砖直接连接到网格的顶部，或者它至少连接着(4个方向)相邻的砖块之一时，它才不会落下。</p>

<p>我们会依次消除一些砖块。每当我们消除&nbsp;(i, j) 位置时， 对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这个消除而落下。</p>

<p>返回一个数组表示每次消除操作对应落下的砖块数目。</p>

<pre>
<strong>示例 1：</strong>
<strong>输入：</strong>
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
<strong>输出:</strong> [2]
<strong>解释: </strong>
如果我们消除(1, 0)位置的砖块, 在(1, 1) 和(1, 2) 的砖块会落下。所以我们应该返回2。</pre>

<pre>
<strong>示例 2：</strong>
<strong>输入：</strong>
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
<strong>输出：</strong>[0,0]
<strong>解释：</strong>
当我们消除(1, 0)的砖块时，(1, 1)的砖块已经由于上一步消除而消失了。所以每次消除操作不会造成砖块落下。注意(1, 0)砖块不会记作落下的砖块。</pre>

<p><strong>注意:</strong></p>

<ul>
	<li>网格的行数和列数的范围是[1, 200]。</li>
	<li>消除的数字不会超过网格的区域。</li>
	<li>可以保证每次的消除都不相同，并且位于网格的内部。</li>
	<li>一个消除的位置可能没有砖块，如果这样的话，就不会有砖块落下。</li>
</ul>
*/


class Solution {
public:
    vector<int> hitBricks(vector<vector<int>>& grid, vector<vector<int>>& hits) {
        
    }
};