/*
<p>A sequence of numbers is called a <strong>wiggle sequence</strong> if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence. </p>

<p>For example, <code>[1,7,4,9,2,5]</code> is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, <code>[1,4,7,2,5]</code> and <code>[1,7,4,5,5]</code> are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.</p>

<p>Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.</p>

<p><b>Examples:</b><br />
<pre>
<b>Input:</b> [1,7,4,9,2,5]
<b>Output:</b> 6
The entire sequence is a wiggle sequence.

<b>Input:</b> [1,17,5,10,13,15,10,5,16,8]
<b>Output:</b> 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

<b>Input:</b> [1,2,3,4,5,6,7,8,9]
<b>Output:</b> 2
</pre>
</p>

<p><b>Follow up:</b><br />
Can you do it in O(<i>n</i>) time?
</p>

<p><b>Credits:</b><br />Special thanks to <a href="https://leetcode.com/agave/">@agave</a> and <a href="https://leetcode.com/stefanpochmann/">@StefanPochmann</a> for adding this problem and creating all test cases.</p><p>如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为<strong>摆动序列。</strong>第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。</p>

<p>例如，&nbsp;<code>[1,7,4,9,2,5]</code> 是一个摆动序列，因为差值 <code>(6,-3,5,-7,3)</code>&nbsp;是正负交替出现的。相反, <code>[1,4,7,2,5]</code>&nbsp;和&nbsp;<code>[1,7,4,5,5]</code> 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。</p>

<p>给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> [1,7,4,9,2,5]
<strong>输出:</strong> 6
<strong>解释:</strong> 整个序列就是一个摆动序列。

<strong>输入:</strong> [1,17,5,10,13,15,10,5,16,8]
<strong>输出:</strong> 7
<strong>解释: </strong>它的几个子序列满足摆动序列。其中一个是[1,17,10,13,10,16,8]。

<strong>输入:</strong> [1,2,3,4,5,6,7,8,9]
<strong>输出:</strong> 2
</pre>

<p><strong>进阶:</strong><br />
你能否用&nbsp;O(<em>n</em>) 时间复杂度完成此题?</p>
<p>如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为<strong>摆动序列。</strong>第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。</p>

<p>例如，&nbsp;<code>[1,7,4,9,2,5]</code> 是一个摆动序列，因为差值 <code>(6,-3,5,-7,3)</code>&nbsp;是正负交替出现的。相反, <code>[1,4,7,2,5]</code>&nbsp;和&nbsp;<code>[1,7,4,5,5]</code> 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。</p>

<p>给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序。</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> [1,7,4,9,2,5]
<strong>输出:</strong> 6
<strong>解释:</strong> 整个序列就是一个摆动序列。

<strong>输入:</strong> [1,17,5,10,13,15,10,5,16,8]
<strong>输出:</strong> 7
<strong>解释: </strong>它的几个子序列满足摆动序列。其中一个是[1,17,10,13,10,16,8]。

<strong>输入:</strong> [1,2,3,4,5,6,7,8,9]
<strong>输出:</strong> 2
</pre>

<p><strong>进阶:</strong><br />
你能否用&nbsp;O(<em>n</em>) 时间复杂度完成此题?</p>
*/


class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        
    }
};