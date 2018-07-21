/**
<p>A car travels from a starting position to a destination which is <code>target</code> miles east of the starting position.</p>

<p>Along the way, there are gas stations.&nbsp; Each <code>station[i]</code>&nbsp;represents a gas station that is <code>station[i][0]</code> miles east of the starting position, and has <code>station[i][1]</code> liters of gas.</p>

<p>The car starts with an infinite tank of gas, which initially has&nbsp;<code>startFuel</code>&nbsp;liters of fuel in it.&nbsp; It uses 1 liter of gas per 1 mile that it drives.</p>

<p>When the car&nbsp;reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.</p>

<p>What is the least number of refueling stops the car must make in order to reach its destination?&nbsp; If it cannot reach the destination, return <code>-1</code>.</p>

<p>Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.&nbsp; If the car reaches the destination with 0 fuel left, it is still considered to have arrived.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>target = <span id="example-input-1-1">1</span>, startFuel = <span id="example-input-1-2">1</span>, stations = <span id="example-input-1-3">[]</span>
<strong>Output: </strong><span id="example-output-1">0</span>
<strong>Explanation: </strong>We can reach the target without refueling.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>target = <span id="example-input-2-1">100</span>, startFuel = <span id="example-input-2-2">1</span>, stations = <span id="example-input-2-3">[[10,100]]</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
<strong>Explanation: </strong>We can&#39;t reach the target (or even the first gas station).
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>target = <span id="example-input-3-1">100</span>, startFuel = <span id="example-input-3-2">10</span>, stations = <span id="example-input-3-3">[[10,60],[20,30],[30,30],[60,40]]</span>
<strong>Output: </strong><span id="example-output-3">2</span>
<strong>Explanation: </strong>
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= target, startFuel, stations[i][1] &lt;= 10^9</code></li>
	<li><code>0 &lt;= stations.length &lt;= 500</code></li>
	<li><code>0 &lt; stations[0][0] &lt; stations[1][0] &lt; ... &lt; stations[stations.length-1][0] &lt; target</code></li>
</ol>
</div>
</div>
</div>
<p>汽车从起点出发驶向目的地，该目的地位于出发位置东面 <code>target</code>&nbsp;英里处。</p>

<p>沿途有加油站，每个&nbsp;<code>station[i]</code>&nbsp;代表一个加油站，它位于出发位置东面&nbsp;<code>station[i][0]</code>&nbsp;英里处，并且有&nbsp;<code>station[i][1]</code>&nbsp;升汽油。</p>

<p>假设汽车油箱的容量是无限的，其中最初有&nbsp;<code>startFuel</code>&nbsp;升燃料。它每行驶 1 英里就会用掉 1 升汽油。</p>

<p>当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。</p>

<p>为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 <code>-1</code> 。</p>

<p>注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>target = 1, startFuel = 1, stations = []
<strong>输出：</strong>0
<strong>解释：</strong>我们可以在不加油的情况下到达目的地。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>target = 100, startFuel = 1, stations = [[10,100]]
<strong>输出：</strong>-1
<strong>解释：</strong>我们无法抵达目的地，甚至无法到达第一个加油站。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
<strong>输出：</strong>2
<strong>解释：</strong>
我们出发时有 10 升燃料。
我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
我们沿途在1两个加油站停靠，所以返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= target, startFuel, stations[i][1] &lt;= 10^9</code></li>
	<li><code>0 &lt;= stations.length &lt;= 500</code></li>
	<li><code>0 &lt; stations[0][0] &lt; stations[1][0] &lt; ... &lt; stations[stations.length-1][0] &lt; target</code></li>
</ol>
<p>汽车从起点出发驶向目的地，该目的地位于出发位置东面 <code>target</code>&nbsp;英里处。</p>

<p>沿途有加油站，每个&nbsp;<code>station[i]</code>&nbsp;代表一个加油站，它位于出发位置东面&nbsp;<code>station[i][0]</code>&nbsp;英里处，并且有&nbsp;<code>station[i][1]</code>&nbsp;升汽油。</p>

<p>假设汽车油箱的容量是无限的，其中最初有&nbsp;<code>startFuel</code>&nbsp;升燃料。它每行驶 1 英里就会用掉 1 升汽油。</p>

<p>当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。</p>

<p>为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 <code>-1</code> 。</p>

<p>注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>target = 1, startFuel = 1, stations = []
<strong>输出：</strong>0
<strong>解释：</strong>我们可以在不加油的情况下到达目的地。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>target = 100, startFuel = 1, stations = [[10,100]]
<strong>输出：</strong>-1
<strong>解释：</strong>我们无法抵达目的地，甚至无法到达第一个加油站。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
<strong>输出：</strong>2
<strong>解释：</strong>
我们出发时有 10 升燃料。
我们开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，我们从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后我们开车抵达目的地。
我们沿途在1两个加油站停靠，所以返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= target, startFuel, stations[i][1] &lt;= 10^9</code></li>
	<li><code>0 &lt;= stations.length &lt;= 500</code></li>
	<li><code>0 &lt; stations[0][0] &lt; stations[1][0] &lt; ... &lt; stations[stations.length-1][0] &lt; target</code></li>
</ol>
**/


class Solution {
    fun minRefuelStops(target: Int, startFuel: Int, stations: Array<IntArray>): Int {
        
    }
}