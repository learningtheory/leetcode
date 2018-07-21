/*
<p>Suppose we abstract our file system by a string in the following manner:</p>

<p>The string <code>"dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"</code> represents:</p>

<pre>dir
    subdir1
    subdir2
        file.ext
</pre>

<p>The directory <code>dir</code> contains an empty sub-directory <code>subdir1</code> and a sub-directory <code>subdir2</code> containing a file <code>file.ext</code>.</p>

<p>The string <code>"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"</code> represents:</p>

<pre>dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
</pre>

<p>The directory <code>dir</code> contains two sub-directories <code>subdir1</code> and <code>subdir2</code>. <code>subdir1</code> contains a file <code>file1.ext</code> and an empty second-level sub-directory <code>subsubdir1</code>. <code>subdir2</code> contains a second-level sub-directory <code>subsubdir2</code> containing a file <code>file2.ext</code>.</p>

<p>We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is <code>"dir/subdir2/subsubdir2/file2.ext"</code>, and its length is <code>32</code> (not including the double quotes).</p>

<p>Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return <code>0</code>.</p>

<p><b>Note:</b><br />
<ul>
<li>The name of a file contains at least a <code>.</code> and an extension.</li>
<li>The name of a directory or sub-directory will not contain a <code>.</code>.</li>
</ul>
</p>

<p>Time complexity required: <code>O(n)</code> where <code>n</code> is the size of the input string.</p>

<p>Notice that <code>a/aa/aaa/file1.txt</code> is not the longest file path, if there is another path <code>aaaaaaaaaaaaaaaaaaaaa/sth.png</code>.</p><p>假设我们以下述方式将我们的文件系统抽象成一个字符串:</p>

<p>字符串&nbsp;<code>&quot;dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext&quot;</code> 表示:</p>

<pre>
dir
    subdir1
    subdir2
        file.ext
</pre>

<p>目录&nbsp;<code>dir</code> 包含一个空的子目录&nbsp;<code>subdir1</code> 和一个包含一个文件&nbsp;<code>file.ext</code>&nbsp;的子目录&nbsp;<code>subdir2</code> 。</p>

<p>字符串&nbsp;<code>&quot;dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext&quot;</code> 表示:</p>

<pre>
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
</pre>

<p>目录&nbsp;<code>dir</code> 包含两个子目录 <code>subdir1</code> 和&nbsp;<code>subdir2</code>。&nbsp;<code>subdir1</code> 包含一个文件&nbsp;<code>file1.ext</code> 和一个空的二级子目录 <code>subsubdir1</code>。<code>subdir2</code> 包含一个二级子目录&nbsp;<code>subsubdir2</code> ，其中包含一个文件&nbsp;<code>file2.ext</code>。</p>

<p>我们致力于寻找我们文件系统中文件的最长 (按字符的数量统计) 绝对路径。例如，在上述的第二个例子中，最长路径为&nbsp;<code>&quot;dir/subdir2/subsubdir2/file2.ext&quot;</code>，其长度为&nbsp;<code>32</code> (不包含双引号)。</p>

<p>给定一个以上述格式表示文件系统的字符串，返回文件系统中文件的最长绝对路径的长度。 如果系统中没有文件，返回&nbsp;<code>0</code>。</p>

<p><strong>说明:</strong></p>

<ul>
	<li>文件名至少存在一个&nbsp;<code>.</code> 和一个扩展名。</li>
	<li>目录或者子目录的名字不能包含&nbsp;<code>.</code>。</li>
</ul>

<p>要求时间复杂度为&nbsp;<code>O(n)</code>&nbsp;，其中&nbsp;<code>n</code> 是输入字符串的大小。</p>

<p>请注意，如果存在路径&nbsp;<code>aaaaaaaaaaaaaaaaaaaaa/sth.png</code>&nbsp;的话，那么&nbsp;&nbsp;<code>a/aa/aaa/file1.txt</code>&nbsp;就不是一个最长的路径。</p>
<p>假设我们以下述方式将我们的文件系统抽象成一个字符串:</p>

<p>字符串&nbsp;<code>&quot;dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext&quot;</code> 表示:</p>

<pre>
dir
    subdir1
    subdir2
        file.ext
</pre>

<p>目录&nbsp;<code>dir</code> 包含一个空的子目录&nbsp;<code>subdir1</code> 和一个包含一个文件&nbsp;<code>file.ext</code>&nbsp;的子目录&nbsp;<code>subdir2</code> 。</p>

<p>字符串&nbsp;<code>&quot;dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext&quot;</code> 表示:</p>

<pre>
dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
</pre>

<p>目录&nbsp;<code>dir</code> 包含两个子目录 <code>subdir1</code> 和&nbsp;<code>subdir2</code>。&nbsp;<code>subdir1</code> 包含一个文件&nbsp;<code>file1.ext</code> 和一个空的二级子目录 <code>subsubdir1</code>。<code>subdir2</code> 包含一个二级子目录&nbsp;<code>subsubdir2</code> ，其中包含一个文件&nbsp;<code>file2.ext</code>。</p>

<p>我们致力于寻找我们文件系统中文件的最长 (按字符的数量统计) 绝对路径。例如，在上述的第二个例子中，最长路径为&nbsp;<code>&quot;dir/subdir2/subsubdir2/file2.ext&quot;</code>，其长度为&nbsp;<code>32</code> (不包含双引号)。</p>

<p>给定一个以上述格式表示文件系统的字符串，返回文件系统中文件的最长绝对路径的长度。 如果系统中没有文件，返回&nbsp;<code>0</code>。</p>

<p><strong>说明:</strong></p>

<ul>
	<li>文件名至少存在一个&nbsp;<code>.</code> 和一个扩展名。</li>
	<li>目录或者子目录的名字不能包含&nbsp;<code>.</code>。</li>
</ul>

<p>要求时间复杂度为&nbsp;<code>O(n)</code>&nbsp;，其中&nbsp;<code>n</code> 是输入字符串的大小。</p>

<p>请注意，如果存在路径&nbsp;<code>aaaaaaaaaaaaaaaaaaaaa/sth.png</code>&nbsp;的话，那么&nbsp;&nbsp;<code>a/aa/aaa/file1.txt</code>&nbsp;就不是一个最长的路径。</p>
*/


class Solution {
public:
    int lengthLongestPath(string input) {
        
    }
};