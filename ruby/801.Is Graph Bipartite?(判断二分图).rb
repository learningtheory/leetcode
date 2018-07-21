=begin
<p>Given an undirected&nbsp;<code>graph</code>, return <code>true</code> if and only if it is bipartite.</p>

<p>Recall that a graph is <em>bipartite</em> if we can split it&#39;s set of nodes into two independent&nbsp;subsets A and B such that every edge in the graph has one node in A and another node in B.</p>

<p>The graph is given in the following form: <code>graph[i]</code> is a list of indexes <code>j</code> for which the edge between nodes <code>i</code> and <code>j</code> exists.&nbsp; Each node is an integer between <code>0</code> and <code>graph.length - 1</code>.&nbsp; There are no self edges or parallel edges: <code>graph[i]</code> does not contain <code>i</code>, and it doesn&#39;t contain any element twice.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> [[1,3], [0,2], [1,3], [0,2]]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> [[1,2,3], [0,2], [0,1,3], [0,2]]
<strong>Output:</strong> false
<strong>Explanation:</strong> 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>graph</code> will have length in range <code>[1, 100]</code>.</li>
	<li><code>graph[i]</code> will contain integers in range <code>[0, graph.length - 1]</code>.</li>
	<li><code>graph[i]</code> will not contain <code>i</code> or duplicate values.</li>
	<li>The graph is undirected: if any element <code>j</code> is in <code>graph[i]</code>, then <code>i</code> will be in <code>graph[j]</code>.</li>
</ul>
<p>给定一个无向图<code>graph</code>，当这个图为二分图时返回<code>true</code>。</p>

<p>如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。</p>

<p><code>graph</code>将会以邻接表方式给出，<code>graph[i]</code>表示图中与节点<code>i</code>相连的所有节点。每个节点都是一个在<code>0</code>到<code>graph.length-1</code>之间的整数。这图中没有自环和平行边：&nbsp;<code>graph[i]</code>&nbsp;中不存在<code>i</code>，并且<code>graph[i]</code>中没有重复的值。</p>

<pre>
<code>
<strong>示例 1:</strong>
输入<strong>:</strong> [[1,3], [0,2], [1,3], [0,2]]
<strong>输出:</strong> true
<strong>解释:</strong> 
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。
</code></pre>

<pre>
<code>
<strong>示例 2:</strong>
<strong>输入:</strong> [[1,2,3], [0,2], [0,1,3], [0,2]]
<strong>输出:</strong> false
<strong>解释:</strong> 
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
</code></pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>graph</code> 的长度范围为 <code>[1, 100]</code>。</li>
	<li><code>graph[i]</code> 中的元素的范围为 <code>[0, graph.length - 1]</code>。</li>
	<li><code>graph[i]</code> 不会包含 <code>i</code> 或者有重复的值。</li>
	<li>图是无向的: 如果<code>j</code> 在 <code>graph[i]</code>里边, 那么 <code>i</code> 也会在 <code>graph[j]</code>里边。</li>
</ul>
<p>给定一个无向图<code>graph</code>，当这个图为二分图时返回<code>true</code>。</p>

<p>如果我们能将一个图的节点集合分割成两个独立的子集A和B，并使图中的每一条边的两个节点一个来自A集合，一个来自B集合，我们就将这个图称为二分图。</p>

<p><code>graph</code>将会以邻接表方式给出，<code>graph[i]</code>表示图中与节点<code>i</code>相连的所有节点。每个节点都是一个在<code>0</code>到<code>graph.length-1</code>之间的整数。这图中没有自环和平行边：&nbsp;<code>graph[i]</code>&nbsp;中不存在<code>i</code>，并且<code>graph[i]</code>中没有重复的值。</p>

<pre>
<code>
<strong>示例 1:</strong>
输入<strong>:</strong> [[1,3], [0,2], [1,3], [0,2]]
<strong>输出:</strong> true
<strong>解释:</strong> 
无向图如下:
0----1
|    |
|    |
3----2
我们可以将节点分成两组: {0, 2} 和 {1, 3}。
</code></pre>

<pre>
<code>
<strong>示例 2:</strong>
<strong>输入:</strong> [[1,2,3], [0,2], [0,1,3], [0,2]]
<strong>输出:</strong> false
<strong>解释:</strong> 
无向图如下:
0----1
| \  |
|  \ |
3----2
我们不能将节点分割成两个独立的子集。
</code></pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>graph</code> 的长度范围为 <code>[1, 100]</code>。</li>
	<li><code>graph[i]</code> 中的元素的范围为 <code>[0, graph.length - 1]</code>。</li>
	<li><code>graph[i]</code> 不会包含 <code>i</code> 或者有重复的值。</li>
	<li>图是无向的: 如果<code>j</code> 在 <code>graph[i]</code>里边, 那么 <code>i</code> 也会在 <code>graph[j]</code>里边。</li>
</ul>

=end


# @param {Integer[][]} graph
# @return {Boolean}
def is_bipartite(graph)
    
end