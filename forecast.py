import math


def calculate_probability(x, mean, std):
    exponent = math.exp(-math.pow(x-mean, 2)/(2*math.pow(std, 2)))
    return 1/(math.sqrt(2*math.pi)*std)*exponent


def calculate_by_class(summaries, inputValue):
    probabilities = {}
    for classValue, classSummary in summaries.iteritems():
        probabilities[classValue] = 1
        for i in range(len(classSummary)):
            mean, std = classSummary[i]
            x = inputValue[i]
            probabilities[classValue] *= calculate_probability(x, mean, std)
    return probabilities


def predict(summaries, Input_Vlaue):
    probabilities = calculate_by_class(summaries, Input_Vlaue)
    best_label, best_probability = None, -1
    for class_value, probability in probabilities.iteritems():
        if class_value is None or probability > best_probability:
            best_label = class_value
            best_probability = probability
    return [best_label, best_probability]


def get_predict(summary, testSet):
    prediction = []
    for i in range(len(testSet)):
        result, _ = predict(summary, testSet[i])
        prediction.append(result)
    return prediction

"""
if __name__ == '__main__':
    x = 71.5
    mean = 73
    std = 6.2
    porbability = calculate_probability(x, mean, std)
    print 'test1:\n'
    print porbability
    # test2
    summaries = {0: [(1, 0.5), (2, 3)], 1: [(20, 5.0)]}
    inputVector = [1.1, 1]
    probabilities = calculate_by_class(summaries, inputVector)
    print 'test2:\n'
    print probabilities
    # test 3
    summaries = {'A': [(1, 0.5)], 'B': [(20, 5.0)]}
    inputVector = [1.1, '?']
    result = predict(summaries, inputVector)
    print 'test3:\n'
    print result

    # test 4
    summaries = {'A': [(1, 0.5)], 'B': [(20, 5.0)]}
    testSet = [[1.1, '?'], [19.1, '?']]
    predictions = get_predict(summaries, testSet)
    print 'test4:\n'
    print predictions
"""