def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        # Overlapping intervals
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged


intervals = [[1,3], [2,6], [8,10], [15,18]]

print(merge_intervals(intervals))

##############################################
def min_coins(coins, amount):
    result = {}

    for coin in sorted(coins, reverse=True):
        count = amount // coin

        if count:
            result[coin] = count

        amount %= coin

    return result


coins = [1, 2, 5]
amount = 18

print(min_coins(coins, amount))