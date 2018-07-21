/*
<p>There are <code>n</code> cities connected by&nbsp;<code>m</code> flights. Each fight starts from city&nbsp;<code>u </code>and arrives at&nbsp;<code>v</code> with a price <code>w</code>.</p>

<p>Now given all the cities and fights, together with starting city <code>src</code> and the destination&nbsp;<code>dst</code>, your task is to find the cheapest price from <code>src</code> to <code>dst</code> with up to <code>k</code> stops. If there is no such route, output <code>-1</code>.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
<strong>Output:</strong> 200
<strong>Explanation:</strong> 
The graph looks like this:
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height:180px; width:246px" />

The cheapest price from city <code>0</code> to city <code>2</code> with at most 1 stop costs 200, as marked red in the picture.</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
<strong>Output:</strong> 500
<strong>Explanation:</strong> 
The graph looks like this:
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height:180px; width:246px" />

The cheapest price from city <code>0</code> to city <code>2</code> with at most 0 stop costs 500, as marked blue in the picture.</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>The number of&nbsp;nodes&nbsp;<code>n</code> will be&nbsp;in range <code>[1, 100]</code>, with nodes labeled from <code>0</code> to <code>n</code><code> - 1</code>.</li>
	<li>The&nbsp;size of <code>flights</code> will be&nbsp;in range <code>[0, n * (n - 1) / 2]</code>.</li>
	<li>The format of each flight will be <code>(src, </code><code>dst</code><code>, price)</code>.</li>
	<li>The price of each flight will be in the range <code>[1, 10000]</code>.</li>
	<li><code>k</code> is in the range of <code>[0, n - 1]</code>.</li>
	<li>There&nbsp;will&nbsp;not&nbsp;be&nbsp;any&nbsp;duplicated&nbsp;flights or&nbsp;self&nbsp;cycles.</li>
</ul><p>有 <code>n</code> 个城市通过 <code>m</code> 个航班连接。每个航班都从城市 <code>u</code> 开始，以价格 <code>w</code> 抵达 <code>v</code>。</p>

<p>现在给定所有的城市和航班，以及出发城市 <code>src</code> 和目的地 <code>dst</code>，你的任务是找到从 <code>src</code> 到 <code>dst</code> 最多经过 <code>k</code>&nbsp;站中转的最便宜的价格。 如果没有这样的路线，则输出 <code>-1</code>。</p>

<pre><strong>示例 1:</strong>
<strong>输入:</strong> 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
<strong>输出:</strong> 200
<strong>解释:</strong> 
城市航班图如下
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height: 180px; width: 246px;">

从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。</pre>

<pre><strong>示例 2:</strong>
<strong>输入:</strong> 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
<strong>输出:</strong> 500
<strong>解释:</strong> 
城市航班图如下
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height: 180px; width: 246px;">

从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n</code> 范围是 <code>[1, 100]</code>，城市标签从 <code>0</code> 到 <code>n</code><code> - 1</code>.</li>
	<li>航班数量范围是 <code>[0, n * (n - 1) / 2]</code>.</li>
	<li>每个航班的格式 <code>(src, </code><code>dst</code><code>, price)</code>.</li>
	<li>每个航班的价格范围是 <code>[1, 10000]</code>.</li>
	<li><code>k</code> 范围是 <code>[0, n - 1]</code>.</li>
	<li>航班没有重复，且不存在环路</li>
</ul>
<p>有 <code>n</code> 个城市通过 <code>m</code> 个航班连接。每个航班都从城市 <code>u</code> 开始，以价格 <code>w</code> 抵达 <code>v</code>。</p>

<p>现在给定所有的城市和航班，以及出发城市 <code>src</code> 和目的地 <code>dst</code>，你的任务是找到从 <code>src</code> 到 <code>dst</code> 最多经过 <code>k</code>&nbsp;站中转的最便宜的价格。 如果没有这样的路线，则输出 <code>-1</code>。</p>

<pre><strong>示例 1:</strong>
<strong>输入:</strong> 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
<strong>输出:</strong> 200
<strong>解释:</strong> 
城市航班图如下
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height: 180px; width: 246px;">

从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。</pre>

<pre><strong>示例 2:</strong>
<strong>输入:</strong> 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
<strong>输出:</strong> 500
<strong>解释:</strong> 
城市航班图如下
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height: 180px; width: 246px;">

从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n</code> 范围是 <code>[1, 100]</code>，城市标签从 <code>0</code> 到 <code>n</code><code> - 1</code>.</li>
	<li>航班数量范围是 <code>[0, n * (n - 1) / 2]</code>.</li>
	<li>每个航班的格式 <code>(src, </code><code>dst</code><code>, price)</code>.</li>
	<li>每个航班的价格范围是 <code>[1, 10000]</code>.</li>
	<li><code>k</code> 范围是 <code>[0, n - 1]</code>.</li>
	<li>航班没有重复，且不存在环路</li>
</ul>
*/


class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        
    }
};