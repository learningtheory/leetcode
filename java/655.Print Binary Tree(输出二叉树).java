/**
<p>Print a binary tree in an m*n 2D string array following these rules: </p>

<ol>
<li>The row number <code>m</code> should be equal to the height of the given binary tree.</li>
<li>The column number <code>n</code> should always be an odd number.</li>
<li>The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (<b>left-bottom part and right-bottom part</b>). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them. </li>
<li>Each unused space should contain an empty string <code>""</code>.</li>
<li>Print the subtrees following the same rules.</li>
</ol>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
     1
    /
   2
<b>Output:</b>
[["", "1", ""],
 ["2", "", ""]]
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>
     1
    / \
   2   3
    \
     4
<b>Output:</b>
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b>
      1
     / \
    2   5
   / 
  3 
 / 
4 
<b>Output:</b>

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
</pre>
</p>

<p><b>Note:</b>
The height of binary tree is in the range of [1, 10].
</p><p>在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：</p>

<ol>
	<li>行数&nbsp;<code>m</code>&nbsp;应当等于给定二叉树的高度。</li>
	<li>列数&nbsp;<code>n</code>&nbsp;应当总是奇数。</li>
	<li>根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（<strong>左下部分和右下部分</strong>）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。</li>
	<li>每个未使用的空间应包含一个空的字符串<code>&quot;&quot;</code>。</li>
	<li>使用相同的规则输出子树。</li>
</ol>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong>
     1
    /
   2
<strong>输出:</strong>
[[&quot;&quot;, &quot;1&quot;, &quot;&quot;],
 [&quot;2&quot;, &quot;&quot;, &quot;&quot;]]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong>
     1
    / \
   2   3
    \
     4
<strong>输出:</strong>
[[&quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;1&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;],
 [&quot;&quot;, &quot;2&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;3&quot;, &quot;&quot;],
 [&quot;&quot;, &quot;&quot;, &quot;4&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;]]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong>
      1
     / \
    2   5
   / 
  3 
 / 
4 
<strong>输出:</strong>
[[&quot;&quot;,  &quot;&quot;,  &quot;&quot;, &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;1&quot;, &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;]
 [&quot;&quot;,  &quot;&quot;,  &quot;&quot;, &quot;2&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;5&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;]
 [&quot;&quot;,  &quot;3&quot;, &quot;&quot;, &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;]
 [&quot;4&quot;, &quot;&quot;,  &quot;&quot;, &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;]]
</pre>

<p><strong>注意:</strong> 二叉树的高度在范围 [1, 10] 中。</p>
<p>在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：</p>

<ol>
	<li>行数&nbsp;<code>m</code>&nbsp;应当等于给定二叉树的高度。</li>
	<li>列数&nbsp;<code>n</code>&nbsp;应当总是奇数。</li>
	<li>根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（<strong>左下部分和右下部分</strong>）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。</li>
	<li>每个未使用的空间应包含一个空的字符串<code>&quot;&quot;</code>。</li>
	<li>使用相同的规则输出子树。</li>
</ol>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong>
     1
    /
   2
<strong>输出:</strong>
[[&quot;&quot;, &quot;1&quot;, &quot;&quot;],
 [&quot;2&quot;, &quot;&quot;, &quot;&quot;]]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong>
     1
    / \
   2   3
    \
     4
<strong>输出:</strong>
[[&quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;1&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;],
 [&quot;&quot;, &quot;2&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;3&quot;, &quot;&quot;],
 [&quot;&quot;, &quot;&quot;, &quot;4&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;]]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong>
      1
     / \
    2   5
   / 
  3 
 / 
4 
<strong>输出:</strong>
[[&quot;&quot;,  &quot;&quot;,  &quot;&quot;, &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;1&quot;, &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;]
 [&quot;&quot;,  &quot;&quot;,  &quot;&quot;, &quot;2&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;5&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;]
 [&quot;&quot;,  &quot;3&quot;, &quot;&quot;, &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;]
 [&quot;4&quot;, &quot;&quot;,  &quot;&quot;, &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;,  &quot;&quot;, &quot;&quot;, &quot;&quot;]]
</pre>

<p><strong>注意:</strong> 二叉树的高度在范围 [1, 10] 中。</p>
**/


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<String>> printTree(TreeNode root) {
        
    }
}