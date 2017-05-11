import math

#Calculates the word frequency
def TF(occur, total):
    return (occur / total)

#calculates the inverse document frequency
def IDF(occurFiles, totalFiles):
    return math.log(totalFiles / occurFiles)

def main():

    files = ["apple.txt", "facebook.txt", "google.txt", "microsoft.txt", "tesla.txt"]
    count = [dict() for x in range(len(files))]
    allWords = {}
    wordTotal = []
    index = 0

    for file in files:
        allWords[file] = []
        words = open(file, "r").read().split(" ")
        wordTotal.append(len(words))

        for word in words:
            if word not in count[index].keys():
                allWords[file].append(word)
                count[index].update({word : 1})
            else:
                count[index][word] = count[index].get(word) + 1

        index += 1

    i = 0

    #This iterates through each dictionary pertaining to that file
    for k in count:
        print("For file " + files[i])
        values = []
        # This is the specific word in each dictionary per file
        for key in k.keys():

            occur = 0
            # Gets number of occurrences of a word in all files
            for w in count:
                if key in w.keys(): occur += 1
            value = TF(k[key], wordTotal[i]) * IDF(occur, len(files))
            values.append([key, value])

        #Sorts and prints top 5 items in each list
        values.sort(key=lambda x: x[1])
        values.reverse()
        for j in range(0, 5, 1):
            print(values[j][0] + " = " + str(values[j][1]))
        i += 1
        print("\n")


if __name__ == '__main__':
    main()