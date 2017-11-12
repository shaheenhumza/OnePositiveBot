import os

def combineTextFiles():
    file = open("trainingData.txt", "w")

    with open("positiveTweets.txt", "r") as f1:
        for line in f1:
            if not line.strip():
                pass
            else:
                file.write(line)

    with open("10ondate.txt") as f2:
        for line in f2:
            if not line.strip():
                pass
            else:
                file.write(line)


    with open("forCachetes.txt") as f3:
        for line in f3:
            if not line.strip():
                pass
            else:
                file.write(line)


    with open("forCachetes2.txt") as f4:
        for line in f4:
            if not line.strip():
                pass
            else:
                file.write(line)


combineTextFiles()
