def main():
    '''This approach maintains two lists of tuples. 'data' acts as a
    permanent record of the starting order. 'd' is the one we move around.
    Making a tuple of (index, value) means we can locate a specific value
    even if there are duplicates.'''

    data = [(i, int(val)*811589153) for i, val in enumerate(open('/path/to/advent_day20_input.txt').readlines())]
    d = data.copy()
    # Both take the form: [(0, 7834270093909), (1, 5200663292424), (2, -2959865640991), ... ]

    for _ in range(10):  # Number of mixings
        for pair in data:
            val = pair[1]
            idx = d.index(pair)
            target = (idx + val)%(len(d)-1)
            d.insert(target, d.pop(idx))

    # reorder the list, starting with 0
    zero_index = d.index((316, 0))
    signal = [v for k, v in (d[zero_index:] + d[:zero_index])]

    answer = sum([signal[(x+1)*1000%len(signal)] for x in range(3)])
    print(answer)


if __name__ == '__main__':
    main()
