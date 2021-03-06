'''
Project 4: K-means Classificiation
Author:
Date: 

Tests your implementation of K-means on the test set.
'''
from proj4 import train, classify
    
def test():
    f = open("iris-train.data")
    l = open("iris-train.labels")

    data = [list(map(float, line.strip().split(","))) for line in f]
    labels = [line.strip() for line in l]

    #train a model on the data and labels
    model = train(data, labels)

    t = open("iris-test.data")
    l2 = open("iris-test.labels")
    lbls = [line.strip() for line in l2]
    right = 0
    total = 0

    #compute the classificaiton of each test sample
    for line,actual in zip(t,lbls):
        total += 1
        sample = list(map(float, line.strip().split(",")))
        prediction = classify(sample, model)
        #did the model get it right?
        if prediction == actual:
            right += 1

    f.close()
    l.close()
    t.close()
    l2.close()
    #display the accuracy of the model
    acc = right / total * 100
    print("Accuracy: {:.2f}%".format(acc))


if __name__ == "__main__":
    test()
