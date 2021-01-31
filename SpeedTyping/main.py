from generator import *
from verification import *
import time

V = Verification()
G = Generator()
rW = G.generate()
tStart = None
tFinish = None
fastestType = None
fastestWord = None
ET = None
while 2:
    print("Word = ", rW)
    if tStart is None:
        tStart = time.perf_counter()

    uW = input("Enter the shown word: ", )

    if V.ver(rW, uW):
        tFinish = time.perf_counter()
        ET = tFinish - tStart
        ET_formatted = "{:.4f}".format(ET)
        print("It took you ", ET_formatted, "seconds to type the word: ", rW)
        if fastestType is None:
            fastestType = ET_formatted
            fastestWord = rW
        if ET_formatted < fastestType:
            fastestType = ET_formatted
            fastestWord = rW
        print("Your current best time is ", fastestType, "seconds with the word: ", fastestWord)
        rW = G.generate()
        tStart = None
        tFinish = None
    else:
        print("WRONG!")
        tStart = None
