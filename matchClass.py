import teamClass

class match:
    firstTeam = ""
    secondTeam = ""
    match_id = "1_1"

    def __init__(self, matchName, firstTeam, secondTeam):
        self.matchName = matchName
        self.firstTeam = firstTeam
        self.secondTeam = secondTeam

    def endMatch(self, fTeamScore, sTeamScore):
        
        firstTeamName = self.firstTeam.getTeamName()
        secondTeamName = self.secondTeam.getTeamName()
        print(firstTeamName)

        #adding to wins/losses of teams
        if fTeamScore > sTeamScore:
            print(firstTeamName + " won the match!")
            print("The final score was " + str(fTeamScore) + " to " + str(sTeamScore))
            self.firstTeam.addWins() 
            self.secondTeam.addLosses()
        elif sTeamScore > fTeamScore:
            print(secondTeamName + " won the match!")
            print("The final score was " + str(sTeamScore) + " to " + str(fTeamScore))
            self.secondTeam.addWins()
            self.firstTeam.addLosses()


    def getMatchName(self):
        print(self.matchName)

    def getFirstTeamScore(self):
        print(self.fTeamScore)

    def getSecondTeamScore(self):
        print(self.sTeamScore)
