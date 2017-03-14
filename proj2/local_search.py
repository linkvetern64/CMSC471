from schedule import Schedule
import copy
import math
import random

#@Name: hillClimb
#@Param: file - string of file name passed in
#@Desc: This function simulates hill climbing algorithm
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

#@Name: Probability
#@Param - curr: the current heuristic value
#@Param - new: the new heuristic value
#@Param - temp: the current temperature value
#@Desc: Calculates probability for simulated annealing
def probability(curr, new, temp):
    if(new < curr): return 1
    return math.exp((curr - new) / temp);

#@Name: Simulated Annealing
#@Param: file - string of file name passed in
#@Desc: This function simulates simulated annealing
def simulatedAnnealing(file):
    schedule = Schedule(0, 0)
    schedule.load(file)
    T = 6000
    while(T > 1):
        for day in schedule.schedule:
            tmp_m = day.morning
            tmp_e = day.evening
            tmp_g = day.graveyard
            best = schedule.value3()

            if T < 1: return schedule
            # handles morning workers
            day.morning = rand_worker = random.randrange(0, schedule.num_workers)
            if schedule.value3() <= best:
                new = schedule.value3()
                day.morning = tmp_m
                curr = schedule.value3()
                if (probability(new, curr, T) > 1):
                    day.morning = rand_worker

            T -= 1
            if T < 1: return schedule

            # handles evening workers
            day.evening = rand_worker = random.randrange(0, schedule.num_workers)
            if schedule.value3() <= best:
                new = schedule.value3()
                day.evening = tmp_e
                curr = schedule.value3()
                if (probability(new, curr, T) > 1):
                    day.evening = rand_worker

            T -= 1
            if T < 1: return schedule

            #Handles the graveyard shift for simulated annealing
            day.graveyard = rand_worker = random.randrange(0, schedule.num_workers)
            if schedule.value3() <= best:
                new = schedule.value3()
                day.graveyard = tmp_g
                curr = schedule.value3()
                if (probability(new, curr, T) > 1):
                    day.graveyard = rand_worker

            T -= 1

    return schedule

#----------------   HOW TO USE ------------------#
# 1. Simply create a variable and call either hillClimb(file) or
#    simulatedAnnealing(file).
#    Ex. hill = hillClimb("schedule.txt")
#
# 2. (file) = file of schedule to load into hillclimb and sim.Annealing algorithms
#
# 3. To test the hillClimb and simulatedAnnealing algorithms, simply change the value of
#    test_file to the test file you choose.
#
# 4. Two output files of the new schedules will be created, as well as printing of the
#    final heuristic value for that schedule.
#
#
def main():
    #CHANGE ME TO TEST PROGRAM
    test_file = "sch2.txt" #<------ change this right here :D
    #CHANGE ME TO TEST PROGRAM

    #Calls hill climb test program and outputs a file
    hill = hillClimb(test_file)
    print("Value of hill climb value3 = " + str(hill.value3()))
    print("Writing new schedule to file...")
    hill.toFile("hill_schedule.txt")

    #Calls simulated annealing test program and outputs a file
    sim = simulatedAnnealing(test_file)
    print("Value of simulated annealing value3 = " + str(sim.value3()))
    print("Writing new schedule to file...")
    sim.toFile("annealing_schedule.txt")

pass

if __name__ == "__main__":
    main()