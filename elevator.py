# imports
import numpy


# Elevator
#   This class implements a simple elevator object. It keeps track of its initial floor, its current floor, its next
#   floor, and the floors it has previously visited. It also maintains its rate, and a range of valid floors.
class Elevator:

    def __init__(self, travelTime: int = 10, initialFloor: int = 0) -> None:
        """
        Initialize elevator object with time to travel between floors, a (currently)
        hardcoded floor range, and an initial floor
        :param travelTime: The time it takes to travel between floors
        :param initialFloor: The floor to start at
        """

        self.travelRate = 1/travelTime
        self.floorRange = [0, 100]
        self.initialFloor = initialFloor
        self.currentFloor = initialFloor
        self.floorsVisited = [self.currentFloor]
        self.nextFloor = None

    def changeFloor(self, nextFloor: int) -> None:
        """
        Change the floor that the elevator is at
        :param nextFloor: The floor to travel to
        """
        if nextFloor not in self.getValidFloorRange():
            exit('Encountered out out range floor, exiting...')

        if nextFloor != self.currentFloor:
            self.nextFloor = float(nextFloor)

    def atDesiredFloor(self) -> bool:
        """
        Return a boolean indicating if the current floor is the same as next floor
        :return: bool
        """

        # Since the current floor can be a float compare the difference to a tolerance to avoid float/int comapre issues.
        return numpy.abs(self.currentFloor - self.nextFloor) < 0.000001

    def updateElevatorState(self) -> None:
        """
        Update the current floor. Move the floor in the direction of the next floor, assuming a dt of 1
        """

        # Currently hardcode dt to 1. This could be changed in the future
        dt = 1

        # Move current floor based on direction the elevator needs to go, travel rate, and dt
        self.currentFloor += numpy.sign(self.nextFloor - self.currentFloor) * self.travelRate * dt

        # If the elevator has reached the next desired floor, update the floors visited list.
        # Also protect against adding a duplicate into the list, in the case an invalid floor input got skipped.
        if self.atDesiredFloor():
            self.floorsVisited.append(int(self.currentFloor))

    def getFloorsVisited(self) -> list:
        """
        Return the list of floors that the elevator has visited
        :return: list
        """
        return self.floorsVisited

    def getValidFloorRange(self) -> range:
        """
        Get a range of valid floors to visit
        :return: range
        """
        # Need to add one to upper end since range function does not include the upper bound
        return range(self.floorRange[0], self.floorRange[1] + 1)

    # Implemented these functions, but they do not currently get used. I could see them being useful in a more dynamic
    # sophisticated simulation
    def initializeElevatorToFloor(self, startingFloor: int) -> None:
        """
        Reset the elevator and change the initial floor
        :param starting_floor:
        """
        self.initialFloor = startingFloor
        self.currentFloor = self.initialFloor
        self.floorsVisited = [startingFloor]
        self.nextFloor = None

    def resetFloors(self):
        """
        This function resets the elevator to the initial state
        """
        self.floorsVisited = [self.initialFloor]
        self.currentFloor = self.initialFloor
        self.nextFloor = None