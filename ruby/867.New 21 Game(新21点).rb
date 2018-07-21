=begin
<p>Alice plays the following game, loosely based on the card game &quot;21&quot;.</p>

<p>Alice starts with <code>0</code> points, and draws numbers while she has less than <code>K</code> points.&nbsp; During each draw, she gains an integer number of points randomly from the range <code>[1, W]</code>, where <code>W</code> is an integer.&nbsp; Each draw is independent and the outcomes have equal probabilities.</p>

<p>Alice stops drawing numbers when she gets <code>K</code> or more points.&nbsp; What is the probability&nbsp;that she has <code>N</code> or less points?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = 10, K = 1, W = 10
<strong>Output: </strong>1.00000
<strong>Explanation: </strong> Alice gets a single card, then stops.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = 6, K = 1, W = 10
<strong>Output: </strong>0.60000
<strong>Explanation: </strong> Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>N = 21, K = 17, W = 10
<strong>Output: </strong>0.73278</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= K &lt;= N &lt;= 10000</code></li>
	<li><code>1 &lt;= W &lt;= 10000</code></li>
	<li>Answers will be accepted as correct if they are within <code>10^-5</code> of the correct answer.</li>
	<li>The judging time limit has been reduced for this question.</li>
</ol>
<p>爱丽丝参与一个大致基于纸牌游戏 &ldquo;21点&rdquo; 规则的游戏，描述如下：</p>

<p>爱丽丝以 <code>0</code> 分开始，并在她的得分少于 <code>K</code> 分时抽取数字。 抽取时，她从 <code>[1, W]</code> 的范围中随机获得一个整数作为分数进行累计，其中 <code>W</code> 是整数。 每次抽取都是独立的，其结果具有相同的概率。</p>

<p>当爱丽丝获得不少于 <code>K</code> 分时，她就停止抽取数字。 爱丽丝的分数不超过 <code>N</code> 的概率是多少？</p>

<p><strong>示例</strong><strong> 1</strong><strong>：</strong></p>

<pre><strong>输入：</strong>N = 10, K = 1, W = 10
<strong>输出：</strong>1.00000
<strong>说明：</strong>爱丽丝得到一张卡，然后停止。</pre>

<p><strong>示例 </strong><strong>2</strong><strong>：</strong></p>

<pre><strong>输入：</strong>N = 6, K = 1, W = 10
<strong>输出：</strong>0.60000
<strong>说明：</strong>爱丽丝得到一张卡，然后停止。
在 W = 10 的 6 种可能下，她的得分不超过 N = 6 分。</pre>

<p><strong>示例 </strong><strong>3</strong><strong>：</strong></p>

<pre><strong>输入：</strong>N = 21, K = 17, W = 10
<strong>输出：</strong>0.73278</pre>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= K &lt;= N &lt;= 10000</code></li>
	<li><code>1 &lt;= W &lt;= 10000</code></li>
	<li>如果答案与正确答案的误差不超过 <code>10^-5</code>，则该答案将被视为正确答案通过。</li>
	<li>此问题的判断限制时间已经减少。</li>
</ol>
<p>爱丽丝参与一个大致基于纸牌游戏 &ldquo;21点&rdquo; 规则的游戏，描述如下：</p>

<p>爱丽丝以 <code>0</code> 分开始，并在她的得分少于 <code>K</code> 分时抽取数字。 抽取时，她从 <code>[1, W]</code> 的范围中随机获得一个整数作为分数进行累计，其中 <code>W</code> 是整数。 每次抽取都是独立的，其结果具有相同的概率。</p>

<p>当爱丽丝获得不少于 <code>K</code> 分时，她就停止抽取数字。 爱丽丝的分数不超过 <code>N</code> 的概率是多少？</p>

<p><strong>示例</strong><strong> 1</strong><strong>：</strong></p>

<pre><strong>输入：</strong>N = 10, K = 1, W = 10
<strong>输出：</strong>1.00000
<strong>说明：</strong>爱丽丝得到一张卡，然后停止。</pre>

<p><strong>示例 </strong><strong>2</strong><strong>：</strong></p>

<pre><strong>输入：</strong>N = 6, K = 1, W = 10
<strong>输出：</strong>0.60000
<strong>说明：</strong>爱丽丝得到一张卡，然后停止。
在 W = 10 的 6 种可能下，她的得分不超过 N = 6 分。</pre>

<p><strong>示例 </strong><strong>3</strong><strong>：</strong></p>

<pre><strong>输入：</strong>N = 21, K = 17, W = 10
<strong>输出：</strong>0.73278</pre>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= K &lt;= N &lt;= 10000</code></li>
	<li><code>1 &lt;= W &lt;= 10000</code></li>
	<li>如果答案与正确答案的误差不超过 <code>10^-5</code>，则该答案将被视为正确答案通过。</li>
	<li>此问题的判断限制时间已经减少。</li>
</ol>

=end


# @param {Integer} n
# @param {Integer} k
# @param {Integer} w
# @return {Float}
def new21_game(n, k, w)
    
end