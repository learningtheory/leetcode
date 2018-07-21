/**
<p>
    You are given an array <i>x</i> of <code>n</code> positive numbers. You start at point <code>(0,0)</code> and moves <code>x[0]</code> metres to the north, then <code>x[1]</code> metres to the west,
    <code>x[2]</code> metres to the south,
    <code>x[3]</code> metres to the east and so on. In other words, after each move your direction changes
    counter-clockwise.
</p>
<p>
    Write a one-pass algorithm with <code>O(1)</code> extra space to determine, if your path crosses itself, or not.
</p>

<p>
<b>Example 1:</b><br/>
<pre>
Given <i>x</i> = <code>[2, 1, 1, 2]</code>,
?????
?   ?
???????>
    ?

Return <b>true</b> (self crossing)
</pre>
</p>

<p>
<b>Example 2:</b><br/>
<pre>
Given <i>x</i> = <code>[1, 2, 3, 4]</code>,
????????
?      ?
?
?
?????????????>

Return <b>false</b> (not self crossing)
</pre>
</p>

<p>
<b>Example 3:</b><br/>
<pre>
Given <i>x</i> = <code>[1, 1, 1, 1]</code>,
?????
?   ?
?????>

Return <b>true</b> (self crossing)
</pre>
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/discuss/user/dietpepsi">@dietpepsi</a> for adding this problem and creating all test cases.</p><p>给定一个含有&nbsp;<code>n</code>&nbsp;个正数的数组&nbsp;<em>x</em>。从点&nbsp;<code>(0,0)</code>&nbsp;开始，先向北移动&nbsp;<code>x[0]</code>&nbsp;米，然后向西移动&nbsp;<code>x[1]</code>&nbsp;米，向南移动&nbsp;<code>x[2]</code>&nbsp;米，向东移动&nbsp;<code>x[3]</code>&nbsp;米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。</p>

<p>编写一个&nbsp;<code>O(1)</code>&nbsp;空间复杂度的一趟扫描算法，判断你所经过的路径是否相交。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入: </strong><code>[2,1,1,2]
</code>
?????
?   ?
???????&gt;
    ?

<strong>输出:</strong> true 
<strong>解释:</strong> 路径交叉了
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入: </strong><code>[1,2,3,4]
</code>
????????
?      ?
?
?
?????????????&gt;

<strong>输出: </strong>false 
<strong>解释:</strong> 路径没有相交
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> <code>[1,1,1,1]
</code>
?????
?   ?
?????&gt;

<strong>输出:</strong> true 
<strong>解释:</strong> 路径相交了
</pre>
<p>给定一个含有&nbsp;<code>n</code>&nbsp;个正数的数组&nbsp;<em>x</em>。从点&nbsp;<code>(0,0)</code>&nbsp;开始，先向北移动&nbsp;<code>x[0]</code>&nbsp;米，然后向西移动&nbsp;<code>x[1]</code>&nbsp;米，向南移动&nbsp;<code>x[2]</code>&nbsp;米，向东移动&nbsp;<code>x[3]</code>&nbsp;米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。</p>

<p>编写一个&nbsp;<code>O(1)</code>&nbsp;空间复杂度的一趟扫描算法，判断你所经过的路径是否相交。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入: </strong><code>[2,1,1,2]
</code>
?????
?   ?
???????&gt;
    ?

<strong>输出:</strong> true 
<strong>解释:</strong> 路径交叉了
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入: </strong><code>[1,2,3,4]
</code>
????????
?      ?
?
?
?????????????&gt;

<strong>输出: </strong>false 
<strong>解释:</strong> 路径没有相交
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> <code>[1,1,1,1]
</code>
?????
?   ?
?????&gt;

<strong>输出:</strong> true 
<strong>解释:</strong> 路径相交了
</pre>
**/


class Solution {
    fun isSelfCrossing(x: IntArray): Boolean {
        
    }
}