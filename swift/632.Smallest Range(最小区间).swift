/*
<p>You have <code>k</code> lists of sorted integers in ascending order. Find the <b>smallest</b> range that includes at least one number from each of the <code>k</code> lists. </p>

<p>We define the range [a,b] is smaller than range [c,d] if <code>b-a < d-c</code> or <code>a < c</code> if <code>b-a == d-c</code>.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
<b>Output:</b> [20,24]
<b>Explanation:</b> 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
</pre>
</p>

<p>
<b>Note:</b><br/>
<ol>
<li>The given list may contain duplicates, so ascending order means >= here.</li>
<li>1 <= <code>k</code> <= 3500</li>
<li> -10<sup>5</sup> <= <code>value of elements</code> <= 10<sup>5</sup>.</li>
<li><b>For Java users, please note that the input type has been changed to List&lt;List&lt;Integer&gt;&gt;. And after you reset the code template, you'll see this point.</b></li>
</ol>
<br/>
</p><p>你有&nbsp;<code>k</code>&nbsp;个升序排列的整数数组。找到一个<strong>最小</strong>区间，使得&nbsp;<code>k</code>&nbsp;个列表中的每个列表至少有一个数包含在其中。</p>

<p>我们定义如果&nbsp;<code>b-a &lt; d-c</code>&nbsp;或者在&nbsp;<code>b-a == d-c</code>&nbsp;时&nbsp;<code>a &lt; c</code>，则区间 [a,b] 比 [c,d] 小。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong>[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
<strong>输出:</strong> [20,24]
<strong>解释:</strong> 
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>给定的列表可能包含重复元素，所以在这里升序表示 &gt;= 。</li>
	<li>1 &lt;= <code>k</code> &lt;= 3500</li>
	<li>-10<sup>5</sup> &lt;= <code>元素的值</code>&nbsp;&lt;= 10<sup>5</sup></li>
	<li><strong>对于使用Java的用户，请注意传入类型已修改为List&lt;List&lt;Integer&gt;&gt;。重置代码模板后可以看到这项改动。</strong></li>
</ol>
<p>你有&nbsp;<code>k</code>&nbsp;个升序排列的整数数组。找到一个<strong>最小</strong>区间，使得&nbsp;<code>k</code>&nbsp;个列表中的每个列表至少有一个数包含在其中。</p>

<p>我们定义如果&nbsp;<code>b-a &lt; d-c</code>&nbsp;或者在&nbsp;<code>b-a == d-c</code>&nbsp;时&nbsp;<code>a &lt; c</code>，则区间 [a,b] 比 [c,d] 小。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong>[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
<strong>输出:</strong> [20,24]
<strong>解释:</strong> 
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>给定的列表可能包含重复元素，所以在这里升序表示 &gt;= 。</li>
	<li>1 &lt;= <code>k</code> &lt;= 3500</li>
	<li>-10<sup>5</sup> &lt;= <code>元素的值</code>&nbsp;&lt;= 10<sup>5</sup></li>
	<li><strong>对于使用Java的用户，请注意传入类型已修改为List&lt;List&lt;Integer&gt;&gt;。重置代码模板后可以看到这项改动。</strong></li>
</ol>
*/


class Solution {
    func smallestRange(_ nums: [[Int]]) -> [Int] {
        
    }
}