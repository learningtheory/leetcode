/*
<p>We are playing the Guess Game. The game is as follows:<p> 

<p>I pick a number from <b>1</b> to <b><i>n</i></b>. You have to guess which number I picked.</p>

<p>Every time you guess wrong, I'll tell you whether the number is higher or lower.</p>

<p>You call a pre-defined API <code>guess(int num)</code> which returns 3 possible results (<code>-1</code>, <code>1</code>, or <code>0</code>):</p>
<pre>
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
</pre>

<p><b>Example:</b><br />
<pre>
n = 10, I pick 6.

Return 6.
</pre>
</p><p>我们正在玩一个猜数字游戏。 游戏规则如下：<br>
我从&nbsp;<strong>1</strong>&nbsp;到&nbsp;<em><strong>n</strong></em>&nbsp;选择一个数字。 你需要猜我选择了哪个数字。<br>
每次你猜错了，我会告诉你这个数字是大了还是小了。<br>
你调用一个预先定义好的接口&nbsp;<code>guess(int num)</code>，它会返回 3 个可能的结果（<code>-1</code>，<code>1</code>&nbsp;或 <code>0</code>）：</p>

<pre>-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！
</pre>

<p><strong>示例:</strong></p>

<pre>n = 10, 我选择 6.

返回 6.
</pre>
<p>我们正在玩一个猜数字游戏。 游戏规则如下：<br>
我从&nbsp;<strong>1</strong>&nbsp;到&nbsp;<em><strong>n</strong></em>&nbsp;选择一个数字。 你需要猜我选择了哪个数字。<br>
每次你猜错了，我会告诉你这个数字是大了还是小了。<br>
你调用一个预先定义好的接口&nbsp;<code>guess(int num)</code>，它会返回 3 个可能的结果（<code>-1</code>，<code>1</code>&nbsp;或 <code>0</code>）：</p>

<pre>-1 : 我的数字比较小
 1 : 我的数字比较大
 0 : 恭喜！你猜对了！
</pre>

<p><strong>示例:</strong></p>

<pre>n = 10, 我选择 6.

返回 6.
</pre>
*/


// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        
    }
};