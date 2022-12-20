import teamClass
import matchClass

#Define teams
team = teamClass.team
team1 = team("Team 1")
team2 = team("Team 2")
team3 = team("Team 3")
team4 = team("Team 4")

#Put teams into matches
match = matchClass.match
match1 = match("Match 1", team1, team2)
match2 = match("Match 2", team3, team4,)

#Test for correct match name
match1.getMatchName()
match2.getMatchName()

#Get Match Results
match1.endMatch(8, 6)
#match2.endMatch(team2, 3, team4, 7)

#Get records
team1.getRecord()
team2.getRecord()
team3.getRecord()
team4.getRecord()

"""

"""