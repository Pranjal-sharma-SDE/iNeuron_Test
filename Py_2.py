def min_distance_between_horses(stalls, k):
    stalls.sort()

    def is_valid(mid):
        horses_placed = 1
        last_position = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - last_position >= mid:
                horses_placed += 1
                last_position = stalls[i]

        return horses_placed >= k

    low, high = 0, stalls[-1] - stalls[0]
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if is_valid(mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

# Example
stalls = [1, 2, 4, 8, 9]
k = 3
result = min_distance_between_horses(stalls, k)
print("Output:", result)


stalls2 = [ 1, 2, 3, 4, 6, 8, 9, 10 ]
k2 = 6
result2 = min_distance_between_horses(stalls2, k2)
print("Output:", result2)