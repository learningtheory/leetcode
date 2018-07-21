/*
<p>Given a binary tree rooted at <code>root</code>, the <em>depth</em> of each node is the shortest distance to the root.</p>

<p>A node is <em>deepest</em> if it has the largest depth possible among&nbsp;any node in the <u>entire tree</u>.</p>

<p>The subtree of a node is that node, plus the set of all descendants of that node.</p>

<p>Return the node with the largest depth such that it contains all the deepest nodes in its subtree.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,5,1,6,2,0,8,null,null,7,4]</span>
<strong>Output: </strong><span id="example-output-1">[2,7,4]</span>
<strong>Explanation:
</strong>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png" style="width: 280px; height: 238px;" />

We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input &quot;[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]&quot; is a serialization of the given tree.
The output &quot;[2, 7, 4]&quot; is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The number of nodes in the tree will be between 1 and 500.</li>
	<li>The values of each node are unique.</li>
</ul>
<p>给定一个根为&nbsp;<code>root</code>&nbsp;的二叉树，每个结点的<em>深度</em>是它到根的最短距离。</p>

<p>如果一个结点在<strong>整个树</strong>的任意结点之间具有最大的深度，则该结点是<em>最深的</em>。</p>

<p>一个结点的子树是该结点加上它的所有后代的集合。</p>

<p>返回能满足&ldquo;以该结点为根的子树中包含所有最深的结点&rdquo;这一条件的具有最大深度的结点。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[3,5,1,6,2,0,8,null,null,7,4]
<strong>输出：</strong>[2,7,4]
<strong>解释：</strong>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png" style="height: 238px; width: 280px;">
我们返回值为 2 的结点，在图中用黄色标记。
在图中用蓝色标记的是树的最深的结点。
输入 &quot;[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]&quot; 是对给定的树的序列化表述。
输出 &quot;[2, 7, 4]&quot; 是对根结点的值为 2 的子树的序列化表述。
输入和输出都具有 TreeNode 类型。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中结点的数量介于&nbsp;1 和&nbsp;500 之间。</li>
	<li>每个结点的值都是独一无二的。</li>
</ul>
<p>给定一个根为&nbsp;<code>root</code>&nbsp;的二叉树，每个结点的<em>深度</em>是它到根的最短距离。</p>

<p>如果一个结点在<strong>整个树</strong>的任意结点之间具有最大的深度，则该结点是<em>最深的</em>。</p>

<p>一个结点的子树是该结点加上它的所有后代的集合。</p>

<p>返回能满足&ldquo;以该结点为根的子树中包含所有最深的结点&rdquo;这一条件的具有最大深度的结点。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[3,5,1,6,2,0,8,null,null,7,4]
<strong>输出：</strong>[2,7,4]
<strong>解释：</strong>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png" style="height: 238px; width: 280px;">
我们返回值为 2 的结点，在图中用黄色标记。
在图中用蓝色标记的是树的最深的结点。
输入 &quot;[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]&quot; 是对给定的树的序列化表述。
输出 &quot;[2, 7, 4]&quot; 是对根结点的值为 2 的子树的序列化表述。
输入和输出都具有 TreeNode 类型。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中结点的数量介于&nbsp;1 和&nbsp;500 之间。</li>
	<li>每个结点的值都是独一无二的。</li>
</ul>
*/


/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var subtreeWithAllDeepest = function(root) {
    
};