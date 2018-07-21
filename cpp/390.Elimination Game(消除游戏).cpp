/*
<p>
There is a list of sorted integers from 1 to <i>n</i>. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.</p>

<p>Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.</p>

<p>We keep repeating the steps again, alternating left to right and right to left, until a single number remains.</p>

<p>Find the last number that remains starting with a list of length <i>n</i>.</p>

<p><b>Example:</b>
<pre>
Input:
n = 9,
<u>1</u> 2 <u>3</u> 4 <u>5</u> 6 <u>7</u> 8 <u>9</u>
2 <u>4</u> 6 <u>8</u>
<u>2</u> 6
6

Output:
6
</pre>
</p><p>给定一个从1 到 n 排序的整数列表。<br />
首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。<br />
第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。<br />
我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。<br />
返回长度为 n 的列表中，最后剩下的数字。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入:</strong>
n = 9,
<u>1</u> 2 <u>3</u> 4 <u>5</u> 6 <u>7</u> 8 <u>9</u>
2 <u>4</u> 6 <u>8</u>
<u>2</u> 6
6

<strong>输出:</strong>
6</pre>
<p>给定一个从1 到 n 排序的整数列表。<br />
首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。<br />
第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。<br />
我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。<br />
返回长度为 n 的列表中，最后剩下的数字。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入:</strong>
n = 9,
<u>1</u> 2 <u>3</u> 4 <u>5</u> 6 <u>7</u> 8 <u>9</u>
2 <u>4</u> 6 <u>8</u>
<u>2</u> 6
6

<strong>输出:</strong>
6</pre>
*/


class Solution {
public:
    int lastRemaining(int n) {
        
    }
};