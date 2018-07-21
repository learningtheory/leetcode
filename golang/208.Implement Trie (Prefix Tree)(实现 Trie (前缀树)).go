/*
<p>Implement a trie with <code>insert</code>, <code>search</code>, and <code>startsWith</code> methods.</p>

<p><b>Example:</b></p>

<pre>
Trie trie = new Trie();

trie.insert(&quot;apple&quot;);
trie.search(&quot;apple&quot;);   // returns true
trie.search(&quot;app&quot;);     // returns false
trie.startsWith(&quot;app&quot;); // returns true
trie.insert(&quot;app&quot;);   
trie.search(&quot;app&quot;);     // returns true
</pre>

<p><b>Note:</b></p>

<ul>
	<li>You may assume that all inputs are consist of lowercase letters <code>a-z</code>.</li>
	<li>All inputs are guaranteed to be non-empty strings.</li>
</ul>
<p>实现一个 Trie (前缀树)，包含&nbsp;<code>insert</code>,&nbsp;<code>search</code>, 和&nbsp;<code>startsWith</code>&nbsp;这三个操作。</p>

<p><strong>示例:</strong></p>

<pre>Trie trie = new Trie();

trie.insert(&quot;apple&quot;);
trie.search(&quot;apple&quot;);   // 返回 true
trie.search(&quot;app&quot;);     // 返回 false
trie.startsWith(&quot;app&quot;); // 返回 true
trie.insert(&quot;app&quot;);   
trie.search(&quot;app&quot;);     // 返回 true</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>你可以假设所有的输入都是由小写字母&nbsp;<code>a-z</code>&nbsp;构成的。</li>
	<li>保证所有输入均为非空字符串。</li>
</ul>
<p>实现一个 Trie (前缀树)，包含&nbsp;<code>insert</code>,&nbsp;<code>search</code>, 和&nbsp;<code>startsWith</code>&nbsp;这三个操作。</p>

<p><strong>示例:</strong></p>

<pre>Trie trie = new Trie();

trie.insert(&quot;apple&quot;);
trie.search(&quot;apple&quot;);   // 返回 true
trie.search(&quot;app&quot;);     // 返回 false
trie.startsWith(&quot;app&quot;); // 返回 true
trie.insert(&quot;app&quot;);   
trie.search(&quot;app&quot;);     // 返回 true</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>你可以假设所有的输入都是由小写字母&nbsp;<code>a-z</code>&nbsp;构成的。</li>
	<li>保证所有输入均为非空字符串。</li>
</ul>
*/


type Trie struct {
    
}


/** Initialize your data structure here. */
func Constructor() Trie {
    
}


/** Inserts a word into the trie. */
func (this *Trie) Insert(word string)  {
    
}


/** Returns if the word is in the trie. */
func (this *Trie) Search(word string) bool {
    
}


/** Returns if there is any word in the trie that starts with the given prefix. */
func (this *Trie) StartsWith(prefix string) bool {
    
}


/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */