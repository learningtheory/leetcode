/**
<p>
In this problem, a tree is an <b>undirected</b> graph that is connected and has no cycles.
</p><p>
The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added.  The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
</p><p>
The resulting graph is given as a 2D-array of <code>edges</code>.  Each element of <code>edges</code> is a pair <code>[u, v]</code> with <code>u < v</code>, that represents an <b>undirected</b> edge connecting nodes <code>u</code> and <code>v</code>.
</p><p>
Return an edge that can be removed so that the resulting graph is a tree of N nodes.  If there are multiple answers, return the answer that occurs last in the given 2D-array.  The answer edge <code>[u, v]</code> should be in the same format, with <code>u < v</code>.
</p><p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [[1,2], [1,3], [2,3]]
<b>Output:</b> [2,3]
<b>Explanation:</b> The given undirected graph will be like this:
  1
 / \
2 - 3
</pre>
</p>
<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [[1,2], [2,3], [3,4], [1,4], [1,5]]
<b>Output:</b> [1,4]
<b>Explanation:</b> The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
</pre>
</p>
<p><b>Note:</b><br />
<li>The size of the input 2D-array will be between 3 and 1000.</li>
<li>Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.</li>
</p>

<br />

<p>
<b><font color="red">Update (2017-09-26):</font></b><br>
We have overhauled the problem description + test cases and specified clearly the graph is an <b><i>undirected</i></b> graph. For the <b><i>directed</i></b> graph follow up please see <b><a href="https://leetcode.com/problems/redundant-connection-ii/description/">Redundant Connection II</a></b>). We apologize for any inconvenience caused.
</p><p>在本问题中, 树指的是一个连通且无环的<strong>无向</strong>图。</p>

<p>输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。</p>

<p>结果图是一个以<code>边</code>组成的二维数组。每一个<code>边</code>的元素是一对<code>[u, v]</code>&nbsp;，满足&nbsp;<code>u &lt; v</code>，表示连接顶点<code>u</code>&nbsp;和<code>v</code>的<strong>无向</strong>图的边。</p>

<p>返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边&nbsp;<code>[u, v]</code> 应满足相同的格式&nbsp;<code>u &lt; v</code>。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> [[1,2], [1,3], [2,3]]
<strong>输出:</strong> [2,3]
<strong>解释:</strong> 给定的无向图为:
  1
 / \
2 - 3
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> [[1,2], [2,3], [3,4], [1,4], [1,5]]
<strong>输出:</strong> [1,4]
<strong>解释:</strong> 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li>输入的二维数组大小在 3 到 1000。</li>
	<li>二维数组中的整数在1到N之间，其中N是输入数组的大小。</li>
</ul>

<p><strong>更新(2017-09-26):</strong><br>
我们已经重新检查了问题描述及测试用例，明确图是<em><strong>无向&nbsp;</strong></em>图。对于有向图详见<strong><a href="https://leetcodechina.com/problems/redundant-connection-ii/description/">冗余连接II</a>。</strong>对于造成任何不便，我们深感歉意。</p>
<p>在本问题中, 树指的是一个连通且无环的<strong>无向</strong>图。</p>

<p>输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。</p>

<p>结果图是一个以<code>边</code>组成的二维数组。每一个<code>边</code>的元素是一对<code>[u, v]</code>&nbsp;，满足&nbsp;<code>u &lt; v</code>，表示连接顶点<code>u</code>&nbsp;和<code>v</code>的<strong>无向</strong>图的边。</p>

<p>返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边&nbsp;<code>[u, v]</code> 应满足相同的格式&nbsp;<code>u &lt; v</code>。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> [[1,2], [1,3], [2,3]]
<strong>输出:</strong> [2,3]
<strong>解释:</strong> 给定的无向图为:
  1
 / \
2 - 3
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> [[1,2], [2,3], [3,4], [1,4], [1,5]]
<strong>输出:</strong> [1,4]
<strong>解释:</strong> 给定的无向图为:
5 - 1 - 2
    |   |
    4 - 3
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li>输入的二维数组大小在 3 到 1000。</li>
	<li>二维数组中的整数在1到N之间，其中N是输入数组的大小。</li>
</ul>

<p><strong>更新(2017-09-26):</strong><br>
我们已经重新检查了问题描述及测试用例，明确图是<em><strong>无向&nbsp;</strong></em>图。对于有向图详见<strong><a href="https://leetcodechina.com/problems/redundant-connection-ii/description/">冗余连接II</a>。</strong>对于造成任何不便，我们深感歉意。</p>
**/


class Solution {
    fun findRedundantConnection(edges: Array<IntArray>): IntArray {
        
    }
}