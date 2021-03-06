/*
<p>In a row of <code>seats</code>, <code>1</code> represents a person sitting in that seat, and <code>0</code> represents that the seat is empty.&nbsp;</p>

<p>There is at least one empty seat, and at least one person sitting.</p>

<p>Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.&nbsp;</p>

<p>Return that maximum distance to closest person.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,0,0,0,1,0,1]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,0,0,0]</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation: </strong>
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= seats.length &lt;= 20000</code></li>
	<li><code>seats</code>&nbsp;contains only 0s or 1s, at least one <code>0</code>, and at least one <code>1</code>.</li>
</ol>
</div>
</div><p>在一排座位（&nbsp;<code>seats</code>）中，<code>1</code>&nbsp;代表有人坐在座位上，<code>0</code>&nbsp;代表座位上是空的。</p>

<p>至少有一个空座位，且至少有一人坐在座位上。</p>

<p>亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。</p>

<p>返回他到离他最近的人的最大距离。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1,0,0,0,1,0,1]
<strong>输出：</strong>2
<strong>解释：
</strong>如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[1,0,0,0]
<strong>输出：</strong>3
<strong>解释： </strong>
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 <span style="">3 </span>。
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= seats.length &lt;= 20000</code></li>
	<li><code>seats</code>&nbsp;中只含有 0 和 1，至少有一个 <code>0</code>，且至少有一个 <code>1</code>。</li>
</ol>
<p>在一排座位（&nbsp;<code>seats</code>）中，<code>1</code>&nbsp;代表有人坐在座位上，<code>0</code>&nbsp;代表座位上是空的。</p>

<p>至少有一个空座位，且至少有一人坐在座位上。</p>

<p>亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。</p>

<p>返回他到离他最近的人的最大距离。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1,0,0,0,1,0,1]
<strong>输出：</strong>2
<strong>解释：
</strong>如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[1,0,0,0]
<strong>输出：</strong>3
<strong>解释： </strong>
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 <span style="">3 </span>。
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= seats.length &lt;= 20000</code></li>
	<li><code>seats</code>&nbsp;中只含有 0 和 1，至少有一个 <code>0</code>，且至少有一个 <code>1</code>。</li>
</ol>
*/


func maxDistToClosest(seats []int) int {
    
}