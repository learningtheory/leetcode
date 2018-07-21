=begin
<p>
You are given two integer arrays <b>nums1</b> and <b>nums2</b> sorted in ascending order and an integer <b>k</b>. 
</p>

<p>Define a pair <b>(u,v)</b> which consists of one element from the first array and one element from the second array.</p>

<p>Find the k pairs <b>(u<sub>1</sub>,v<sub>1</sub>),(u<sub>2</sub>,v<sub>2</sub>) ...(u<sub>k</sub>,v<sub>k</sub>)</b> with the smallest sums.
</p>

<p><b>Example 1:</b><br />
<pre>
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
</pre>
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/elmirap/">@elmirap</a> and <a href="https://leetcode.com/stefanpochmann/">@StefanPochmann</a> for adding this problem and creating all test cases.</p><p>给定两个以升序排列的整形数组 <strong>nums1</strong> 和 <strong>nums2</strong>, 以及一个整数 <strong>k</strong>。</p>

<p>定义一对值&nbsp;<strong>(u,v)</strong>，其中第一个元素来自&nbsp;<strong>nums1</strong>，第二个元素来自 <strong>nums2</strong>。</p>

<p>找到和最小的 k 对数字&nbsp;<strong>(u<sub>1</sub>,v<sub>1</sub>), (u<sub>2</sub>,v<sub>2</sub>) ... (u<sub>k</sub>,v<sub>k</sub>)</strong>。</p>

<p><strong>示例 1:</strong></p>

<pre>
给出： nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

返回： [1,2],[1,4],[1,6]

返回序列中的前 3 对数：
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
给出：nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

返回： [1,1],[1,1]

返回序列中的前 2 对数：
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
给出：nums1 = [1,2], nums2 = [3],  k = 3 

返回： [1,3],[2,3]

也可能序列中所有的数对都被返回:
[1,3],[2,3]
</pre>

<p><strong>致谢:</strong><br />
特别感谢&nbsp;<a href="https://leetcode.com/elmirap/">@elmirap</a> 和&nbsp;<a href="https://leetcode.com/stefanpochmann/">@StefanPochmann</a>&nbsp;添加这个问题并创建所有的测试用例。</p>
<p>给定两个以升序排列的整形数组 <strong>nums1</strong> 和 <strong>nums2</strong>, 以及一个整数 <strong>k</strong>。</p>

<p>定义一对值&nbsp;<strong>(u,v)</strong>，其中第一个元素来自&nbsp;<strong>nums1</strong>，第二个元素来自 <strong>nums2</strong>。</p>

<p>找到和最小的 k 对数字&nbsp;<strong>(u<sub>1</sub>,v<sub>1</sub>), (u<sub>2</sub>,v<sub>2</sub>) ... (u<sub>k</sub>,v<sub>k</sub>)</strong>。</p>

<p><strong>示例 1:</strong></p>

<pre>
给出： nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

返回： [1,2],[1,4],[1,6]

返回序列中的前 3 对数：
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
给出：nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

返回： [1,1],[1,1]

返回序列中的前 2 对数：
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
给出：nums1 = [1,2], nums2 = [3],  k = 3 

返回： [1,3],[2,3]

也可能序列中所有的数对都被返回:
[1,3],[2,3]
</pre>

<p><strong>致谢:</strong><br />
特别感谢&nbsp;<a href="https://leetcode.com/elmirap/">@elmirap</a> 和&nbsp;<a href="https://leetcode.com/stefanpochmann/">@StefanPochmann</a>&nbsp;添加这个问题并创建所有的测试用例。</p>

=end


# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer[][]}
def k_smallest_pairs(nums1, nums2, k)
    
end