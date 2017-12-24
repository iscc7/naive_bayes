import csv
import random


def load_csv(filename):
    lines = csv.reader(open(filename, 'rb'))
    data_set = list(lines)
    for item in range(len(data_set)):
        data_set[item] = [float(x) for x in data_set[item]]
    return data_set


def spilt_data(all_data, ratio):

    train_size = len(all_data) * ratio
    train_set = []
    copy = list(all_data[:])
    counter = 0
    while counter < train_size:
        index = random.randrange(len(copy))
        train_set.append(copy[index])
        copy.pop(index)
        counter += 1
    return [train_set, copy]

# this part is for test
"""
if __name__ == '__main__':
    # test of first function
    file_name = './pima-indians-diabetes.data.csv'
    data = load_csv(file_name)
    print 'test1:\n'
    print data[0]

    # test of second function
    dataset = [[0], [1], [2], [3], [4], [5]]
    split_ratio = 0.66
    print 'test2:\n'
    train, test_set =  spilt_data(dataset, split_ratio)
    print train, test_set
"""
