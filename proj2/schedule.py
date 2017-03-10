#File: schedule.py
#Author: Michael Neary & Max Morawski
#Description: represents a schedule of employees

from random import choice
from day import Day 
import sys

try:
    from prettytable import PrettyTable
except:
    pass

#represents a sequence of days as one cohesive schedule
class Schedule:

    #initializes a blank schedule given the numbers of workers and days
    def __init__(self, num_workers, num_days):
        self.num_workers = num_workers
        self.num_days = num_days

        self.workers = list(range(num_workers))
        self.schedule = []

        for d in range(num_days):
            day = Day(-1, -1, -1)
            self.schedule.append(day)

    def toFile(self, filename):
        with open(filename,"w") as f:
            for day in self.schedule:
                f.write(str(day) + "\n")
    
    #load schedule from file
    #this is mostly for testing
    def load(self, filename):
        with open(filename) as f:
            lines = f.readlines()
            self.num_workers = int(lines[0].strip())
            self.num_days = int(lines[1].strip())
            self.schedule = [None]*self.num_days


            for n,d in enumerate(lines[2:]):
                m,e,g = map(int, d.split(","))
                day = Day(m,e,g)
                self.schedule[n] = day
                self.num_workers = max([m,e,g,self.num_workers])
                
            self.workers = list(range(self.num_workers))

    #randomizes the current schedule
    def randomize(self):    
        for d in range(self.num_days):
            workerA = choice(self.workers)
            workerB = choice(self.workers)
            workerC = choice(self.workers)
            day = Day(workerA, workerB, workerC)
            self.schedule[d] = day

    #set schedule on day for a shift to be a specific employee
    def set(self, day, shift, worker):

        if type(worker) != int or worker < 0 or worker >= self.num_workers:
            msg = "{} is not a valid worker number for this schedule.".format(worker)
            raise ValueError(msg)

        if type(day) != int or day < 0 or day >= self.num_days:
            msg = "{} is not a valid day for this schedule.".format(day)
            raise ValueError(msg)

        self.schedule[day].set(shift, worker)
    
    #string representation of this schedule
    def __str__(self):

        if 'prettytable' not in sys.modules:
            #DELETE
            print("Day and Worker info:")
            print("Day #:" + str(self.num_days))
            print("Worker #:" + str(self.num_workers))

            #DELETE
            out = ''
            for n,day in enumerate(self.schedule):
                out += str(n)+ ": " + str(day) + "\n"
        else:
            out = PrettyTable()
            out.add_column("", ["Morning","Evening","Graveyard"])

            for n, day in enumerate(self.schedule):
                out.add_column("Day: " + str(n), str(day).split(","))

        return str(out)

    def value1(self):
        value = 0
        for day in self.schedule:
            if day.morning != day.evening: value += 1
            if day.morning != day.graveyard: value += 1
            if day.graveyard != day.evening: value += 1
        return value

    def value2(self):
        value = self.value1(self)

        for day in self.schedule:
            #check if all odd or all even
            if self.allEven(self, day) or self.allOdd(self, day): value += 1
        return value

    def value3(self):
        value = self.value2(self)
        evenShifts = (self.num_days * 3) // self.num_workers
        lastGrave = -1
        workerShiftCount = [0] * self.num_workers

        for day in self.schedule:
            #Update the amount of times a worker works
            workerShiftCount[day.morning] += 1
            workerShiftCount[day.evening] += 1
            workerShiftCount[day.graveyard] += 1

            #check if graveyard works following morning
            if lastGrave > -1 and lastGrave != day.morning: value+= 1
            lastGrave = day.graveyard


        #check if schedule is unbalanced,
        for count in workerShiftCount:
            if count == evenShifts: value+= 1

        return value

    def allOdd(self, day):
        return self.isOdd(self, day.morning) and self.isOdd(self, day.evening) and self.isOdd(self, day.graveyard)

    def allEven(self, day):
        return self.isEven(self, day.morning) and self.isEven(self, day.evening) and self.isEven(self, day.graveyard)

    def isOdd(self, num):
        return bool(num % 2)

    def isEven(self, num):
        return not bool((num % 2))
    #add any other methods you need here
