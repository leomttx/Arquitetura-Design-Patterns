import abc
from abc import ABC, abstractmethod

class Worker(ABC):
    
    @abstractmethod 
    def work(self):
            pass

class toEat(ABC):
    @abstractmethod 
    def eat(self):
        pass

class HumanWorker(toEat):    
    def eat(self):
        print("Eating lunch!")

class RobotWorker(Worker):
    def work(self):
        print("Working non-stop!")

class main:
    def main():
        human = HumanWorker()
        robot = RobotWorker()
        human.eat()
        robot.work()

main.main()

