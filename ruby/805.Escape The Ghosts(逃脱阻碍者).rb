=begin
<p>You are playing a simplified Pacman game. You&nbsp;start at the point <code>(0, 0)</code>, and your destination is<code> (target[0], target[1])</code>. There are several ghosts on the map, the i-th ghost starts at<code> (ghosts[i][0], ghosts[i][1])</code>.</p>

<p>Each turn, you and all ghosts simultaneously *may* move in one of 4 cardinal directions: north, east, west, or south, going from the previous point to a new point 1 unit of distance away.</p>

<p>You escape if and only if you can reach the target before any ghost reaches you (for any given moves the ghosts may take.)&nbsp; If you reach any square (including the target) at the same time as a ghost, it doesn&#39;t count as an escape.</p>

<p>Return True if and only if it is possible to escape.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> 
ghosts = [[1, 0], [0, 3]]
target = [0, 1]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
You can directly reach the destination (0, 1) at time 1, while the ghosts located at (1, 0) or (0, 3) have no way to catch up with you.
</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> 
ghosts = [[1, 0]]
target = [2, 0]
<strong>Output:</strong> false
<strong>Explanation:</strong> 
You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.
</pre>

<pre>
<strong>Example 3:</strong>
<strong>Input:</strong> 
ghosts = [[2, 0]]
target = [1, 0]
<strong>Output:</strong> false
<strong>Explanation:</strong> 
The ghost can reach the target at the same time as you.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>All points have coordinates with absolute value &lt;= <code>10000</code>.</li>
	<li>The number of ghosts will not exceed <code>100</code>.</li>
</ul>
<p>你在进行一个简化版的吃豆人游戏。你从&nbsp;<code>(0, 0)</code>&nbsp;点开始出发，你的目的地是&nbsp;<code>(target[0], target[1])</code>&nbsp;。地图上有一些阻碍者，第 i 个阻碍者从&nbsp;<code>(ghosts[i][0], ghosts[i][1])</code>&nbsp;出发。</p>

<p>每一回合，你和阻碍者们*可以*同时向东，西，南，北四个方向移动，每次可以移动到距离原位置1个单位的新位置。</p>

<p>如果你可以在任何阻碍者抓住你之前到达目的地（阻碍者可以采取任意行动方式），则被视为逃脱成功。如果你和阻碍者同时到达了一个位置（包括目的地）都不算是逃脱成功。</p>

<p>当且仅当你有可能成功逃脱时，输出 True。</p>

<pre><strong>示例 1:</strong>
<strong>输入：</strong> 
ghosts = [[1, 0], [0, 3]]
target = [0, 1]
<strong>输出：</strong>true
<strong>解释：
</strong>你可以直接一步到达目的地(0,1)，在(1, 0)或者(0, 3)位置的阻碍者都不可能抓住你。 
</pre>

<pre><strong>示例 2:</strong>
<strong>输入：</strong> 
ghosts = [[1, 0]]
target = [2, 0]
<strong>输出：</strong>false
<strong>解释：</strong>
你需要走到位于(2, 0)的目的地，但是在(1, 0)的阻碍者位于你和目的地之间。 
</pre>

<pre><strong>示例 3:</strong>
<strong>输入：</strong> 
ghosts = [[2, 0]]
target = [1, 0]
<strong>输出：</strong>false
<strong>解释：
</strong>阻碍者可以和你同时达到目的地。 
</pre>

<p><strong>说明：</strong></p>

<ul>
	<li>所有的点的坐标值的绝对值 &lt;=&nbsp;<code>10000</code>。</li>
	<li>阻碍者的数量不会超过&nbsp;<code>100</code>。</li>
</ul>
<p>你在进行一个简化版的吃豆人游戏。你从&nbsp;<code>(0, 0)</code>&nbsp;点开始出发，你的目的地是&nbsp;<code>(target[0], target[1])</code>&nbsp;。地图上有一些阻碍者，第 i 个阻碍者从&nbsp;<code>(ghosts[i][0], ghosts[i][1])</code>&nbsp;出发。</p>

<p>每一回合，你和阻碍者们*可以*同时向东，西，南，北四个方向移动，每次可以移动到距离原位置1个单位的新位置。</p>

<p>如果你可以在任何阻碍者抓住你之前到达目的地（阻碍者可以采取任意行动方式），则被视为逃脱成功。如果你和阻碍者同时到达了一个位置（包括目的地）都不算是逃脱成功。</p>

<p>当且仅当你有可能成功逃脱时，输出 True。</p>

<pre><strong>示例 1:</strong>
<strong>输入：</strong> 
ghosts = [[1, 0], [0, 3]]
target = [0, 1]
<strong>输出：</strong>true
<strong>解释：
</strong>你可以直接一步到达目的地(0,1)，在(1, 0)或者(0, 3)位置的阻碍者都不可能抓住你。 
</pre>

<pre><strong>示例 2:</strong>
<strong>输入：</strong> 
ghosts = [[1, 0]]
target = [2, 0]
<strong>输出：</strong>false
<strong>解释：</strong>
你需要走到位于(2, 0)的目的地，但是在(1, 0)的阻碍者位于你和目的地之间。 
</pre>

<pre><strong>示例 3:</strong>
<strong>输入：</strong> 
ghosts = [[2, 0]]
target = [1, 0]
<strong>输出：</strong>false
<strong>解释：
</strong>阻碍者可以和你同时达到目的地。 
</pre>

<p><strong>说明：</strong></p>

<ul>
	<li>所有的点的坐标值的绝对值 &lt;=&nbsp;<code>10000</code>。</li>
	<li>阻碍者的数量不会超过&nbsp;<code>100</code>。</li>
</ul>

=end


# @param {Integer[][]} ghosts
# @param {Integer[]} target
# @return {Boolean}
def escape_ghosts(ghosts, target)
    
end