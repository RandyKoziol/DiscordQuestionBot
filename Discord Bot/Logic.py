from random import randint
def readAnswers():
    f=  open("Answers.txt","r")
        
    ans = f.readlines()
    f.close()
    return ans

def selectAns(ans):
    
    selectedAns = randint(0, (len(ans) - 1 ))
    
    return ans[selectedAns]
