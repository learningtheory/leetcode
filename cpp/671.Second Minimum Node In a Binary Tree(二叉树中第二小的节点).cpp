/*
<p>
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly <code>two</code> or <code>zero</code> sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. 
</p>

<p>
Given such a binary tree, you need to output the <b>second minimum</b> value in the set made of all the nodes' value in the whole tree. 
</p>

<p>
If no such second minimum value exists, output -1 instead.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
    2
   / \
  2   5
     / \
    5   7

<b>Output:</b> 5
<b>Explanation:</b> The smallest value is 2, the second smallest value is 5.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
    2
   / \
  2   2

<b>Output:</b> -1
<b>Explanation:</b> The smallest value is 2, but there isn't any second smallest value.
</pre>
</p><p>给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为&nbsp;<code>2</code>&nbsp;或&nbsp;<code>0</code>。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。&nbsp;</p>

<p>给出这样的一个二叉树，你需要输出所有节点中的<strong>第二小的值。</strong>如果第二小的值不存在的话，输出 -1 <strong>。</strong></p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
    2
   / \
  2   5
     / \
    5   7

<strong>输出:</strong> 5
<strong>说明:</strong> 最小的值是 2 ，第二小的值是 5 。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
    2
   / \
  2   2

<strong>输出:</strong> -1
<strong>说明:</strong> 最小的值是 2, 但是不存在第二小的值。
</pre>
<p>给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为&nbsp;<code>2</code>&nbsp;或&nbsp;<code>0</code>。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。&nbsp;</p>

<p>给出这样的一个二叉树，你需要输出所有节点中的<strong>第二小的值。</strong>如果第二小的值不存在的话，输出 -1 <strong>。</strong></p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
    2
   / \
  2   5
     / \
    5   7

<strong>输出:</strong> 5
<strong>说明:</strong> 最小的值是 2 ，第二小的值是 5 。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
    2
   / \
  2   2

<strong>输出:</strong> -1
<strong>说明:</strong> 最小的值是 2, 但是不存在第二小的值。
</pre>
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
    int findSecondMinimumValue(TreeNode* root) {
        
    }
};