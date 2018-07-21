/**
<p>Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.</p>

<p>However, there is a non-negative cooling interval <b>n</b> that means between two <b>same tasks</b>, there must be at least n intervals that CPU are doing different tasks or just be idle. </p>

<p>You need to return the <b>least</b> number of intervals the CPU will take to finish all the given tasks.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> tasks = ["A","A","A","B","B","B"], n = 2
<b>Output:</b> 8
<b>Explanation:</b> A -> B -> idle -> A -> B -> idle -> A -> B.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The number of tasks is in the range [1, 10000].</li>
<li>The integer n is in the range [0, 100].</li>
</ol>
</p><p>给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。</p>

<p>然而，两个<strong>相同种类</strong>的任务之间必须有长度为<strong>&nbsp;n </strong>的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。</p>

<p>你需要计算完成所有任务所需要的<strong>最短时间</strong>。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 2
<strong>输出:</strong> 8
<strong>执行顺序:</strong> A -&gt; B -&gt; (待命) -&gt; A -&gt; B -&gt; (待命) -&gt; A -&gt; B.
</pre>

<p><strong>注：</strong></p>

<ol>
	<li>任务的总个数为&nbsp;[1, 10000]。</li>
	<li>n 的取值范围为 [0, 100]。</li>
</ol>
<p>给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。</p>

<p>然而，两个<strong>相同种类</strong>的任务之间必须有长度为<strong>&nbsp;n </strong>的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。</p>

<p>你需要计算完成所有任务所需要的<strong>最短时间</strong>。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> tasks = [&quot;A&quot;,&quot;A&quot;,&quot;A&quot;,&quot;B&quot;,&quot;B&quot;,&quot;B&quot;], n = 2
<strong>输出:</strong> 8
<strong>执行顺序:</strong> A -&gt; B -&gt; (待命) -&gt; A -&gt; B -&gt; (待命) -&gt; A -&gt; B.
</pre>

<p><strong>注：</strong></p>

<ol>
	<li>任务的总个数为&nbsp;[1, 10000]。</li>
	<li>n 的取值范围为 [0, 100]。</li>
</ol>
**/


class Solution {
    public int leastInterval(char[] tasks, int n) {
        
    }
}