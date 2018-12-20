import random

def runGameTrickyHost(strategy):
    carLocation = random.randint(1,3)
    playerChoice = random.randint(1,3)
    doors = [1,2,3]
    doors.remove(carLocation)
    if carLocation != playerChoice:
        doors.remove(playerChoice)
    
    #hostChoice = random.choice(doors)
    hostChoice = doors[0]
    remainingDoors = [1,2,3]
    remainingDoors.remove(hostChoice)
    finalChoice = playerChoice
    if strategy=="switch":
        remainingDoors.remove(playerChoice)
        finalChoice = remainingDoors[0]
    
    if finalChoice == carLocation:
        return "car"
    else:
        return "goat"

def runGameNormal(strategy):
    carLocation = random.randint(1,3)
    playerChoice = random.randint(1,3)
    doors = [1,2,3]
    doors.remove(carLocation)
    if carLocation != playerChoice:
        doors.remove(playerChoice)
    
    hostChoice = random.choice(doors)
    remainingDoors = [1,2,3]
    remainingDoors.remove(hostChoice)
    finalChoice = playerChoice
    if strategy=="switch":
        remainingDoors.remove(playerChoice)
        finalChoice = remainingDoors[0]
    
    if finalChoice == carLocation:
        return "car"
    else:
        return "goat"

def main():
    results = {"car": 0, "goat": 0}
    N = 10000
    for i in range(1,N+1):
        res = runGameTrickyHost("switch")
        if res == "car":
            results["car"] = results["car"]+1
        elif res == "goat":
            results["goat"] = results["goat"]+1
    carPct = float(results["car"])/float(N)
    goatPct = float(results["goat"])/float(N)

    print "Car: %f" % (carPct*100)
    print "Goat: %f" % (goatPct*100)

if __name__ == '__main__':
    main()