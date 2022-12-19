class team:
    wins = 0
    losses = 0

    def __init__(self, name):
        self.name = name 

    def getTeamName(self):
        print(self.name)

    def addWins(self):
        self.wins+=1

    def addLosses(self):
        self.losses+=1;

    def getRecord(self):
        print(str(self.wins) + " wins and " + str(self.losses) + " losses")
