=begin
<p>We have jobs: <code>difficulty[i]</code>&nbsp;is the difficulty of the&nbsp;<code>i</code>th job, and&nbsp;<code>profit[i]</code>&nbsp;is the profit of the&nbsp;<code>i</code>th job.&nbsp;</p>

<p>Now we have some workers.&nbsp;<code>worker[i]</code>&nbsp;is the ability of the&nbsp;<code>i</code>th worker, which means that this worker can only complete a job with difficulty at most&nbsp;<code>worker[i]</code>.&nbsp;</p>

<p>Every worker can be assigned at most one job, but one job&nbsp;can be completed multiple times.</p>

<p>For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.&nbsp; If a worker cannot complete any job, his profit is $0.</p>

<p>What is the most profit we can make?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
<strong>Output: </strong>100 
<strong>Explanation: W</strong>orkers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.</pre>

<p><strong>Notes:</strong></p>

<ul>
	<li><code>1 &lt;= difficulty.length = profit.length &lt;= 10000</code></li>
	<li><code>1 &lt;= worker.length &lt;= 10000</code></li>
	<li><code>difficulty[i], profit[i], worker[i]</code>&nbsp; are in range&nbsp;<code>[1, 10^5]</code></li>
</ul><p>有一些工作：<code>difficulty[i]&nbsp;</code>表示第<code>i</code>个工作的难度，<code>profit[i]</code>表示第<code>i</code>个工作的收益。</p>

<p>现在我们有一些工人。<code>worker[i]</code>是第<code>i</code>个工人的能力，即该工人只能完成难度小于等于<code>worker[i]</code>的工作。</p>

<p>每一个工人都最多只能安排一个工作，但是一个工作可以完成多次。</p>

<p>举个例子，如果3个工人都尝试完成一份报酬为1的同样工作，那么总收益为 $3。如果一个工人不能完成任何工作，他的收益为 $0 。</p>

<p>我们能得到的最大收益是多少？</p>

<p><strong>示例：</strong></p>

<pre><strong>输入: </strong>difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
<strong>输出: </strong>100 
<strong>解释: </strong>工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= difficulty.length = profit.length &lt;= 10000</code></li>
	<li><code>1 &lt;= worker.length &lt;= 10000</code></li>
	<li><code>difficulty[i], profit[i], worker[i]</code>&nbsp; 的范围是&nbsp;<code>[1, 10^5]</code></li>
</ul>
<p>有一些工作：<code>difficulty[i]&nbsp;</code>表示第<code>i</code>个工作的难度，<code>profit[i]</code>表示第<code>i</code>个工作的收益。</p>

<p>现在我们有一些工人。<code>worker[i]</code>是第<code>i</code>个工人的能力，即该工人只能完成难度小于等于<code>worker[i]</code>的工作。</p>

<p>每一个工人都最多只能安排一个工作，但是一个工作可以完成多次。</p>

<p>举个例子，如果3个工人都尝试完成一份报酬为1的同样工作，那么总收益为 $3。如果一个工人不能完成任何工作，他的收益为 $0 。</p>

<p>我们能得到的最大收益是多少？</p>

<p><strong>示例：</strong></p>

<pre><strong>输入: </strong>difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
<strong>输出: </strong>100 
<strong>解释: </strong>工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。</pre>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= difficulty.length = profit.length &lt;= 10000</code></li>
	<li><code>1 &lt;= worker.length &lt;= 10000</code></li>
	<li><code>difficulty[i], profit[i], worker[i]</code>&nbsp; 的范围是&nbsp;<code>[1, 10^5]</code></li>
</ul>

=end


# @param {Integer[]} difficulty
# @param {Integer[]} profit
# @param {Integer[]} worker
# @return {Integer}
def max_profit_assignment(difficulty, profit, worker)
    
end