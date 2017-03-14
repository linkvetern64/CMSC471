from schedule import Schedule
import copy
import math
import random

def hillClimb(file):
    schedule = tmp = Schedule(0,0)
    schedule.load(file)
    #For each day
    #for each worker
    #deep copy the schedule
    #update each worker until you get better heuristic
    #set schedule to new schedule created
    #if no the schedule is no longer producing better heuristics
    #return the schedule
    #IF IT DOESNT CHANGE KEEP IT AS IT IS
    tmp = copy.deepcopy(schedule)
    print(schedule.value3())
    for day in schedule.schedule:
        tmp_m = day.morning
        tmp_e = day.evening
        tmp_g = day.graveyard
        best = schedule.value3()
        #assigning day a value, changes it for entire schedule
        for worker in schedule.workers:
            day.morning = worker
            if schedule.value3() >= best:
                best = schedule.value3()
                tmp_m = worker
        day.morning = tmp_m

        for worker in schedule.workers:
            day.evening = worker
            if schedule.value3() >= best:
                best = schedule.value3()
                tmp_e = worker
        day.evening = tmp_e

        for worker in schedule.workers:
            day.graveyard = worker
            if schedule.value3() >= best:
                best = schedule.value3()
                tmp_g = worker
        day.graveyard = tmp_g
    return schedule

def probability(curr, new, )

#simulatedAnnealing is like hill climb
#except with a probablistic choice at the end
def simulatedAnnealing(file):
    print(file)
    schedule = Schedule(0, 0)
    schedule.load(file)
    T = 100
    for day in schedule.schedule:
        tmp_m = day.morning
        tmp_e = day.evening
        tmp_g = day.graveyard
        best = schedule.value3()
        rand_worker = random.randrange(0, schedule.num_workers)

        day.morning = rand_worker
        if schedule.value3() > best:
            print("Test")

        rand_worker = random.randrange(0, schedule.num_workers)
        #do a deep copy of the schedule and make changes to see if the change is better
        #run that value through a probablistic function
        #pick a random shift and a random worker
        #
        #
        #

        day.morning = tmp_m
        day.evening = tmp_e
        day.graveyard = tmp_g
    return schedule

def main():
    #take from args optionally?
    #do the thing
    #schedule = hillClimb("sch2.txt")

    schedule = simulatedAnnealing("sch2.txt")

    schedule.toFile("new_schedule.txt")
    print(schedule.value3())
    #let TA know how to use program
    pass

if __name__ == "__main__":
    main()