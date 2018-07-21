=begin
<p>
You are given <code>n</code> pairs of numbers. In every pair, the first number is always smaller than the second number.
</p>

<p>
Now, we define a pair <code>(c, d)</code> can follow another pair <code>(a, b)</code> if and only if <code>b < c</code>. Chain of pairs can be formed in this fashion. 
</p>

<p>
Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [[1,2], [2,3], [3,4]]
<b>Output:</b> 2
<b>Explanation:</b> The longest chain is [1,2] -> [3,4]
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The number of given pairs will be in the range [1, 1000].</li>
</ol>
</p><p>给出&nbsp;<code>n</code>&nbsp;个数对。&nbsp;在每一个数对中，第一个数字总是比第二个数字小。</p>

<p>现在，我们定义一种跟随关系，当且仅当&nbsp;<code>b &lt; c</code>&nbsp;时，数对<code>(c, d)</code>&nbsp;才可以跟在&nbsp;<code>(a, b)</code>&nbsp;后面。我们用这种形式来构造一个数对链。</p>

<p>给定一个对数集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。</p>

<p><strong>示例 :</strong></p>

<pre>
<strong>输入:</strong> [[1,2], [2,3], [3,4]]
<strong>输出:</strong> 2
<strong>解释:</strong> 最长的数对链是 [1,2] -&gt; [3,4]
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li>给出数对的个数在&nbsp;[1, 1000] 范围内。</li>
</ol>
<p>给出&nbsp;<code>n</code>&nbsp;个数对。&nbsp;在每一个数对中，第一个数字总是比第二个数字小。</p>

<p>现在，我们定义一种跟随关系，当且仅当&nbsp;<code>b &lt; c</code>&nbsp;时，数对<code>(c, d)</code>&nbsp;才可以跟在&nbsp;<code>(a, b)</code>&nbsp;后面。我们用这种形式来构造一个数对链。</p>

<p>给定一个对数集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。</p>

<p><strong>示例 :</strong></p>

<pre>
<strong>输入:</strong> [[1,2], [2,3], [3,4]]
<strong>输出:</strong> 2
<strong>解释:</strong> 最长的数对链是 [1,2] -&gt; [3,4]
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li>给出数对的个数在&nbsp;[1, 1000] 范围内。</li>
</ol>

=end


# @param {Integer[][]} pairs
# @return {Integer}
def find_longest_chain(pairs)
    
end