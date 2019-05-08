class Solution:
    def kClosest(self, points, K):
        heap = points[:K]
        for i in range(K//2, -1, -1):
            self.maintainHeap(heap, i, K)
        
        for j in range(K, len(points)):
            if(self.distanceSquare(points[j]) < self.distanceSquare(heap[0])):
                heap[0] = points[j]
                self.maintainHeap(heap, 0, K)
        
        return heap
    
    
    def maintainHeap(self, heap, i, length):
        left = i*2 + 1
        right = i*2 + 2
        largest = i
        if(left < length and self.distanceSquare(heap[left]) > self.distanceSquare(heap[i])):
            largest = left
        if(right < length and self.distanceSquare(heap[right]) > self.distanceSquare(heap[largest])):
            largest = right
        if(largest != i):
            heap[i], heap[largest] = heap[largest], heap[i]
            self.maintainHeap(heap, largest, length)
    
    def distanceSquare(self, point):
        return point[0]*point[0] + point[1]*point[1]


if __name__ == '__main__':

    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    S = Solution()
    print(Solution.kClosest(S, points, K))