from random import randint
from timeit import repeat



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j]:
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key
    return lst


def test(arr: list[int], func, name: str):

    REPEAT_TIMES = 10

    times = repeat(
        lambda: func(arr.copy()),
        repeat=REPEAT_TIMES,
        number=1
    )

    print(f"{name}".ljust(16), f"{REPEAT_TIMES} inerations")
    print(f"MIN: {min(times):.4f} seconds")
    print(f"MAX: {max(times):.4f} seconds")
    print(f"AVR: {sum(times)/len(times):.4f} seconds")
    print(f"SUM: {sum(times):.4f} seconds")
    print()

def main():
    N = 10_000

    datasets = {
        "Random": [randint(-(2**31), (2**31)-1) for _ in range(N)],
        "Sorted": list(range(N)),
        "Reversed": list(range(N, 0, -1)),
    }

    for name in datasets:
        print('=' * 30)
        print(f"Dataset:  {name}")
        print('=' * 30)
        test(datasets[name], sorted, "Timsort")
        test(datasets[name], merge_sort, "Merge Sort")
        test(datasets[name], insertion_sort, "Insertion Sort")
        print()

if __name__ == "__main__":
    main()
