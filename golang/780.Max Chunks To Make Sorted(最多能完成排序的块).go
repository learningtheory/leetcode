/*
<p>Given an array <code>arr</code> that is a permutation of <code>[0, 1, ..., arr.length - 1]</code>, we split the array into some number of &quot;chunks&quot; (partitions), and individually sort each chunk.&nbsp; After concatenating them,&nbsp;the result equals the sorted array.</p>

<p>What is the most number of chunks we could have made?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [4,3,2,1,0]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn&#39;t sorted.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,0,2,3,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>arr</code> will have length in range <code>[1, 10]</code>.</li>
	<li><code>arr[i]</code> will be a permutation of <code>[0, 1, ..., arr.length - 1]</code>.</li>
</ul>

<p>&nbsp;</p><p>数组<code>arr</code>是<code>[0, 1, ..., arr.length - 1]</code>的一种排列，我们将这个数组分割成几个&ldquo;块&rdquo;，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。</p>

<p>我们最多能将数组分成多少块？</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> arr = [4,3,2,1,0]
<strong>输出:</strong> 1
<strong>解释:</strong>
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> arr = [1,0,2,3,4]
<strong>输出:</strong> 4
<strong>解释:</strong>
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>arr</code> 的长度在 <code>[1, 10]</code> 之间。</li>
	<li><code>arr[i]</code>是 <code>[0, 1, ..., arr.length - 1]</code>的一种排列。</li>
</ul>
<p>数组<code>arr</code>是<code>[0, 1, ..., arr.length - 1]</code>的一种排列，我们将这个数组分割成几个&ldquo;块&rdquo;，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。</p>

<p>我们最多能将数组分成多少块？</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> arr = [4,3,2,1,0]
<strong>输出:</strong> 1
<strong>解释:</strong>
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> arr = [1,0,2,3,4]
<strong>输出:</strong> 4
<strong>解释:</strong>
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>arr</code> 的长度在 <code>[1, 10]</code> 之间。</li>
	<li><code>arr[i]</code>是 <code>[0, 1, ..., arr.length - 1]</code>的一种排列。</li>
</ul>
*/


func maxChunksToSorted(arr []int) int {
    
}