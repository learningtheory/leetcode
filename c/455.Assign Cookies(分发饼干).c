/*
<p>
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie. Each child i has a greed factor g<sub>i</sub>, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s<sub>j</sub>. If s<sub>j</sub> >= g<sub>i</sub>, we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
</p>

<p><b>Note:</b><br />
You may assume the greed factor is always positive. <br />
You cannot assign more than one cookie to one child.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,2,3], [1,1]

<b>Output:</b> 1

<b>Explanation:</b> You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1,2], [1,2,3]

<b>Output:</b> 2

<b>Explanation:</b> You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
</pre>
</p><p>假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值&nbsp;g<sub>i ，</sub>这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 s<sub>j&nbsp;</sub>。如果 s<sub>j</sub> &gt;= g<sub>i&nbsp;</sub>，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。</p>

<p><strong>注意：</strong></p>

<p>你可以假设胃口值为正。<br />
一个小朋友最多只能拥有一块饼干。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> [1,2,3], [1,1]

<strong>输出:</strong> 1

<strong>解释:</strong> 
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> [1,2], [1,2,3]

<strong>输出:</strong> 2

<strong>解释:</strong> 
你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.
</pre>
<p>假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值&nbsp;g<sub>i ，</sub>这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 s<sub>j&nbsp;</sub>。如果 s<sub>j</sub> &gt;= g<sub>i&nbsp;</sub>，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。</p>

<p><strong>注意：</strong></p>

<p>你可以假设胃口值为正。<br />
一个小朋友最多只能拥有一块饼干。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> [1,2,3], [1,1]

<strong>输出:</strong> 1

<strong>解释:</strong> 
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> [1,2], [1,2,3]

<strong>输出:</strong> 2

<strong>解释:</strong> 
你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.
</pre>
*/


int findContentChildren(int* g, int gSize, int* s, int sSize) {
    
}