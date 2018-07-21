=begin
<p>Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.</p>

<p>Calling <code>next()</code> will return the next smallest number in the BST.</p>

<p><b>Note: </b><code>next()</code> and <code>hasNext()</code> should run in average O(1) time and uses O(<i>h</i>) memory, where <i>h</i> is the height of the tree. </p>

<p><b>Credits:</b><br />Special thanks to <a href="https://oj.leetcode.com/discuss/user/ts">@ts</a> for adding this problem and creating all test cases.</p><p>实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。</p>

<p>调用 <code>next()</code> 将返回二叉搜索树中的下一个最小的数。</p>

<p>注意:<strong> </strong><code>next()</code> 和<code>hasNext()</code>&nbsp;操作的时间复杂度是O(1)，并使用&nbsp;<em>O(h)&nbsp;</em>内存，其中&nbsp;<em>h&nbsp;</em>是树的高度。</p>
<p>实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。</p>

<p>调用 <code>next()</code> 将返回二叉搜索树中的下一个最小的数。</p>

<p>注意:<strong> </strong><code>next()</code> 和<code>hasNext()</code>&nbsp;操作的时间复杂度是O(1)，并使用&nbsp;<em>O(h)&nbsp;</em>内存，其中&nbsp;<em>h&nbsp;</em>是树的高度。</p>

=end


# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

class BSTIterator
    # @param {TreeNode} root
    def initialize(root)
        
    end

    # @return {Boolean}
    def has_next
        
    end

    # @return {Integer}
    def next
        
    end
end

# Your BSTIterator will be called like this:
# i, v = BSTIterator.new(root), []
# while i.has_next()
#    v << i.next
# end