/*
<p>
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings. 
</p>
<p>
You need to help them find out their <b>common interest</b> with the <b>least list index sum</b>. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
</p>


<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
<b>Output:</b> ["Shogun"]
<b>Explanation:</b> The only restaurant they both like is "Shogun".
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b>
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
<b>Output:</b> ["Shogun"]
<b>Explanation:</b> The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
</pre>
</p>


<p><b>Note:</b><br>
<ol>
<li>The length of both lists will be in the range of [1, 1000].</li>
<li>The length of strings in both lists will be in the range of [1, 30].</li>
<li>The index is starting from 0 to the list length minus 1.</li>
<li>No duplicates in both lists.</li>
</ol>
</p><p>假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。</p>

<p>你需要帮助他们用<strong>最少的索引和</strong>找出他们<strong>共同喜爱的餐厅</strong>。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong>
[&quot;Shogun&quot;, &quot;Tapioca Express&quot;, &quot;Burger King&quot;, &quot;KFC&quot;]
[&quot;Piatti&quot;, &quot;The Grill at Torrey Pines&quot;, &quot;Hungry Hunter Steakhouse&quot;, &quot;Shogun&quot;]
<strong>输出:</strong> [&quot;Shogun&quot;]
<strong>解释:</strong> 他们唯一共同喜爱的餐厅是&ldquo;Shogun&rdquo;。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>
[&quot;Shogun&quot;, &quot;Tapioca Express&quot;, &quot;Burger King&quot;, &quot;KFC&quot;]
[&quot;KFC&quot;, &quot;Shogun&quot;, &quot;Burger King&quot;]
<strong>输出:</strong> [&quot;Shogun&quot;]
<strong>解释:</strong> 他们共同喜爱且具有最小索引和的餐厅是&ldquo;Shogun&rdquo;，它有最小的索引和1(0+1)。
</pre>

<p><strong>提示:</strong></p>

<ol>
	<li>两个列表的长度范围都在&nbsp;[1, 1000]内。</li>
	<li>两个列表中的字符串的长度将在[1，30]的范围内。</li>
	<li>下标从0开始，到列表的长度减1。</li>
	<li>两个列表都没有重复的元素。</li>
</ol>
<p>假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。</p>

<p>你需要帮助他们用<strong>最少的索引和</strong>找出他们<strong>共同喜爱的餐厅</strong>。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong>
[&quot;Shogun&quot;, &quot;Tapioca Express&quot;, &quot;Burger King&quot;, &quot;KFC&quot;]
[&quot;Piatti&quot;, &quot;The Grill at Torrey Pines&quot;, &quot;Hungry Hunter Steakhouse&quot;, &quot;Shogun&quot;]
<strong>输出:</strong> [&quot;Shogun&quot;]
<strong>解释:</strong> 他们唯一共同喜爱的餐厅是&ldquo;Shogun&rdquo;。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>
[&quot;Shogun&quot;, &quot;Tapioca Express&quot;, &quot;Burger King&quot;, &quot;KFC&quot;]
[&quot;KFC&quot;, &quot;Shogun&quot;, &quot;Burger King&quot;]
<strong>输出:</strong> [&quot;Shogun&quot;]
<strong>解释:</strong> 他们共同喜爱且具有最小索引和的餐厅是&ldquo;Shogun&rdquo;，它有最小的索引和1(0+1)。
</pre>

<p><strong>提示:</strong></p>

<ol>
	<li>两个列表的长度范围都在&nbsp;[1, 1000]内。</li>
	<li>两个列表中的字符串的长度将在[1，30]的范围内。</li>
	<li>下标从0开始，到列表的长度减1。</li>
	<li>两个列表都没有重复的元素。</li>
</ol>
*/


/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function(list1, list2) {
    
};