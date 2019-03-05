class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        思路：给一个单词字典，把一个起始单词变为结束单词，每次只能变化一个字符，而且变化的中间词都在字典中，求最短的变化路径。

本质上是一个求无向无权图的单源最短路径问题，首选的解法是广度优先遍历（BFS）。
beginWord相当于路径的源点，而endWord相当于路径的终点。dictionary中的每个单词相当于一个节点，相互之间只差一个字符的两个单词其对应节点相互邻接，从而构成了一个无向无权图。
为了进行广度优先遍历，我们需要一个队列Queue作为辅助的数据结构。在进入循环之前，先把beginWord添加到队列中以初始化队列；当Queue为空时，结束循环。
由于题目要求的是路径的长度，我们可以用一个变量来记录广度优先遍历的当前层次数，并用一个内循环来完成一层遍历。这样，当找到endWord时，结束遍历，此时该变量的值就是路径的长度。

这道题的场景与图论中求单源最短路径不同之处在于，图论中遍历一个节点的邻接节点通常可以直接从该节点的属性中读取，而这道题中无法直接得到一个单词的邻接单词。
对于这个问题，有两种可以参考的解决思路：
（1）用一个Set来记录已经处理过的单词。每次要求一个单词A的邻接单词时，就遍历字典——如果当前单词不在Set（即还没有被处理过），就把当前单词入队列Queue；否则，表明该单词已经处理过，直接略过。
这种求邻接单词的方法需要遍历整个字典，因此时间复杂度为O(n)，其中n表示字典的规模。在最坏情况下，要对字典中的每一个单词都处理之后才能得到这道题的最终结果，因此这种解法的总的时间复杂度是O(n^2)。用到了两个辅助的数据结构——Set和Queue，最坏情形下需要2*n的辅助空间，因此空间复杂度为O(n)。

参考：

http://blog.csdn.net/lemonpi/article/details/78759263

http://www.cnblogs.com/love-yh/p/7136573.html
"""
    
        distance, cur, visited, lookup = 0, [beginWord],set([beginWord]),set(wordList)
        while cur:
            next_queue = []
            for word in cur:
                if word == endWord:
                    return distance + 1
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in lookup:
                            next_queue.append(candidate)
                            visited.add(candidate)
            distance += 1
            cur = next_queue
        return 0
