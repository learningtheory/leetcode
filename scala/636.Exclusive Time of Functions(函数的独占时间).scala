/**
<p>Given the running logs of <b>n</b> functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions. </p>

<p>Each function has a unique id, start from <b>0</b> to <b>n-1</b>. A function may be called recursively or by another function.</p>

<p>A log is a string has this format : <code>function_id:start_or_end:timestamp</code>. For example, <code>"0:start:0"</code> means function 0 starts from the very beginning of time 0. <code>"0:end:0"</code> means function 0 ends to the very end of time 0. </p>

<p>Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions should not be considered as this function's exclusive time. You should return the exclusive time of each function sorted by their function id.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
n = 2
logs = 
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
<b>Output:</b>[3, 4]
<b>Explanation:</b>
Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1. 
Now function 0 <b>calls function 1</b>, function 1 starts at time 2, executes 4 units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time. 
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>Input logs will be sorted by timestamp, NOT log id.</li>
<li>Your output should be sorted by function id, which means the 0th element of your output corresponds to the exclusive time of function 0.</li>
<li>Two functions won't start or end at the same time.</li>
<li>Functions could be called recursively, and will always end.</li>
<li>1 <= n <= 100</li>
</ol>
</p><p>给出一个非抢占单线程CPU的 <strong>n </strong>个函数运行日志，找到函数的独占时间。</p>

<p>每个函数都有一个唯一的 Id，从 <strong>0</strong> 到<strong> n-1</strong>，函数可能会递归调用或者被其他函数调用。</p>

<p>日志是具有以下格式的字符串：<code>function_id：start_or_end：timestamp</code>。例如：<code>&quot;0:start:0&quot;</code>&nbsp;表示函数 0 从 0 时刻开始运行。<code>&quot;0:end:0&quot;</code>&nbsp;表示函数 0 在 0 时刻结束。</p>

<p>函数的独占时间定义是在该方法中花费的时间，调用其他函数花费的时间不算该函数的独占时间。你需要根据函数的 Id 有序地返回每个函数的独占时间。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong>
n = 2
logs = 
[&quot;0:start:0&quot;,
 &quot;1:start:2&quot;,
 &quot;1:end:5&quot;,
 &quot;0:end:6&quot;]
<strong>输出:</strong>[3, 4]
<strong>说明：</strong>
函数 0 在时刻 0 开始，在执行了  2个时间单位结束于时刻 1。
现在函数 0 调用函数 1，函数 1 在时刻 2 开始，执行 4 个时间单位后结束于时刻 5。
函数 0 再次在时刻 6 开始执行，并在时刻 6 结束运行，从而执行了 1 个时间单位。
所以函数 0 总共的执行了 2 +1 =3 个时间单位，函数 1 总共执行了 4 个时间单位。
</pre>

<p><strong>说明：</strong></p>

<ol>
	<li>输入的日志会根据时间戳排序，而不是根据日志Id排序。</li>
	<li>你的输出会根据函数Id排序，也就意味着你的输出数组中序号为 0 的元素相当于函数 0 的执行时间。</li>
	<li>两个函数不会在同时开始或结束。</li>
	<li>函数允许被递归调用，直到运行结束。</li>
	<li>1 &lt;= n &lt;= 100</li>
</ol>
<p>给出一个非抢占单线程CPU的 <strong>n </strong>个函数运行日志，找到函数的独占时间。</p>

<p>每个函数都有一个唯一的 Id，从 <strong>0</strong> 到<strong> n-1</strong>，函数可能会递归调用或者被其他函数调用。</p>

<p>日志是具有以下格式的字符串：<code>function_id：start_or_end：timestamp</code>。例如：<code>&quot;0:start:0&quot;</code>&nbsp;表示函数 0 从 0 时刻开始运行。<code>&quot;0:end:0&quot;</code>&nbsp;表示函数 0 在 0 时刻结束。</p>

<p>函数的独占时间定义是在该方法中花费的时间，调用其他函数花费的时间不算该函数的独占时间。你需要根据函数的 Id 有序地返回每个函数的独占时间。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong>
n = 2
logs = 
[&quot;0:start:0&quot;,
 &quot;1:start:2&quot;,
 &quot;1:end:5&quot;,
 &quot;0:end:6&quot;]
<strong>输出:</strong>[3, 4]
<strong>说明：</strong>
函数 0 在时刻 0 开始，在执行了  2个时间单位结束于时刻 1。
现在函数 0 调用函数 1，函数 1 在时刻 2 开始，执行 4 个时间单位后结束于时刻 5。
函数 0 再次在时刻 6 开始执行，并在时刻 6 结束运行，从而执行了 1 个时间单位。
所以函数 0 总共的执行了 2 +1 =3 个时间单位，函数 1 总共执行了 4 个时间单位。
</pre>

<p><strong>说明：</strong></p>

<ol>
	<li>输入的日志会根据时间戳排序，而不是根据日志Id排序。</li>
	<li>你的输出会根据函数Id排序，也就意味着你的输出数组中序号为 0 的元素相当于函数 0 的执行时间。</li>
	<li>两个函数不会在同时开始或结束。</li>
	<li>函数允许被递归调用，直到运行结束。</li>
	<li>1 &lt;= n &lt;= 100</li>
</ol>
**/


object Solution {
    def exclusiveTime(n: Int, logs: List[String]): Array[Int] = {
        
    }
}