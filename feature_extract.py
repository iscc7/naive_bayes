# This part is data extractor
import math


def separate_by_class(data_set):
    separate = {}
    for i in range(len(data_set)):
        vector = data_set[i]
        if vector[-1] not in separate:
            separate[vector[-1]] = []
        separate[vector[-1]].append(vector[:-1])
    return separate


def mean(numbers):
    return sum(numbers)/len(numbers)


def std(numbers):
    av = mean(numbers)
    variance = sum([pow(x-av, 2) for x in numbers])/float(len(numbers)-1)
    return math.sqrt(variance)


def summary(data_set):
    summaries = [(mean(attribute), std(attribute)) for attribute in zip(*data_set)]
    return summaries


def summary_by_class(data_set):
    separate = separate_by_class(data_set)
    summaries = {}
    for class_value, instances in separate.iteritems():
        summaries[class_value] = summary(instances)
    return summaries

"""
if __name__ == '__main__':
    data_set = [[1, 20, 1], [2, 21, 0], [3, 22, 1], [4, 22, 0]]
    spearate = separate_by_class(data_set)
    print 'test1:\n'
    print spearate

    abstract = summary(data_set)
    print 'test2:\n'
    print abstract

    summaries = summary_by_class(data_set)
    print 'test3\n'
    print summaries
"""