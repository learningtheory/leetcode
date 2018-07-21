/**
<p>You are playing the following <a href="https://en.wikipedia.org/wiki/Bulls_and_Cows" target="_blank">Bulls and Cows</a> game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called &quot;bulls&quot;) and how many digits match the secret number but locate in the wrong position (called &quot;cows&quot;). Your friend will use successive guesses and hints to eventually derive the secret number.</p>

<p>Write a function to return a hint according to the secret number and friend&#39;s guess, use <code>A</code> to indicate the bulls and <code>B</code> to indicate the cows.&nbsp;</p>

<p>Please note that both secret number and friend&#39;s guess may contain duplicate digits.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> secret = &quot;1807&quot;, guess = &quot;7810&quot;

<strong>Output:</strong> &quot;1A3B&quot;

<strong>Explanation:</strong> <code>1</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;"> bull and </span><code>3</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;"> cows. The bull is </span><code>8</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">, the cows are </span><code>0</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">, </span><code>1</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;"> and </span><code>7<font face="sans-serif, Arial, Verdana, Trebuchet MS">.</font></code></pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> secret = &quot;1123&quot;, guess = &quot;0111&quot;

<strong>Output:</strong> &quot;1A1B&quot;

<strong>Explanation: </strong>The 1st <code>1 </code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">in friend&#39;s guess is a bull, the 2nd or 3rd </span><code>1</code><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;"> is a cow</span><span style="font-family: sans-serif, Arial, Verdana, &quot;Trebuchet MS&quot;;">.</span></pre>

<p><strong>Note: </strong>You may assume that the secret number and your friend&#39;s guess only contain digits, and their lengths are always equal.</p><p>你正在和你的朋友玩&nbsp;<a href="https://baike.baidu.com/item/%E7%8C%9C%E6%95%B0%E5%AD%97/83200?fromtitle=Bulls+and+Cows&amp;fromid=12003488&amp;fr=aladdin" target="_blank">猜数字（Bulls and Cows）</a>游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对了（称为&ldquo;Bulls&rdquo;, 公牛），有多少位数字猜对了但是位置不对（称为&ldquo;Cows&rdquo;, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。</p>

<p>请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 <code>A</code> 表示公牛，用&nbsp;<code>B</code>&nbsp;表示奶牛。</p>

<p>请注意秘密数字和朋友的猜测数都可能含有重复数字。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> secret = &quot;1807&quot;, guess = &quot;7810&quot;

<strong>输出:</strong> &quot;1A3B&quot;

<strong>解释:</strong> <code>1</code>&nbsp;公牛和&nbsp;<code>3</code>&nbsp;奶牛。公牛是 <code>8</code>，奶牛是 <code>0</code>, <code>1</code>&nbsp;和 <code>7</code>。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> secret = &quot;1123&quot;, guess = &quot;0111&quot;

<strong>输出:</strong> &quot;1A1B&quot;

<strong>解释: </strong>朋友猜测数中的第一个 <code>1</code>&nbsp;是公牛，第二个或第三个 <code>1</code>&nbsp;可被视为奶牛。</pre>

<p><strong>说明: </strong>你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。</p>
<p>你正在和你的朋友玩&nbsp;<a href="https://baike.baidu.com/item/%E7%8C%9C%E6%95%B0%E5%AD%97/83200?fromtitle=Bulls+and+Cows&amp;fromid=12003488&amp;fr=aladdin" target="_blank">猜数字（Bulls and Cows）</a>游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对了（称为&ldquo;Bulls&rdquo;, 公牛），有多少位数字猜对了但是位置不对（称为&ldquo;Cows&rdquo;, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。</p>

<p>请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 <code>A</code> 表示公牛，用&nbsp;<code>B</code>&nbsp;表示奶牛。</p>

<p>请注意秘密数字和朋友的猜测数都可能含有重复数字。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> secret = &quot;1807&quot;, guess = &quot;7810&quot;

<strong>输出:</strong> &quot;1A3B&quot;

<strong>解释:</strong> <code>1</code>&nbsp;公牛和&nbsp;<code>3</code>&nbsp;奶牛。公牛是 <code>8</code>，奶牛是 <code>0</code>, <code>1</code>&nbsp;和 <code>7</code>。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> secret = &quot;1123&quot;, guess = &quot;0111&quot;

<strong>输出:</strong> &quot;1A1B&quot;

<strong>解释: </strong>朋友猜测数中的第一个 <code>1</code>&nbsp;是公牛，第二个或第三个 <code>1</code>&nbsp;可被视为奶牛。</pre>

<p><strong>说明: </strong>你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。</p>
**/


class Solution {
    public String getHint(String secret, String guess) {
        
    }
}