/*
<p>
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most <b>k</b> distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most <b>k</b> distinct projects. 
</p>

<p>
You are given several projects. For each project <b>i</b>, it has a pure profit <b>P<sub>i</sub></b> and a minimum capital of <b>C<sub>i</sub></b> is needed to start the corresponding project. Initially, you have <b>W</b> capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.
</p>

<p>
To sum up, pick a list of at most <b>k</b> distinct projects from given projects to maximize your final capital, and output your final maximized capital.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

<b>Output:</b> 4

<b>Explanation:</b> Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>You may assume all numbers in the input are non-negative integers.</li>
<li>The length of Profits array and Capital array will not exceed 50,000.</li>
<li>The answer is guaranteed to fit in a 32-bit signed integer.</li>
</ol>
</p><p>假设 LeetCode 即将开始其 IPO。为了以更高的价格将股票卖给风险投资公司，LeetCode希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 <strong>k</strong> 个不同的项目。帮助 LeetCode 设计完成最多 <strong>k</strong> 个不同项目后得到最大总资本的方式。</p>

<p>给定若干个项目。对于每个项目 <strong>i</strong>，它都有一个纯利润 <strong>P<sub>i</sub></strong>，并且需要最小的资本 <strong>C<sub>i</sub></strong> 来启动相应的项目。最初，你有 <strong>W</strong> 资本。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。</p>

<p>总而言之，从给定项目中选择最多 <strong>k</strong> 个不同项目的列表，以最大化最终资本，并输出最终可获得的最多资本。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

<strong>输出:</strong> 4

<strong>解释:
</strong>由于你的初始资本为 0，你尽可以从 0 号项目开始。
在完成后，你将获得 1 的利润，你的总资本将变为 1。
此时你可以选择开始 1 号或 2 号项目。
由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。
</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<ol>
	<li>假设所有输入数字都是非负整数。</li>
	<li>表示利润和资本的数组的长度不超过 50000。</li>
	<li>答案保证在 32 位有符号整数范围内。</li>
</ol>

<p>&nbsp;</p>
<p>假设 LeetCode 即将开始其 IPO。为了以更高的价格将股票卖给风险投资公司，LeetCode希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 <strong>k</strong> 个不同的项目。帮助 LeetCode 设计完成最多 <strong>k</strong> 个不同项目后得到最大总资本的方式。</p>

<p>给定若干个项目。对于每个项目 <strong>i</strong>，它都有一个纯利润 <strong>P<sub>i</sub></strong>，并且需要最小的资本 <strong>C<sub>i</sub></strong> 来启动相应的项目。最初，你有 <strong>W</strong> 资本。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。</p>

<p>总而言之，从给定项目中选择最多 <strong>k</strong> 个不同项目的列表，以最大化最终资本，并输出最终可获得的最多资本。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

<strong>输出:</strong> 4

<strong>解释:
</strong>由于你的初始资本为 0，你尽可以从 0 号项目开始。
在完成后，你将获得 1 的利润，你的总资本将变为 1。
此时你可以选择开始 1 号或 2 号项目。
由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。
</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<ol>
	<li>假设所有输入数字都是非负整数。</li>
	<li>表示利润和资本的数组的长度不超过 50000。</li>
	<li>答案保证在 32 位有符号整数范围内。</li>
</ol>

<p>&nbsp;</p>
*/


int findMaximizedCapital(int k, int W, int* Profits, int ProfitsSize, int* Capital, int CapitalSize) {
    
}