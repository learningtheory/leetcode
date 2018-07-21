"""
<p>
Given two arrays, write a function to compute their intersection.
</p>

<p><b>Example:</b><br />
Given <i>nums1</i> = <code>[1, 2, 2, 1]</code>, <i>nums2</i> = <code>[2, 2]</code>, return <code>[2, 2]</code>.
</p>

<p><b>Note:</b><br />
<ul>
<li>Each element in the result should appear as many times as it shows in both arrays.</li>
<li>The result can be in any order.</li>
</ul>
</p>

<p><b>Follow up:</b><br />
<ul>
<li>What if the given array is already sorted? How would you optimize your algorithm?</li>
<li>What if <i>nums1</i>'s size is small compared to <i>nums2</i>'s size? Which algorithm is better?</li>
<li>What if elements of <i>nums2</i> are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?</li>
</ul>
</p><p>给定两个数组，写一个方法来计算它们的交集。</p>

<p><strong>例如:</strong><br />
给定<strong>&nbsp;</strong><em>nums1</em> = <code>[1, 2, 2, 1]</code>, <em>nums2</em> = <code>[2, 2]</code>, 返回&nbsp;<code>[2, 2]</code>.</p>

<p><strong>注意：</strong></p>

<ul>
	<li><strong>&nbsp;</strong>&nbsp; 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。</li>
	<li>&nbsp; &nbsp;我们可以不考虑输出结果的顺序。</li>
</ul>

<p><strong><strong>跟进:</strong></strong></p>

<ul>
	<li>如果给定的数组已经排好序呢？你将如何优化你的算法？</li>
	<li>如果&nbsp;<em>nums1&nbsp;</em>的大小比&nbsp;<em>nums2&nbsp;</em>小很多，哪种方法更优？</li>
	<li>如果<em>nums2</em>的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？</li>
</ul>
<p>给定两个数组，写一个方法来计算它们的交集。</p>

<p><strong>例如:</strong><br />
给定<strong>&nbsp;</strong><em>nums1</em> = <code>[1, 2, 2, 1]</code>, <em>nums2</em> = <code>[2, 2]</code>, 返回&nbsp;<code>[2, 2]</code>.</p>

<p><strong>注意：</strong></p>

<ul>
	<li><strong>&nbsp;</strong>&nbsp; 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。</li>
	<li>&nbsp; &nbsp;我们可以不考虑输出结果的顺序。</li>
</ul>

<p><strong><strong>跟进:</strong></strong></p>

<ul>
	<li>如果给定的数组已经排好序呢？你将如何优化你的算法？</li>
	<li>如果&nbsp;<em>nums1&nbsp;</em>的大小比&nbsp;<em>nums2&nbsp;</em>小很多，哪种方法更优？</li>
	<li>如果<em>nums2</em>的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？</li>
</ul>
"""


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        