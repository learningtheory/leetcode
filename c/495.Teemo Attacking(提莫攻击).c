/*
<p>
In LOL world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition. Now, given the Teemo's attacking <b>ascending</b> time series towards Ashe and the poisoning time duration per Teemo's attacking, you need to output the total time that Ashe is in poisoned condition.
</p>

<p>You may assume that Teemo attacks at the very beginning of a specific time point, and makes Ashe be in poisoned condition immediately.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,4], 2
<b>Output:</b> 4
<b>Explanation:</b> At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned immediately. <br />This poisoned status will last 2 seconds until the end of time point 2. <br />And at time point 4, Teemo attacks Ashe again, and causes Ashe to be in poisoned status for another 2 seconds. <br />So you finally need to output 4.
</pre>
</p>


<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [1,2], 2
<b>Output:</b> 3
<b>Explanation:</b> At time point 1, Teemo starts attacking Ashe and makes Ashe be poisoned. <br />This poisoned status will last 2 seconds until the end of time point 2. <br/>However, at the beginning of time point 2, Teemo attacks Ashe again who is already in poisoned status. <br/>Since the poisoned status won't add up together, though the second poisoning attack will still work at time point 2, it will stop at the end of time point 3. <br/>So you finally need to output 3.
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>You may assume the length of given time series array won't exceed 10000.</li>
<li>You may assume the numbers in the Teemo's attacking time series and his poisoning time duration per attacking are non-negative integers, which won't exceed 10,000,000.</li>
</ol>
</p><p>在《英雄联盟》的世界中，有一个叫&ldquo;提莫&rdquo;的英雄，他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。现在，给出提莫对艾希的攻击时间序列和提莫攻击的中毒持续时间，你需要输出艾希的中毒状态总时长。</p>

<p>你可以认为提莫在给定的时间点进行攻击，并立即使艾希处于中毒状态。</p>

<p><strong>示例1:</strong></p>

<pre>
<strong>输入:</strong> [1,4], 2
<strong>输出:</strong> 4
<strong>原因:</strong> 在第1秒开始时，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持2秒钟，直到第2秒钟结束。
在第4秒开始时，提莫再次攻击艾希，使得艾希获得另外2秒的中毒时间。
所以最终输出4秒。
</pre>

<p><strong>示例2:</strong></p>

<pre>
<strong>输入:</strong> [1,2], 2
<strong>输出:</strong> 3
<strong>原因:</strong> 在第1秒开始时，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持2秒钟，直到第2秒钟结束。
但是在第2秒开始时，提莫再次攻击了已经处于中毒状态的艾希。
由于中毒状态不可叠加，提莫在第2秒开始时的这次攻击会在第3秒钟结束。
所以最终输出3。
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li>你可以假定时间序列数组的总长度不超过10000。</li>
	<li>你可以假定提莫攻击时间序列中的数字和提莫攻击的中毒持续时间都是非负整数，并且不超过10,000,000。</li>
</ol>
<p>在《英雄联盟》的世界中，有一个叫&ldquo;提莫&rdquo;的英雄，他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。现在，给出提莫对艾希的攻击时间序列和提莫攻击的中毒持续时间，你需要输出艾希的中毒状态总时长。</p>

<p>你可以认为提莫在给定的时间点进行攻击，并立即使艾希处于中毒状态。</p>

<p><strong>示例1:</strong></p>

<pre>
<strong>输入:</strong> [1,4], 2
<strong>输出:</strong> 4
<strong>原因:</strong> 在第1秒开始时，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持2秒钟，直到第2秒钟结束。
在第4秒开始时，提莫再次攻击艾希，使得艾希获得另外2秒的中毒时间。
所以最终输出4秒。
</pre>

<p><strong>示例2:</strong></p>

<pre>
<strong>输入:</strong> [1,2], 2
<strong>输出:</strong> 3
<strong>原因:</strong> 在第1秒开始时，提莫开始对艾希进行攻击并使其立即中毒。中毒状态会维持2秒钟，直到第2秒钟结束。
但是在第2秒开始时，提莫再次攻击了已经处于中毒状态的艾希。
由于中毒状态不可叠加，提莫在第2秒开始时的这次攻击会在第3秒钟结束。
所以最终输出3。
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li>你可以假定时间序列数组的总长度不超过10000。</li>
	<li>你可以假定提莫攻击时间序列中的数字和提莫攻击的中毒持续时间都是非负整数，并且不超过10,000,000。</li>
</ol>
*/


int findPoisonedDuration(int* timeSeries, int timeSeriesSize, int duration) {
    
}