'''
逆波兰表达式是更利于计算机运算的表达式形式, 需要用到栈(先进后出的数据结构).

遍历表达式:

碰到数字则入栈
碰到运算符则连续从栈中取出2个元素, 使用该运算符运算然后将结果入栈
最后栈中剩余一个数字, 就是结果.
'''
class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i not in ('+', '-', '*', '/'):
                stack.append(int(i))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '+': stack.append(op1 + op2)
                elif i == '-': stack.append(op1 - op2)
                elif i == '*': stack.append(op1 * op2)
                else: stack.append(int(op1 * 1.0 / op2))
        return stack[0]
