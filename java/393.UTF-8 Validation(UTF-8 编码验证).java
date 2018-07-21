/**
<p>A character in UTF8 can be from <b>1 to 4 bytes</b> long, subjected to the following rules:</p>
<ol>
<li>For 1-byte character, the first bit is a 0, followed by its unicode code.</li>
<li>For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.</li>
</ol>
<p>This is how the UTF-8 encoding would work:</p>

<pre><code>   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
</code></pre>
<p>
Given an array of integers representing the data, return whether it is a valid utf-8 encoding.
</p>
<p>
<b>Note:</b><br />
The input is an array of integers. Only the <b>least significant 8 bits</b> of each integer is used to store the data. This means each integer represents only 1 byte of data.
</p>

<p>
<b>Example 1:</b>
<pre>
data = [197, 130, 1], which represents the octet sequence: <b>11000101 10000010 00000001</b>.

Return <b>true</b>.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
</pre>
</p>

<p>
<b>Example 2:</b>
<pre>
data = [235, 140, 4], which represented the octet sequence: <b>11101011 10001100 00000100</b>.

Return <b>false</b>.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
</pre>
</p><p>UTF-8 中的一个字符可能的长度为 <strong>1 到 4 字节</strong>，遵循以下的规则：</p>

<ol>
	<li>对于 1 字节的字符，字节的第一位设为0，后面7位为这个符号的unicode码。</li>
	<li>对于 n 字节的字符 (n &gt; 1)，第一个字节的前 n 位都设为1，第 n+1 位设为0，后面字节的前两位一律设为10。剩下的没有提及的二进制位，全部为这个符号的unicode码。</li>
</ol>

<p>这是 UTF-8 编码的工作方式：</p>

<pre>
<code>   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
</code></pre>

<p>给定一个表示数据的整数数组，返回它是否为有效的 utf-8 编码。</p>

<p><strong>注意:</strong><br />
输入是整数数组。只有每个整数的<strong>最低 8 个有效位</strong>用来存储数据。这意味着每个整数只表示 1 字节的数据。</p>

<p><strong>示例 1:</strong></p>

<pre>
data = [197, 130, 1], 表示 8 位的序列: <strong>11000101 10000010 00000001</strong>.

返回 <strong>true </strong>。
这是有效的 utf-8 编码，为一个2字节字符，跟着一个1字节字符。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
data = [235, 140, 4], 表示 8 位的序列: <strong>11101011 10001100 00000100</strong>.

返回<strong> false</strong> 。
前 3 位都是 1 ，第 4 位为 0 表示它是一个3字节字符。
下一个字节是开头为 10 的延续字节，这是正确的。
但第二个延续字节不以 10 开头，所以是不符合规则的。
</pre>
<p>UTF-8 中的一个字符可能的长度为 <strong>1 到 4 字节</strong>，遵循以下的规则：</p>

<ol>
	<li>对于 1 字节的字符，字节的第一位设为0，后面7位为这个符号的unicode码。</li>
	<li>对于 n 字节的字符 (n &gt; 1)，第一个字节的前 n 位都设为1，第 n+1 位设为0，后面字节的前两位一律设为10。剩下的没有提及的二进制位，全部为这个符号的unicode码。</li>
</ol>

<p>这是 UTF-8 编码的工作方式：</p>

<pre>
<code>   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
</code></pre>

<p>给定一个表示数据的整数数组，返回它是否为有效的 utf-8 编码。</p>

<p><strong>注意:</strong><br />
输入是整数数组。只有每个整数的<strong>最低 8 个有效位</strong>用来存储数据。这意味着每个整数只表示 1 字节的数据。</p>

<p><strong>示例 1:</strong></p>

<pre>
data = [197, 130, 1], 表示 8 位的序列: <strong>11000101 10000010 00000001</strong>.

返回 <strong>true </strong>。
这是有效的 utf-8 编码，为一个2字节字符，跟着一个1字节字符。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
data = [235, 140, 4], 表示 8 位的序列: <strong>11101011 10001100 00000100</strong>.

返回<strong> false</strong> 。
前 3 位都是 1 ，第 4 位为 0 表示它是一个3字节字符。
下一个字节是开头为 10 的延续字节，这是正确的。
但第二个延续字节不以 10 开头，所以是不符合规则的。
</pre>
**/


class Solution {
    public boolean validUtf8(int[] data) {
        
    }
}