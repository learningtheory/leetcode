/*
<p>A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.</p>

<p>For example, these are arithmetic sequence:</p>
<pre>1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9</pre>

<p>The following sequence is not arithmetic.</p> <pre>1, 1, 2, 5, 7</pre> 
<br/>

<p>A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.</p>

<p>A slice (P, Q) of array A is called arithmetic if the sequence:<br/>
    A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.</p>

<p>The function should return the number of arithmetic slices in the array A. </p>
<br/>

<p><b>Example:</b>
<pre>
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
</pre><p>如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。</p>

<p>例如，以下数列为等差数列:</p>

<pre>
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9</pre>

<p>以下数列不是等差数列。</p>

<pre>
1, 1, 2, 5, 7</pre>

<p>&nbsp;</p>

<p>数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0&lt;=P&lt;Q&lt;N 。</p>

<p>如果满足以下条件，则称子数组(P, Q)为等差数组：</p>

<p>元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且&nbsp;P + 1 &lt; Q 。</p>

<p>函数要返回数组 A 中所有为等差数组的子数组个数。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre>
A = [1, 2, 3, 4]

返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
</pre>
<p>如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。</p>

<p>例如，以下数列为等差数列:</p>

<pre>
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9</pre>

<p>以下数列不是等差数列。</p>

<pre>
1, 1, 2, 5, 7</pre>

<p>&nbsp;</p>

<p>数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0&lt;=P&lt;Q&lt;N 。</p>

<p>如果满足以下条件，则称子数组(P, Q)为等差数组：</p>

<p>元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且&nbsp;P + 1 &lt; Q 。</p>

<p>函数要返回数组 A 中所有为等差数组的子数组个数。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre>
A = [1, 2, 3, 4]

返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。
</pre>
*/


int numberOfArithmeticSlices(int* A, int ASize) {
    
}