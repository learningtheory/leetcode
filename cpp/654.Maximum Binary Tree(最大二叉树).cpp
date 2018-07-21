/*
<p>
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
<ol>
<li>The root is the maximum number in the array. </li>
<li>The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.</li>
<li>The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.</li> 
</ol>
</p>

<p>
Construct the maximum tree by the given array and output the root node of this tree.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [3,2,1,6,0,5]
<b>Output:</b> return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The size of the given array will be in the range [1,1000].</li>
</ol>
</p><p>给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：</p>

<ol>
	<li>二叉树的根是数组中的最大元素。</li>
	<li>左子树是通过数组中最大值左边部分构造出的最大二叉树。</li>
	<li>右子树是通过数组中最大值右边部分构造出的最大二叉树。</li>
</ol>

<p>通过给定的数组构建最大二叉树，并且输出这个树的根节点。</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>输入:</strong> [3,2,1,6,0,5]
<strong>输入:</strong> 返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>给定的数组的大小在 [1, 1000] 之间。</li>
</ol>
<p>给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：</p>

<ol>
	<li>二叉树的根是数组中的最大元素。</li>
	<li>左子树是通过数组中最大值左边部分构造出的最大二叉树。</li>
	<li>右子树是通过数组中最大值右边部分构造出的最大二叉树。</li>
</ol>

<p>通过给定的数组构建最大二叉树，并且输出这个树的根节点。</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>输入:</strong> [3,2,1,6,0,5]
<strong>输入:</strong> 返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>给定的数组的大小在 [1, 1000] 之间。</li>
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
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        
    }
};