import heapq

# class MedianFinder:

#     def __init__(self):

#         self.lst=[]

#     def addNum(self, num: int) -> None:
#         self.lst.append(num)

#     def findMedian(self) -> float:
#         self.lst.sort()
#         mid=len(self.lst)//2
#         if len(self.lst)%2==0:
#             return (self.lst[mid-1]+self.lst[mid])/2
#         else:
#             return self.lst[mid]


# # Your MedianFinder object will be instantiated and called as such:
# # obj = MedianFinder()
# # obj.addNum(num)
# # param_2 = obj.findMedian()


from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.s = SortedList()

    def addNum(self, num: int) -> None:
        self.s.add(num)

    def findMedian(self) -> float:
        l = len(self.s)
        if l%2==0:
            return (self.s[l//2-1]+self.s[l//2])/2
        return self.s[l//2]

class MedianFinder:

    def __init__(self):
        # Initialize data structure
        # two heaps, large(minheap), small(maxheap)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure every num in small is <= every num in large
        if (self.small and self.large and
                (-1 * self.small[0] > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()