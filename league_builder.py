#! usr/bin/env python3
# building a youth soccer league

import csv

if __name__ == "__main__":
    def build_league(file_name):
        impFile = open(file_name) # opens file with player info
        impReader = csv.reader(impFile)
        impData = list(impReader) # builds list of list of player info
        if impData == None: # checks to make sure a file was imported
            print("Import failed. Make sure you're using the correct file name.")
        else:
            print("Import complete.")
        player = {} # dict used to store player info
        dragons = [] 
        dpt = "March 17, 1PM"
        dxp = 0 # number of dragons w/ experience
        raptors = [] 
        rpt = "March 17, 3PM" 
        rxp = 0 # number of raptors w/ experience
        sharks = [] 
        spt = "March 18, 1PM" 
        sxp = 0 # number of sharks w/ experience
        letterToMom = "Dear {}, \nYour son, {}, has been placed on the {} youth soccer league team. The {}' first practice will be {}. Don't be late and remember to bring water!\n Sincerely, The YSL Coordinator"
        for i in range(1,19): # exports formatted player info to dictionary
            player.update({"Player Name": impData[i][0]})
            player.update({"Height": impData[i][1]})
            player.update({"Experience": impData[i][2]})
            player.update({"Guardians": impData[i][3]})
            letter_name = (player['Player Name'].replace(" ", "_").lower() + ".txt")
            newLetter = open(letter_name, 'w')
            print(player) # prints player info
            if player['Experience'].lower() == "yes": # if player is experienced, assigns to team with least experience (default is dragons)
                if dxp <= rxp and dxp <= sxp:
                    dragons.append(player["Player Name"])
                    print(player['Player Name'] + " assigned to Dragons.")
                    dxp += 1
                    newLetter.write(letterToMom.format(player['Guardians'],player['Player Name'],"Dragons", "Dragons", dpt))            
                elif rxp <= dxp and rxp <= sxp:
                    raptors.append(player["Player Name"])
                    print(player['Player Name'] + " assigned to Raptors.")
                    rxp += 1
                    newLetter.write(letterToMom.format(player['Guardians'],player['Player Name'],"Raptors", "Raptors", rpt))  
                else:
                    sharks.append(player['Player Name'])
                    print(player['Player Name'] + " assigned to Sharks.")
                    sxp += 1
                    newLetter.write(letterToMom.format(player['Guardians'],player['Player Name'],"Sharks", "Sharks", spt))  
            else: # if player is not experience, assigns to team with lowest number of players (default is dragons)
                if len(dragons) <= len(raptors) and len(dragons) <= len(sharks):
                    dragons.append(player["Player Name"])
                    print(player['Player Name'] + " assigned to Dragons.")
                    newLetter.write(letterToMom.format(player['Guardians'],player['Player Name'],"Dragons", "Dragons", dpt))  
                elif len(raptors) <= len(sharks) and len(raptors) <= len(dragons):
                    raptors.append(player["Player Name"])
                    print(player['Player Name'] + " assigned to Raptors.")
                    newLetter.write(letterToMom.format(player['Guardians'],player['Player Name'],"Raptors", "Raptors", rpt)) 
                else:
                    sharks.append(player['Player Name'])
                    print(player['Player Name'] + " assigned to Sharks.")
                    newLetter.write(letterToMom.format(player['Guardians'],player['Player Name'],"Sharks", "Sharks", spt))  
            print("Raptors team: " + str(raptors)) # prints final team list
            print("Sharks team: " + str(sharks))
            print("Dragons team: " + str(dragons))

    build_league("soccer_players.csv")
