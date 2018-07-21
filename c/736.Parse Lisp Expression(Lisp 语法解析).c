/*
<p>
You are given a string <code>expression</code> representing a Lisp-like expression to return the integer value of.
</p><p>
The syntax for these expressions is given as follows.
</p><p>
<li>An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable.  Expressions always evaluate to a single integer.</li>
</p><p>
<li>(An integer could be positive or negative.)</li>
</p><p>
<li>A let-expression takes the form <code>(let v1 e1 v2 e2 ... vn en expr)</code>, where <code>let</code> is always the string <code>"let"</code>, then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable <code>v1</code> is assigned the value of the expression <code>e1</code>, the second variable <code>v2</code> is assigned the value of the expression <code>e2</code>, and so on <b>sequentially</b>; and then the value of this let-expression is the value of the expression <code>expr</code>.</li>
</p><p>
<li>An add-expression takes the form <code>(add e1 e2)</code> where <code>add</code> is always the string <code>"add"</code>, there are always two expressions <code>e1, e2</code>, and this expression evaluates to the addition of the evaluation of <code>e1</code> and the evaluation of <code>e2</code>.</li>
</p><p>
<li>A mult-expression takes the form <code>(mult e1 e2)</code> where <code>mult</code> is always the string <code>"mult"</code>, there are always two expressions <code>e1, e2</code>, and this expression evaluates to the multiplication of the evaluation of <code>e1</code> and the evaluation of <code>e2</code>.</li>
</p><p>
<li>For the purposes of this question, we will use a smaller subset of variable names.  A variable starts with a lowercase letter, then zero or more lowercase letters or digits.  Additionally for your convenience, the names "add", "let", or "mult" are protected and will never be used as variable names.</li>
</p><p>
<li>Finally, there is the concept of scope.  When an expression of a variable name is evaluated, <b>within the context of that evaluation</b>, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially.  It is guaranteed that every expression is legal.  Please see the examples for more details on scope.</li>
</p>

<p><b>Evaluation Examples:</b><br />
<pre>
<b>Input:</b> (add 1 2)
<b>Output:</b> 3

<b>Input:</b> (mult 3 (add 2 3))
<b>Output:</b> 15

<b>Input:</b> (let x 2 (mult x 5))
<b>Output:</b> 10

<b>Input:</b> (let x 2 (mult x (let x 3 y 4 (add x y))))
<b>Output:</b> 14
<b>Explanation:</b> In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.

<b>Input:</b> (let x 3 x 2 x)
<b>Output:</b> 2
<b>Explanation:</b> Assignment in let statements is processed sequentially.

<b>Input:</b> (let x 1 y 2 x (add x y) (add x y))
<b>Output:</b> 5
<b>Explanation:</b> The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.

<b>Input:</b> (let x 2 (add (let x 3 (let x 4 x)) x))
<b>Output:</b> 6
<b>Explanation:</b> Even though (let x 4 x) has a deeper scope, it is outside the context
of the final x in the add-expression.  That final x will equal 2.

<b>Input:</b> (let a1 3 b2 (add a1 1) b2) 
<b>Output</b> 4
<b>Explanation:</b> Variable names can contain digits after the first character.

</pre>

<p><b>Note:</b>
<li>The given string <code>expression</code> is well formatted: There are no leading or trailing spaces, there is only a single space separating different components of the string, and no space between adjacent parentheses.  The expression is guaranteed to be legal and evaluate to an integer.</li>
<li>The length of <code>expression</code> is at most 2000.  (It is also non-empty, as that would not be a legal expression.)</li>
<li>The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.</li>
</p><p>给定一个类似 Lisp 语句的表达式 <code>expression</code>，求出其计算结果。</p>

<p>表达式语法如下所示:</p>

<ul>
	<li>表达式可以为整数，let 语法，add 语法，mult 语法。表达式的结果总是一个整数。</li>
	<li>(整数可以是正整数、负整数、0)</li>
	<li>let 语法表示为&nbsp;<code>(let v1 e1 v2 e2 ... vn en expr)</code>,&nbsp;其中&nbsp;<code>let</code>语法总是以字符串&nbsp;<code>&quot;let&quot;</code>来表示，接下来会跟随一个或多个交替变量或表达式，也就是说，第一个变量&nbsp;<code>v1</code>被分配为表达式&nbsp;<code>e1</code>&nbsp;的值，第二个变量&nbsp;<code>v2</code>&nbsp;被分配为表达式&nbsp;<code>e2</code>&nbsp;的值，<strong>以此类推</strong>；最终 let 语法的值为&nbsp;<code>expr</code>表达式的值。</li>
	<li>add语法表示为&nbsp;<code>(add e1 e2)</code>，其中&nbsp;<code>add</code>&nbsp;语法总是以字符串&nbsp;<code>&quot;add&quot;</code>来表示，该语法总是有两个表达式<code>e1</code><font color="#333333" face="Helvetica Neue, Helvetica, Arial, sans-serif"><span style="background-color:#ffffff; font-size:14px">、</span></font><code>e2</code>, 该语法的最终结果是&nbsp;<code>e1</code> 表达式的值与&nbsp;<code>e2</code>&nbsp;表达式的值之<strong>和</strong>。</li>
	<li>mult语法表示为&nbsp;<code>(mult e1 e2)</code>&nbsp;，其中&nbsp;<code>mult</code>&nbsp;语法总是以字符串<code>&quot;mult&quot;</code>表示， 该语法总是有两个表达式 <code>e1</code>、<code>e2</code>，该语法的最终结果是&nbsp;<code>e1</code> 表达式的值与&nbsp;<code>e2</code>&nbsp;表达式的值之<strong>积</strong>。</li>
	<li>在该题目中，变量的命名以小写字符开始，之后跟随0个或多个小写字符或数字。为了方便，&quot;add&quot;，&quot;let&quot;，&quot;mult&quot;会被定义为&quot;关键字&quot;，不会在表达式的变量命名中出现。</li>
	<li>最后，要说一下范围的概念。在做计算时，<strong>需要注意优先级</strong>，在最内层(根据括号)的表达式的值应该先计算,然后依次计算外层的表达式。我们将保证每一个测试的表达式都是合法的。有关范围的更多详细信息，请参阅示例。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> (add 1 2)
<strong>输出:</strong> 3

<strong>输入:</strong> (mult 3 (add 2 3))
<strong>输出:</strong> 15

<strong>输入:</strong> (let x 2 (mult x 5))
<strong>输出:</strong> 10

<strong>输入:</strong> (let x 2 (mult x (let x 3 y 4 (add x y))))
<strong>输出:</strong> 14
<strong>解释:</strong> 
表达式 (add x y), 在获取 x 值时, 我们应当由最内层依次向外计算, 首先遇到了 x=3, 所以此处的 x 值是 3.


<strong>输入:</strong> (let x 3 x 2 x)
<strong>输出:</strong> 2
<strong>解释:</strong> let 语句中的赋值运算按顺序处理即可

<strong>输入:</strong> (let x 1 y 2 x (add x y) (add x y))
<strong>输出:</strong> 5
<strong>解释:</strong> 
第一个 (add x y) 计算结果是 3，并且将此值赋给了 x 。
第二个 (add x y) 计算结果就是 3+2 = 5 。

<strong>输入:</strong> (let x 2 (add (let x 3 (let x 4 x)) x))
<strong>输出:</strong> 6
<strong>解释:</strong> 
(let x 4 x) 中的 x 的作用范围仅在()之内。所以最终做加法操作时，x 的值是 2 。

<strong>输入:</strong> (let a1 3 b2 (add a1 1) b2) 
<strong>输出: </strong>4
<strong>解释:</strong> 
变量命名时可以在第一个小写字母后跟随数字.

</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<ul>
	<li>我们给定的&nbsp;<code>expression</code>&nbsp;表达式都是格式化后的：表达式前后没有多余的空格，表达式的不同部分(关键字、变量、表达式)之间仅使用一个空格分割，并且在相邻括号之间也没有空格。我们给定的表达式均为合法的且最终结果为整数。</li>
	<li>我们给定的表达式长度最多为 2000&nbsp;(表达式也不会为空，因为那不是一个合法的表达式)。</li>
	<li>最终的结果和中间的计算结果都将是一个 32 位整数。</li>
</ul>

<p>&nbsp;</p>
<p>给定一个类似 Lisp 语句的表达式 <code>expression</code>，求出其计算结果。</p>

<p>表达式语法如下所示:</p>

<ul>
	<li>表达式可以为整数，let 语法，add 语法，mult 语法。表达式的结果总是一个整数。</li>
	<li>(整数可以是正整数、负整数、0)</li>
	<li>let 语法表示为&nbsp;<code>(let v1 e1 v2 e2 ... vn en expr)</code>,&nbsp;其中&nbsp;<code>let</code>语法总是以字符串&nbsp;<code>&quot;let&quot;</code>来表示，接下来会跟随一个或多个交替变量或表达式，也就是说，第一个变量&nbsp;<code>v1</code>被分配为表达式&nbsp;<code>e1</code>&nbsp;的值，第二个变量&nbsp;<code>v2</code>&nbsp;被分配为表达式&nbsp;<code>e2</code>&nbsp;的值，<strong>以此类推</strong>；最终 let 语法的值为&nbsp;<code>expr</code>表达式的值。</li>
	<li>add语法表示为&nbsp;<code>(add e1 e2)</code>，其中&nbsp;<code>add</code>&nbsp;语法总是以字符串&nbsp;<code>&quot;add&quot;</code>来表示，该语法总是有两个表达式<code>e1</code><font color="#333333" face="Helvetica Neue, Helvetica, Arial, sans-serif"><span style="background-color:#ffffff; font-size:14px">、</span></font><code>e2</code>, 该语法的最终结果是&nbsp;<code>e1</code> 表达式的值与&nbsp;<code>e2</code>&nbsp;表达式的值之<strong>和</strong>。</li>
	<li>mult语法表示为&nbsp;<code>(mult e1 e2)</code>&nbsp;，其中&nbsp;<code>mult</code>&nbsp;语法总是以字符串<code>&quot;mult&quot;</code>表示， 该语法总是有两个表达式 <code>e1</code>、<code>e2</code>，该语法的最终结果是&nbsp;<code>e1</code> 表达式的值与&nbsp;<code>e2</code>&nbsp;表达式的值之<strong>积</strong>。</li>
	<li>在该题目中，变量的命名以小写字符开始，之后跟随0个或多个小写字符或数字。为了方便，&quot;add&quot;，&quot;let&quot;，&quot;mult&quot;会被定义为&quot;关键字&quot;，不会在表达式的变量命名中出现。</li>
	<li>最后，要说一下范围的概念。在做计算时，<strong>需要注意优先级</strong>，在最内层(根据括号)的表达式的值应该先计算,然后依次计算外层的表达式。我们将保证每一个测试的表达式都是合法的。有关范围的更多详细信息，请参阅示例。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> (add 1 2)
<strong>输出:</strong> 3

<strong>输入:</strong> (mult 3 (add 2 3))
<strong>输出:</strong> 15

<strong>输入:</strong> (let x 2 (mult x 5))
<strong>输出:</strong> 10

<strong>输入:</strong> (let x 2 (mult x (let x 3 y 4 (add x y))))
<strong>输出:</strong> 14
<strong>解释:</strong> 
表达式 (add x y), 在获取 x 值时, 我们应当由最内层依次向外计算, 首先遇到了 x=3, 所以此处的 x 值是 3.


<strong>输入:</strong> (let x 3 x 2 x)
<strong>输出:</strong> 2
<strong>解释:</strong> let 语句中的赋值运算按顺序处理即可

<strong>输入:</strong> (let x 1 y 2 x (add x y) (add x y))
<strong>输出:</strong> 5
<strong>解释:</strong> 
第一个 (add x y) 计算结果是 3，并且将此值赋给了 x 。
第二个 (add x y) 计算结果就是 3+2 = 5 。

<strong>输入:</strong> (let x 2 (add (let x 3 (let x 4 x)) x))
<strong>输出:</strong> 6
<strong>解释:</strong> 
(let x 4 x) 中的 x 的作用范围仅在()之内。所以最终做加法操作时，x 的值是 2 。

<strong>输入:</strong> (let a1 3 b2 (add a1 1) b2) 
<strong>输出: </strong>4
<strong>解释:</strong> 
变量命名时可以在第一个小写字母后跟随数字.

</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<ul>
	<li>我们给定的&nbsp;<code>expression</code>&nbsp;表达式都是格式化后的：表达式前后没有多余的空格，表达式的不同部分(关键字、变量、表达式)之间仅使用一个空格分割，并且在相邻括号之间也没有空格。我们给定的表达式均为合法的且最终结果为整数。</li>
	<li>我们给定的表达式长度最多为 2000&nbsp;(表达式也不会为空，因为那不是一个合法的表达式)。</li>
	<li>最终的结果和中间的计算结果都将是一个 32 位整数。</li>
</ul>

<p>&nbsp;</p>
*/


int evaluate(char* expression) {
    
}