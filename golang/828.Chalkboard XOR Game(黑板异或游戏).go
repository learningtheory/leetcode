/*
<p>We are given non-negative integers nums[i] which are written on a chalkboard.&nbsp; Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.&nbsp; If erasing a number causes&nbsp;the bitwise XOR of all the elements of the chalkboard to become&nbsp;0, then that player loses.&nbsp; (Also, we&#39;ll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)</p>

<p>Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.</p>

<p>Return True if and only if Alice wins the game, assuming both players play optimally.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> nums = [1, 1, 2]
<strong>Output:</strong> false
<strong>Explanation:</strong> 
Alice has two choices: erase 1 or erase 2. 
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.

</pre>

<p><strong>Notes: </strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 1000</code>.&nbsp;</li>
	<li><code>0 &lt;= nums[i] &lt;= 2^16</code>.</li>
</ul>

<p>&nbsp;</p>
<p>一个黑板上写着一个非负整数数组 nums[i] 。小红和小明轮流从黑板上擦掉一个数字，小红先手。如果擦除一个数字后，剩余的所有数字按位异或运算得出的结果等于 0 的话，当前玩家游戏失败。&nbsp;(另外，如果只剩一个数字，按位异或运算得到它本身；如果无数字剩余，按位异或运算结果为&nbsp;0。）</p>

<p>换种说法就是，轮到某个玩家时，如果当前黑板上所有数字按位异或运算结果等于 0，这个玩家获胜。</p>

<p>假设两个玩家每步都使用最优解，当且仅当小红获胜时返回 true。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> nums = [1, 1, 2]
<strong>输出:</strong> false
<strong>解释:</strong> 
小红有两个选择: 擦掉数字 1 或 2。
如果擦掉 1, 数组变成 [1, 2]。剩余数字按位异或得到 1 XOR 2 = 3。那么小明可以擦掉任意数字，因为小红会成为擦掉最后一个数字的人，她总是会输。
如果小红擦掉 2，那么数组变成[1, 1]。剩余数字按位异或得到 1 XOR 1 = 0。小红仍然会输掉游戏。
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li><code>0 &lt;= N &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 2^16</code></li>
</ul>
<p>一个黑板上写着一个非负整数数组 nums[i] 。小红和小明轮流从黑板上擦掉一个数字，小红先手。如果擦除一个数字后，剩余的所有数字按位异或运算得出的结果等于 0 的话，当前玩家游戏失败。&nbsp;(另外，如果只剩一个数字，按位异或运算得到它本身；如果无数字剩余，按位异或运算结果为&nbsp;0。）</p>

<p>换种说法就是，轮到某个玩家时，如果当前黑板上所有数字按位异或运算结果等于 0，这个玩家获胜。</p>

<p>假设两个玩家每步都使用最优解，当且仅当小红获胜时返回 true。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> nums = [1, 1, 2]
<strong>输出:</strong> false
<strong>解释:</strong> 
小红有两个选择: 擦掉数字 1 或 2。
如果擦掉 1, 数组变成 [1, 2]。剩余数字按位异或得到 1 XOR 2 = 3。那么小明可以擦掉任意数字，因为小红会成为擦掉最后一个数字的人，她总是会输。
如果小红擦掉 2，那么数组变成[1, 1]。剩余数字按位异或得到 1 XOR 1 = 0。小红仍然会输掉游戏。
</pre>

<p><strong>说明: </strong></p>

<ul>
	<li><code>0 &lt;= N &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 2^16</code></li>
</ul>
*/


func xorGame(nums []int) bool {
    
}