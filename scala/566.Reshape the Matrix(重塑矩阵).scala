/**
<p>In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.
</p>

<p>
You're given a matrix represented by a two-dimensional array, and two <b>positive</b> integers <b>r</b> and <b>c</b> representing the <b>row</b> number and <b>column</b> number of the wanted reshaped matrix, respectively.</p>

 <p>The reshaped matrix need to be filled with all the elements of the original matrix in the same <b>row-traversing</b> order as they were.
</p>

<p>
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
<b>Output:</b> 
[[1,2,3,4]]
<b>Explanation:</b><br>The <b>row-traversing</b> of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
<b>Output:</b> 
[[1,2],
 [3,4]]
<b>Explanation:</b><br>There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The height and width of the given matrix is in range [1, 100].</li>
<li>The given r and c are all positive.</li>
</ol>
</p><p>在MATLAB中，有一个非常有用的函数 <code>reshape</code>，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。</p>

<p>给出一个由二维数组表示的矩阵，以及两个正整数<code>r</code>和<code>c</code>，分别表示想要的重构的矩阵的行数和列数。</p>

<p>重构后的矩阵需要将原始矩阵的所有元素以相同的<strong>行遍历顺序</strong>填充。</p>

<p>如果具有给定参数的<code>reshape</code>操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
<strong>输出:</strong> 
[[1,2,3,4]]
<strong>解释:</strong>
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
<strong>输出:</strong> 
[[1,2],
 [3,4]]
<strong>解释:</strong>
没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li>给定矩阵的宽和高范围在 [1, 100]。</li>
	<li>给定的 r 和 c 都是正数。</li>
</ol>
<p>在MATLAB中，有一个非常有用的函数 <code>reshape</code>，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。</p>

<p>给出一个由二维数组表示的矩阵，以及两个正整数<code>r</code>和<code>c</code>，分别表示想要的重构的矩阵的行数和列数。</p>

<p>重构后的矩阵需要将原始矩阵的所有元素以相同的<strong>行遍历顺序</strong>填充。</p>

<p>如果具有给定参数的<code>reshape</code>操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
<strong>输出:</strong> 
[[1,2,3,4]]
<strong>解释:</strong>
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
<strong>输出:</strong> 
[[1,2],
 [3,4]]
<strong>解释:</strong>
没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li>给定矩阵的宽和高范围在 [1, 100]。</li>
	<li>给定的 r 和 c 都是正数。</li>
</ol>
**/


object Solution {
    def matrixReshape(nums: Array[Array[Int]], r: Int, c: Int): Array[Array[Int]] = {
        
    }
}