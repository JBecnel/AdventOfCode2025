def merge_overlap_intervals(arr):
    
    # Sort intervals based on start values
    arr.sort()

    res = []
    res.append(arr[0])

    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]

        # If current interval overlaps with the last merged
        # interval, merge them 
        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)

    return res



intervals = []
file_name = "sample_input5.txt"
file_name = "input5.txt"
with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        
        if line != '':            
            # Parse the #-# format
            parts = line.split('-')
            intervals.append([int(parts[0]), int(parts[1])])
        else:
            break
            
#print(intervals)
merged_intervals = merge_overlap_intervals(intervals)
#print("Merged Intervals:", merged_intervals)

total = 0
for interval in merged_intervals:
    total += (interval[1] - interval[0] + 1)
print("Count of ingredients within ranges:", total)