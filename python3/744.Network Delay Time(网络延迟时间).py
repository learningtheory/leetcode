"""
<p>
There are <code>N</code> network nodes, labelled <code>1</code> to <code>N</code>.
</p><p>
Given <code>times</code>, a list of travel times as <b>directed</b> edges <code>times[i] = (u, v, w)</code>, where <code>u</code> is the source node, <code>v</code> is the target node, and <code>w</code> is the time it takes for a signal to travel from source to target.
</p><p>
Now, we send a signal from a certain node <code>K</code>.  How long will it take for all nodes to receive the signal?  If it is impossible, return <code>-1</code>.
</p>

<p><b>Note:</b><br>
<ol>
<li><code>N</code> will be in the range <code>[1, 100]</code>.</li>
<li><code>K</code> will be in the range <code>[1, N]</code>.</li>
<li>The length of <code>times</code> will be in the range <code>[1, 6000]</code>.</li>
<li>All edges <code>times[i] = (u, v, w)</code> will have <code>1 <= u, v <= N</code> and <code>1 <= w <= 100</code>.</li>
</ol>
</p><p>有&nbsp;<code>N</code>&nbsp;个网络节点，标记为&nbsp;<code>1</code>&nbsp;到&nbsp;<code>N</code>。</p>

<p>给定一个列表&nbsp;<code>times</code>，表示信号经过<strong>有向</strong>边的传递时间。&nbsp;<code>times[i] = (u, v, w)</code>，其中&nbsp;<code>u</code>&nbsp;是源节点，<code>v</code>&nbsp;是目标节点， <code>w</code>&nbsp;是一个信号从源节点传递到目标节点的时间。</p>

<p>现在，我们向当前的节点&nbsp;<code>K</code>&nbsp;发送了一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回&nbsp;<code>-1</code>。</p>

<p><strong>注意:</strong></p>

<ol>
	<li><code>N</code>&nbsp;的范围在&nbsp;<code>[1, 100]</code>&nbsp;之间。</li>
	<li><code>K</code>&nbsp;的范围在&nbsp;<code>[1, N]</code>&nbsp;之间。</li>
	<li><code>times</code>&nbsp;的长度在&nbsp;<code>[1, 6000]</code>&nbsp;之间。</li>
	<li>所有的边&nbsp;<code>times[i] = (u, v, w)</code>&nbsp;都有&nbsp;<code>1 &lt;= u, v &lt;= N</code>&nbsp;且&nbsp;<code>1 &lt;= w &lt;= 100</code>。</li>
</ol>
<p>有&nbsp;<code>N</code>&nbsp;个网络节点，标记为&nbsp;<code>1</code>&nbsp;到&nbsp;<code>N</code>。</p>

<p>给定一个列表&nbsp;<code>times</code>，表示信号经过<strong>有向</strong>边的传递时间。&nbsp;<code>times[i] = (u, v, w)</code>，其中&nbsp;<code>u</code>&nbsp;是源节点，<code>v</code>&nbsp;是目标节点， <code>w</code>&nbsp;是一个信号从源节点传递到目标节点的时间。</p>

<p>现在，我们向当前的节点&nbsp;<code>K</code>&nbsp;发送了一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回&nbsp;<code>-1</code>。</p>

<p><strong>注意:</strong></p>

<ol>
	<li><code>N</code>&nbsp;的范围在&nbsp;<code>[1, 100]</code>&nbsp;之间。</li>
	<li><code>K</code>&nbsp;的范围在&nbsp;<code>[1, N]</code>&nbsp;之间。</li>
	<li><code>times</code>&nbsp;的长度在&nbsp;<code>[1, 6000]</code>&nbsp;之间。</li>
	<li>所有的边&nbsp;<code>times[i] = (u, v, w)</code>&nbsp;都有&nbsp;<code>1 &lt;= u, v &lt;= N</code>&nbsp;且&nbsp;<code>1 &lt;= w &lt;= 100</code>。</li>
</ol>
"""


class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        