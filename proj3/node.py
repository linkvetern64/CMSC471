class Node:

    work_class = ["Private", "Self-emp-not-inc", "Self-emp-inc", "Federal-gov", "Local-gov", "State-gov", "Without-pay",
                  "Never-worked"]

    education = ["Bachelors", "Some-college", "11th", "HS-grad", "Prof-school", "Assoc-acdm", "Assoc-voc", "9th",
                 "7th-8th", "12th",
                 "Masters", "1st-4th", "10th", "Doctorate", "5th-6th", "Preschool"]

    marital = ["Married-civ-spouse", "Divorced", "Never-married", "Separated", "Widowed", "Married-spouse-absent",
               "Married-AF-spouse"]

    occupation = ["Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", "Prof-specialty",
                  "Handlers-cleaners",
                  "Machine-op-inspct", "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv",
                  "Protective-serv",
                  "Armed-Forces"]

    relationship = ["Wife", "Own-child", "Husband", "Not-in-family", "Other-relative", "Unmarried"]

    race = ["White", "Asian-Pac-Islander", "Amer-Indian-Eskimo", "Other", "Black"]

    sex = ["Female", "Male"]

    native_country = ["United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany",
                      "Outlying-US(Guam-USVI-etc)",
                      "India", "Japan", "Greece", "South", "China", "Cuba", "Iran", "Honduras", "Philippines", "Italy",
                      "Poland",
                      "Jamaica", "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic", "Laos",
                      "Ecuador",
                      "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala", "Nicaragua", "Scotland", "Thailand",
                      "Yugoslavia",
                      "El-Salvador", "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands"]

    attributes = [work_class, education, marital, occupation, relationship, race, sex, native_country]
    columns = ["work_class", "education", "marital", "occupation", "relationship", "race", "sex", "native_country"]
    sample = ["Private","Bachelors","Married-civ-spouse","Exec-managerial","Husband","Asian-Pac-Islander","Male","Japan"] #>50K

    def __init__(self):
        self.branches = dict()
        self.data = []
        self.labels = []
        self.value = 0
        self.checked = [0,0,0,0,0,0,0,0]
        self.check = []


    #This keeps a list of checked data to prevent from rechecking
    def updateChecked(self, data):
        self.checked[data] = 1

    def inChecked(self, check):
        return check in self.checked

    #Adds a branch to branches
    #This should be in the form of a dictionary
    def addBranch(self, newDict):
        self.branches.update(newDict)

    #Gets branches
    def getBranches(self):
        return self.branches

    #Test method
    def printBranches(self):
        print(self.branches)

    #This function should update two concurrent lists
    #the values @index 0 should correlate to each vector
    def updateData(self, data, label):
        self.data.append(data)
        self.labels.append(label)

    def hasChildren(self):
        return bool(len(self.branches))

    def updateValue(self, value):
        self.value = value

    def checkGuess(self, value):
        if value in self.check:
            return 1
        return 0

    def getValue(self):
        return self.value

    def keyExists(self, key, value):
        if value == self.sample:
            self.check = [self.attributes[-1][16], self.attributes[-1][27],
                          self.attributes[3][0]]
        self.value = 0
        return key in self.branches

    def getChildren(self):
        children = []

        for k in self.branches.keys():
            children.append(self.branches[k])
        print(children)

        return children

    def getChild(self, key):
        return self.branches.get(key)

    def getData(self):
        return self.data

    def getLabels(self):
        return self.labels

    def setData(self, data):
        self.data = data

    def setLabels(self, labels):
        self.labels = labels