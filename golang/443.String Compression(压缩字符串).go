/*
<p>Given an array of characters, compress it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><b>in-place</b></a>.</p>

<p>The length after compression must always be smaller than or equal to the original array.</p>

<p>Every element of the array should be a <b>character</b> (not int) of length 1.</p>
 
<p>After you are done <b>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></b>, return the new length of the array.</p>

<br />

<p><b>Follow up:</b><br />
Could you solve it using only O(1) extra space?
</p>

<br />

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
["a","a","b","b","c","c","c"]

<b>Output:</b>
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

<b>Explanation:</b>
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>
["a"]

<b>Output:</b>
Return 1, and the first 1 characters of the input array should be: ["a"]

<b>Explanation:</b>
Nothing is replaced.
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b>
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

<b>Output:</b>
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

<b>Explanation:</b>
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>All characters have an ASCII value in <code>[35, 126]</code>.</li>
<li><code>1 <= len(chars) <= 1000</code>.</li>
</ol>
</p><p>给定一组字符，使用<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95">原地算法</a>将其压缩。</p>

<p>压缩后的长度必须始终小于或等于原数组长度。</p>

<p>数组的每个元素应该是长度为1&nbsp;的<strong>字符</strong>（不是 int 整数类型）。</p>

<p>在完成<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95">原地</a><strong>修改输入数组</strong>后，返回数组的新长度。</p>

<p>&nbsp;</p>

<p><strong>进阶：</strong><br />
你能否仅使用O(1) 空间解决问题？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
[&quot;a&quot;,&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]

<strong>输出：</strong>
返回6，输入数组的前6个字符应该是：[&quot;a&quot;,&quot;2&quot;,&quot;b&quot;,&quot;2&quot;,&quot;c&quot;,&quot;3&quot;]

<strong>说明：</strong>
&quot;aa&quot;被&quot;a2&quot;替代。&quot;bb&quot;被&quot;b2&quot;替代。&quot;ccc&quot;被&quot;c3&quot;替代。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>
[&quot;a&quot;]

<strong>输出：</strong>
返回1，输入数组的前1个字符应该是：[&quot;a&quot;]

<strong>说明：</strong>
没有任何字符串被替代。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>
[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;]

<strong>输出：</strong>
返回4，输入数组的前4个字符应该是：[&quot;a&quot;,&quot;b&quot;,&quot;1&quot;,&quot;2&quot;]。

<strong>说明：</strong>
由于字符&quot;a&quot;不重复，所以不会被压缩。&quot;bbbbbbbbbbbb&quot;被&ldquo;b12&rdquo;替代。
注意每个数字在数组中都有它自己的位置。
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li>所有字符都有一个ASCII值在<code>[35, 126]</code>区间内。</li>
	<li><code>1 &lt;= len(chars) &lt;= 1000</code>。</li>
</ol>
<p>给定一组字符，使用<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95">原地算法</a>将其压缩。</p>

<p>压缩后的长度必须始终小于或等于原数组长度。</p>

<p>数组的每个元素应该是长度为1&nbsp;的<strong>字符</strong>（不是 int 整数类型）。</p>

<p>在完成<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95">原地</a><strong>修改输入数组</strong>后，返回数组的新长度。</p>

<p>&nbsp;</p>

<p><strong>进阶：</strong><br />
你能否仅使用O(1) 空间解决问题？</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
[&quot;a&quot;,&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;c&quot;,&quot;c&quot;,&quot;c&quot;]

<strong>输出：</strong>
返回6，输入数组的前6个字符应该是：[&quot;a&quot;,&quot;2&quot;,&quot;b&quot;,&quot;2&quot;,&quot;c&quot;,&quot;3&quot;]

<strong>说明：</strong>
&quot;aa&quot;被&quot;a2&quot;替代。&quot;bb&quot;被&quot;b2&quot;替代。&quot;ccc&quot;被&quot;c3&quot;替代。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>
[&quot;a&quot;]

<strong>输出：</strong>
返回1，输入数组的前1个字符应该是：[&quot;a&quot;]

<strong>说明：</strong>
没有任何字符串被替代。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>
[&quot;a&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;,&quot;b&quot;]

<strong>输出：</strong>
返回4，输入数组的前4个字符应该是：[&quot;a&quot;,&quot;b&quot;,&quot;1&quot;,&quot;2&quot;]。

<strong>说明：</strong>
由于字符&quot;a&quot;不重复，所以不会被压缩。&quot;bbbbbbbbbbbb&quot;被&ldquo;b12&rdquo;替代。
注意每个数字在数组中都有它自己的位置。
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li>所有字符都有一个ASCII值在<code>[35, 126]</code>区间内。</li>
	<li><code>1 &lt;= len(chars) &lt;= 1000</code>。</li>
</ol>
*/


func compress(chars []byte) int {
    
}