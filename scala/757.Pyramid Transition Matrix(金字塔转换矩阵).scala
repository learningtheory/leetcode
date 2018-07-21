/**
<p>
We are stacking blocks to form a pyramid.  Each block has a color which is a one letter string, like `'Z'`.
</p><p>
For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`.  We are allowed to place the block there only if `(A, B, C)` is an allowed triple.
</p><p>
We start with a bottom row of <code>bottom</code>, represented as a single string.  We also start with a list of allowed triples <code>allowed</code>.  Each allowed triple is represented as a string of length 3.
</p><p>
Return true if we can build the pyramid all the way to the top, otherwise false.
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
<b>Output:</b> true
<b>Explanation:</b>
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
<b>Output:</b> false
<b>Explanation:</b>
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li><code>bottom</code> will be a string with length in range <code>[2, 8]</code>.</li>
<li><code>allowed</code> will have length in range <code>[0, 200]</code>.</li>
<li>Letters in all strings will be chosen from the set <code>{'A', 'B', 'C', 'D', 'E', 'F', 'G'}</code>.</li>
</ol>
</p><p>现在，我们用一些方块来堆砌一个金字塔。 每个方块用仅包含一个字母的字符串表示，例如 &ldquo;Z&rdquo;。</p>

<p>使用三元组表示金字塔的堆砌规则如下：</p>

<p>(A, B, C) 表示，&ldquo;C&rdquo;为顶层方块，方块&ldquo;A&rdquo;、&ldquo;B&rdquo;分别作为方块&ldquo;C&rdquo;下一层的的左、右子块。当且仅当(A, B, C)是被允许的三元组，我们才可以将其堆砌上。</p>

<p>初始时，给定金字塔的基层&nbsp;<code>bottom</code>，用一个字符串表示。一个允许的三元组列表&nbsp;<code>allowed</code>，每个三元组用一个长度为 3 的字符串表示。</p>

<p>如果可以由基层一直堆到塔尖返回true，否则返回false。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> bottom = &quot;XYZ&quot;, allowed = [&quot;XYD&quot;, &quot;YZE&quot;, &quot;DEA&quot;, &quot;FFF&quot;]
<strong>输出:</strong> true
<strong>解析:</strong>
可以堆砌成这样的金字塔:
    A
   / \
  D   E
 / \ / \
X   Y   Z

因为符合(&#39;X&#39;, &#39;Y&#39;, &#39;D&#39;), (&#39;Y&#39;, &#39;Z&#39;, &#39;E&#39;) 和 (&#39;D&#39;, &#39;E&#39;, &#39;A&#39;) 三种规则。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> bottom = &quot;XXYX&quot;, allowed = [&quot;XXX&quot;, &quot;XXY&quot;, &quot;XYX&quot;, &quot;XYY&quot;, &quot;YXZ&quot;]
<strong>输出:</strong> false
<strong>解析:</strong>
无法一直堆到塔尖。
注意, 允许存在三元组(A, B, C)和 (A, B, D) ，其中 C != D.
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li><code>bottom</code> 的长度范围在&nbsp;<code>[2, 8]</code>。</li>
	<li><code>allowed</code> 的长度范围在<code>[0, 200]</code>。</li>
	<li>方块的标记字母范围为<code>{&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;, &#39;F&#39;, &#39;G&#39;}</code>。</li>
</ol>
<p>现在，我们用一些方块来堆砌一个金字塔。 每个方块用仅包含一个字母的字符串表示，例如 &ldquo;Z&rdquo;。</p>

<p>使用三元组表示金字塔的堆砌规则如下：</p>

<p>(A, B, C) 表示，&ldquo;C&rdquo;为顶层方块，方块&ldquo;A&rdquo;、&ldquo;B&rdquo;分别作为方块&ldquo;C&rdquo;下一层的的左、右子块。当且仅当(A, B, C)是被允许的三元组，我们才可以将其堆砌上。</p>

<p>初始时，给定金字塔的基层&nbsp;<code>bottom</code>，用一个字符串表示。一个允许的三元组列表&nbsp;<code>allowed</code>，每个三元组用一个长度为 3 的字符串表示。</p>

<p>如果可以由基层一直堆到塔尖返回true，否则返回false。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> bottom = &quot;XYZ&quot;, allowed = [&quot;XYD&quot;, &quot;YZE&quot;, &quot;DEA&quot;, &quot;FFF&quot;]
<strong>输出:</strong> true
<strong>解析:</strong>
可以堆砌成这样的金字塔:
    A
   / \
  D   E
 / \ / \
X   Y   Z

因为符合(&#39;X&#39;, &#39;Y&#39;, &#39;D&#39;), (&#39;Y&#39;, &#39;Z&#39;, &#39;E&#39;) 和 (&#39;D&#39;, &#39;E&#39;, &#39;A&#39;) 三种规则。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> bottom = &quot;XXYX&quot;, allowed = [&quot;XXX&quot;, &quot;XXY&quot;, &quot;XYX&quot;, &quot;XYY&quot;, &quot;YXZ&quot;]
<strong>输出:</strong> false
<strong>解析:</strong>
无法一直堆到塔尖。
注意, 允许存在三元组(A, B, C)和 (A, B, D) ，其中 C != D.
</pre>

<p><strong>注意：</strong></p>

<ol>
	<li><code>bottom</code> 的长度范围在&nbsp;<code>[2, 8]</code>。</li>
	<li><code>allowed</code> 的长度范围在<code>[0, 200]</code>。</li>
	<li>方块的标记字母范围为<code>{&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;, &#39;F&#39;, &#39;G&#39;}</code>。</li>
</ol>
**/


object Solution {
    def pyramidTransition(bottom: String, allowed: List[String]): Boolean = {
        
    }
}