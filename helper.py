from random import randrange


def random_or(first, second):
    return randrange(first, second + 1, abs(first - second))


def fit_range(value, target_range):
    return min(target_range[-1], max(target_range[0], value))
