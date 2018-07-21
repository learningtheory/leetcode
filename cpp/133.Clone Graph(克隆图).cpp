/*
<p>
Clone an undirected graph. Each node in the graph contains a <code>label</code> and a list of its <code>neighbors</code>.
</p>

<div>
<br>
<b>OJ's undirected graph serialization:</b>

<p>
Nodes are labeled uniquely.
</p>

We use <code>#</code> as a separator for each node, and <code>,</code> as a separator for node label and each neighbor of the node.
</p>


<p>
As an example, consider the serialized graph <code><font color="red">{<font color="black">0</font>,1,2#</font><font color="blue"><font color="black">1</font>,2#</font><font color="green"><font color="black">2</font>,2}</font></code>.
</p>

<p>
The graph has a total of three nodes, and therefore contains three parts as separated by <code>#</code>.
<ol>
<li>First node is labeled as <code><font color="black">0</font></code>. Connect node <code><font color="black">0</font></code> to both nodes <code><font color="red">1</font></code> and <code><font color="red">2</font></code>.</li>
<li>Second node is labeled as <code><font color="black">1</font></code>. Connect node <code><font color="black">1</font></code> to node <code><font color="blue">2</font></code>.</li>
<li>Third node is labeled as <code><font color="black">2</font></code>. Connect node <code><font color="black">2</font></code> to node <code><font color="green">2</font></code> (itself), thus forming a self-cycle.</li>
</ol>
</p>

<p>
Visually, the graph looks like the following:
<pre>
       1
      / \
     /   \
    0 --- 2
         / \
         \_/
</pre>
</p>

</div><p>克隆一张无向图，图中的每个节点包含一个&nbsp;<code>label</code>&nbsp;（标签）和一个&nbsp;<code>neighbors</code>&nbsp;（邻接点）列表 。</p>

<p><strong>OJ的无向图序列化：</strong></p>

<p>节点被唯一标记。</p>

<p>我们用 <code>#</code> 作为每个节点的分隔符，用&nbsp;<code>,</code>&nbsp;作为节点标签和邻接点的分隔符。</p>

<p>例如，序列化无向图 <code>{0,1,2#1,2#2,2}</code>。</p>

<p>该图总共有三个节点, 被两个分隔符&nbsp; <code>#</code>&nbsp;分为三部分。&nbsp;</p>

<ol>
	<li>第一个节点的标签为 <code>0</code>，存在从节点 <code>0</code> 到节点 <code>1</code> 和节点 <code>2</code> 的两条边。</li>
	<li>第二个节点的标签为 <code>1</code>，存在从节点 <code>1</code> 到节点 <code>2</code> 的一条边。</li>
	<li>第三个节点的标签为 <code>2</code>，存在从节点 <code>2</code> 到节点 <code>2</code> (本身) 的一条边，从而形成自环。</li>
</ol>

<p>我们将图形可视化如下：</p>

<pre>       1
      / \
     /   \
    0 --- 2
         / \
         \_/
</pre>
<p>克隆一张无向图，图中的每个节点包含一个&nbsp;<code>label</code>&nbsp;（标签）和一个&nbsp;<code>neighbors</code>&nbsp;（邻接点）列表 。</p>

<p><strong>OJ的无向图序列化：</strong></p>

<p>节点被唯一标记。</p>

<p>我们用 <code>#</code> 作为每个节点的分隔符，用&nbsp;<code>,</code>&nbsp;作为节点标签和邻接点的分隔符。</p>

<p>例如，序列化无向图 <code>{0,1,2#1,2#2,2}</code>。</p>

<p>该图总共有三个节点, 被两个分隔符&nbsp; <code>#</code>&nbsp;分为三部分。&nbsp;</p>

<ol>
	<li>第一个节点的标签为 <code>0</code>，存在从节点 <code>0</code> 到节点 <code>1</code> 和节点 <code>2</code> 的两条边。</li>
	<li>第二个节点的标签为 <code>1</code>，存在从节点 <code>1</code> 到节点 <code>2</code> 的一条边。</li>
	<li>第三个节点的标签为 <code>2</code>，存在从节点 <code>2</code> 到节点 <code>2</code> (本身) 的一条边，从而形成自环。</li>
</ol>

<p>我们将图形可视化如下：</p>

<pre>       1
      / \
     /   \
    0 --- 2
         / \
         \_/
</pre>
*/


/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        
    }
};