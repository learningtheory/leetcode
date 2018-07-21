=begin
<p>We have two integer sequences <code>A</code> and <code>B</code> of the same non-zero length.</p>

<p>We are allowed to swap elements <code>A[i]</code> and <code>B[i]</code>.&nbsp; Note that both elements are in the same index position in their respective sequences.</p>

<p>At the end of some number of swaps, <code>A</code> and <code>B</code> are both strictly increasing.&nbsp; (A sequence is <em>strictly increasing</em> if and only if <code>A[0] &lt; A[1] &lt; A[2] &lt; ... &lt; A[A.length - 1]</code>.)</p>

<p>Given A and B, return the minimum number of swaps to make both sequences strictly increasing.&nbsp; It is guaranteed that the given input always makes it possible.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> A = [1,3,5,4], B = [1,2,3,7]
<strong>Output:</strong> 1
<strong>Explanation: </strong>
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>A, B</code> are arrays with the same length, and that length will be in the range <code>[1, 1000]</code>.</li>
	<li><code>A[i], B[i]</code> are integer values in the range <code>[0, 2000]</code>.</li>
</ul><p>我们有两个长度相等且不为空的整型数组&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;。</p>

<p>我们可以交换&nbsp;<code>A[i]</code>&nbsp;和&nbsp;<code>B[i]</code>&nbsp;的元素。注意这两个元素在各自的序列中应该处于相同的位置。</p>

<p>在交换过一些元素之后，数组&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;都应该是严格递增的（数组严格递增的条件仅为<code>A[0] &lt; A[1] &lt; A[2] &lt; ... &lt; A[A.length - 1]</code>）。</p>

<p>给定数组&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;，请返回使得两个数组均保持严格递增状态的最小交换次数。假设给定的输入总是有效的。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> A = [1,3,5,4], B = [1,2,3,7]
<strong>输出:</strong> 1
<strong>解释: </strong>
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>A, B</code>&nbsp;两个数组的长度总是相等的，且长度的范围为&nbsp;<code>[1, 1000]</code>。</li>
	<li><code>A[i], B[i]</code>&nbsp;均为&nbsp;<code>[0, 2000]</code>区间内的整数。</li>
</ul>
<p>我们有两个长度相等且不为空的整型数组&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;。</p>

<p>我们可以交换&nbsp;<code>A[i]</code>&nbsp;和&nbsp;<code>B[i]</code>&nbsp;的元素。注意这两个元素在各自的序列中应该处于相同的位置。</p>

<p>在交换过一些元素之后，数组&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;都应该是严格递增的（数组严格递增的条件仅为<code>A[0] &lt; A[1] &lt; A[2] &lt; ... &lt; A[A.length - 1]</code>）。</p>

<p>给定数组&nbsp;<code>A</code>&nbsp;和&nbsp;<code>B</code>&nbsp;，请返回使得两个数组均保持严格递增状态的最小交换次数。假设给定的输入总是有效的。</p>

<pre>
<strong>示例:</strong>
<strong>输入:</strong> A = [1,3,5,4], B = [1,2,3,7]
<strong>输出:</strong> 1
<strong>解释: </strong>
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>A, B</code>&nbsp;两个数组的长度总是相等的，且长度的范围为&nbsp;<code>[1, 1000]</code>。</li>
	<li><code>A[i], B[i]</code>&nbsp;均为&nbsp;<code>[0, 2000]</code>区间内的整数。</li>
</ul>

=end


# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer}
def min_swap(a, b)
    
end