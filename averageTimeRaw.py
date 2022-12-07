import os

fileName = os.sys.argv[1]

f = open(fileName)
data = f.readlines()
finalData = {}

for line in data:
    line = line.split()
    #print(line)
    targetName = line[0]
    time = int(line[len(line)-1])
    if targetName in finalData.keys():
        finalData[targetName].append(time)
    else:
        tempList = []
        tempList.append(time)
        finalData[targetName]= tempList

for key in finalData:
    print(key)
    for i in finalData[key]:
        print(i/1000)

    # print("{},{}".format("Average time(ms):",round(sum(finalData[key])/len(finalData[key]),2)))
    # print("{},{}".format("Average time(s):",round(sum(finalData[key])/len(finalData[key])/1000,4)))
