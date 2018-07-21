"""
<p><em>This question is the same as &quot;Max Chunks to Make Sorted&quot; except the integers of the given array are not necessarily distinct, the input array could be up to length <code>2000</code>, and the elements could be up to <code>10**8</code>.</em></p>

<hr />

<p>Given an array <code>arr</code> of integers (<strong>not necessarily distinct</strong>), we split the array into some number of &quot;chunks&quot; (partitions), and individually sort each chunk.&nbsp; After concatenating them,&nbsp;the result equals the sorted array.</p>

<p>What is the most number of chunks we could have made?</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [5,4,3,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn&#39;t sorted.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [2,1,3,4,4]
<strong>Output:</strong> 4
<strong>Explanation:</strong>
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>arr</code> will have length in range <code>[1, 2000]</code>.</li>
	<li><code>arr[i]</code> will be an integer in range <code>[0, 10**8]</code>.</li>
</ul>

<p>&nbsp;</p><p><em>这个问题和&ldquo;最多能完成排序的块&rdquo;相似，但给定数组中的元素可以重复，输入数组最大长度为<code>2000</code>，其中的元素最大为<code>10**8</code>。</em></p>

<p><code>arr</code>是一个可能包含<strong>重复元素</strong>的整数数组，我们将这个数组分割成几个&ldquo;块&rdquo;，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。</p>

<p>我们最多能将数组分成多少块？</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> arr = [5,4,3,2,1]
<strong>输出:</strong> 1
<strong>解释:</strong>
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。 
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> arr = [2,1,3,4,4]
<strong>输出:</strong> 4
<strong>解释:</strong>
我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。 
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>arr</code>的长度在<code>[1, 2000]</code>之间。</li>
	<li><code>arr[i]</code>的大小在<code>[0, 10**8]</code>之间。</li>
</ul>
<p><em>这个问题和&ldquo;最多能完成排序的块&rdquo;相似，但给定数组中的元素可以重复，输入数组最大长度为<code>2000</code>，其中的元素最大为<code>10**8</code>。</em></p>

<p><code>arr</code>是一个可能包含<strong>重复元素</strong>的整数数组，我们将这个数组分割成几个&ldquo;块&rdquo;，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。</p>

<p>我们最多能将数组分成多少块？</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> arr = [5,4,3,2,1]
<strong>输出:</strong> 1
<strong>解释:</strong>
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。 
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> arr = [2,1,3,4,4]
<strong>输出:</strong> 4
<strong>解释:</strong>
我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。 
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>arr</code>的长度在<code>[1, 2000]</code>之间。</li>
	<li><code>arr[i]</code>的大小在<code>[0, 10**8]</code>之间。</li>
</ul>
"""


class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        