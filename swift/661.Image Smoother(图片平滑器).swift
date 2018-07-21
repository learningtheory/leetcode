/*
<p>Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.  If a cell has less than 8 surrounding cells, then use as many as you can.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
[[1,1,1],
 [1,0,1],
 [1,1,1]]
<b>Output:</b>
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
<b>Explanation:</b>
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The value in the given matrix is in the range of [0, 255].</li>
<li>The length and width of the given matrix are in the range of [1, 150].</li>
</ol>
</p><p>包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度&nbsp;(向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong>
[[1,1,1],
 [1,0,1],
 [1,1,1]]
<strong>输出:</strong>
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
<strong>解释:</strong>
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>给定矩阵中的整数范围为 [0, 255]。</li>
	<li>矩阵的长和宽的范围均为&nbsp;[1, 150]。</li>
</ol>
<p>包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度&nbsp;(向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong>
[[1,1,1],
 [1,0,1],
 [1,1,1]]
<strong>输出:</strong>
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
<strong>解释:</strong>
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>给定矩阵中的整数范围为 [0, 255]。</li>
	<li>矩阵的长和宽的范围均为&nbsp;[1, 150]。</li>
</ol>
*/


class Solution {
    func imageSmoother(_ M: [[Int]]) -> [[Int]] {
        
    }
}