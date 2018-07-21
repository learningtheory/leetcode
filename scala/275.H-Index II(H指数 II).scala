/**
<p>Given an array of citations <strong>sorted&nbsp;in ascending order </strong>(each citation is a non-negative integer) of a researcher, write a function to compute the researcher&#39;s h-index.</p>

<p>According to the&nbsp;<a href="https://en.wikipedia.org/wiki/H-index" target="_blank">definition of h-index on Wikipedia</a>: &quot;A scientist has index&nbsp;<i>h</i>&nbsp;if&nbsp;<i>h</i>&nbsp;of his/her&nbsp;<i>N</i>&nbsp;papers have&nbsp;<b>at least</b>&nbsp;<i>h</i>&nbsp;citations each, and the other&nbsp;<i>N &minus; h</i>&nbsp;papers have&nbsp;<b>no more than</b>&nbsp;<i>h&nbsp;</i>citations each.&quot;</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> <code>citations = [0,1,3,5,6]</code>
<b>Output:</b> 3 
<strong>Explanation: </strong><code>[0,1,3,5,6] </code>means the researcher has <code>5</code> papers in total and each of them had 
             received 0<code>, 1, 3, 5, 6</code> citations respectively. 
&nbsp;            Since the researcher has <code>3</code> papers with <b>at least</b> <code>3</code> citations each and the remaining 
&nbsp;            two with <b>no more than</b> <code>3</code> citations each, her h-index is <code>3</code>.</pre>

<p><strong>Note:</strong></p>

<p>If there are several possible values for&nbsp;<em>h</em>, the maximum one is taken as the h-index.</p>

<p><strong>Follow up:</strong></p>

<ul>
	<li>This is a follow up problem to&nbsp;<a href="/problems/h-index/description/">H-Index</a>, where <code>citations</code> is now guaranteed to be sorted in ascending order.</li>
	<li>Could you solve it in logarithmic time complexity?</li>
</ul>
<p>给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照<strong>升序排列</strong>。编写一个方法，计算出研究者的 <em>h</em> 指数。</p>

<p><a href="https://baike.baidu.com/item/h-index/3991452?fr=aladdin">h 指数的定义</a>: &ldquo;一位有&nbsp;<em>h</em>&nbsp;指数的学者，代表他（她）的<em> N</em> 篇论文中<strong>至多</strong>有<em> h </em>篇论文，分别被引用了<strong>至少</strong>&nbsp;<em>h</em> 次，其余的&nbsp;<em>N - h&nbsp;</em>篇论文每篇被引用次数<strong>不多于 </strong><em>h </em>次。&quot;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> <code>citations = [0,1,3,5,6]</code>
<strong>输出:</strong> 3 
<strong>解释: </strong>给定数组表示研究者总共有 <code>5</code> 篇论文，每篇论文相应的被引用了 0<code>, 1, 3, 5, 6</code> 次。
&nbsp;    由于研究者有 <code>3 </code>篇论文每篇<strong>至少</strong>被引用了 <code>3</code> 次，其余两篇论文每篇被引用<strong>不多于</strong> <code>3</code> 次，所以她的<em> h </em>指数是 <code>3</code>。</pre>

<p><strong>说明:</strong></p>

<p>如果 <em>h </em>有多有种可能的值 ，<em>h</em> 指数是其中最大的那个。</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>这是&nbsp;<a href="/problems/h-index/description/">H指数</a>&nbsp;的延伸题目，本题中的&nbsp;<code>citations</code>&nbsp;数组是保证有序的。</li>
	<li>你可以优化你的算法到对数时间复杂度吗？</li>
</ul>
<p>给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照<strong>升序排列</strong>。编写一个方法，计算出研究者的 <em>h</em> 指数。</p>

<p><a href="https://baike.baidu.com/item/h-index/3991452?fr=aladdin">h 指数的定义</a>: &ldquo;一位有&nbsp;<em>h</em>&nbsp;指数的学者，代表他（她）的<em> N</em> 篇论文中<strong>至多</strong>有<em> h </em>篇论文，分别被引用了<strong>至少</strong>&nbsp;<em>h</em> 次，其余的&nbsp;<em>N - h&nbsp;</em>篇论文每篇被引用次数<strong>不多于 </strong><em>h </em>次。&quot;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> <code>citations = [0,1,3,5,6]</code>
<strong>输出:</strong> 3 
<strong>解释: </strong>给定数组表示研究者总共有 <code>5</code> 篇论文，每篇论文相应的被引用了 0<code>, 1, 3, 5, 6</code> 次。
&nbsp;    由于研究者有 <code>3 </code>篇论文每篇<strong>至少</strong>被引用了 <code>3</code> 次，其余两篇论文每篇被引用<strong>不多于</strong> <code>3</code> 次，所以她的<em> h </em>指数是 <code>3</code>。</pre>

<p><strong>说明:</strong></p>

<p>如果 <em>h </em>有多有种可能的值 ，<em>h</em> 指数是其中最大的那个。</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>这是&nbsp;<a href="/problems/h-index/description/">H指数</a>&nbsp;的延伸题目，本题中的&nbsp;<code>citations</code>&nbsp;数组是保证有序的。</li>
	<li>你可以优化你的算法到对数时间复杂度吗？</li>
</ul>
**/


object Solution {
    def hIndex(citations: Array[Int]): Int = {
        
    }
}