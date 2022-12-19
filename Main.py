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
match1 = match("Match 1", team1, 8, team2, 5)
match2 = match("Match 2", team3, 2, team4, 6)

#Test for correct match name
match1.getMatchName()
match2.getMatchName()

#Get Match Results
match1.getMatchResults()
match2.getMatchResults()

#Get records
team1.getRecord()
team2.getRecord()
team3.getRecord()
team4.getRecord()