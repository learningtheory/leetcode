"""
<p>An undirected, connected graph of N nodes (labeled&nbsp;<code>0, 1, 2, ..., N-1</code>) is given as <code>graph</code>.</p>

<p><code>graph.length = N</code>, and <code>j != i</code>&nbsp;is in the list&nbsp;<code>graph[i]</code>&nbsp;exactly once, if and only if nodes <code>i</code> and <code>j</code> are connected.</p>

<p>Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[1,2,3],[0],[0],[0]]
<strong>Output: </strong>4
<strong>Explanation</strong>: One possible path is [1,0,2,0,3]</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[[1],[0,2,4],[1,3,4],[2],[1,2]]
<strong>Output: </strong>4
<strong>Explanation</strong>: One possible path is [0,1,4,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= graph.length &lt;= 12</code></li>
	<li><code>0 &lt;= graph[i].length &lt;&nbsp;graph.length</code></li>
</ol><p>给出&nbsp;<code>graph</code>&nbsp;为有 N 个节点（编号为&nbsp;<code>0, 1, 2, ..., N-1</code>）的无向连通图。&nbsp;</p>

<p><code>graph.length = N</code>，且只有节点 <code>i</code>&nbsp;和 <code>j</code>&nbsp;连通时，<code>j != i</code>&nbsp;在列表&nbsp;<code>graph[i]</code>&nbsp;中恰好出现一次。</p>

<p>返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[[1,2,3],[0],[0],[0]]
<strong>输出：</strong>4
<strong>解释：</strong>一个可能的路径为 [1,0,2,0,3]</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[[1],[0,2,4],[1,3,4],[2],[1,2]]
<strong>输出：</strong>4
<strong>解释：</strong>一个可能的路径为 [0,1,4,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= graph.length &lt;= 12</code></li>
	<li><code>0 &lt;= graph[i].length &lt;&nbsp;graph.length</code></li>
</ol>
<p>给出&nbsp;<code>graph</code>&nbsp;为有 N 个节点（编号为&nbsp;<code>0, 1, 2, ..., N-1</code>）的无向连通图。&nbsp;</p>

<p><code>graph.length = N</code>，且只有节点 <code>i</code>&nbsp;和 <code>j</code>&nbsp;连通时，<code>j != i</code>&nbsp;在列表&nbsp;<code>graph[i]</code>&nbsp;中恰好出现一次。</p>

<p>返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[[1,2,3],[0],[0],[0]]
<strong>输出：</strong>4
<strong>解释：</strong>一个可能的路径为 [1,0,2,0,3]</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[[1],[0,2,4],[1,3,4],[2],[1,2]]
<strong>输出：</strong>4
<strong>解释：</strong>一个可能的路径为 [0,1,4,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= graph.length &lt;= 12</code></li>
	<li><code>0 &lt;= graph[i].length &lt;&nbsp;graph.length</code></li>
</ol>
"""


class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        