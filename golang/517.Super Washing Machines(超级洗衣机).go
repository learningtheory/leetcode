/*
<p>You have <b>n</b> super washing machines on a line. Initially, each washing machine has some dresses or is empty. 
</p>

<p>For each <b>move</b>, you could choose <b>any m</b> (1 &le; m &le; n) washing machines, and pass <b>one dress</b> of each washing machine to one of its adjacent washing machines <b> at the same time </b>.  </p>

<p>Given an integer array representing the number of dresses in each washing machine from left to right on the line, you should find the <b>minimum number of moves</b> to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.</p>

<p><b>Example1</b>
<pre>
<b>Input:</b> [1,0,5]

<b>Output:</b> 3

<b>Explanation:</b> 
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3    
3rd move:    2     1 <-- 3    =>    2     2     2   
</pre>

<p><b>Example2</b>
<pre>
<b>Input:</b> [0,3,0]

<b>Output:</b> 2

<b>Explanation:</b> 
1st move:    0 <-- 3     0    =>    1     2     0    
2nd move:    1     2 --> 0    =>    1     1     1     
</pre>

<p><b>Example3</b>
<pre>
<b>Input:</b> [0,2,0]

<b>Output:</b> -1

<b>Explanation:</b> 
It's impossible to make all the three washing machines have the same number of dresses. 
</pre>

</p>

<p><b>Note:</b><br>
<ol>
<li>The range of n is [1, 10000].</li>
<li>The range of dresses number in a super washing machine is [0, 1e5].</li>
</ol>
</p><p>假设有 <strong>n&nbsp;</strong>台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。</p>

<p>在<strong>每一步操作</strong>中，你可以选择<strong>任意 m&nbsp;</strong>（1 &le; m &le; n）&nbsp;台洗衣机，与此<strong>同时</strong>将每台洗衣机的<strong>一件衣服</strong>送到相邻的一台洗衣机。</p>

<p>给定一个非负整数数组代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的<strong>最少的操作步数</strong>。如果不能使每台洗衣机中衣物的数量相等，则返回 -1。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> [1,0,5]

<strong>输出:</strong> 3

<strong>解释:</strong> 
第一步:    1     0 &lt;-- 5    =&gt;    1     1     4
第二步:    1 &lt;-- 1 &lt;-- 4    =&gt;    2     1     3    
第三步:    2     1 &lt;-- 3    =&gt;    2     2     2   
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> [0,3,0]

<strong>输出:</strong> 2

<strong>解释:</strong> 
第一步:    0 &lt;-- 3     0    =&gt;    1     2     0    
第二步:    1     2 --&gt; 0    =&gt;    1     1     1     
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> [0,2,0]

<strong>输出:</strong> -1

<strong>解释:</strong> 
不可能让所有三个洗衣机同时剩下相同数量的衣物。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>n 的范围是 [1, 10000]。</li>
	<li>在每台超级洗衣机中，衣物数量的范围是 [0, 1e5]。</li>
</ol>

<p>&nbsp;</p>
<p>假设有 <strong>n&nbsp;</strong>台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。</p>

<p>在<strong>每一步操作</strong>中，你可以选择<strong>任意 m&nbsp;</strong>（1 &le; m &le; n）&nbsp;台洗衣机，与此<strong>同时</strong>将每台洗衣机的<strong>一件衣服</strong>送到相邻的一台洗衣机。</p>

<p>给定一个非负整数数组代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的<strong>最少的操作步数</strong>。如果不能使每台洗衣机中衣物的数量相等，则返回 -1。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> [1,0,5]

<strong>输出:</strong> 3

<strong>解释:</strong> 
第一步:    1     0 &lt;-- 5    =&gt;    1     1     4
第二步:    1 &lt;-- 1 &lt;-- 4    =&gt;    2     1     3    
第三步:    2     1 &lt;-- 3    =&gt;    2     2     2   
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> [0,3,0]

<strong>输出:</strong> 2

<strong>解释:</strong> 
第一步:    0 &lt;-- 3     0    =&gt;    1     2     0    
第二步:    1     2 --&gt; 0    =&gt;    1     1     1     
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> [0,2,0]

<strong>输出:</strong> -1

<strong>解释:</strong> 
不可能让所有三个洗衣机同时剩下相同数量的衣物。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li>n 的范围是 [1, 10000]。</li>
	<li>在每台超级洗衣机中，衣物数量的范围是 [0, 1e5]。</li>
</ol>

<p>&nbsp;</p>
*/


func findMinMoves(machines []int) int {
    
}