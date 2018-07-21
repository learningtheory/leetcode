"""
<p>Implement a data structure supporting the following operations:</p>

<p>
<ol>
<li>Inc(Key) - Inserts a new key <Key> with value 1. Or increments an existing key by 1. Key is guaranteed to be a <b>non-empty</b> string.</li>
<li>Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a <b>non-empty</b> string.</li>
<li>GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string <code>""</code>.</li>
<li>GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string <code>""</code>.</li>
</ol>
</p>

<p>
Challenge: Perform all these in O(1) time complexity.
</p><p>实现一个数据结构支持以下操作：</p>

<ol>
	<li>Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。</li>
	<li>Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否者使一个存在的 key 值减一。如果这个 key 不存在，这个函数不做任何事情。key 保证不为空字符串。</li>
	<li>GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串<code>&quot;&quot;</code>。</li>
	<li>GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串<code>&quot;&quot;</code>。</li>
</ol>

<p>挑战：以 O(1) 的时间复杂度实现所有操作。</p>
<p>实现一个数据结构支持以下操作：</p>

<ol>
	<li>Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。</li>
	<li>Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否者使一个存在的 key 值减一。如果这个 key 不存在，这个函数不做任何事情。key 保证不为空字符串。</li>
	<li>GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串<code>&quot;&quot;</code>。</li>
	<li>GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串<code>&quot;&quot;</code>。</li>
</ol>

<p>挑战：以 O(1) 的时间复杂度实现所有操作。</p>
"""


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()