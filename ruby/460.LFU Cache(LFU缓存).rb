=begin
<p>Design and implement a data structure for <a href="https://en.wikipedia.org/wiki/Least_frequently_used" target="_blank">Least Frequently Used (LFU)</a> cache. It should support the following operations: <code>get</code> and <code>put</code>.
</p>

<p>
<code>get(key)</code> - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.<br>
<code>put(key, value)</code> - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least <b>recently</b> used key would be evicted.
</p>

<p><b>Follow up:</b><br />
Could you do both operations in <b>O(1)</b> time complexity?</p>

<p><b>Example:</b>
<pre>
LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
</pre>
</p><p>设计并实现<a href="https://baike.baidu.com/item/%E7%BC%93%E5%AD%98%E7%AE%97%E6%B3%95">最不经常使用（LFU）</a>缓存的数据结构。它应该支持以下操作：<code>get</code>&nbsp;和&nbsp;<code>put</code>。</p>

<p><code>get(key)</code>&nbsp;- 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。<br />
<code>put(key, value)</code>&nbsp;- 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，<strong>最近</strong>最少使用的键将被去除。</p>

<p><strong>进阶：</strong><br />
你是否可以在&nbsp;<strong>O(1)&nbsp;</strong>时间复杂度内执行两项操作？</p>

<p><strong>示例：</strong></p>

<pre>
LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4</pre>
<p>设计并实现<a href="https://baike.baidu.com/item/%E7%BC%93%E5%AD%98%E7%AE%97%E6%B3%95">最不经常使用（LFU）</a>缓存的数据结构。它应该支持以下操作：<code>get</code>&nbsp;和&nbsp;<code>put</code>。</p>

<p><code>get(key)</code>&nbsp;- 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。<br />
<code>put(key, value)</code>&nbsp;- 如果键不存在，请设置或插入值。当缓存达到其容量时，它应该在插入新项目之前，使最不经常使用的项目无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，<strong>最近</strong>最少使用的键将被去除。</p>

<p><strong>进阶：</strong><br />
你是否可以在&nbsp;<strong>O(1)&nbsp;</strong>时间复杂度内执行两项操作？</p>

<p><strong>示例：</strong></p>

<pre>
LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4</pre>

=end


class LFUCache

=begin
    :type capacity: Integer
=end
    def initialize(capacity)
        
    end


=begin
    :type key: Integer
    :rtype: Integer
=end
    def get(key)
        
    end


=begin
    :type key: Integer
    :type value: Integer
    :rtype: Void
=end
    def put(key, value)
        
    end


end

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)