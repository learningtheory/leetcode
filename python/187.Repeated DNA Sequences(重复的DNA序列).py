"""
<p>
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.</p>

<p>Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.</p>

<p>
For example,</p>
<pre>
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
</pre><p>所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：&ldquo;ACGAATTCCG&rdquo;。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。</p>

<p>编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> s = &quot;AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT&quot;

<strong>输出:</strong> [&quot;AAAAACCCCC&quot;, &quot;CCCCCAAAAA&quot;]</pre>
<p>所有 DNA 由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：&ldquo;ACGAATTCCG&rdquo;。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。</p>

<p>编写一个函数来查找 DNA 分子中所有出现超多一次的10个字母长的序列（子串）。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> s = &quot;AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT&quot;

<strong>输出:</strong> [&quot;AAAAACCCCC&quot;, &quot;CCCCCAAAAA&quot;]</pre>
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        