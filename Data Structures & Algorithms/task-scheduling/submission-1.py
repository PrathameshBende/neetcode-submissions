from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        pq = [(count, task) for task, count in freq.items()]
        heapq.heapify_max(pq)

        cooldown = deque()
        time = 0

        while pq or cooldown:
            time += 1

            if cooldown and cooldown[0][0] == time:
                _, count, task = cooldown.popleft()
                heapq.heappush_max(pq, (count, task))

            if pq:
                count, task = heapq.heappop_max(pq)
                count -= 1

                if count > 0:
                    cooldown.append((time + n + 1, count, task))

        return time