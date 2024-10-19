import heapq

def closest_points(points, k):
    max_heap = []
    k = min(k, len(points))

    if len(points) == 0:
        return None
    
    max_heap = [(-(x**2 + y**2), (x,y)) for x, y in points[:k]]
    heapq.heapify(max_heap)

    for j in range(k, len(points)):
        largest_distance = -max_heap[0][0]
        cur_distance = points[j][0] ** 2 + points[j][1] ** 2
        if largest_distance > cur_distance:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-cur_distance, (points[j][0], points[j][1])))

    return [s[1] for s in heapq.nlargest(k, max_heap)]

if __name__ == "__main__":
    print(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))