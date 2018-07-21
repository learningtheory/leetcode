/**
<p>
A magical string <b>S</b> consists of only '1' and '2' and obeys the following rules:
</p>
<p>
The string <b>S</b> is magical because concatenating the number of contiguous occurrences of characters '1' and '2' generates the string <b>S</b> itself.
</p>

<p>
The first few elements of string <b>S</b> is the following:
<b>S</b> = "1221121221221121122……"
</p>

<p>
If we group the consecutive '1's and '2's in <b>S</b>, it will be:
</p>
<p>
1   22  11  2  1  22  1  22  11  2  11  22 ......
</p>
<p>
and the occurrences of '1's or '2's in each group are:
</p>
<p>
1   2	   2    1   1    2     1    2     2    1    2    2 ......
</p>

<p>
You can see that the occurrence sequence above is the <b>S</b> itself. 
</p>

<p>
Given an integer N as input, return the number of '1's in the first N number in the magical string <b>S</b>.
</p>

<p><b>Note:</b>
N will not exceed 100,000.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 6
<b>Output:</b> 3
<b>Explanation:</b> The first 6 elements of magical string S is "12211" and it contains three 1's, so return 3.
</pre>
</p><p>神奇的字符串&nbsp;<strong>S&nbsp;</strong>只包含 &#39;1&#39; 和 &#39;2&#39;，并遵守以下规则：</p>

<p>字符串 <strong>S</strong> 是神奇的，因为串联字符 &#39;1&#39; 和 &#39;2&#39; 的连续出现次数会生成字符串 <strong>S</strong> 本身。</p>

<p>字符串&nbsp;<strong>S&nbsp;</strong>的前几个元素如下：<strong>S </strong>= &ldquo;1221121221221121122 ......&rdquo;</p>

<p>如果我们将&nbsp;<strong>S</strong> 中连续的 1 和 2 进行分组，它将变成：</p>

<p>1 22 11 2 1 22 1 22 11 2 11 22 ......</p>

<p>并且每个组中 &#39;1&#39; 或 &#39;2&#39; 的出现次数分别是：</p>

<p>1 2 2 1 1 2 1 2 2 1 2 2 ......</p>

<p>你可以看到上面的出现次数就是 <strong>S</strong> 本身。</p>

<p>给定一个整数 N 作为输入，返回神奇字符串 <strong>S&nbsp;</strong>中前 N 个数字中的 &#39;1&#39; 的数目。</p>

<p><strong>注意：</strong>N 不会超过 100,000。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>6
<strong>输出：</strong>3
<strong>解释：</strong>神奇字符串 S 的前 6 个元素是 &ldquo;12211&rdquo;，它包含三个 1，因此返回 3。
</pre>

<p>&nbsp;</p>
<p>神奇的字符串&nbsp;<strong>S&nbsp;</strong>只包含 &#39;1&#39; 和 &#39;2&#39;，并遵守以下规则：</p>

<p>字符串 <strong>S</strong> 是神奇的，因为串联字符 &#39;1&#39; 和 &#39;2&#39; 的连续出现次数会生成字符串 <strong>S</strong> 本身。</p>

<p>字符串&nbsp;<strong>S&nbsp;</strong>的前几个元素如下：<strong>S </strong>= &ldquo;1221121221221121122 ......&rdquo;</p>

<p>如果我们将&nbsp;<strong>S</strong> 中连续的 1 和 2 进行分组，它将变成：</p>

<p>1 22 11 2 1 22 1 22 11 2 11 22 ......</p>

<p>并且每个组中 &#39;1&#39; 或 &#39;2&#39; 的出现次数分别是：</p>

<p>1 2 2 1 1 2 1 2 2 1 2 2 ......</p>

<p>你可以看到上面的出现次数就是 <strong>S</strong> 本身。</p>

<p>给定一个整数 N 作为输入，返回神奇字符串 <strong>S&nbsp;</strong>中前 N 个数字中的 &#39;1&#39; 的数目。</p>

<p><strong>注意：</strong>N 不会超过 100,000。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>6
<strong>输出：</strong>3
<strong>解释：</strong>神奇字符串 S 的前 6 个元素是 &ldquo;12211&rdquo;，它包含三个 1，因此返回 3。
</pre>

<p>&nbsp;</p>
**/


class Solution {
    fun magicalString(n: Int): Int {
        
    }
}