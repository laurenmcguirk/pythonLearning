class team:
    wins = 0
    losses = 0

    def __init__(self, name):
        self.name = name 

    def getTeamName(self):
        return self.name

    def addWins(self):
        self.wins+=1

    def addLosses(self):
        self.losses+=1;

    def getRecord(self):
        print(self.name + ": " + str(self.wins) + " wins and " + str(self.losses) + " losses")
