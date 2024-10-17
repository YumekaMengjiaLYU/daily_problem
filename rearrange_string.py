from collections import Counter
import heapq

def rearrange_string(s): 
    # Count number of times each value appears
    # Select values in order from most frequent to least frequent
    # Add selected value to final output, incrementing the index by 2 each time
    # Reset index to 1 if index out of bounds
    freq_dict = Counter(s)
    if max(freq_dict.values()) > len(s) // 2:
        return None
    char_list = []
    rearranged = [''] * len(s)
    heap = [(-count, char) for char, count in freq_dict.items()]
    heapq.heapify(heap)
    index = 0
    while heap:
        count, char = heapq.heappop(heap)
        for _ in range(-count):
            rearranged[index] = char
            index = index + 2 if index + 2 < len(s) else 1
            print(f"indx is {index}, list is {rearranged}")

    return "".join(rearranged)


if __name__ == "__main__":
    result = rearrange_string('abbccc')
    print(result)