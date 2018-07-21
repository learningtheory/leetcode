/*
<p>Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.</p>

<p><b>Note:</b> The length of path between two nodes is represented by the number of edges between them.</p>

<p>
<b>Example 1:</b>
</p>


<p>
Input:
<pre>
              5
             / \
            4   5
           / \   \
          1   1   5
</pre>
</p>

<p>
Output:
<pre>
2
</pre>
</p>

<p>
<b>Example 2:</b>
</p>


<p>
Input:
<pre>
              1
             / \
            4   5
           / \   \
          4   4   5
</pre>
</p>

<p>
Output:
<pre>
2
</pre>
</p>

<p><b>Note:</b>
The given binary tree has not more than 10000 nodes.  The height of the tree is not more than 1000.
</p><p>给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。</p>

<p><strong>注意</strong>：两个节点之间的路径长度由它们之间的边数表示。</p>

<p><strong>示例 1:</strong></p>

<p>输入:</p>

<pre>
              5
             / \
            4   5
           / \   \
          1   1   5
</pre>

<p>输出:</p>

<pre>
2
</pre>

<p><strong>示例 2:</strong></p>

<p>输入:</p>

<pre>
              1
             / \
            4   5
           / \   \
          4   4   5
</pre>

<p>输出:</p>

<pre>
2
</pre>

<p><strong>注意:</strong> 给定的二叉树不超过10000个结点。&nbsp;树的高度不超过1000。</p>
<p>给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。</p>

<p><strong>注意</strong>：两个节点之间的路径长度由它们之间的边数表示。</p>

<p><strong>示例 1:</strong></p>

<p>输入:</p>

<pre>
              5
             / \
            4   5
           / \   \
          1   1   5
</pre>

<p>输出:</p>

<pre>
2
</pre>

<p><strong>示例 2:</strong></p>

<p>输入:</p>

<pre>
              1
             / \
            4   5
           / \   \
          4   4   5
</pre>

<p>输出:</p>

<pre>
2
</pre>

<p><strong>注意:</strong> 给定的二叉树不超过10000个结点。&nbsp;树的高度不超过1000。</p>
*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int longestUnivaluePath(struct TreeNode* root) {
    
}