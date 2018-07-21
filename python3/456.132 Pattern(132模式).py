"""
<p>
Given a sequence of n integers a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>, a 132 pattern is a subsequence a<sub><b>i</b></sub>, a<sub><b>j</b></sub>, a<sub><b>k</b></sub> such
that <b>i</b> < <b>j</b> < <b>k</b> and a<sub><b>i</b></sub> < a<sub><b>k</b></sub> < a<sub><b>j</b></sub>. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.</p>

<p><b>Note:</b> n will be less than 15,000.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1, 2, 3, 4]

<b>Output:</b> False

<b>Explanation:</b> There is no 132 pattern in the sequence.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [3, 1, 4, 2]

<b>Output:</b> True

<b>Explanation:</b> There is a 132 pattern in the sequence: [1, 4, 2].
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> [-1, 3, 2, 0]

<b>Output:</b> True

<b>Explanation:</b> There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
</pre>
</p><p>给定一个整数序列：a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>，一个132模式的子序列&nbsp;a<sub><strong>i</strong></sub>, a<sub><strong>j</strong></sub>, a<sub><strong>k</strong></sub>&nbsp;被定义为：当 <strong>i</strong> &lt; <strong>j</strong> &lt; <strong>k</strong> 时，a<sub><strong>i</strong></sub> &lt; a<sub><strong>k</strong></sub> &lt; a<sub><strong>j</strong></sub>。设计一个算法，当给定有&nbsp;n 个数字的序列时，验证这个序列中是否含有132模式的子序列。</p>

<p><strong>注意：</strong>n 的值小于15000。</p>

<p><strong>示例1:</strong></p>

<pre>
<strong>输入:</strong> [1, 2, 3, 4]

<strong>输出:</strong> False

<strong>解释:</strong> 序列中不存在132模式的子序列。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [3, 1, 4, 2]

<strong>输出:</strong> True

<strong>解释:</strong> 序列中有 1 个132模式的子序列： [1, 4, 2].
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> [-1, 3, 2, 0]

<strong>输出:</strong> True

<strong>解释:</strong> 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
</pre>
<p>给定一个整数序列：a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>，一个132模式的子序列&nbsp;a<sub><strong>i</strong></sub>, a<sub><strong>j</strong></sub>, a<sub><strong>k</strong></sub>&nbsp;被定义为：当 <strong>i</strong> &lt; <strong>j</strong> &lt; <strong>k</strong> 时，a<sub><strong>i</strong></sub> &lt; a<sub><strong>k</strong></sub> &lt; a<sub><strong>j</strong></sub>。设计一个算法，当给定有&nbsp;n 个数字的序列时，验证这个序列中是否含有132模式的子序列。</p>

<p><strong>注意：</strong>n 的值小于15000。</p>

<p><strong>示例1:</strong></p>

<pre>
<strong>输入:</strong> [1, 2, 3, 4]

<strong>输出:</strong> False

<strong>解释:</strong> 序列中不存在132模式的子序列。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [3, 1, 4, 2]

<strong>输出:</strong> True

<strong>解释:</strong> 序列中有 1 个132模式的子序列： [1, 4, 2].
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> [-1, 3, 2, 0]

<strong>输出:</strong> True

<strong>解释:</strong> 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
</pre>
"""


class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        