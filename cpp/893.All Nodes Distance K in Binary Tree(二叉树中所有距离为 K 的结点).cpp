/*
<p>We are given a binary tree (with root node&nbsp;<code>root</code>), a <code>target</code> node, and an integer value `<font face="monospace">K`</font>.</p>

<p>Return a list of the values of all&nbsp;nodes that have a distance <code>K</code> from the <code>target</code> node.&nbsp; The answer can be returned in any order.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>root = <span id="example-input-1-1">[3,5,1,6,2,0,8,null,null,7,4]</span>, target = <span id="example-input-1-2">5</span>, K = <span id="example-input-1-3">2</span>
<strong>Output: </strong><span id="example-output-1">[7,4,1]</span>
<strong>Explanation: </strong>
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png" style="width: 280px; height: 240px;" />
Note that the inputs &quot;root&quot; and &quot;target&quot; are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

</pre>

<p><strong>Note:</strong></p>

<ol>
	<li>The given tree is non-empty.</li>
	<li>Each node in the tree has unique values&nbsp;<code>0 &lt;= node.val &lt;= 500</code>.</li>
	<li>The <code>target</code>&nbsp;node is a node in the tree.</li>
	<li><code>0 &lt;= K &lt;= 1000</code>.</li>
</ol>
</div><p>给定一个二叉树（具有根结点&nbsp;<code>root</code>），&nbsp;一个目标结点&nbsp;<code>target</code>&nbsp;，和一个整数值 <code>K</code> 。</p>

<p>返回到目标结点 <code>target</code> 距离为 <code>K</code> 的所有结点的值的列表。 答案可以以任何顺序返回。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

<strong>输出：</strong>[7,4,1]

<strong>解释：</strong>
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png" style="height: 240px; width: 280px;">

注意，输入的 &quot;root&quot; 和 &quot;target&quot; 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>给定的树是非空的，且最多有&nbsp;<code>K</code>&nbsp;个结点。</li>
	<li>树上的每个结点都具有唯一的值&nbsp;<code>0 &lt;= node.val &lt;= 500</code>&nbsp;。</li>
	<li>目标结点&nbsp;<code>target</code>&nbsp;是树上的结点。</li>
	<li><code>0 &lt;= K &lt;= 1000</code>.</li>
</ol>
<p>给定一个二叉树（具有根结点&nbsp;<code>root</code>），&nbsp;一个目标结点&nbsp;<code>target</code>&nbsp;，和一个整数值 <code>K</code> 。</p>

<p>返回到目标结点 <code>target</code> 距离为 <code>K</code> 的所有结点的值的列表。 答案可以以任何顺序返回。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

<strong>输出：</strong>[7,4,1]

<strong>解释：</strong>
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png" style="height: 240px; width: 280px;">

注意，输入的 &quot;root&quot; 和 &quot;target&quot; 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>给定的树是非空的，且最多有&nbsp;<code>K</code>&nbsp;个结点。</li>
	<li>树上的每个结点都具有唯一的值&nbsp;<code>0 &lt;= node.val &lt;= 500</code>&nbsp;。</li>
	<li>目标结点&nbsp;<code>target</code>&nbsp;是树上的结点。</li>
	<li><code>0 &lt;= K &lt;= 1000</code>.</li>
</ol>
*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> distanceK(TreeNode* root, TreeNode* target, int K) {
        
    }
};