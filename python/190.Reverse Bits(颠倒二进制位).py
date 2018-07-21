"""
<p>Reverse bits of a given 32 bits unsigned integer.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong> 43261596
<strong>Output:</strong> 964176192
<strong>Explanation: </strong>43261596 represented in binary as <b>00000010100101000001111010011100</b>, 
&nbsp;            return 964176192 represented in binary as <b>00111001011110000010100101000000</b>.
</pre>

<p><b>Follow up</b>:<br />
If this function is called many times, how would you optimize it?</p><p>颠倒给定的 32 位无符号整数的二进制位。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 43261596
<strong>输出:</strong> 964176192
<strong>解释: </strong>43261596 的二进制表示形式为 <strong>00000010100101000001111010011100 </strong>，
&nbsp;    返回 964176192，其二进制表示形式为 <strong>00111001011110000010100101000000 </strong>。</pre>

<p><strong>进阶</strong>:<br>
如果多次调用这个函数，你将如何优化你的算法？</p>
<p>颠倒给定的 32 位无符号整数的二进制位。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 43261596
<strong>输出:</strong> 964176192
<strong>解释: </strong>43261596 的二进制表示形式为 <strong>00000010100101000001111010011100 </strong>，
&nbsp;    返回 964176192，其二进制表示形式为 <strong>00111001011110000010100101000000 </strong>。</pre>

<p><strong>进阶</strong>:<br>
如果多次调用这个函数，你将如何优化你的算法？</p>
"""


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):