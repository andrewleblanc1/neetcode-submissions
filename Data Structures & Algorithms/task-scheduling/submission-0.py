class Solution:
    import heapq
    from collections import deque
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #first get counts
        has = {}
        heap = []
        for task in tasks:
            if has.get(task) is None:
                has.update({task: 1})
            else:
                curr = has.get(task)
                curr += 1
                has.update({task:curr})
        for x in has.values():
            heapq.heappush_max(heap, x)
        queue = deque([])
        time = 0
        while heap or queue:
            time += 1
            if heap:
                curr = heapq.heappop_max(heap)
                curr -= 1
                if curr != 0:
                    queue.append([curr, n + time])
            if queue:
                if queue[0][1] == time:
                    curr = queue.popleft()
                    curr = curr[0]
                    heapq.heappush_max(heap, curr)
        return time

        
          


        


        