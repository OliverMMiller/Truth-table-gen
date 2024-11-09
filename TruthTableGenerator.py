import csv
with open('TruthTable.csv', 'w', newline='') as TruthTable:
    myCSVWriter = csv.writer(TruthTable, delimiter=',')
    myInputs = ["enable","open 1","close 1","open 2","close 2","PS1","10s timer out","counter >10","RS"]
    numInputs = len(myInputs) + 1
    header = myInputs + ["","buzzer","oper hatch","close hatch","10s timer reset","increment counter","pliot light"]
    myCSVWriter.writerow(header)
    i = 0
    def getBin(num):
        num = list(bin(i))
        num.pop(0)
        num.pop(0)
        num.reverse()
        return num

    thisrow = getBin(i)

    while True:#i < (9)**2
        thisrow = getBin(i)
        for j in range(len(thisrow)):
            thisrow[j] = int(thisrow[j])
        if len(thisrow) > len(myInputs):
            break
        else:
            while len(thisrow) < len(myInputs): 
                thisrow.append(0)


        thisrow.append("")
        thisrow.append(thisrow[5])
        thisrow.append(thisrow[0]&(thisrow[1]|thisrow[3])&~thisrow[2]&~thisrow[4]&~thisrow[5])
        thisrow.append(thisrow[5]|thisrow[2]|thisrow[4])
        thisrow.append(thisrow[0]&(thisrow[1]|thisrow[3])&~thisrow[2]&~thisrow[4]&~thisrow[5])
        thisrow.append(thisrow[8])
        thisrow.append(thisrow[7] * -1 + 1)
        myCSVWriter.writerow(thisrow)
        i += 1
        # print(i)
