# MISSION: The complete set of examples and source code for ''Python 2000: Beyond
# The Basics''.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-2000
# DATE: 2017-03-01 17:25:28
# FILE: MyWrap.py
# AUTHOR: Randall Nagy
#

class MyWrap():
    
    def __init__(self):
        self._pwFile = None
        
    def __init__(self, file):
        self._pwFile = file
        
    def __enter__(self):
        print("enter", self._pwFile)
        return self # Important!
       
    def __exit__(self, able, baker, charley):
        print("exit")
        self._pwFile.__exit__(able, baker, charley)

    def writeLines(self, aList):
        if self._pwFile is None:
            return False
        for ref, ss in enumerate(aList, 1000):
            print(ss, ref, file=self._pwFile)
        return True

    def readLines(self):
        if self._pwFile is None:
            return []
        return self._pwFile.readlines()

    @staticmethod
    def openz(file, mode):
        return MyWrap(open(file, mode))

# static factory
def Vola(file, mode):
    return MyWrap(open(file, mode))
     

if __name__ == "__main__":
    file = "./MyWrapSelfTest.txt"
    
    with MyWrap.openz(file, "w") as ofile:
            print(str(type(ofile)))
            ofile.writeLines(["tAble", "tBaker", "tZulu"])

    with MyWrap.openz(file, "r") as ifile:
        data = ifile.readLines()
        for ref in data:
            print(ref, end = "")
    
