class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        pq = []
        for p, t in classes:
            n_p = p + 1
            n_t = t + 1
            heapq.heappush(pq, (p/t - n_p/n_t, p, t))

        for i in range(extraStudents):
            diff, p, t = heapq.heappop(pq)
            p = p + 1
            t = t + 1
            n_p = p + 1
            n_t = t + 1
            heapq.heappush(pq, (p/t - n_p/n_t, p, t))

        res = 0.0
        while pq:
            diff, p, t = heapq.heappop(pq)
            res += p/t
        return res/n
        