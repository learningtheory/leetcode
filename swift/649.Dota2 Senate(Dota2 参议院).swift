/*
<p>
In the world of Dota2, there are two parties: the <code>Radiant</code> and the <code>Dire</code>.
</p>

<p>
The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise <code>one</code> of the two rights:
<ol>
<li><code>Ban one senator's right</code>: <br/>A senator can make another senator lose <b>all his rights</b> in this and all the following rounds.</li>
<li><code>Announce the victory</code>: <br/>If this senator found the senators who still have rights to vote are all from <b>the same party</b>, he can announce the victory and make the decision about the change in the game.</li>
</ol>
</p>

<p>
Given a string representing each senator's party belonging. The character 'R' and 'D' represent the <code>Radiant</code> party and the <code>Dire</code> party respectively. Then if there are <code>n</code> senators, the size of the given string will be <code>n</code>.
</p>

<p>
The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.
</p>

<p>
Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be <code>Radiant</code> or <code>Dire</code>.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "RD"
<b>Output:</b> "Radiant"
<b>Explanation:</b> The first senator comes from Radiant and he can just ban the next senator's right in the round 1. <br/>And the second senator can't exercise any rights any more since his right has been banned. <br/>And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "RDD"
<b>Output:</b> "Dire"
<b>Explanation:</b> 
The first senator comes from Radiant and he can just ban the next senator's right in the round 1. <br/>And the second senator can't exercise any rights anymore since his right has been banned. <br/>And the third senator comes from Dire and he can ban the first senator's right in the round 1. <br/>And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The length of the given string will in the range [1, 10,000].</li>
</ol>
</p><p>&nbsp;Dota2 的世界里有两个阵营：<code>Radiant</code>(天辉)和&nbsp;<code>Dire</code>(夜魇)</p>

<p>Dota2 参议院由来自两派的参议员组成。现在参议院希望对一个 Dota2 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。在每一轮中，每一位参议员都可以行使两项权利中的<code><strong>一</strong></code>项：</p>

<ol>
	<li>
	<p><code>禁止一名参议员的权利</code>：</p>

	<p>参议员可以让另一位参议员在这一轮和随后的几轮中丧失<strong>所有的权利</strong>。</p>
	</li>
	<li>
	<p><br />
	<code>宣布胜利</code>：如果参议员发现有权利投票的参议员都是<strong>同一个阵营的</strong>，他可以宣布胜利并决定在游戏中的有关变化。</p>
	</li>
</ol>

<p>给定一个字符串代表每个参议员的阵营。字母&ldquo;R&rdquo;和&ldquo;D&rdquo;分别代表了<code>Radiant</code>(天辉)和&nbsp;<code>Dire</code>(夜魇)。然后，如果有 n 个参议员，给定字符串的大小将是<code>n</code>。</p>

<p>以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。</p>

<p>假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。输出应该是&nbsp;<code>Radiant</code>&nbsp;或&nbsp;<code>Dire</code>。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> &quot;RD&quot;
<strong>输出:</strong> &quot;Radiant&quot;
<strong>解释:  </strong><code>第一个参议员来自  Radiant 阵营并且他可以使用第一项权利让第二个参议员失去权力，因此第二个参议员将被跳过因为他没有任何权利。然后在第二轮的时候，第一个参议员可以宣布胜利，因为他是唯一一个有投票权的人</code>
</pre>

<p>&nbsp;</p>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> &quot;RDD&quot;
<strong>输出:</strong> &quot;Dire&quot;
<strong>解释:</strong> 
第一轮中,第一个<code>来自 Radiant 阵营的</code>参议员可以使用第一项权利禁止第二个参议员的权利
第二个<code>来自 Dire 阵营的</code>参议员会被跳过因为他的权利被禁止
第三个<code>来自 Dire 阵营的</code>参议员可以使用他的第一项权利禁止第一个参议员的权利
因此在第二轮只剩下第三个参议员拥有投票的权利,于是他可以宣布胜利
</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<ol>
	<li>给定字符串的长度在 [1, 10,000] 之间.</li>
</ol>

<p>&nbsp;</p>
<p>&nbsp;Dota2 的世界里有两个阵营：<code>Radiant</code>(天辉)和&nbsp;<code>Dire</code>(夜魇)</p>

<p>Dota2 参议院由来自两派的参议员组成。现在参议院希望对一个 Dota2 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。在每一轮中，每一位参议员都可以行使两项权利中的<code><strong>一</strong></code>项：</p>

<ol>
	<li>
	<p><code>禁止一名参议员的权利</code>：</p>

	<p>参议员可以让另一位参议员在这一轮和随后的几轮中丧失<strong>所有的权利</strong>。</p>
	</li>
	<li>
	<p><br />
	<code>宣布胜利</code>：如果参议员发现有权利投票的参议员都是<strong>同一个阵营的</strong>，他可以宣布胜利并决定在游戏中的有关变化。</p>
	</li>
</ol>

<p>给定一个字符串代表每个参议员的阵营。字母&ldquo;R&rdquo;和&ldquo;D&rdquo;分别代表了<code>Radiant</code>(天辉)和&nbsp;<code>Dire</code>(夜魇)。然后，如果有 n 个参议员，给定字符串的大小将是<code>n</code>。</p>

<p>以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。</p>

<p>假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。输出应该是&nbsp;<code>Radiant</code>&nbsp;或&nbsp;<code>Dire</code>。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> &quot;RD&quot;
<strong>输出:</strong> &quot;Radiant&quot;
<strong>解释:  </strong><code>第一个参议员来自  Radiant 阵营并且他可以使用第一项权利让第二个参议员失去权力，因此第二个参议员将被跳过因为他没有任何权利。然后在第二轮的时候，第一个参议员可以宣布胜利，因为他是唯一一个有投票权的人</code>
</pre>

<p>&nbsp;</p>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> &quot;RDD&quot;
<strong>输出:</strong> &quot;Dire&quot;
<strong>解释:</strong> 
第一轮中,第一个<code>来自 Radiant 阵营的</code>参议员可以使用第一项权利禁止第二个参议员的权利
第二个<code>来自 Dire 阵营的</code>参议员会被跳过因为他的权利被禁止
第三个<code>来自 Dire 阵营的</code>参议员可以使用他的第一项权利禁止第一个参议员的权利
因此在第二轮只剩下第三个参议员拥有投票的权利,于是他可以宣布胜利
</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<ol>
	<li>给定字符串的长度在 [1, 10,000] 之间.</li>
</ol>

<p>&nbsp;</p>
*/


class Solution {
    func predictPartyVictory(_ senate: String) -> String {
        
    }
}