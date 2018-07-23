"""
<p>You are given two <b>non-empty</b> linked lists representing two non-negative integers. The digits are stored in <b>reverse order</b> and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>
<b>Example</b>
<pre>
<b>Input:</b> (2 -> 4 -> 3) + (5 -> 6 -> 4)
<b>Output:</b> 7 -> 0 -> 8
<b>Explanation:</b> 342 + 465 = 807.
</pre>
</p><p>给定两个<strong>非空</strong>链表来表示两个非负整数。位数按照<strong>逆序</strong>方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。</p>

<p>你可以假设除了数字 0 之外，这两个数字都不会以零开头。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>(2 -&gt; 4 -&gt; 3) + (5 -&gt; 6 -&gt; 4)
<strong>输出：</strong>7 -&gt; 0 -&gt; 8
<strong>原因：</strong>342 + 465 = 807
</pre>
<p>给定两个<strong>非空</strong>链表来表示两个非负整数。位数按照<strong>逆序</strong>方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。</p>

<p>你可以假设除了数字 0 之外，这两个数字都不会以零开头。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>(2 -&gt; 4 -&gt; 3) + (5 -&gt; 6 -&gt; 4)
<strong>输出：</strong>7 -&gt; 0 -&gt; 8
<strong>原因：</strong>342 + 465 = 807
</pre>
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        """
        1562 个通过测试用例
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            raise Exception('l1 or l2 is None!')
        sum1 = sum2 = 0
        k = 0
        while l1 or l2:
            k += 1
            if l1:
                sum1 += l1.val * 10 ** k
                l1 = l1.next

            if l2:
                sum2 += l2.val * 10 ** k
                l2 = l2.next

        # 获取逆序的数字字符
        # sum_str = str(sum1 + sum2)
        strs = str(sum1 + sum2)[::-1]
        # 判断溢位
        bit = max([len(str(sum1)), len(str(sum2))])
        l = len(strs) - bit
        if l >= 0 and strs.startswith('0') and len(strs) > 1:
            strs = strs[1:]
        # 相差三位
        sum_str = str(int(strs)) if len(strs) > 3 and l >= 2 else strs
        # sum_str = str(int(str(sum1 + sum2)[::-1]))
        # 创建listNode
        tmp = ListNode(0)
        for i in sum_str:
            self.appendNext(tmp, int(i))

        res = tmp.next
        return res

    def appendNext(self, res, content):
        if res.next is None:
            res.next = ListNode(content)
        else:
            self.appendNext(res.next, content)

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        tmp = ListNode(0)
        res = tmp
        flag = 0
        while l1 or l2:
            tmpsum = 0
            if l1:
                tmpsum = l1.val
                l1 = l1.next
            if l2:
                tmpsum += l2.val
                l2 = l2.next
            tmpres = ((tmpsum + flag) % 10)
            flag = ((tmpsum + flag) // 10)
            res.next = ListNode(tmpres)
            res = res.next
        if flag:
            res.next = ListNode(1)
        res = tmp.next
        del tmp
        return res


def pro(l1, l2):
    a = Solution().addTwoNumbers(l1, l2)
    print('==============')
    while a is not None:
        print(a.val)
        a = a.next


if __name__ == '__main__':
    # 899
    # 0 0
    l1 = ListNode(0)
    l2 = ListNode(1)
    pro(l1, l2)
    print('+++++++++++++++')

    #
    l1 = ListNode(0)
    l2 = ListNode(0)
    pro(l1, l2)
    print('+++++++++++++++')

    l1 = ListNode(8)
    l2 = ListNode(2)
    Solution().appendNext(l1, 9)
    Solution().appendNext(l1, 9)
    pro(l1, l2)
    print('+++++++++++++++')

    #
    l1 = ListNode(5)
    l2 = ListNode(5)
    pro(l1, l2)
    print('+++++++++++++++')

    l1 = ListNode(2)
    l2 = ListNode(5)
    Solution().appendNext(l1, 4)
    Solution().appendNext(l1, 3)
    Solution().appendNext(l2, 6)
    Solution().appendNext(l2, 4)
    pro(l1, l2)
    print('+++++++++++++++')
