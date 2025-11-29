def merge_k_lists(lists: list[list[int]]):

    if not isinstance(lists, list):
        raise TypeError("Argument musts be a list of lists")

    if not all([isinstance(sub, list) for sub in lists]):
        raise TypeError("Argument musts be a list of lists")

    if not len(lists):
        return []

    lens: dict[int, int] = {}
    for n in range(len(lists)):
        if len(lists[n]) != 0:
            lens.update({n: len(lists[n])})

    out = []
    while lens:

        key = list(lens.keys())[0]
        min_pair = (key, lists[key][0])

        for key in lens:
            if lists[key][0] < min_pair[1]:
                min_pair = (key, lists[key][0])

        out.append(min_pair[1])

        lists[min_pair[0]].pop(0)

        lens[min_pair[0]] -= 1
        if lens[min_pair[0]] == 0:
            del lens[min_pair[0]]

    return out



def main():
    def test(input):
        print(input, end="\n")
        print(merge_k_lists(input))
        print()

    test([[1, 4, 5], [1, 3, 4], [2, 6]])
    test([[1, 4, 5], [1, 2, 32, 43, 56]])
    test([[1, 4, 5], []])
    test([[1, 4, 12], [], [5, 8, 10]])
    test([])

if __name__ == "__main__":
    main()
