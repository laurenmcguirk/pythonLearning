"""

bracketClass.py

    bracketSetUp = 0

    Method:   newBracket(self, teams):
    self.totalMatches = 0
    matchGenerator = teams
    initialMatches = teams/2
    
    while matchGenerator > 1:
        matchGenerator = matchGenerator/2
        totalMatches += matchGenerator

    Methhod:    assignTeams:
        unsetMatches = self.initialMatches
        if bracketSetUp = 0
            while unsetMatches > 0 
                input("team 1: )    *get user unput*    
                                    *then have look for team object to see if it exists*
        else
            print("Bracket is already setup.")

    *give matches IDs that correlate with the match and round (round 1 = 1), (round 2 = 1_1), etc.
    *start by assigning them in the main, then assign then using a loop

    printTeams():
        *Print out bracket, use ASCII Art (look up python3 bracket)


Main.py
    Function: *take team name and check if team exists*


teamClass and matchClass:
    *go check what the classes print and make them return what they should return


Overall Nesting:    
(o) = object    (v) = saved variable in (o)     (m) = methods     (c) = calls another (m)
    (o)bracket
        (m)newBracket [creates a new bracket]
            (v)all matches
                (v)assigned
                (v)unassigned
        (m)assignTeams
            (c)team()
        (m)printTeams
        (o)matches
            (o)teams
                (v)names
                (v)records


"""