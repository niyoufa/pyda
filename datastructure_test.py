#coding=utf-8

from collections import Counter
from collections import deque
from collections import defaultdict

if __name__ == "__main__":

    # Counter
    # li = ["Dog","Cat","Mouse","Cat","Dog"]
    # res = Counter(li)
    # print res
    # print len(set(li))
    # print "{0}:{1}".format(res.values(),res.keys())
    # print res.most_common(3)

    # deque
    # c = deque()
    # if isinstance(c, deque):
    #     for i in xrange(10):
    #         c.append(i)
    #     print c
    #
    #
    #     c.appendleft("niyoufa")
    #     print c
    #
    #     c.pop()
    #     print c
    #
    #     c.popleft()
    #     print c
    #
    #     c.rotate()
    #     print c
    #
    #     c.rotate(-1)
    #     print c

    #defaultdict
    # s  = "the quick brown fox jumps over the lazy dog"
    # words = s.split()
    # print words
    # location = defaultdict(list)
    # location[0]
    # for item in location:
    #     print item,location[item]
    # print location

    # array
    # import array
    # a = array.array("i",[1,2,3,4,5,"fas"])
    # print a

    # heapq 堆
    # heappush(heap, x)
    # 将x入堆

    # heappop(heap)
    # 将堆中最小的元素弹出

    # heapify(heap)
    # 将heap属性强制应用到任意一个列表

    # heapreplace(heap, x)
    # 将堆中最小的元素弹出，同时将x入堆

    # nlargest(n, iter)
    # 返回iter中第n大的元素

    # nsmallest(n, iter)
    # 返回iter中第n小的元素

    import heapq
    heap = [60,70]
    for i in [20,30,10,40,50]:
        heapq.heappush(heap,i)
    print heap
    print heapq.nlargest(len(heap),heap)
    print heapq.nsmallest(len(heap),heap)
    print heap
    while heap:
        print heapq.heappop(heap)

    heap = [{"name":"liuxiaoyan"},{"name":"niyoufa"}]
    print heap
    print heapq.nlargest(len(heap),heap,key=lambda x:x["name"])
