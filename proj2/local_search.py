from schedule import Schedule

def hillClimb():
    print("Hill Climbing: ")
    schedule = Schedule
    schedule.load(schedule, "sch1.txt")
    #print(schedule.__str__(schedule))
    print(schedule.value2(schedule))

#simulatedAnnealing is like hill climb
#except with a probablistic choice at the end
def simulatedAnnealing():
    print("Simulated Annealing: ")

def main():
    #do the thing
    hillClimb()


    pass

if __name__ == "__main__":
    main()