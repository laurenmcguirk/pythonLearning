import teamClass

class match:
    def __init__(self, matchName, firstTeam, fTeamScore, secondTeam, sTeamScore):
        self.matchName = matchName
        self.firstTeam = firstTeam
        self.fTeamScore = fTeamScore
        self.secondTeam = secondTeam
        self.sTeamScore = sTeamScore

        #adding to wins/losses of teams
        if fTeamScore > sTeamScore:
                firstTeam.addWins() 
        elif sTeamScore > fTeamScore:
            secondTeam.addWins()
        
        def getMatchResults(self):
            if fTeamScore > sTeamScore:
                print(self.firstTeam + " won the match!")
                print("The final score was " + fTeamScore + " to " + sTeamScore)

            elif sTeamScore > fTeamScore:
                print(self.secondTeam + " won the match!")
                print("The final score was " + sTeamScore + " to " + fTeamScore)

        def getMatchName(self):
            print(self.matchName)

        def getFirstTeamScore(self):
            print(self.fTeamScore)

        def getSecondTeamScore(self):
            print(self.sTeamScore)
