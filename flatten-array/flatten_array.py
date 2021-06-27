def flatten_helper(iterable):
    for item in iterable:
        if isinstance(item, (tuple, list)):
            yield from flatten_helper(item)
        elif item is not None:
            yield item


def flatten(iterable):
    return list(flatten_helper(iterable))

print(flatten([1, [2, 3, 4, 5, 6, 7], 8]))