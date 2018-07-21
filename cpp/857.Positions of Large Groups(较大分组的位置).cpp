/*
<p>In a string&nbsp;<code>S</code>&nbsp;of lowercase letters, these letters form consecutive groups of the same character.</p>

<p>For example, a string like <code>S = &quot;abbxxxxzyy&quot;</code> has the groups <code>&quot;a&quot;</code>, <code>&quot;bb&quot;</code>, <code>&quot;xxxx&quot;</code>, <code>&quot;z&quot;</code> and&nbsp;<code>&quot;yy&quot;</code>.</p>

<p>Call a group <em>large</em> if it has 3 or more characters.&nbsp; We would like the starting and ending positions of every large group.</p>

<p>The final answer should be in lexicographic order.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>&quot;abbxxxxzzy&quot;
<strong>Output: </strong>[[3,6]]
<strong>Explanation</strong>: <code>&quot;xxxx&quot; is the single </code>large group with starting  3 and ending positions 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>&quot;abc&quot;
<strong>Output: </strong>[]
<strong>Explanation</strong>: We have &quot;a&quot;,&quot;b&quot; and &quot;c&quot; but no large group.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>&quot;abcdddeeeeaabbbcd&quot;
<strong>Output: </strong>[[3,5],[6,9],[12,14]]</pre>

<p>&nbsp;</p>

<p><strong>Note:&nbsp;</strong>&nbsp;<code>1 &lt;= S.length &lt;= 1000</code></p><p>在一个由小写字母构成的字符串&nbsp;<code>S</code>&nbsp;中，包含由一些连续的相同字符所构成的分组。</p>

<p>例如，在字符串 <code>S = &quot;abbxxxxzyy&quot;</code>&nbsp;中，就含有 <code>&quot;a&quot;</code>, <code>&quot;bb&quot;</code>, <code>&quot;xxxx&quot;</code>, <code>&quot;z&quot;</code> 和 <code>&quot;yy&quot;</code> 这样的一些分组。</p>

<p>我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。</p>

<p>最终结果按照字典顺序输出。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入: </strong>&quot;abbxxxxzzy&quot;
<strong>输出: </strong>[[3,6]]
<strong>解释</strong>: <code>&quot;xxxx&quot; 是一个起始于 3 且终止于 6 的较大分组</code>。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>&quot;abc&quot;
<strong>输出: </strong>[]
<strong>解释</strong>: &quot;a&quot;,&quot;b&quot; 和 &quot;c&quot; 均不是符合要求的较大分组。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>&quot;abcdddeeeeaabbbcd&quot;
<strong>输出: </strong>[[3,5],[6,9],[12,14]]</pre>

<p><strong>说明:&nbsp;</strong>&nbsp;<code>1 &lt;= S.length &lt;= 1000</code></p>
<p>在一个由小写字母构成的字符串&nbsp;<code>S</code>&nbsp;中，包含由一些连续的相同字符所构成的分组。</p>

<p>例如，在字符串 <code>S = &quot;abbxxxxzyy&quot;</code>&nbsp;中，就含有 <code>&quot;a&quot;</code>, <code>&quot;bb&quot;</code>, <code>&quot;xxxx&quot;</code>, <code>&quot;z&quot;</code> 和 <code>&quot;yy&quot;</code> 这样的一些分组。</p>

<p>我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。</p>

<p>最终结果按照字典顺序输出。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入: </strong>&quot;abbxxxxzzy&quot;
<strong>输出: </strong>[[3,6]]
<strong>解释</strong>: <code>&quot;xxxx&quot; 是一个起始于 3 且终止于 6 的较大分组</code>。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>&quot;abc&quot;
<strong>输出: </strong>[]
<strong>解释</strong>: &quot;a&quot;,&quot;b&quot; 和 &quot;c&quot; 均不是符合要求的较大分组。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入: </strong>&quot;abcdddeeeeaabbbcd&quot;
<strong>输出: </strong>[[3,5],[6,9],[12,14]]</pre>

<p><strong>说明:&nbsp;</strong>&nbsp;<code>1 &lt;= S.length &lt;= 1000</code></p>
*/


class Solution {
public:
    vector<vector<int>> largeGroupPositions(string S) {
        
    }
};