"""
<p>Given a C++ program, remove comments from it. The program <code>source</code> is an array where <code>source[i]</code> is the <code>i</code>-th line of the source code.  This represents the result of splitting the original source code string by the newline character <code>\n</code>.</p>

<p>In C++, there are two types of comments, line comments, and block comments.</p>
<p>
The string <code>//</code> denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.
</p><p>
The string <code>/*</code> denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of <code>*/</code> should be ignored.  (Here, occurrences happen in reading order: line by line from left to right.)  To be clear, the string <code>/*/</code> does not yet end the block comment, as the ending would be overlapping the beginning.
</p><p>
The first effective comment takes precedence over others: if the string <code>//</code> occurs in a block comment, it is ignored. Similarly, if the string <code>/*</code> occurs in a line or block comment, it is also ignored.
</p><p>
If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.
</p><p>
There will be no control characters, single quote, or double quote characters.  For example, <code>source = "string s = "/* Not a comment. */";"</code> will not be a test case.  (Also, nothing else such as defines or macros will interfere with the comments.)
</p><p>
It is guaranteed that every open block comment will eventually be closed, so <code>/*</code> outside of a line or block comment always starts a new comment.
</p><p>
Finally, implicit newline characters can be deleted by block comments.  Please see the examples below for details.
</p>

<p>After removing the comments from the source code, return the source code in the same format.</p>

<p><b>Example 1:</b><br />
<pre style="white-space: pre-wrap">
<b>Input:</b> 
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

The line by line code is visualized as below:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}

<b>Output:</b> ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{ 
  
int a, b, c;
a = b + c;
}

<b>Explanation:</b> 
The string <code>/*</code> denotes a block comment, including line 1 and lines 6-9. The string <code>//</code> denotes line 4 as comments.
</pre>
</p>

<p><b>Example 2:</b><br />
<pre style="white-space: pre-wrap">
<b>Input:</b> 
source = ["a/*comment", "line", "more_comment*/b"]
<b>Output:</b> ["ab"]
<b>Explanation:</b> The original source string is "a/*comment<b>\n</b>line<b>\n</b>more_comment*/b", where we have bolded the newline characters.  After deletion, the <i>implicit</i> newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>source</code> is in the range <code>[1, 100]</code>.</li>
<li>The length of <code>source[i]</code> is in the range <code>[0, 80]</code>.</li>
<li>Every open block comment is eventually closed.</li>
<li>There are no single-quote, double-quote, or control characters in the source code.</li>
</p><p>给一个 C++ 程序，删除程序中的注释。这个程序<code>source</code>是一个数组，其中<code>source[i]</code>表示第<code>i</code>行源码。&nbsp;这表示每行源码由<code>\n</code>分隔。</p>

<p>在 C++ 中有两种注释风格，行内注释和块注释。</p>

<p>字符串<code>//</code> 表示行注释，表示<code>//</code>和其右侧的其余字符应该被忽略。</p>

<p>字符串<code>/*</code> 表示一个块注释，它表示直到<code>*/</code>的下一个（非重叠）出现的所有字符都应该被忽略。（阅读顺序为从左到右）非重叠是指，字符串<code>/*/</code>并没有结束块注释，因为注释的结尾与开头相重叠。</p>

<p>第一个有效注释优先于其他注释：如果字符串<code>//</code>出现在块注释中会被忽略。 同样，如果字符串<code>/*</code>出现在行或块注释中也会被忽略。</p>

<p>如果一行在删除注释之后变为空字符串，那么<strong>不要</strong>输出该行。即，答案列表中的每个字符串都是非空的。</p>

<p>样例中<strong>没有</strong>控制字符，单引号或双引号字符。比如，<code>source = &quot;string s = &quot;/* Not a comment. */&quot;;&quot;</code> 不会出现在测试样例里。（此外，没有其他内容（如定义或宏）会干扰注释。）</p>

<p>我们保证每一个块注释最终都会被闭合， 所以在行或块注释之外的<code>/*</code>总是开始新的注释。</p>

<p>最后，隐式换行符<strong>可以</strong>通过块注释删除。 有关详细信息，请参阅下面的示例。</p>

<p>从源代码中删除注释后，需要以相同的格式返回源代码。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> 
source = [&quot;/*Test program */&quot;, &quot;int main()&quot;, &quot;{ &quot;, &quot;  // variable declaration &quot;, &quot;int a, b, c;&quot;, &quot;/* This is a test&quot;, &quot;   multiline  &quot;, &quot;   comment for &quot;, &quot;   testing */&quot;, &quot;a = b + c;&quot;, &quot;}&quot;]

示例代码可以编排成这样:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}

<strong>输出:</strong> [&quot;int main()&quot;,&quot;{ &quot;,&quot;  &quot;,&quot;int a, b, c;&quot;,&quot;a = b + c;&quot;,&quot;}&quot;]

编排后:
int main()
{ 
  
int a, b, c;
a = b + c;
}

<strong>解释:</strong> 
第 1 行和第 6-9 行的字符串 /* 表示块注释。第 4 行的字符串 // 表示行注释。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
source = [&quot;a/*comment&quot;, &quot;line&quot;, &quot;more_comment*/b&quot;]
<strong>输出:</strong> [&quot;ab&quot;]
<strong>解释:</strong> 原始的 source 字符串是 &quot;a/*comment<strong>\n</strong>line<strong>\n</strong>more_comment*/b&quot;, 其中我们用粗体显示了换行符。删除注释后，隐含的换行符被删除，留下字符串 &quot;ab&quot; 用换行符分隔成数组时就是 [&quot;ab&quot;].
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>source</code>的长度范围为<code>[1, 100]</code>.</li>
	<li><code>source[i]</code>的长度范围为<code>[0, 80]</code>.</li>
	<li>每个块注释都会被闭合。</li>
	<li>给定的源码中不会有单引号、双引号或其他控制字符。</li>
</ul>
<p>给一个 C++ 程序，删除程序中的注释。这个程序<code>source</code>是一个数组，其中<code>source[i]</code>表示第<code>i</code>行源码。&nbsp;这表示每行源码由<code>\n</code>分隔。</p>

<p>在 C++ 中有两种注释风格，行内注释和块注释。</p>

<p>字符串<code>//</code> 表示行注释，表示<code>//</code>和其右侧的其余字符应该被忽略。</p>

<p>字符串<code>/*</code> 表示一个块注释，它表示直到<code>*/</code>的下一个（非重叠）出现的所有字符都应该被忽略。（阅读顺序为从左到右）非重叠是指，字符串<code>/*/</code>并没有结束块注释，因为注释的结尾与开头相重叠。</p>

<p>第一个有效注释优先于其他注释：如果字符串<code>//</code>出现在块注释中会被忽略。 同样，如果字符串<code>/*</code>出现在行或块注释中也会被忽略。</p>

<p>如果一行在删除注释之后变为空字符串，那么<strong>不要</strong>输出该行。即，答案列表中的每个字符串都是非空的。</p>

<p>样例中<strong>没有</strong>控制字符，单引号或双引号字符。比如，<code>source = &quot;string s = &quot;/* Not a comment. */&quot;;&quot;</code> 不会出现在测试样例里。（此外，没有其他内容（如定义或宏）会干扰注释。）</p>

<p>我们保证每一个块注释最终都会被闭合， 所以在行或块注释之外的<code>/*</code>总是开始新的注释。</p>

<p>最后，隐式换行符<strong>可以</strong>通过块注释删除。 有关详细信息，请参阅下面的示例。</p>

<p>从源代码中删除注释后，需要以相同的格式返回源代码。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> 
source = [&quot;/*Test program */&quot;, &quot;int main()&quot;, &quot;{ &quot;, &quot;  // variable declaration &quot;, &quot;int a, b, c;&quot;, &quot;/* This is a test&quot;, &quot;   multiline  &quot;, &quot;   comment for &quot;, &quot;   testing */&quot;, &quot;a = b + c;&quot;, &quot;}&quot;]

示例代码可以编排成这样:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}

<strong>输出:</strong> [&quot;int main()&quot;,&quot;{ &quot;,&quot;  &quot;,&quot;int a, b, c;&quot;,&quot;a = b + c;&quot;,&quot;}&quot;]

编排后:
int main()
{ 
  
int a, b, c;
a = b + c;
}

<strong>解释:</strong> 
第 1 行和第 6-9 行的字符串 /* 表示块注释。第 4 行的字符串 // 表示行注释。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> 
source = [&quot;a/*comment&quot;, &quot;line&quot;, &quot;more_comment*/b&quot;]
<strong>输出:</strong> [&quot;ab&quot;]
<strong>解释:</strong> 原始的 source 字符串是 &quot;a/*comment<strong>\n</strong>line<strong>\n</strong>more_comment*/b&quot;, 其中我们用粗体显示了换行符。删除注释后，隐含的换行符被删除，留下字符串 &quot;ab&quot; 用换行符分隔成数组时就是 [&quot;ab&quot;].
</pre>

<p><strong>注意:</strong></p>

<ul>
	<li><code>source</code>的长度范围为<code>[1, 100]</code>.</li>
	<li><code>source[i]</code>的长度范围为<code>[0, 80]</code>.</li>
	<li>每个块注释都会被闭合。</li>
	<li>给定的源码中不会有单引号、双引号或其他控制字符。</li>
</ul>
"""


class Solution:
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        