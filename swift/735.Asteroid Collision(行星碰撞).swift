/*
<p>
We are given an array <code>asteroids</code> of integers representing asteroids in a row.
</p><p>
For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).  Each asteroid moves at the same speed.
</p><p>
Find out the state of the asteroids after all collisions.  If two asteroids meet, the smaller one will explode.  If both are the same size, both will explode.  Two asteroids moving in the same direction will never meet.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
asteroids = [5, 10, -5]
<b>Output:</b> [5, 10]
<b>Explanation:</b> 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
asteroids = [8, -8]
<b>Output:</b> []
<b>Explanation:</b> 
The 8 and -8 collide exploding each other.
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> 
asteroids = [10, 2, -5]
<b>Output:</b> [10]
<b>Explanation:</b> 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
</pre>
</p>

<p><b>Example 4:</b><br />
<pre>
<b>Input:</b> 
asteroids = [-2, -1, 1, 2]
<b>Output:</b> [-2, -1, 1, 2]
<b>Explanation:</b> 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>asteroids</code> will be at most <code>10000</code>.</li>
<li>Each asteroid will be a non-zero integer in the range <code>[-1000, 1000].</code>.</li>
</p><p>给定一个整数数组 <code>asteroids</code>，表示在同一行的行星。</p>

<p>对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。</p>

<p>找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
asteroids = [5, 10, -5]
<strong>输出:</strong> [5, 10]
<strong>解释:</strong> 
10 和 -5 碰撞后只剩下 10。 5 和 10 永远不会发生碰撞。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
asteroids = [8, -8]
<strong>输出:</strong> []
<strong>解释:</strong> 
8 和 -8 碰撞后，两者都发生爆炸。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> 
asteroids = [10, 2, -5]
<strong>输出:</strong> [10]
<strong>解释:</strong> 
2 和 -5 发生碰撞后剩下 -5。10 和 -5 发生碰撞后剩下 10。
</pre>

<p><strong>示例 4:</strong></p>

<pre>
<strong>输入:</strong> 
asteroids = [-2, -1, 1, 2]
<strong>输出:</strong> [-2, -1, 1, 2]
<strong>解释:</strong> 
-2 和 -1 向左移动，而 1 和 2 向右移动。
由于移动方向相同的行星不会发生碰撞，所以最终没有行星发生碰撞。
</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>数组&nbsp;<code>asteroids</code> 的长度不超过&nbsp;<code>10000</code>。</li>
	<li>每一颗行星的大小都是非零整数，范围是&nbsp;<code>[-1000, 1000]</code>&nbsp;。</li>
</ul>
<p>给定一个整数数组 <code>asteroids</code>，表示在同一行的行星。</p>

<p>对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。</p>

<p>找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
asteroids = [5, 10, -5]
<strong>输出:</strong> [5, 10]
<strong>解释:</strong> 
10 和 -5 碰撞后只剩下 10。 5 和 10 永远不会发生碰撞。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
asteroids = [8, -8]
<strong>输出:</strong> []
<strong>解释:</strong> 
8 和 -8 碰撞后，两者都发生爆炸。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> 
asteroids = [10, 2, -5]
<strong>输出:</strong> [10]
<strong>解释:</strong> 
2 和 -5 发生碰撞后剩下 -5。10 和 -5 发生碰撞后剩下 10。
</pre>

<p><strong>示例 4:</strong></p>

<pre>
<strong>输入:</strong> 
asteroids = [-2, -1, 1, 2]
<strong>输出:</strong> [-2, -1, 1, 2]
<strong>解释:</strong> 
-2 和 -1 向左移动，而 1 和 2 向右移动。
由于移动方向相同的行星不会发生碰撞，所以最终没有行星发生碰撞。
</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>数组&nbsp;<code>asteroids</code> 的长度不超过&nbsp;<code>10000</code>。</li>
	<li>每一颗行星的大小都是非零整数，范围是&nbsp;<code>[-1000, 1000]</code>&nbsp;。</li>
</ul>
*/


class Solution {
    func asteroidCollision(_ asteroids: [Int]) -> [Int] {
        
    }
}