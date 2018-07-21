=begin
<p>
There is a room with <code>n</code> lights which are turned on initially and 4 buttons on the wall. After performing exactly <code>m</code> unknown operations towards buttons, you need to return how many different kinds of status of the <code>n</code> lights could be.
</p>

<p>
Suppose <code>n</code> lights are labeled as number [1, 2, 3 ..., n], function of these 4 buttons are given below:

<ol>
<li>Flip all the lights.</li>
<li>Flip lights with even numbers.</li>
<li>Flip lights with odd numbers.</li>
<li>Flip lights with (3k + 1) numbers, k = 0, 1, 2, ...</li>
</ol>
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> n = 1, m = 1.
<b>Output:</b> 2
<b>Explanation:</b> Status can be: [on], [off]
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> n = 2, m = 1.
<b>Output:</b> 3
<b>Explanation:</b> Status can be: [on, off], [off, on], [off, off]
</pre>
</p>


<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> n = 3, m = 1.
<b>Output:</b> 4
<b>Explanation:</b> Status can be: [off, on, off], [on, off, on], [off, off, off], [off, on, on].
</pre>
</p>

<p><b>Note:</b>
<code>n</code> and <code>m</code> both fit in range [0, 1000].
</p>
<p>现有一个房间，墙上挂有&nbsp;<code>n</code>&nbsp;只已经打开的灯泡和 4 个按钮。在进行了&nbsp;<code>m</code>&nbsp;次未知操作后，你需要返回这&nbsp;<code>n</code>&nbsp;只灯泡可能有多少种不同的状态。</p>

<p>假设这 <code>n</code> 只灯泡被编号为 [1, 2, 3 ..., n]，这 4 个按钮的功能如下：</p>

<ol>
	<li>将所有灯泡的状态反转（即开变为关，关变为开）</li>
	<li>将编号为偶数的灯泡的状态反转</li>
	<li>将编号为奇数的灯泡的状态反转</li>
	<li>将编号为 <code>3k+1</code> 的灯泡的状态反转（k = 0, 1, 2, ...)</li>
</ol>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> n = 1, m = 1.
<strong>输出:</strong> 2
<strong>说明:</strong> 状态为: [开], [关]
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> n = 2, m = 1.
<strong>输出:</strong> 3
<strong>说明:</strong> 状态为: [开, 关], [关, 开], [关, 关]
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> n = 3, m = 1.
<strong>输出:</strong> 4
<strong>说明:</strong> 状态为: [关, 开, 关], [开, 关, 开], [关, 关, 关], [关, 开, 开].
</pre>

<p><strong>注意：</strong>&nbsp;<code>n</code>&nbsp;和&nbsp;<code>m</code> 都属于 [0, 1000].</p>
<p>现有一个房间，墙上挂有&nbsp;<code>n</code>&nbsp;只已经打开的灯泡和 4 个按钮。在进行了&nbsp;<code>m</code>&nbsp;次未知操作后，你需要返回这&nbsp;<code>n</code>&nbsp;只灯泡可能有多少种不同的状态。</p>

<p>假设这 <code>n</code> 只灯泡被编号为 [1, 2, 3 ..., n]，这 4 个按钮的功能如下：</p>

<ol>
	<li>将所有灯泡的状态反转（即开变为关，关变为开）</li>
	<li>将编号为偶数的灯泡的状态反转</li>
	<li>将编号为奇数的灯泡的状态反转</li>
	<li>将编号为 <code>3k+1</code> 的灯泡的状态反转（k = 0, 1, 2, ...)</li>
</ol>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> n = 1, m = 1.
<strong>输出:</strong> 2
<strong>说明:</strong> 状态为: [开], [关]
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> n = 2, m = 1.
<strong>输出:</strong> 3
<strong>说明:</strong> 状态为: [开, 关], [关, 开], [关, 关]
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> n = 3, m = 1.
<strong>输出:</strong> 4
<strong>说明:</strong> 状态为: [关, 开, 关], [开, 关, 开], [关, 关, 关], [关, 开, 开].
</pre>

<p><strong>注意：</strong>&nbsp;<code>n</code>&nbsp;和&nbsp;<code>m</code> 都属于 [0, 1000].</p>

=end


# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def flip_lights(n, m)
    
end