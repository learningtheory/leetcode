/*
<p>Implement the following operations of a stack using queues.</p>

<ul>
	<li>push(x) -- Push element x onto stack.</li>
	<li>pop() -- Removes the element on top of the stack.</li>
	<li>top() -- Get the top element.</li>
	<li>empty() -- Return whether the stack is empty.</li>
</ul>

<p><b>Example:</b></p>

<pre>
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false</pre>

<p><b>Notes:</b></p>

<ul>
	<li>You must use <i>only</i> standard operations of a queue -- which means only <code>push to back</code>, <code>peek/pop from front</code>, <code>size</code>, and <code>is empty</code> operations are valid.</li>
	<li>Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.</li>
	<li>You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).</li>
</ul>
<p>使用队列实现栈的下列操作：</p>

<ul>
	<li>push(x) -- 元素 x 入栈</li>
	<li>pop() -- 移除栈顶元素</li>
	<li>top() -- 获取栈顶元素</li>
	<li>empty() -- 返回栈是否为空</li>
</ul>

<p><strong>注意:</strong></p>

<ul>
	<li>你只能使用队列的基本操作-- 也就是&nbsp;<code>push to back</code>, <code>peek/pop from front</code>, <code>size</code>, 和&nbsp;<code>is empty</code>&nbsp;这些操作是合法的。</li>
	<li>你所使用的语言也许不支持队列。&nbsp;你可以使用 list 或者 deque（双端队列）来模拟一个队列&nbsp;, 只要是标准的队列操作即可。</li>
	<li>你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。</li>
</ul>
<p>使用队列实现栈的下列操作：</p>

<ul>
	<li>push(x) -- 元素 x 入栈</li>
	<li>pop() -- 移除栈顶元素</li>
	<li>top() -- 获取栈顶元素</li>
	<li>empty() -- 返回栈是否为空</li>
</ul>

<p><strong>注意:</strong></p>

<ul>
	<li>你只能使用队列的基本操作-- 也就是&nbsp;<code>push to back</code>, <code>peek/pop from front</code>, <code>size</code>, 和&nbsp;<code>is empty</code>&nbsp;这些操作是合法的。</li>
	<li>你所使用的语言也许不支持队列。&nbsp;你可以使用 list 或者 deque（双端队列）来模拟一个队列&nbsp;, 只要是标准的队列操作即可。</li>
	<li>你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。</li>
</ul>
*/


typedef struct {
    
} MyStack;

/** Initialize your data structure here. */
MyStack* myStackCreate(int maxSize) {
    
}

/** Push element x onto stack. */
void myStackPush(MyStack* obj, int x) {
    
}

/** Removes the element on top of the stack and returns that element. */
int myStackPop(MyStack* obj) {
    
}

/** Get the top element. */
int myStackTop(MyStack* obj) {
    
}

/** Returns whether the stack is empty. */
bool myStackEmpty(MyStack* obj) {
    
}

void myStackFree(MyStack* obj) {
    
}

/**
 * Your MyStack struct will be instantiated and called as such:
 * struct MyStack* obj = myStackCreate(maxSize);
 * myStackPush(obj, x);
 * int param_2 = myStackPop(obj);
 * int param_3 = myStackTop(obj);
 * bool param_4 = myStackEmpty(obj);
 * myStackFree(obj);
 */