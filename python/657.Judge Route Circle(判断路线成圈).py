"""
<p>
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to <b>the original place</b>. 
</p>

<p>
The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are <code>R</code> (Right), <code>L</code> (Left), <code>U</code> (Up) and <code>D</code> (down). The output should be true or false representing whether the robot makes a circle.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> "UD"
<b>Output:</b> true
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> "LL"
<b>Output:</b> false
</pre>
</p><p>初始位置 (0, 0) 处有一个机器人。给出它的一系列动作，判断这个机器人的移动路线是否形成一个圆圈，换言之就是判断它是否会移回到<strong>原来的位置</strong>。</p>

<p>移动顺序由一个字符串表示。每一个动作都是由一个字符来表示的。机器人有效的动作有&nbsp;<code>R</code>（右），<code>L</code>（左），<code>U</code>（上）和 <code>D</code>（下）。输出应为&nbsp;true 或 false，表示机器人移动路线是否成圈。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> &quot;UD&quot;
<strong>输出:</strong> true
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> &quot;LL&quot;
<strong>输出:</strong> false
</pre>
<p>初始位置 (0, 0) 处有一个机器人。给出它的一系列动作，判断这个机器人的移动路线是否形成一个圆圈，换言之就是判断它是否会移回到<strong>原来的位置</strong>。</p>

<p>移动顺序由一个字符串表示。每一个动作都是由一个字符来表示的。机器人有效的动作有&nbsp;<code>R</code>（右），<code>L</code>（左），<code>U</code>（上）和 <code>D</code>（下）。输出应为&nbsp;true 或 false，表示机器人移动路线是否成圈。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> &quot;UD&quot;
<strong>输出:</strong> true
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> &quot;LL&quot;
<strong>输出:</strong> false
</pre>
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        