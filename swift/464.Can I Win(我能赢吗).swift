/*
<p>In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins. </p>

<p>What if we change the game so that players cannot re-use integers? </p>

<p>For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.</p>

<p>Given an integer <code>maxChoosableInteger</code> and another integer <code>desiredTotal</code>, determine if the first player to move can force a win, assuming both players play optimally. </p>

<p>You can always assume that <code>maxChoosableInteger</code> will not be larger than 20 and <code>desiredTotal</code> will not be larger than 300.
</p>

<p><b>Example</b>
<pre>
<b>Input:</b>
maxChoosableInteger = 10
desiredTotal = 11

<b>Output:</b>
false

<b>Explanation:</b>
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
</pre>
</p><p>在 &quot;100 game&quot; 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到 100 的玩家，即为胜者。</p>

<p>如果我们将游戏规则改为 &ldquo;玩家不能重复使用整数&rdquo; 呢？</p>

<p>例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 &gt;= 100。</p>

<p>给定一个整数&nbsp;<code>maxChoosableInteger</code>&nbsp;（整数池中可选择的最大数）和另一个整数&nbsp;<code>desiredTotal</code>（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？</p>

<p>你可以假设&nbsp;<code>maxChoosableInteger</code>&nbsp;不会大于 20，&nbsp;<code>desiredTotal</code>&nbsp;不会大于 300。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>
maxChoosableInteger = 10
desiredTotal = 11

<strong>输出：</strong>
false

<strong>解释：
</strong>无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 &gt;= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
</pre>
<p>在 &quot;100 game&quot; 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和达到 100 的玩家，即为胜者。</p>

<p>如果我们将游戏规则改为 &ldquo;玩家不能重复使用整数&rdquo; 呢？</p>

<p>例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 &gt;= 100。</p>

<p>给定一个整数&nbsp;<code>maxChoosableInteger</code>&nbsp;（整数池中可选择的最大数）和另一个整数&nbsp;<code>desiredTotal</code>（累计和），判断先出手的玩家是否能稳赢（假设两位玩家游戏时都表现最佳）？</p>

<p>你可以假设&nbsp;<code>maxChoosableInteger</code>&nbsp;不会大于 20，&nbsp;<code>desiredTotal</code>&nbsp;不会大于 300。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>
maxChoosableInteger = 10
desiredTotal = 11

<strong>输出：</strong>
false

<strong>解释：
</strong>无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 &gt;= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
</pre>
*/


class Solution {
    func canIWin(_ maxChoosableInteger: Int, _ desiredTotal: Int) -> Bool {
        
    }
}