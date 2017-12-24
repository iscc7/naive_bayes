

def get_accuracy(testset, predict):
    correct = 0
    for i in range(len(testset)):
        if predict[i] == testset[i][-1]:
            correct += 1
    return correct/float(len(predict))

"""
if __name__ == '__main__':
    testSet = [[1, 1, 1, 'a'], [2, 2, 2, 'a'], [3, 3, 3, 'b']]
    predictions = ['a', 'a', 'a']
    accuracy = get_accuracy(testSet, predictions)
    print 'test1:\n'
    print accuracy
"""