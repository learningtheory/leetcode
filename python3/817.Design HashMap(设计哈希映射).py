"""
<p>Design a HashMap&nbsp;without using any built-in hash table libraries.</p>

<p>To be specific, your design should include these two functions:</p>

<ul>
	<li><code>put(key, value)</code> :&nbsp;Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.</li>
	<li><code>get(key)</code>: Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.</li>
	<li><code>remove(key)</code> :&nbsp;Remove the mapping for the value key if this map contains the mapping for the key.</li>
</ul>

<p><br />
<strong>Example:</strong></p>

<pre>
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
hashMap.put(2, 2); &nbsp; &nbsp; &nbsp; &nbsp; 
hashMap.get(1); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// returns 1
hashMap.get(3); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// returns -1 (not found)
hashMap.put(2, 1); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// update the existing value
hashMap.get(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// returns 1 
hashMap.remove(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// remove the mapping for 2
hashMap.get(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// returns -1 (not found) 
</pre>

<p><br />
<strong>Note:</strong></p>

<ul>
	<li>All values will be in the range of <code>[1, 1000000]</code>.</li>
	<li>The number of operations will be in the range of&nbsp;<code>[1, 10000]</code>.</li>
	<li>Please do not use the built-in HashMap library.</li>
</ul><p>不使用任何内建的哈希表库设计一个哈希映射</p>

<p>具体地说，你的设计应该包含以下的功能</p>

<ul>
	<li><code>put(key, value)</code>：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。</li>
	<li><code>get(key)</code>：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。</li>
	<li><code>remove(key)</code>：如果映射中存在这个键，删除这个数值对。</li>
</ul>

<p><br />
<strong>示例：</strong></p>

<pre>
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
hashMap.put(2, 2); &nbsp; &nbsp; &nbsp; &nbsp; 
hashMap.get(1); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// 返回 1
hashMap.get(3); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// 返回 -1 (未找到)
hashMap.put(2, 1); &nbsp; &nbsp; &nbsp; &nbsp; // 更新已有的值
hashMap.get(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// 返回 1 
hashMap.remove(2); &nbsp; &nbsp; &nbsp; &nbsp; // 删除键为2的数据
hashMap.get(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// 返回 -1 (未找到) 
</pre>

<p><br />
<strong>注意：</strong></p>

<ul>
	<li>所有的值都在&nbsp;<code>[1, 1000000]</code>的范围内。</li>
	<li>操作的总数目在<code>[1, 10000]</code>范围内。</li>
	<li>不要使用内建的哈希库。</li>
</ul>
<p>不使用任何内建的哈希表库设计一个哈希映射</p>

<p>具体地说，你的设计应该包含以下的功能</p>

<ul>
	<li><code>put(key, value)</code>：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。</li>
	<li><code>get(key)</code>：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。</li>
	<li><code>remove(key)</code>：如果映射中存在这个键，删除这个数值对。</li>
</ul>

<p><br />
<strong>示例：</strong></p>

<pre>
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;
hashMap.put(2, 2); &nbsp; &nbsp; &nbsp; &nbsp; 
hashMap.get(1); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// 返回 1
hashMap.get(3); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// 返回 -1 (未找到)
hashMap.put(2, 1); &nbsp; &nbsp; &nbsp; &nbsp; // 更新已有的值
hashMap.get(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// 返回 1 
hashMap.remove(2); &nbsp; &nbsp; &nbsp; &nbsp; // 删除键为2的数据
hashMap.get(2); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// 返回 -1 (未找到) 
</pre>

<p><br />
<strong>注意：</strong></p>

<ul>
	<li>所有的值都在&nbsp;<code>[1, 1000000]</code>的范围内。</li>
	<li>操作的总数目在<code>[1, 10000]</code>范围内。</li>
	<li>不要使用内建的哈希库。</li>
</ul>
"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)