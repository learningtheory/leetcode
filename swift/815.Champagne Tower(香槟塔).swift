/*
<p>We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.&nbsp; Each glass holds one cup (250ml) of champagne.</p>

<p>Then, some champagne is poured in the first glass at the top.&nbsp; When the top most glass is full, any excess liquid poured will fall equally to the glass immediately to the left and right of it.&nbsp; When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.&nbsp; (A glass at the bottom row has it&#39;s excess champagne fall on the floor.)</p>

<p>For example, after one cup of champagne is poured, the top most glass is full.&nbsp; After two cups of champagne are poured, the two glasses on the second row are half full.&nbsp; After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.&nbsp; After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png" style="height:200px; width:290px" /></p>

<p>Now after pouring some non-negative integer cups of champagne, return how full the j-th glass in the i-th row is (both i and j are 0 indexed.)</p>

<p>&nbsp;</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> poured = 1, query_glass = 1, query_row = 1
<strong>Output:</strong> 0.0
<strong>Explanation:</strong> We poured 1 cup of champange to the top glass of the tower (which is indexed as (0, 0)). There will be no excess liquid so all the glasses under the top glass will remain empty.

<strong>Example 2:</strong>
<strong>Input:</strong> poured = 2, query_glass = 1, query_row = 1
<strong>Output:</strong> 0.5
<strong>Explanation:</strong> We poured 2 cups of champange to the top glass of the tower (which is indexed as (0, 0)). There is one cup of excess liquid. The glass indexed as (1, 0) and the glass indexed as (1, 1) will share the excess liquid equally, and each will get half cup of champange.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>poured</code>&nbsp;will&nbsp;be&nbsp;in the range of <code>[0, 10 ^ 9]</code>.</li>
	<li><code>query_glass</code> and <code>query_row</code> will be in the range of <code>[0, 99]</code>.</li>
</ul>

<p>&nbsp;</p>
<p>我们把玻璃杯摆成金字塔的形状，其中第一层有1个玻璃杯，第二层有2个，依次类推到第100层，每个玻璃杯(250ml)将盛有香槟。</p>

<p>从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等流量的流向左右两侧的玻璃杯。当左右两边的杯子也满了，就会等流量的流向它们左右两边的杯子，依次类推。（当最底层的玻璃杯满了，香槟会流到地板上）</p>

<p>例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯各自盛放一半的香槟。在倒三杯香槟后，第二层的香槟满了 - 此时总共有三个满的玻璃杯。在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之一的香槟，如下图所示。</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png" style="height:200px; width:290px" /></p>

<p>现在当倾倒了非负整数杯香槟后，返回第 i 行 j 个玻璃杯所盛放的香槟占玻璃杯容积的比例（i 和 j都从0开始）。</p>

<p>&nbsp;</p>

<pre>
<strong>示例 1:</strong>
<strong>输入:</strong> poured(倾倒香槟总杯数) = 1, query_glass(杯子的位置数) = 1, query_row(行数) = 1
<strong>输出:</strong> 0.0
<strong>解释:</strong> 我们在顶层（下标是（0，0））倒了一杯香槟后，没有溢出，因此所有在顶层以下的玻璃杯都是空的。

<strong>示例 2:</strong>
<strong>输入:</strong> poured(倾倒香槟总杯数) = 2, query_glass(杯子的位置数) = 1, query_row(行数) = 1
<strong>输出:</strong> 0.5
<strong>解释:</strong> 我们在顶层（下标是（0，0）倒了两杯香槟后，有一杯量的香槟将从顶层溢出，位于（1，0）的玻璃杯和（1，1）的玻璃杯平分了这一杯香槟，所以每个玻璃杯有一半的香槟。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>poured</code>&nbsp;的范围<code>[0, 10 ^ 9]</code>。</li>
	<li><code>query_glass</code>&nbsp;和<code>query_row</code>&nbsp;的范围&nbsp;<code>[0, 99]</code>。</li>
</ul>
<p>我们把玻璃杯摆成金字塔的形状，其中第一层有1个玻璃杯，第二层有2个，依次类推到第100层，每个玻璃杯(250ml)将盛有香槟。</p>

<p>从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等流量的流向左右两侧的玻璃杯。当左右两边的杯子也满了，就会等流量的流向它们左右两边的杯子，依次类推。（当最底层的玻璃杯满了，香槟会流到地板上）</p>

<p>例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯各自盛放一半的香槟。在倒三杯香槟后，第二层的香槟满了 - 此时总共有三个满的玻璃杯。在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之一的香槟，如下图所示。</p>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png" style="height:200px; width:290px" /></p>

<p>现在当倾倒了非负整数杯香槟后，返回第 i 行 j 个玻璃杯所盛放的香槟占玻璃杯容积的比例（i 和 j都从0开始）。</p>

<p>&nbsp;</p>

<pre>
<strong>示例 1:</strong>
<strong>输入:</strong> poured(倾倒香槟总杯数) = 1, query_glass(杯子的位置数) = 1, query_row(行数) = 1
<strong>输出:</strong> 0.0
<strong>解释:</strong> 我们在顶层（下标是（0，0））倒了一杯香槟后，没有溢出，因此所有在顶层以下的玻璃杯都是空的。

<strong>示例 2:</strong>
<strong>输入:</strong> poured(倾倒香槟总杯数) = 2, query_glass(杯子的位置数) = 1, query_row(行数) = 1
<strong>输出:</strong> 0.5
<strong>解释:</strong> 我们在顶层（下标是（0，0）倒了两杯香槟后，有一杯量的香槟将从顶层溢出，位于（1，0）的玻璃杯和（1，1）的玻璃杯平分了这一杯香槟，所以每个玻璃杯有一半的香槟。
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>poured</code>&nbsp;的范围<code>[0, 10 ^ 9]</code>。</li>
	<li><code>query_glass</code>&nbsp;和<code>query_row</code>&nbsp;的范围&nbsp;<code>[0, 99]</code>。</li>
</ul>
*/


class Solution {
    func champagneTower(_ poured: Int, _ query_row: Int, _ query_glass: Int) -> Double {
        
    }
}