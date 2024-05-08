class TreasureChest:
    def __init__(self, question, answer, points):
        self.question = question # DECLARE question : STRING
        self.answer = answer # DECLARE answer : INTEGER
        self.points = points # DECLARE points : INTEGER

    def getQuestion(self):
        return self.question
    
    def checkAnswer(self, ans):
        if int(self.answer) == ans:
            return True
        else: 
            return False
        
    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.points)
        elif attempts == 2:
            return (int(self.points)//2)
        elif attempts == 3 or attempts == 4:
            return (int(self.points)//4)
        else:
            return 0


def readData():
    try:
        f = open("TreasureChestData.txt")
        temp = f.readlines()
        for i in temp:
            i.replace("/n", "")
        global arrayTreasure
        arrayTreasure = []
        for i in range(0, len(temp), 3):
            arrayTreasure.append(TreasureChest(temp[i], temp[i+1], temp[i+2]))
    except FileNotFoundError:
        print("File not found.")


    

readData()
num = int(input("Enter a number between 1 and 5:  "))
attempts = 0
flag = True
while flag:
    print(arrayTreasure[num - 1].getQuestion())
    ans = int(input("Enter your answer:  "))
    attempts += 1
    if (arrayTreasure[num - 1].checkAnswer(ans)):
        flag = False

print(arrayTreasure[num - 1].getPoints(attempts))


