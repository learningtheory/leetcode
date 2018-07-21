"""
<p>
N couples sit in 2N seats arranged in a row and want to hold hands.  We want to know the minimum number of swaps so that every couple is sitting side by side.  A <i>swap</i> consists of choosing <b>any</b> two people, then they stand up and switch seats. 
</p><p>
The people and seats are represented by an integer from <code>0</code> to <code>2N-1</code>, the couples are numbered in order, the first couple being <code>(0, 1)</code>, the second couple being <code>(2, 3)</code>, and so on with the last couple being <code>(2N-2, 2N-1)</code>.
</p><p>
The couples' initial seating is given by <code>row[i]</code> being the value of the person who is initially sitting in the i-th seat.

<p><b>Example 1:</b><br /><pre>
<b>Input:</b> row = [0, 2, 1, 3]
<b>Output:</b> 1
<b>Explanation:</b> We only need to swap the second (row[1]) and third (row[2]) person.
</pre></p>

<p><b>Example 2:</b><br /><pre>
<b>Input:</b> row = [3, 2, 0, 1]
<b>Output:</b> 0
<b>Explanation:</b> All couples are already seated side by side.
</pre></p>

<p>
<b>Note:</b>
<ol> 
<li> <code>len(row)</code> is even and in the range of <code>[4, 60]</code>.</li>
<li> <code>row</code> is guaranteed to be a permutation of <code>0...len(row)-1</code>.</li>
</ol><p>N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 <em>一</em>次交换可选择任意两人，让他们站起来交换座位。</p>

<p>人和座位用&nbsp;<code>0</code>&nbsp;到&nbsp;<code>2N-1</code>&nbsp;的整数表示，情侣们按顺序编号，第一对是&nbsp;<code>(0, 1)</code>，第二对是&nbsp;<code>(2, 3)</code>，以此类推，最后一对是&nbsp;<code>(2N-2, 2N-1)</code>。</p>

<p>这些情侣的初始座位&nbsp;&nbsp;<code>row[i]</code>&nbsp;是由最初始坐在第 i 个座位上的人决定的。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> row = [0, 2, 1, 3]
<strong>输出:</strong> 1
<strong>解释:</strong> 我们只需要交换row[1]和row[2]的位置即可。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> row = [3, 2, 0, 1]
<strong>输出:</strong> 0
<strong>解释:</strong> 无需交换座位，所有的情侣都已经可以手牵手了。
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li><code>len(row)</code> 是偶数且数值在&nbsp;<code>[4, 60]</code>范围内。</li>
	<li>可以保证<code>row</code> 是序列&nbsp;<code>0...len(row)-1</code>&nbsp;的一个全排列。</li>
</ol>
<p>N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 <em>一</em>次交换可选择任意两人，让他们站起来交换座位。</p>

<p>人和座位用&nbsp;<code>0</code>&nbsp;到&nbsp;<code>2N-1</code>&nbsp;的整数表示，情侣们按顺序编号，第一对是&nbsp;<code>(0, 1)</code>，第二对是&nbsp;<code>(2, 3)</code>，以此类推，最后一对是&nbsp;<code>(2N-2, 2N-1)</code>。</p>

<p>这些情侣的初始座位&nbsp;&nbsp;<code>row[i]</code>&nbsp;是由最初始坐在第 i 个座位上的人决定的。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> row = [0, 2, 1, 3]
<strong>输出:</strong> 1
<strong>解释:</strong> 我们只需要交换row[1]和row[2]的位置即可。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> row = [3, 2, 0, 1]
<strong>输出:</strong> 0
<strong>解释:</strong> 无需交换座位，所有的情侣都已经可以手牵手了。
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li><code>len(row)</code> 是偶数且数值在&nbsp;<code>[4, 60]</code>范围内。</li>
	<li>可以保证<code>row</code> 是序列&nbsp;<code>0...len(row)-1</code>&nbsp;的一个全排列。</li>
</ol>
"""


class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """