/*
<p>
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
</p>

<p>
Determine the maximum amount of money the thief can rob tonight without alerting the police.
</p>

<p><b>Example 1:</b><br />
<pre>
     <font color="red">3</font>
    / \
   2   3
    \   \ 
     <font color="red">3   1</font>
</pre>
Maximum amount of money the thief can rob = <font color="red">3</font> + <font color="red">3</font> + <font color="red">1</font> = <b>7</b>.
</p>

<p><b>Example 2:</b><br />
<pre>
     3
    / \
   <font color="red">4</font>   <font color="red">5</font>
  / \   \ 
 1   3   1
</pre>
Maximum amount of money the thief can rob = <font color="red">4</font> + <font color="red">5</font> = <b>9</b>.
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/discuss/user/dietpepsi">@dietpepsi</a> for adding this problem and creating all test cases.</p><p>小偷又发现一个新的可行窃的地点。 这个地区只有一个入口，称为&ldquo;根&rdquo;。 除了根部之外，每栋房子有且只有一个父房子。 一番侦察之后，聪明的小偷意识到&ldquo;这个地方的所有房屋形成了一棵二叉树&rdquo;。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。</p>

<p>在不触动警报的情况下，计算小偷一晚能盗取的最高金额。</p>

<p><strong>示例 1:</strong></p>

<pre>
     <font color="red">3</font>
    / \
   2   3
    \   \ 
     <font color="red">3   1</font>
</pre>

<p>能盗取的最高金额 = <font color="red">3</font> + <font color="red">3</font> + <font color="red">1</font> = <strong>7</strong>.</p>

<p><strong>示例 2:</strong></p>

<pre>
     3
    / \
   <font color="red">4</font>   <font color="red">5</font>
  / \   \ 
 1   3   1
</pre>

<p>能盗取的最高金额&nbsp;= <font color="red">4</font> + <font color="red">5</font> = <strong>9</strong>.</p>

<p><strong>致谢:</strong><br>
特别感谢&nbsp;<a href="https://leetcode.com/discuss/user/dietpepsi">@dietpepsi</a>&nbsp;添加此题并创建所有测试用例。</p><p>小偷又发现一个新的可行窃的地点。 这个地区只有一个入口，称为&ldquo;根&rdquo;。 除了根部之外，每栋房子有且只有一个父房子。 一番侦察之后，聪明的小偷意识到&ldquo;这个地方的所有房屋形成了一棵二叉树&rdquo;。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。</p>

<p>在不触动警报的情况下，计算小偷一晚能盗取的最高金额。</p>

<p><strong>示例 1:</strong></p>

<pre>
     <font color="red">3</font>
    / \
   2   3
    \   \ 
     <font color="red">3   1</font>
</pre>

<p>能盗取的最高金额 = <font color="red">3</font> + <font color="red">3</font> + <font color="red">1</font> = <strong>7</strong>.</p>

<p><strong>示例 2:</strong></p>

<pre>
     3
    / \
   <font color="red">4</font>   <font color="red">5</font>
  / \   \ 
 1   3   1
</pre>

<p>能盗取的最高金额&nbsp;= <font color="red">4</font> + <font color="red">5</font> = <strong>9</strong>.</p>

<p><strong>致谢:</strong><br>
特别感谢&nbsp;<a href="https://leetcode.com/discuss/user/dietpepsi">@dietpepsi</a>&nbsp;添加此题并创建所有测试用例。</p>*/


/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rob(root *TreeNode) int {
    
}