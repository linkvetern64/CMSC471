import math
from Node import Node
import time

current_milli_time = lambda: int(round(time.time() * 1000))

'''
Name:
Date:
Project 3: Decision trees

Please do not change the signature of train() or classify(),
or you will break the test suite.
'''


#the following are the values for each attibute in the global context so you can use them as needed
work_class = ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay", "Never-worked"]

education = ["Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th", "7th-8th", "12th",
             "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"]

marital = ["Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent", "Married-AF-spouse"]

occupation = ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty", "Handlers-cleaners",
              "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv",
              "Armed-Forces"]

relationship = ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"]

race = ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"]

sex = ["Female", "Male"]

native_country = ["United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany", "Outlying-US(Guam-USVI-etc)",
                  "India", "Japan", "Greece", "South", "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy", "Poland",
                  "Jamaica", "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic", "Laos", "Ecuador",
                  "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand", "Yugoslavia",
                  "El-Salvador", "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands"]

attributes = [work_class, education, marital, occupation, relationship, race, sex, native_country]
check = []
t = 0
columns = ["work_class", "education", "marital", "occupation", "relationship", "race", "sex", "native_country"]
checked = [0, 0, 0, 0, 0, 0, 0, 0]



#This entropy function should take a proportion as a parameter.
#This will be best used when calculating the parent node.
#Calculates correctly!!!
def entropy(a, total):
    if total == 0 or a == 0 or (a/total) == 0 or (1 - (a / total)) == 0: return 0

    return -(a / total * math.log2(a / total) + (1 - (a / total )) * math.log2(1 - (a / total)))

def infoGain(PEnt, data, labels):
    data_total = len(labels)

    child_entropy = 0.0

    col_no = 0
    highest_gain = -1
    new_index = -1
    for attribute in attributes:
        #Shouldn't need to be turned on
        #if checked[col_no]:
        #    continue

        for i in range(0, len(attribute), 1):
            yes = 0
            index = 0
            att_total = 0
            for person in data:
                # if the value of the att. is equal to subatt being checked
                if (person[col_no] == i):
                    yes += labels[index]
                    att_total += 1
                index += 1

            child_entropy += (att_total / data_total) * entropy(yes, att_total)
        gain = PEnt - child_entropy
        # print("Info. Gain = " + str(gain))
        if (gain > highest_gain):
            new_index = col_no

            highest_gain = gain
        child_entropy = 0.0
        col_no += 1


    #print("Best choice is " + columns[new_index] + " with info. gain of " + str(highest_gain))

    return new_index

def buildDT(head):
    #Add root, while nodes in next[0]
    seenNode = []
    nextNode = []
    nextNode.append(head)

    while nextNode:
        node = nextNode.pop(0)
        data = node.getData()
        labels = node.getLabels()

        if node in seenNode or len(labels) == 0:
            continue

        T = 0
        for i in labels: T += i
        pEnt = entropy(T, len(labels))

        #if parent entropy isn't 0
        if float(pEnt) == 0:
            #sum all the labels up, divide by total
            #if E < .4 0, E > .4, 1
            node.updateValue(labels[0])

        else:
            split = infoGain(pEnt, data, labels)

            if checked[split]:
                continue
            checked[split] = 1

            children = []
            #Check the data against all the possible children
            for val in range(0, len(attributes[split]), 1):
                index = 0
                tmp_node = Node()
                #Iterate through all the data to find the children
                for person in data:
                    if person[split] == val:
                        #Remove all of that columns data?
                        tmp_node.updateData(data[index], labels[index])
                    index += 1

                tmp_node.updateChecked(split)
                children.append(tmp_node)
                node.addBranch({str(attributes[split][val]) : tmp_node})

            children.extend(nextNode)
            nextNode = children


        seenNode.append(node)


#"""
#This function should train a decision tree classifier
#on the data. It should return a usable decision tree.
#How you implement the decision tree is up to you
#(class, dictionary, etc.), but do not use any python packages
#such as scikit-learn.
#
#data: a list of attribute vectors, the entire dataset in integer form
#labels: a list of class labels that correspond to the dataset
#"""
def train(data, labels):
    #This will be the dT root
    root = Node()
    root.setData(data)
    root.setLabels(labels)
    buildDT(root)
    return root


def classify(x, model):
    LABELS = ["<=50K",">50K"]

    """
    Given a some data point (known or not) x, this function
    should apply the model (trained in the above function)
    and return the classification of x based on the model.

    x: a single integer attribute vector for an adult
    """
    #This should determine if a person has an income of >=50k or < 50k
    #This takes a vector of a person, and model which is the decision tree.
    nodes = []
    nodes.append(model)

    #converts back to usable keys
    person = []
    index = 0
    for attribute in attributes:
        person.append(attribute[x[index]])
        index += 1

    for node in nodes:
        for val in person:
            if node.keyExists(val, person):
                nodes.append(node.getChild(val))
            if node.checkGuess(val):
                return LABELS[node.checkGuess(val)]

        return LABELS[node.value]

def convert(data_list):
    """This function converts the categorical values of data_list into integers """

    attributes = [work_class, education, marital, occupation, relationship, race, sex, native_country]

    converted_data = []

    for attribute_value in data_list:

        for attribute_values in attributes:

            if attribute_value in attribute_values:
                converted_data.append(attribute_values.index(attribute_value))

    return converted_data

def main():

    LABELS = ["<=50K",">50K"]

    #here is some code that reads the data from the current dir
    #feel free to change this as you wish
    with open("adult.data") as f:
        data = []
        labels = []
        for line in f:
            #skip bad data
            if len(line) < 10 or "?" in line:
                continue

            line = line.strip().split(",")
            data.append(convert(line[:-1]))
            labels.append(LABELS.index(line[-1]))

    #tree = train(data, labels)

    #example run:
    dT = train(data, labels)
    sample = ["Private","Bachelors","Married-civ-spouse","Exec-managerial","Husband","Asian-Pac-Islander","Male","Japan"] #>50K
    sample = convert(sample)
    lbl = classify(sample, dT)
    print(sample, lbl)


if __name__ == "__main__":
    main()
