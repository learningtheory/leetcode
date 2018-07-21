/*
<p>Design a HashSet&nbsp;without using any built-in hash table libraries.</p>

<p>To be specific, your design should include these two functions:</p>

<ul>
	<li><code>add(value)</code>:&nbsp;Insert a value into the HashSet.&nbsp;</li>
	<li><code>contains(value)</code> : Return whether the value exists in the HashSet or not.</li>
	<li><code>remove(value)</code>: Remove a value in&nbsp;the HashSet. If the value does not exist in the HashSet, do nothing.</li>
</ul>

<p><br />
<strong>Example:</strong></p>

<pre>
MyHashSet hashSet = new MyHashSet();
hashSet.add(1); &nbsp; &nbsp; &nbsp; &nbsp; 
hashSet.add(2); &nbsp; &nbsp; &nbsp; &nbsp; 
hashSet.contains(1); &nbsp;&nbsp;&nbsp;// returns true
hashSet.contains(3); &nbsp;&nbsp;&nbsp;// returns false (not found)
hashSet.add(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
hashSet.contains(2); &nbsp;&nbsp;&nbsp;// returns true
hashSet.remove(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
hashSet.contains(2); &nbsp;&nbsp;&nbsp;// returns false (already removed)
</pre>

<p><br />
<strong>Note:</strong></p>

<ul>
	<li>All values will be in the range of <code>[1, 1000000]</code>.</li>
	<li>The number of operations will be in the range of&nbsp;<code>[1, 10000]</code>.</li>
	<li>Please do not use the built-in HashSet library.</li>
</ul><p>不使用任何内建的哈希表库设计一个哈希集合</p>

<p>具体地说，你的设计应该包含以下的功能</p>

<ul>
	<li><code>add(value)</code>：向哈希集合中插入一个值。</li>
	<li><code>contains(value)</code> ：返回哈希集合中是否存在这个值。</li>
	<li><code>remove(value)</code>：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。</li>
</ul>

<p><br>
<strong>示例:</strong></p>

<pre>MyHashSet hashSet = new MyHashSet();
hashSet.add(1); &nbsp; &nbsp; &nbsp; &nbsp; 
hashSet.add(2); &nbsp; &nbsp; &nbsp; &nbsp; 
hashSet.contains(1); &nbsp;&nbsp;&nbsp;// 返回 true
hashSet.contains(3); &nbsp;&nbsp;&nbsp;// 返回 false (未找到)
hashSet.add(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
hashSet.contains(2); &nbsp;&nbsp;&nbsp;// 返回 true
hashSet.remove(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
hashSet.contains(2); &nbsp;&nbsp;&nbsp;// 返回  false (已经被删除)
</pre>

<p><br>
<strong>注意：</strong></p>

<ul>
	<li>所有的值都在&nbsp;<code>[1, 1000000]</code>的范围内。</li>
	<li>操作的总数目在<code>[1, 10000]</code>范围内。</li>
	<li>不要使用内建的哈希集合库。</li>
</ul>
<p>不使用任何内建的哈希表库设计一个哈希集合</p>

<p>具体地说，你的设计应该包含以下的功能</p>

<ul>
	<li><code>add(value)</code>：向哈希集合中插入一个值。</li>
	<li><code>contains(value)</code> ：返回哈希集合中是否存在这个值。</li>
	<li><code>remove(value)</code>：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。</li>
</ul>

<p><br>
<strong>示例:</strong></p>

<pre>MyHashSet hashSet = new MyHashSet();
hashSet.add(1); &nbsp; &nbsp; &nbsp; &nbsp; 
hashSet.add(2); &nbsp; &nbsp; &nbsp; &nbsp; 
hashSet.contains(1); &nbsp;&nbsp;&nbsp;// 返回 true
hashSet.contains(3); &nbsp;&nbsp;&nbsp;// 返回 false (未找到)
hashSet.add(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
hashSet.contains(2); &nbsp;&nbsp;&nbsp;// 返回 true
hashSet.remove(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
hashSet.contains(2); &nbsp;&nbsp;&nbsp;// 返回  false (已经被删除)
</pre>

<p><br>
<strong>注意：</strong></p>

<ul>
	<li>所有的值都在&nbsp;<code>[1, 1000000]</code>的范围内。</li>
	<li>操作的总数目在<code>[1, 10000]</code>范围内。</li>
	<li>不要使用内建的哈希集合库。</li>
</ul>
*/


typedef struct {
    
} MyHashSet;

/** Initialize your data structure here. */
MyHashSet* myHashSetCreate() {
    
}

void myHashSetAdd(MyHashSet* obj, int key) {
    
}

void myHashSetRemove(MyHashSet* obj, int key) {
    
}

/** Returns true if this set did not already contain the specified element */
bool myHashSetContains(MyHashSet* obj, int key) {
    
}

void myHashSetFree(MyHashSet* obj) {
    
}

/**
 * Your MyHashSet struct will be instantiated and called as such:
 * struct MyHashSet* obj = myHashSetCreate();
 * myHashSetAdd(obj, key);
 * myHashSetRemove(obj, key);
 * bool param_3 = myHashSetContains(obj, key);
 * myHashSetFree(obj);
 */