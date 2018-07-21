=begin
<p>Given the root node of a binary search tree (BST) and a value to be inserted into the tree,&nbsp;insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.</p>

<p>Note that there may exist&nbsp;multiple valid ways for the&nbsp;insertion, as long as the tree remains a BST after insertion. You can return any of them.</p>

<p>For example,&nbsp;</p>

<pre>
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
</pre>

<p>You can return this binary search tree:</p>

<pre>
         4
       /   \
      2     7
     / \   /
    1   3 5
</pre>

<p>This tree is also valid:</p>

<pre>
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
</pre><p>给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。</p>

<p>注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。</p>

<p>例如,&nbsp;</p>

<pre>
给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和 插入的值: 5
</pre>

<p>你可以返回这个二叉搜索树:</p>

<pre>
         4
       /   \
      2     7
     / \   /
    1   3 5
</pre>

<p>或者这个树也是有效的:</p>

<pre>
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
</pre>
<p>给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。</p>

<p>注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。</p>

<p>例如,&nbsp;</p>

<pre>
给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和 插入的值: 5
</pre>

<p>你可以返回这个二叉搜索树:</p>

<pre>
         4
       /   \
      2     7
     / \   /
    1   3 5
</pre>

<p>或者这个树也是有效的:</p>

<pre>
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
</pre>

=end


# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {Integer} val
# @return {TreeNode}
def insert_into_bst(root, val)
    
end