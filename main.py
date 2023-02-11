


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
    
    def printCounters(self, counterDict):
        print("\nPattern Counters")
        print("~~~~~~~")
        for key in counterDict.keys():
            print(key + ":" + str(counterDict[key]))
        print("~~~~~~~")
    
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

def patternFinder(pattern, binaryString):
    counterDict= pattern.counterDict()
    # iterate through each input binary string
    print("input: " + "".join(binaryString))
    # init streak bools
    isHitStreak = False
    isMissStreak = False
    # before first nested iteration, get first 3 digits 
    for index, digit in enumerate(binaryString):
        eIndex = index + 3
        # stop looping at end 
        if eIndex > len(binaryString):
            pattern.printCounters(counterDict)
            return pattern
        # if on a streak, don't double count 
        if ((isHitStreak and binaryString[(eIndex-1)] == '1') or (isMissStreak and binaryString[(eIndex-1)] == '0')):
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
                pattern.printCounters(counterDict)
                return pattern
            fourDigitStr = binaryString[index:eIndex]
            if pattern.patternMatcher(fourDigitStr, counterDict) > 0:
                if fourDigitStr=='1111':
                    isHitStreak=True
                if fourDigitStr=='0000':
                    isMissStreak=True
    pattern.printCounters(counterDict)
    return pattern

for p in strLst1:
    p1 = Pattern()
    p1 = patternFinder(p1, p)

for p in strLst2:
    p1 = patternFinder(p1, p)

for p in strLst3:
    p3 = Pattern()
    p3 = patternFinder(p3, p)


