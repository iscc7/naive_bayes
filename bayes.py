# this part is the main function
from data_process import load_csv, spilt_data
from feature_extract import summary_by_class
from forecast import get_predict
from accuracy import get_accuracy

if __name__ == '__main__':
    filename = 'pima-indians-diabetes.data.csv'
    splitRatio = 0.67
    dataset = load_csv(filename)
    trainingSet, testSet = spilt_data(dataset, splitRatio)
    # prepare model
    summaries = summary_by_class(trainingSet)
    # test model
    predictions = get_predict(summaries, testSet)
    accuracy = get_accuracy(testSet, predictions)
    print accuracy
    print predictions

