import teamClass

class match:
    def __init__(self, matchName, firstTeam, secondTeam):
        self.matchName = matchName
        self.firstTeam = firstTeam.name
        self.secondTeam = secondTeam.name

    def endMatch(self, firstTeam, fTeamScore, secondTeam, sTeamScore):
        self.fristTeam = firstTeam
        self.fTeamScore = fTeamScore
        self.secondTeam = secondTeam
        self.sTeamScore = sTeamScore

        #adding to wins/losses of teams
        if fTeamScore > sTeamScore:
            print(self.firstTeam + " won the match!")
            print("The final score was " + str(self.fTeamScore) + " to " + str(self.sTeamScore))
            firstTeam.addWins() 
            secondTeam.addLosses()
        elif sTeamScore > fTeamScore:
            print(self.secondTeam + " won the match!")
            print("The final score was " + str(self.sTeamScore) + " to " + str(self.fTeamScore))
            secondTeam.addWins()
            firstTeam.addLosses()


    def getMatchName(self):
        print(self.matchName)

    def getFirstTeamScore(self):
        print(self.fTeamScore)

    def getSecondTeamScore(self):
        print(self.sTeamScore)
