/*
<p>A matrix is <em>Toeplitz</em> if every diagonal from top-left to bottom-right has the same element.</p>

<p>Now given an <code>M x N</code> matrix, return&nbsp;<code>True</code>&nbsp;if and only if the matrix is <em>Toeplitz</em>.<br />
&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
<strong>Output:</strong> True
<strong>Explanation:</strong>
1234
5123
9512

In the above grid, the&nbsp;diagonals are &quot;[9]&quot;, &quot;[5, 5]&quot;, &quot;[1, 1, 1]&quot;, &quot;[2, 2, 2]&quot;, &quot;[3, 3]&quot;, &quot;[4]&quot;, and in each diagonal all elements are the same, so the answer is True.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> matrix = [[1,2],[2,2]]
<strong>Output:</strong> False
<strong>Explanation:</strong>
The diagonal &quot;[1, 2]&quot; has different elements.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>matrix</code> will be a 2D array of integers.</li>
	<li><code>matrix</code> will have a number of rows and columns in range <code>[1, 20]</code>.</li>
	<li><code>matrix[i][j]</code> will be integers in range <code>[0, 99]</code>.</li>
</ol>

<p>&nbsp;</p><p>如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是<em>托普利茨矩阵</em>。</p>

<p>给定一个&nbsp;<code>M x N</code>&nbsp;的矩阵，当且仅当它是<em>托普利茨矩阵</em>时返回&nbsp;<code>True</code>。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> 
matrix = [
&nbsp; [1,2,3,4],
&nbsp; [5,1,2,3],
&nbsp; [9,5,1,2]
]
<strong>输出:</strong> True
<strong>解释:</strong>
在上述矩阵中, 其对角线为:
&quot;[9]&quot;, &quot;[5, 5]&quot;, &quot;[1, 1, 1]&quot;, &quot;[2, 2, 2]&quot;, &quot;[3, 3]&quot;, &quot;[4]&quot;。
各条对角线上的所有元素均相同, 因此答案是True。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>
matrix = [
&nbsp; [1,2],
&nbsp; [2,2]
]
<strong>输出:</strong> False
<strong>解释: 
</strong>对角线&quot;[1, 2]&quot;上的元素不同。
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>&nbsp;<code>matrix</code>&nbsp;是一个包含整数的二维数组。</li>
	<li><code>matrix</code>&nbsp;的行数和列数均在&nbsp;<code>[1, 20]</code>范围内。</li>
	<li><code>matrix[i][j]</code>&nbsp;包含的整数在&nbsp;<code>[0, 99]</code>范围内。</li>
</ol>

<p><strong>进阶:</strong></p>

<ol>
	<li>如果矩阵存储在磁盘上，并且磁盘内存是有限的，因此一次最多只能将一行矩阵加载到内存中，该怎么办？</li>
	<li>如果矩阵太大以至于只能一次将部分行加载到内存中，该怎么办？</li>
</ol>
<p>如果一个矩阵的每一方向由左上到右下的对角线上具有相同元素，那么这个矩阵是<em>托普利茨矩阵</em>。</p>

<p>给定一个&nbsp;<code>M x N</code>&nbsp;的矩阵，当且仅当它是<em>托普利茨矩阵</em>时返回&nbsp;<code>True</code>。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> 
matrix = [
&nbsp; [1,2,3,4],
&nbsp; [5,1,2,3],
&nbsp; [9,5,1,2]
]
<strong>输出:</strong> True
<strong>解释:</strong>
在上述矩阵中, 其对角线为:
&quot;[9]&quot;, &quot;[5, 5]&quot;, &quot;[1, 1, 1]&quot;, &quot;[2, 2, 2]&quot;, &quot;[3, 3]&quot;, &quot;[4]&quot;。
各条对角线上的所有元素均相同, 因此答案是True。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>
matrix = [
&nbsp; [1,2],
&nbsp; [2,2]
]
<strong>输出:</strong> False
<strong>解释: 
</strong>对角线&quot;[1, 2]&quot;上的元素不同。
</pre>

<p><strong>说明:</strong></p>

<ol>
	<li>&nbsp;<code>matrix</code>&nbsp;是一个包含整数的二维数组。</li>
	<li><code>matrix</code>&nbsp;的行数和列数均在&nbsp;<code>[1, 20]</code>范围内。</li>
	<li><code>matrix[i][j]</code>&nbsp;包含的整数在&nbsp;<code>[0, 99]</code>范围内。</li>
</ol>

<p><strong>进阶:</strong></p>

<ol>
	<li>如果矩阵存储在磁盘上，并且磁盘内存是有限的，因此一次最多只能将一行矩阵加载到内存中，该怎么办？</li>
	<li>如果矩阵太大以至于只能一次将部分行加载到内存中，该怎么办？</li>
</ol>
*/


bool isToeplitzMatrix(int** matrix, int matrixRowSize, int *matrixColSizes) {
    
}