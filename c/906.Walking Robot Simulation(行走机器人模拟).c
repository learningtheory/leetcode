/*
<p>A robot on an infinite grid starts at point (0, 0) and faces north.&nbsp; The robot can receive one of three possible types of commands:</p>

<ul>
	<li><code>-2</code>: turn left 90 degrees</li>
	<li><code>-1</code>: turn right 90 degrees</li>
	<li><code>1 &lt;= x &lt;= 9</code>: move forward <code>x</code> units</li>
</ul>

<p>Some of the grid squares are obstacles.&nbsp;</p>

<p>The <code>i</code>-th obstacle is at grid point <code>(obstacles[i][0], obstacles[i][1])</code></p>

<p>If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)</p>

<p>Return the <strong>square</strong> of the maximum Euclidean distance that the robot will be from the origin.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>commands = <span id="example-input-1-1">[4,-1,3]</span>, obstacles = <span id="example-input-1-2">[]</span>
<strong>Output: </strong><span id="example-output-1">25</span>
<span>Explanation: </span>robot will go to (3, 4)
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>commands = <span id="example-input-2-1">[4,-1,4,-2,4]</span>, obstacles = <span id="example-input-2-2">[[2,4]]</span>
<strong>Output: </strong><span id="example-output-2">65</span>
<strong>Explanation</strong>: robot will be stuck at (1, 4) before turning left and going to (1, 8)
</pre>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= commands.length &lt;= 10000</code></li>
	<li><code>0 &lt;= obstacles.length &lt;= 10000</code></li>
	<li><code>-30000 &lt;= obstacle[i][0] &lt;= 30000</code></li>
	<li><code>-30000 &lt;= obstacle[i][1] &lt;= 30000</code></li>
	<li>The answer is guaranteed to be less than <code>2 ^ 31</code>.</li>
</ol>
<p>无限网格上的机器人从点&nbsp;(0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：</p>

<ul>
	<li><code>-2</code>：向左转&nbsp;90 度</li>
	<li><code>-1</code>：向右转 90 度</li>
	<li><code>1 &lt;= x &lt;= 9</code>：向前移动&nbsp;<code>x</code>&nbsp;个单位长度</li>
</ul>

<p>有一些网格方块被视作障碍物。&nbsp;</p>

<p>第 <code>i</code>&nbsp;个障碍物位于网格点 &nbsp;<code>(obstacles[i][0], obstacles[i][1])</code></p>

<p>如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。</p>

<p>返回从原点到机器人的最大欧式距离的<strong>平方</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入: </strong>commands = [4,-1,3], obstacles = []
<strong>输出: </strong>25
<strong>解释:</strong> 机器人将会到达 (3, 4)
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre><strong>输入: </strong>commands = [4,-1,4,-2,4], obstacles = [[2,4]]
<strong>输出: </strong>65
<strong>解释</strong>: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= commands.length &lt;= 10000</code></li>
	<li><code>0 &lt;= obstacles.length &lt;= 10000</code></li>
	<li><code>-30000 &lt;= obstacle[i][0] &lt;= 30000</code></li>
	<li><code>-30000 &lt;= obstacle[i][1] &lt;= 30000</code></li>
	<li>答案保证小于&nbsp;<code>2 ^ 31</code></li>
</ol>
<p>无限网格上的机器人从点&nbsp;(0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：</p>

<ul>
	<li><code>-2</code>：向左转&nbsp;90 度</li>
	<li><code>-1</code>：向右转 90 度</li>
	<li><code>1 &lt;= x &lt;= 9</code>：向前移动&nbsp;<code>x</code>&nbsp;个单位长度</li>
</ul>

<p>有一些网格方块被视作障碍物。&nbsp;</p>

<p>第 <code>i</code>&nbsp;个障碍物位于网格点 &nbsp;<code>(obstacles[i][0], obstacles[i][1])</code></p>

<p>如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。</p>

<p>返回从原点到机器人的最大欧式距离的<strong>平方</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入: </strong>commands = [4,-1,3], obstacles = []
<strong>输出: </strong>25
<strong>解释:</strong> 机器人将会到达 (3, 4)
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre><strong>输入: </strong>commands = [4,-1,4,-2,4], obstacles = [[2,4]]
<strong>输出: </strong>65
<strong>解释</strong>: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= commands.length &lt;= 10000</code></li>
	<li><code>0 &lt;= obstacles.length &lt;= 10000</code></li>
	<li><code>-30000 &lt;= obstacle[i][0] &lt;= 30000</code></li>
	<li><code>-30000 &lt;= obstacle[i][1] &lt;= 30000</code></li>
	<li>答案保证小于&nbsp;<code>2 ^ 31</code></li>
</ol>
*/


int robotSim(int* commands, int commandsSize, int** obstacles, int obstaclesRowSize, int *obstaclesColSizes) {
    
}