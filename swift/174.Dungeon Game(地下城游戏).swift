/*
<style type="text/css">table.dungeon, .dungeon th, .dungeon td {
  border:3px solid black;
}

 .dungeon th, .dungeon td {
    text-align: center;
    height: 70px;
    width: 70px;
}
</style>
<p>The demons had captured the princess (<strong>P</strong>) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (<strong>K</strong>) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.</p>

<p>The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.</p>

<p>Some of the rooms are guarded by demons, so the knight loses health (<em>negative</em> integers) upon entering these rooms; other rooms are either empty (<em>0&#39;s</em>) or contain magic orbs that increase the knight&#39;s health (<em>positive</em> integers).</p>

<p>In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.</p>

<p>&nbsp;</p>

<p><strong>Write a function to determine the knight&#39;s minimum initial health so that he is able to rescue the princess.</strong></p>

<p>For example, given the dungeon below, the initial health of the knight must be at least <strong>7</strong> if he follows the optimal path <code>RIGHT-&gt; RIGHT -&gt; DOWN -&gt; DOWN</code>.</p>

<table class="dungeon">
	<tbody>
		<tr>
			<td>-2 (K)</td>
			<td>-3</td>
			<td>3</td>
		</tr>
		<tr>
			<td>-5</td>
			<td>-10</td>
			<td>1</td>
		</tr>
		<tr>
			<td>10</td>
			<td>30</td>
			<td>-5 (P)</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The knight&#39;s health has no upper bound.</li>
	<li>Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.</li>
</ul>
<style>
table.dungeon, .dungeon th, .dungeon td {
  border:3px solid black;
}

 .dungeon th, .dungeon td {
    text-align: center;
    height: 70px;
    width: 70px;
}
</style>

<p>一些恶魔抓住了公主（<strong>P</strong>）并将她关在了地下城的右下角。地下城是由&nbsp;M x N 个房间组成的二维网格。我们英勇的骑士（<strong>K</strong>）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。</p>

<p>骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。</p>

<p>有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为<em>负整数</em>，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 <em>0</em>），要么包含增加骑士健康点数的魔法球（若房间里的值为<em>正整数</em>，则表示骑士将增加健康点数）。</p>

<p>为了尽快到达公主，骑士决定每次只向右或向下移动一步。</p>

<p>&nbsp;</p>

<p><strong>编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。</strong></p>

<p>例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 <code>右 -&gt; 右 -&gt; 下 -&gt; 下</code>，则骑士的初始健康点数至少为 <strong>7</strong>。</p>

<table class="dungeon">
<tr> 
<td>-2 (K)</td> 
<td>-3</td> 
<td>3</td> 
</tr> 
<tr> 
<td>-5</td> 
<td>-10</td> 
<td>1</td> 
</tr> 
<tr> 
<td>10</td> 
<td>30</td> 
<td>-5 (P)</td> 
</tr> 
</table>
<!---2K   -3  3
-5   -10   1
10 30   5P-->

<p>&nbsp;</p>

<p><strong>说明:</strong></p>

<ul>
	<li>
	<p>骑士的健康点数没有上限。</p>
	</li>
	<li>任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。</li>
</ul><style>
table.dungeon, .dungeon th, .dungeon td {
  border:3px solid black;
}

 .dungeon th, .dungeon td {
    text-align: center;
    height: 70px;
    width: 70px;
}
</style>

<p>一些恶魔抓住了公主（<strong>P</strong>）并将她关在了地下城的右下角。地下城是由&nbsp;M x N 个房间组成的二维网格。我们英勇的骑士（<strong>K</strong>）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。</p>

<p>骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。</p>

<p>有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为<em>负整数</em>，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 <em>0</em>），要么包含增加骑士健康点数的魔法球（若房间里的值为<em>正整数</em>，则表示骑士将增加健康点数）。</p>

<p>为了尽快到达公主，骑士决定每次只向右或向下移动一步。</p>

<p>&nbsp;</p>

<p><strong>编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。</strong></p>

<p>例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 <code>右 -&gt; 右 -&gt; 下 -&gt; 下</code>，则骑士的初始健康点数至少为 <strong>7</strong>。</p>

<table class="dungeon">
<tr> 
<td>-2 (K)</td> 
<td>-3</td> 
<td>3</td> 
</tr> 
<tr> 
<td>-5</td> 
<td>-10</td> 
<td>1</td> 
</tr> 
<tr> 
<td>10</td> 
<td>30</td> 
<td>-5 (P)</td> 
</tr> 
</table>
<!---2K   -3  3
-5   -10   1
10 30   5P-->

<p>&nbsp;</p>

<p><strong>说明:</strong></p>

<ul>
	<li>
	<p>骑士的健康点数没有上限。</p>
	</li>
	<li>任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。</li>
</ul>*/


class Solution {
    func calculateMinimumHP(_ dungeon: [[Int]]) -> Int {
        
    }
}