# Step 1: Parse & Format Input
#   binary values separated by spaces =>
#   list of binary values as strings 

# input - raw text of whitespace-separated binary 
input = '10110011 11000011 11110000 10101010'


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
#pattern010Count = 0
#pattern011Count = 0
#pattern100Count = 0
#pattern101Count = 0
#pattern110Count = 0
#pattern111Count = 0
#pattern0000Count = 0
#pattern0001Count = 0
#pattern1000Count = 0
#pattern1001Count = 0
#pattern1010Count = 0
#pattern1011Count = 0
#pattern1100Count = 0
#pattern1101Count = 0
#pattern1110Count = 0
#pattern1111Count = 0


class Pattern:
    masterLst = ["000", "001", "110", "111", "0000", "0001", "1110", "1111"]
    
    counterDict = {"pattern000Count": 0,
                        "pattern001Count": 0,  
                        "pattern110Count": 0,
                        "pattern111Count": 0,
                        "pattern0000Count": 0,
                        "pattern0001Count": 0,
                        "pattern1110Count": 0,
                        "pattern1111Count": 0}
    
    def printCounters(self):
        print("\nPattern Counters")
        print("~~~~~~~")
        for key in self.counterDict.keys():
            print(key + ":" + str(self.counterDict[key]))
        print("~~~~~~~")
    
    # increments the corresponding counter
    # returns unique int, or 0 if None
    def patternMatcher(self, pattern, ):
        match pattern:
            case "000":
                self.counterDict["pattern000Count"] += 1
                return 1
            case "001":
                self.counterDict["pattern001Count"] += 1
                return 2
            case "110":
                self.counterDict["pattern110Count"] += 1
                return 3
            case "111":
                self.counterDict["pattern111Count"] += 1
                return 4
            case "0000":
                self.counterDict["pattern0000Count"] += 1
                return 5
            case "0001":
                self.counterDict["pattern0001Count"] += 1
                return 6
            case "1110":
                self.counterDict["pattern1110Count"] += 1
                return 7
            case "1111":
                self.counterDict["pattern1111Count"] += 1
                return 8
            case _:
                return 0
        
        
# initialize pattern object 
p1 = Pattern()

# parse input into string list 
strLst = parseFormatBinary(input)

#print(patternObject.patternCounter.Pattern111Count)
#patternObject.patternCounter.Pattern111Count += 5
#print(patternObject.patternCounter.Pattern111Count)


# iterate through values
for value in strLst:
    # before first nested iteration, get first 3 digits 
    firstThreeDigits = value[0:3]
    print(firstThreeDigits)
    # check if digits match any patterns 
    # true case
    if p1.patternMatcher(firstThreeDigits) > 0:
        print("\nMatch found!")
        p1.printCounters()
    firstFourDigits = value[0:4]
    print(firstFourDigits)
    if p1.patternMatcher(firstFourDigits) > 0:
        print("\nMatch found!")
        p1.printCounters()
        
    
        
    

#def patternMatcher():
#    match 

