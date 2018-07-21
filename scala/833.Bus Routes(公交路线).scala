/**
<p>We have a list of bus routes. Each <code>routes[i]</code> is a bus route that the i-th bus&nbsp;repeats forever. For example if <code>routes[0] = [1, 5, 7]</code>, this means that the first&nbsp;bus (0-th indexed) travels in the sequence 1-&gt;5-&gt;7-&gt;1-&gt;5-&gt;7-&gt;1-&gt;... forever.</p>

<p>We start at bus stop <code>S</code> (initially not on a bus), and we want to go to bus stop <code>T</code>. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
</pre>

<p><strong>Note: </strong></p>

<ul>
	<li><code>1 &lt;= routes.length &lt;= 500</code>.</li>
	<li><code>1 &lt;= routes[i].length &lt;= 500</code>.</li>
	<li><code>0 &lt;= routes[i][j] &lt; 10 ^ 6</code>.</li>
</ul><p>我们有一系列公交路线。每一条路线 <code>routes[i]</code>&nbsp;上都有一辆公交车在上面循环行驶。例如，有一条路线&nbsp;<code>routes[0] = [1, 5, 7]</code>，表示第一辆 (下标为0) 公交车会一直按照&nbsp;1-&gt;5-&gt;7-&gt;1-&gt;5-&gt;7-&gt;1-&gt;...&nbsp;的车站路线行驶。</p>

<p>假设我们从&nbsp;<code>S</code>&nbsp;车站开始（初始时不在公交车上），要去往&nbsp;<code>T</code>&nbsp;站。 期间仅可乘坐公交车，求出最少乘坐的公交车数量。返回 -1 表示不可能到达终点车站。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
<strong>输出:</strong> 2
<strong>解释:</strong> 
最优策略是先乘坐第一辆公交车到达车站 7, 然后换乘第二辆公交车到车站 6。
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li><code>1 &lt;= routes.length &lt;= 500</code>.</li>
	<li><code>1 &lt;= routes[i].length &lt;= 500</code>.</li>
	<li><code>0 &lt;= routes[i][j] &lt; 10 ^ 6</code>.</li>
</ul>
<p>我们有一系列公交路线。每一条路线 <code>routes[i]</code>&nbsp;上都有一辆公交车在上面循环行驶。例如，有一条路线&nbsp;<code>routes[0] = [1, 5, 7]</code>，表示第一辆 (下标为0) 公交车会一直按照&nbsp;1-&gt;5-&gt;7-&gt;1-&gt;5-&gt;7-&gt;1-&gt;...&nbsp;的车站路线行驶。</p>

<p>假设我们从&nbsp;<code>S</code>&nbsp;车站开始（初始时不在公交车上），要去往&nbsp;<code>T</code>&nbsp;站。 期间仅可乘坐公交车，求出最少乘坐的公交车数量。返回 -1 表示不可能到达终点车站。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
<strong>输出:</strong> 2
<strong>解释:</strong> 
最优策略是先乘坐第一辆公交车到达车站 7, 然后换乘第二辆公交车到车站 6。
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li><code>1 &lt;= routes.length &lt;= 500</code>.</li>
	<li><code>1 &lt;= routes[i].length &lt;= 500</code>.</li>
	<li><code>0 &lt;= routes[i][j] &lt; 10 ^ 6</code>.</li>
</ul>
**/


object Solution {
    def numBusesToDestination(routes: Array[Array[Int]], S: Int, T: Int): Int = {
        
    }
}