def first(size, *args ):
    total_args = len(args)
    return size + total_args


def second(size, **args):
    total_args = len(args)
    return size + total_args