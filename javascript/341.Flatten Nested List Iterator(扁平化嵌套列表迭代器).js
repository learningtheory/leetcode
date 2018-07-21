/*
<p>Given a nested list of integers, implement an iterator to flatten it.</p>

<p>Each element is either an integer, or a list -- whose elements may also be integers or other lists.</p>

<p><b>Example 1:</b><br />
Given the list <code>[[1,1],2,[1,1]]</code>,
<p>
By calling <i>next</i> repeatedly until <i>hasNext</i> returns false, the order of elements returned by <i>next</i> should be: <code>[1,1,2,1,1]</code>.
</p>
</p>

<p><b>Example 2:</b><br />
Given the list <code>[1,[4,[6]]]</code>,
<p>
By calling <i>next</i> repeatedly until <i>hasNext</i> returns false, the order of elements returned by <i>next</i> should be: <code>[1,4,6]</code>.
</p>
</p><p>给出一个嵌套的整型列表。设计一个迭代器，遍历这个整型列表中的所有整数。</p>

<p>列表中的项或者为一个整数，或者是另一个列表。</p>

<p><strong>示例 1:</strong><br />
给定列表&nbsp;<code>[[1,1],2,[1,1]]</code>,</p>

<p>通过重复调用&nbsp;<em>next </em>直到&nbsp;<em>hasNex</em>t 返回false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,1,2,1,1]</code>.</p>

<p><strong>示例&nbsp;2:</strong><br />
给定列表&nbsp;<code>[1,[4,[6]]]</code>,</p>

<p>通过重复调用&nbsp;<em>next&nbsp;</em>直到&nbsp;<em>hasNex</em>t 返回false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,4,6]</code>.</p>
<p>给出一个嵌套的整型列表。设计一个迭代器，遍历这个整型列表中的所有整数。</p>

<p>列表中的项或者为一个整数，或者是另一个列表。</p>

<p><strong>示例 1:</strong><br />
给定列表&nbsp;<code>[[1,1],2,[1,1]]</code>,</p>

<p>通过重复调用&nbsp;<em>next </em>直到&nbsp;<em>hasNex</em>t 返回false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,1,2,1,1]</code>.</p>

<p><strong>示例&nbsp;2:</strong><br />
给定列表&nbsp;<code>[1,[4,[6]]]</code>,</p>

<p>通过重复调用&nbsp;<em>next&nbsp;</em>直到&nbsp;<em>hasNex</em>t 返回false，<em>next&nbsp;</em>返回的元素的顺序应该是: <code>[1,4,6]</code>.</p>
*/


/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * function NestedInteger() {
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     @return {boolean}
 *     this.isInteger = function() {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     @return {integer}
 *     this.getInteger = function() {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds, if it holds a nested list
 *     Return null if this NestedInteger holds a single integer
 *     @return {NestedInteger[]}
 *     this.getList = function() {
 *         ...
 *     };
 * };
 */
/**
 * @constructor
 * @param {NestedInteger[]} nestedList
 */
var NestedIterator = function(nestedList) {
    
};


/**
 * @this NestedIterator
 * @returns {boolean}
 */
NestedIterator.prototype.hasNext = function() {
    
};

/**
 * @this NestedIterator
 * @returns {integer}
 */
NestedIterator.prototype.next = function() {
    
};

/**
 * Your NestedIterator will be called like this:
 * var i = new NestedIterator(nestedList), a = [];
 * while (i.hasNext()) a.push(i.next());
*/