/*
<p>A city&#39;s skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are <b>given the locations and height of all the buildings</b> as shown on a cityscape photo (Figure A), write a program to <b>output the skyline</b> formed by these buildings collectively (Figure B).</p>
<!-- Cityscape --><a href="/static/images/problemset/skyline1.jpg" target="_blank"><img alt="Buildings" border="0" src="/static/images/problemset/skyline1.jpg" style=" max-width: 45%;" /> </a> <!-- Use this image for the 'turning point' description of skyline --> <a href="/static/images/problemset/skyline2.jpg" target="_blank"> <img alt="Skyline Contour" border="0" src="/static/images/problemset/skyline2.jpg" style="max-width: 45%;" /> </a> <!-- Use the following image if we'd like to define the output as 'horizontal lines' rather than 'turning points'--> <!--
<a href="http://tinypic.com?ref=mij3wi" target="_blank">
<img style="max-width: 45%;" src="http://i59.tinypic.com/mij3wi.jpg" border="0" alt="Skyline Contour">
</a>
-->

<p>The geometric information of each building is represented by a triplet of integers <code>[Li, Ri, Hi]</code>, where <code>Li</code> and <code>Ri</code> are the x coordinates of the left and right edge of the ith building, respectively, and <code>Hi</code> is its height. It is guaranteed that <code>0 &le; Li, Ri &le; INT_MAX</code>, <code>0 &lt; Hi &le; INT_MAX</code>, and <code>Ri - Li &gt; 0</code>. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.</p>

<p>For instance, the dimensions of all buildings in Figure A are recorded as: <code>[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] </code>.</p>

<p>The output is a list of &quot;<b>key points</b>&quot; (red dots in Figure B) in the format of <code>[ [x1,y1], [x2, y2], [x3, y3], ... ]</code> that uniquely defines a skyline. <b>A key point is the left endpoint of a horizontal line segment</b>. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.</p>

<p>For instance, the skyline in Figure B should be represented as:<code>[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]</code>.</p>

<p><b>Notes:</b></p>

<ul>
	<li>The number of buildings in any input list is guaranteed to be in the range <code>[0, 10000]</code>.</li>
	<li>The input list is already sorted in ascending order by the left x position <code>Li</code>.</li>
	<li>The output list must be sorted by the x position.</li>
	<li>There must be no consecutive horizontal lines of equal height in the output skyline. For instance, <code>[...[2 3], [4 5], [7 5], [11 5], [12 7]...]</code> is not acceptable; the three lines of height 5 should be merged into one in the final output as such: <code>[...[2 3], [4 5], [12 7], ...]</code></li>
</ul>
<p>城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。现在，假设您获得了城市风光照片（图A）上<strong>显示的所有建筑物的位置和高度</strong>，请编写一个程序以输出由这些建筑物<strong>形成的天际线</strong>（图B）。</p>

<!-- Cityscape -->
<a href="/static/images/problemset/skyline1.jpg" target="_blank">
    <img style=" max-width: 45%;" src="/static/images/problemset/skyline1.jpg" border="0" alt="Buildings">
</a>

<!-- Use this image for the 'turning point' description of skyline -->
<a href="/static/images/problemset/skyline2.jpg" target="_blank">
    <img style="max-width: 45%;" src="/static/images/problemset/skyline2.jpg" border="0" alt="Skyline Contour">
</a>

<!-- Use the following image if we'd like to define the output as 'horizontal lines' rather than 'turning points'-->
<!--
<a href="http://tinypic.com?ref=mij3wi" target="_blank">
<img style="max-width: 45%;" src="http://i59.tinypic.com/mij3wi.jpg" border="0" alt="Skyline Contour">
</a>
-->

<p>每个建筑物的几何信息用三元组&nbsp;<code>[Li，Ri，Hi]</code> 表示，其中 <code>Li</code> 和 <code>Ri</code> 分别是第 i 座建筑物左右边缘的 x 坐标，<code>Hi</code> 是其高度。可以保证&nbsp;<code>0 &le; Li, Ri &le; INT_MAX</code>,&nbsp;<code>0 &lt; Hi &le; INT_MAX</code> 和 <code>Ri - Li &gt; 0</code>。您可以假设所有建筑物都是在绝对平坦且高度为 0 的表面上的完美矩形。</p>

<p>例如，图A中所有建筑物的尺寸记录为：<code>[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] </code>。</p>

<p>输出是以&nbsp;<code>[ [x1,y1], [x2, y2], [x3, y3], ... ]</code> 格式的&ldquo;<strong>关键点</strong>&rdquo;（图B中的红点）的列表，它们唯一地定义了天际线。<strong>关键点是水平线段的左端点</strong>。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。</p>

<p>例如，图B中的天际线应该表示为：<code>[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]</code>。</p>

<p><strong>说明:</strong></p>

<ul>
	<li>任何输入列表中的建筑物数量保证在 <code>[0, 10000]</code>&nbsp;范围内。</li>
	<li>输入列表已经按升序排列在左边的 x 位置 <code>Li</code> 。</li>
	<li>输出列表必须按 x 位排序。</li>
	<li>输出天际线中不得有连续的相同高度的水平线。例如 <code>[...[2 3], [4 5], [7 5], [11 5], [12 7]...]</code> 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：<code>[...[2 3], [4 5], [12 7], ...]</code></li>
</ul><p>城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。现在，假设您获得了城市风光照片（图A）上<strong>显示的所有建筑物的位置和高度</strong>，请编写一个程序以输出由这些建筑物<strong>形成的天际线</strong>（图B）。</p>

<!-- Cityscape -->
<a href="/static/images/problemset/skyline1.jpg" target="_blank">
    <img style=" max-width: 45%;" src="/static/images/problemset/skyline1.jpg" border="0" alt="Buildings">
</a>

<!-- Use this image for the 'turning point' description of skyline -->
<a href="/static/images/problemset/skyline2.jpg" target="_blank">
    <img style="max-width: 45%;" src="/static/images/problemset/skyline2.jpg" border="0" alt="Skyline Contour">
</a>

<!-- Use the following image if we'd like to define the output as 'horizontal lines' rather than 'turning points'-->
<!--
<a href="http://tinypic.com?ref=mij3wi" target="_blank">
<img style="max-width: 45%;" src="http://i59.tinypic.com/mij3wi.jpg" border="0" alt="Skyline Contour">
</a>
-->

<p>每个建筑物的几何信息用三元组&nbsp;<code>[Li，Ri，Hi]</code> 表示，其中 <code>Li</code> 和 <code>Ri</code> 分别是第 i 座建筑物左右边缘的 x 坐标，<code>Hi</code> 是其高度。可以保证&nbsp;<code>0 &le; Li, Ri &le; INT_MAX</code>,&nbsp;<code>0 &lt; Hi &le; INT_MAX</code> 和 <code>Ri - Li &gt; 0</code>。您可以假设所有建筑物都是在绝对平坦且高度为 0 的表面上的完美矩形。</p>

<p>例如，图A中所有建筑物的尺寸记录为：<code>[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] </code>。</p>

<p>输出是以&nbsp;<code>[ [x1,y1], [x2, y2], [x3, y3], ... ]</code> 格式的&ldquo;<strong>关键点</strong>&rdquo;（图B中的红点）的列表，它们唯一地定义了天际线。<strong>关键点是水平线段的左端点</strong>。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。</p>

<p>例如，图B中的天际线应该表示为：<code>[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]</code>。</p>

<p><strong>说明:</strong></p>

<ul>
	<li>任何输入列表中的建筑物数量保证在 <code>[0, 10000]</code>&nbsp;范围内。</li>
	<li>输入列表已经按升序排列在左边的 x 位置 <code>Li</code> 。</li>
	<li>输出列表必须按 x 位排序。</li>
	<li>输出天际线中不得有连续的相同高度的水平线。例如 <code>[...[2 3], [4 5], [7 5], [11 5], [12 7]...]</code> 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：<code>[...[2 3], [4 5], [12 7], ...]</code></li>
</ul>*/


class Solution {
    func getSkyline(_ buildings: [[Int]]) -> [[Int]] {
        
    }
}