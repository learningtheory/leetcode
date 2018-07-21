/**
<p>Let <code>f(x)</code> be the number of zeroes at the end of <code>x!</code>. (Recall that <code>x! = 1 * 2 * 3 * ... * x</code>, and by convention, <code>0! = 1</code>.)</p>

<p>For example, <code>f(3) = 0</code> because 3! = 6 has no zeroes at the end, while <code>f(11) = 2</code> because 11! = 39916800 has 2 zeroes at the end. Given <code>K</code>, find how many non-negative integers <code>x</code> have the property that <code>f(x) = K</code>.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> K = 0
<strong>Output:</strong> 5
<strong>Explanation:</strong> 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

<strong>Example 2:</strong>
<strong>Input:</strong> K = 5
<strong>Output:</strong> 0
<strong>Explanation:</strong> There is no x such that x! ends in K = 5 zeroes.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>K</code> will be an integer in the range <code>[0, 10^9]</code>.</li>
</ul>
<p>&nbsp;<code>f(x)</code>&nbsp;是&nbsp;<code>x!</code>&nbsp;末尾是0的数量。（回想一下&nbsp;<code>x! = 1 * 2 * 3 * ... * x</code>，且<code>0! = 1</code>）</p>

<p>例如，&nbsp;<code>f(3) = 0</code>&nbsp;，因为3! = 6的末尾没有0；而&nbsp;<code>f(11) = 2</code>&nbsp;，因为11!= 39916800末端有2个0。给定&nbsp;<code>K</code>，找出多少个非负整数<code>x</code>&nbsp;，有&nbsp;<code>f(x) = K</code>&nbsp;的性质。</p>

<pre>
<strong>示例 1:
输入:</strong>K = 0<strong>
输出:</strong>5<strong>
解释:</strong>&nbsp;0!, 1!, 2!, 3!, and 4!&nbsp;均符合 K = 0 的条件。<strong>

示例 2:
输入:</strong>K = 5<strong>
输出:</strong>0<strong>
解释:</strong>没有匹配到这样的 x!，符合K = 5 的条件<strong>。</strong>
</pre>

<p><strong>注意：</strong></p>

<ul>
	<li>
	<p><code>K</code>是范围在&nbsp;<code>[0, 10^9]</code>&nbsp;的整数<strong>。</strong></p>
	</li>
</ul>
<p>&nbsp;<code>f(x)</code>&nbsp;是&nbsp;<code>x!</code>&nbsp;末尾是0的数量。（回想一下&nbsp;<code>x! = 1 * 2 * 3 * ... * x</code>，且<code>0! = 1</code>）</p>

<p>例如，&nbsp;<code>f(3) = 0</code>&nbsp;，因为3! = 6的末尾没有0；而&nbsp;<code>f(11) = 2</code>&nbsp;，因为11!= 39916800末端有2个0。给定&nbsp;<code>K</code>，找出多少个非负整数<code>x</code>&nbsp;，有&nbsp;<code>f(x) = K</code>&nbsp;的性质。</p>

<pre>
<strong>示例 1:
输入:</strong>K = 0<strong>
输出:</strong>5<strong>
解释:</strong>&nbsp;0!, 1!, 2!, 3!, and 4!&nbsp;均符合 K = 0 的条件。<strong>

示例 2:
输入:</strong>K = 5<strong>
输出:</strong>0<strong>
解释:</strong>没有匹配到这样的 x!，符合K = 5 的条件<strong>。</strong>
</pre>

<p><strong>注意：</strong></p>

<ul>
	<li>
	<p><code>K</code>是范围在&nbsp;<code>[0, 10^9]</code>&nbsp;的整数<strong>。</strong></p>
	</li>
</ul>
**/


object Solution {
    def preimageSizeFZF(K: Int): Int = {
        
    }
}