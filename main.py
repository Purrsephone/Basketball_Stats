from collections import Counter

# Step 1: Parse & Format Input
#   binary values separated by spaces =>
#   list of binary values as strings 

# input - raw text of whitespace-separated binary 

# doesn't double count
input1 = '11111101'
input2 = '010100111110'
input3 = '11111111111 10110011 11000011 1111000000 10101010'



def parseFormatBinary(input):
    # binaryLst - list of binary values from input,
    #             split by the space " " character 
    binaryLst = input.split(" ")

    # initialize a new list to hold string values
    strLst=[]

    # convert each item to string
    # save result in strLst
    for value in binaryLst:
        strLst.append(str(value))
    
    return strLst 
    
def counterSummary(counterDict):
        print("\nSummary:")
        print("~~~~~~~")
        for key in counterDict.keys():
            print(key + ":" + str(counterDict[key]))
        print("~~~~~~~")
        print("\n")
    
# Step 2: Initialize Pattern Variables 
class Pattern:
    masterLst = ["000", "001", "110", "111", "0000", "0001", "1110", "1111"]
    
    def counterDict(self):
        return {"pattern000Count": 0,
                "pattern001Count": 0,  
                "pattern110Count": 0,
                "pattern111Count": 0,
                "pattern0000Count": 0,
                "pattern0001Count": 0,
                "pattern1110Count": 0,
                "pattern1111Count": 0}
    
    def cpyCounterDict(self, counterDict, newDict):
        for key in counterDict.keys():
            newDict[key] = counterDict[key]
        return newDict
        
    def printCounters(self, counterDict):
        print("\nPattern Counters")
        print("~~~~~~~")
        for key in counterDict.keys():
            print(key + ":" + str(counterDict[key]))
        print("~~~~~~~")
        print("\n")
        
    # increments the corresponding counter
    # returns unique int, or 0 if None
    def patternMatcher(self, pattern, counterDict):
        match pattern:
            case "000":
                counterDict["pattern000Count"] += 1
                return 1
            case "001":
                counterDict["pattern001Count"] += 1
                return 2
            case "110":
                counterDict["pattern110Count"] += 1
                return 3
            case "111":
                counterDict["pattern111Count"] += 1
                return 4
            case "0000":
                counterDict["pattern0000Count"] += 1
                return 5
            case "0001":
                counterDict["pattern0001Count"] += 1
                return 6
            case "1110":
                counterDict["pattern1110Count"] += 1
                return 7
            case "1111":
                counterDict["pattern1111Count"] += 1
                return 8
            case _:
                return 0
    

# parse input into string list 
strLst1 = parseFormatBinary(input1)
strLst2 = parseFormatBinary(input2)
strLst3 = parseFormatBinary(input3)

def patternFinder(pattern, binaryString, newDict, printall):
    counterDict= pattern.counterDict()
    # iterate through each input binary string
    if printall:
        print("input: " + "".join(binaryString))
    # init streak bools
    isHitStreak = False
    isMissStreak = False
    # before first nested iteration, get first 3 digits 
    for index, digit in enumerate(binaryString):
        eIndex = index + 3
        # stop looping at end 
        if eIndex > len(binaryString):
            if printall:
                pattern.printCounters(counterDict)
            pattern.cpyCounterDict(counterDict, newDict)
            return newDict
        # if on a streak, don't double count 
        if isHitStreak:
            if binaryString[(eIndex-1)] == '0':
                isHitStreak = False
            continue 
        if isMissStreak:
            if binaryString[(eIndex-1)] == '1':
                isMissStreak = False
            continue 
        # streaks ended 
        isHitStreak = False
        isMissStreak = False
        threeDigitStr = binaryString[index:eIndex]
        # check if digits match any patterns 
        if pattern.patternMatcher(threeDigitStr, counterDict) > 0:
        # only need to check 4th digit if there is a match for first 3
        # has to be either 000 or 111
            eIndex = index + 4
            # check if index out of bounds
            if eIndex > len(binaryString):
                if printall:
                    pattern.printCounters(counterDict)
                pattern.cpyCounterDict(counterDict, newDict)
                return newDict
            fourDigitStr = binaryString[index:eIndex]
            if pattern.patternMatcher(fourDigitStr, counterDict) > 0:
                if fourDigitStr=='1111':
                    isHitStreak=True
                if fourDigitStr=='0000':
                    isMissStreak=True
    if printall:
        pattern.printCounters(counterDict)
    pattern.cpyCounterDict(counterDict, newDict)
    return newDict

def basketballStats(input, printall):
    print("input: " + " ".join(input))
    dicts = []
    for p in input:
        p1 = Pattern() 
        emptyDict = p1.counterDict()
        newDict = {}
        p1 = patternFinder(p1, p, newDict, printall)
        dicts.append(newDict)
    d = {k: v for k in dicts[0] for v in [sum(d[k] for d in dicts)]}
    counterSummary(d)
    
basketballStats(strLst1, False)
basketballStats(strLst2, False)
basketballStats(strLst3, False)



