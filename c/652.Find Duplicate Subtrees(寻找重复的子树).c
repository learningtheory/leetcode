/*
<p>Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any <b>one</b> of them.</p>

<p>Two trees are duplicate if they have the same structure with same node values.</p>

<p><b>Example 1: </b></p>

<pre>
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
</pre>

<p>The following are two duplicate subtrees:</p>

<pre>
      2
     /
    4
</pre>

<p>and</p>

<pre>
    4
</pre>
Therefore, you need to return above trees&#39; root in the form of a list.<p>给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意<strong>一棵</strong>的根结点即可。</p>

<p>两棵树重复是指它们具有相同的结构以及相同的结点值。</p>

<p><strong>示例 1：</strong></p>

<pre>        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
</pre>

<p>下面是两个重复的子树：</p>

<pre>      2
     /
    4
</pre>

<p>和</p>

<pre>    4
</pre>

<p>因此，你需要以列表的形式返回上述重复子树的根结点。</p>
<p>给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意<strong>一棵</strong>的根结点即可。</p>

<p>两棵树重复是指它们具有相同的结构以及相同的结点值。</p>

<p><strong>示例 1：</strong></p>

<pre>        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
</pre>

<p>下面是两个重复的子树：</p>

<pre>      2
     /
    4
</pre>

<p>和</p>

<pre>    4
</pre>

<p>因此，你需要以列表的形式返回上述重复子树的根结点。</p>
*/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct TreeNode** findDuplicateSubtrees(struct TreeNode* root, int* returnSize) {
    
}