/**
<p>
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.
</p>

<p>
Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
</p>

<div style="float:right"><img src="/static/images/problemset/rectangle_perfect.gif" /></div>
<p><b>Example 1:</b>
<pre>
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
</pre>
</p>

<div style="clear:both"></div>

<div style="float:right"><img src="/static/images/problemset/rectangle_separated.gif" /></div>
<p><b>Example 2:</b>
<pre>
rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
</pre>
</p>

<div style="clear:both"></div>

<div style="float:right"><img src="/static/images/problemset/rectangle_hole.gif" /></div>
<p><b>Example 3:</b>
<pre>
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
</pre>
</p>

<div style="clear:both"></div>

<div style="float:right"><img src="/static/images/problemset/rectangle_intersect.gif" /></div>
<p><b>Example 4:</b>
<pre>
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
</pre>
</p>

<div style="clear:both"></div><p>我们有 N 个与坐标轴对齐的矩形, 其中 N &gt; 0, 判断它们是否能精确地覆盖一个矩形区域。</p>

<p>每个矩形用左下角的点和右上角的点的坐标来表示。例如，&nbsp;一个单位正方形可以表示为 [1,1,2,2]。&nbsp;( 左下角的点的坐标为 (1, 1) 以及右上角的点的坐标为 (2, 2) )。</p>

<div style="float:right"><img src="https://leetcode.com/static/images/problemset/rectangle_perfect.gif" /></div>

<p><strong>示例 1:</strong>

<pre>
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

返回 true。5个矩形一起可以精确地覆盖一个矩形区域。
</pre>
</p>

<div style="clear:both"></div>

<div style="float:right"><img src="https://leetcode.com/static/images/problemset/rectangle_separated.gif" /></div>

<p><strong>示例&nbsp;2:</strong>

<pre>
rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。
</pre>
</p>

<div style="clear:both"></div>

<div style="float:right"><img src="https://leetcode.com/static/images/problemset/rectangle_hole.gif" /></div>

<p><strong>示例 3:</strong>

<pre>
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

返回 false。图形顶端留有间隔，无法覆盖成一个矩形。
</pre>
</p>

<div style="clear:both"></div>

<div style="float:right"><img src="https://leetcode.com/static/images/problemset/rectangle_intersect.gif" /></div>

<p><strong>示例 4:</strong>

<pre>
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
</pre>
</p>

<div style="clear:both"></div><p>我们有 N 个与坐标轴对齐的矩形, 其中 N &gt; 0, 判断它们是否能精确地覆盖一个矩形区域。</p>

<p>每个矩形用左下角的点和右上角的点的坐标来表示。例如，&nbsp;一个单位正方形可以表示为 [1,1,2,2]。&nbsp;( 左下角的点的坐标为 (1, 1) 以及右上角的点的坐标为 (2, 2) )。</p>

<div style="float:right"><img src="https://leetcode.com/static/images/problemset/rectangle_perfect.gif" /></div>

<p><strong>示例 1:</strong>

<pre>
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

返回 true。5个矩形一起可以精确地覆盖一个矩形区域。
</pre>
</p>

<div style="clear:both"></div>

<div style="float:right"><img src="https://leetcode.com/static/images/problemset/rectangle_separated.gif" /></div>

<p><strong>示例&nbsp;2:</strong>

<pre>
rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。
</pre>
</p>

<div style="clear:both"></div>

<div style="float:right"><img src="https://leetcode.com/static/images/problemset/rectangle_hole.gif" /></div>

<p><strong>示例 3:</strong>

<pre>
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

返回 false。图形顶端留有间隔，无法覆盖成一个矩形。
</pre>
</p>

<div style="clear:both"></div>

<div style="float:right"><img src="https://leetcode.com/static/images/problemset/rectangle_intersect.gif" /></div>

<p><strong>示例 4:</strong>

<pre>
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
</pre>
</p>

<div style="clear:both"></div>**/


class Solution {
    public boolean isRectangleCover(int[][] rectangles) {
        
    }
}