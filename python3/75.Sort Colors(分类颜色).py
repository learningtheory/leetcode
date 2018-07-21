"""
<p>Given an array with <em>n</em> objects colored red, white or blue, sort them <strong><a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a>&nbsp;</strong>so that objects of the same color are adjacent, with the colors in the order red, white and blue.</p>

<p>Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.</p>

<p><strong>Note:</strong>&nbsp;You are not suppose to use the library&#39;s sort function for this problem.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> [2,0,2,1,1,0]
<strong>Output:</strong> [0,0,1,1,2,2]</pre>

<p><strong>Follow up:</strong></p>

<ul>
	<li>A rather straight forward solution is a two-pass algorithm using counting sort.<br />
	First, iterate the array counting number of 0&#39;s, 1&#39;s, and 2&#39;s, then overwrite array with total number of 0&#39;s, then 1&#39;s and followed by 2&#39;s.</li>
	<li>Could you come up with a&nbsp;one-pass algorithm using only constant space?</li>
</ul>
<p>给定一个包含红色、白色和蓝色，一共&nbsp;<em>n </em>个元素的数组，<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong>对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。</p>

<p>此题中，我们使用整数 0、&nbsp;1 和 2 分别表示红色、白色和蓝色。</p>

<p><strong>注意:</strong><br>
不能使用代码库中的排序函数来解决这道题。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [2,0,2,1,1,0]
<strong>输出:</strong> [0,0,1,1,2,2]</pre>

<p><strong>进阶：</strong></p>

<ul>
	<li>一个直观的解决方案是使用计数排序的两趟扫描算法。<br>
	首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。</li>
	<li>你能想出一个仅使用常数空间的一趟扫描算法吗？</li>
</ul>
<p>给定一个包含红色、白色和蓝色，一共&nbsp;<em>n </em>个元素的数组，<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong>对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。</p>

<p>此题中，我们使用整数 0、&nbsp;1 和 2 分别表示红色、白色和蓝色。</p>

<p><strong>注意:</strong><br>
不能使用代码库中的排序函数来解决这道题。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [2,0,2,1,1,0]
<strong>输出:</strong> [0,0,1,1,2,2]</pre>

<p><strong>进阶：</strong></p>

<ul>
	<li>一个直观的解决方案是使用计数排序的两趟扫描算法。<br>
	首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。</li>
	<li>你能想出一个仅使用常数空间的一趟扫描算法吗？</li>
</ul>
"""


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        