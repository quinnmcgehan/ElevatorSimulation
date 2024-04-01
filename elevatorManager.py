# imports
from elevator import Elevator


# ElevatorManager
#   This class implements an elevator manager object. It is responsible for instantiating and keeping track of the
#   elevator objects and the desired floors for the elevators to visit
class ElevatorManager:

    def __init__(self, numberOfElevators: int = 1, travelTimes: list = [10], initialFloor: int = 0):
        # Constructor
        #    Initialize elevator and floor dictionaries, and instantiate elevators

        if numberOfElevators != len(travelTimes):
            exit('Number of elevators didn''t match number of travel times')

        self.elevators = {}
        self.floorsDict = {}
        for idx in range(0,numberOfElevators):
            self.elevators[idx] = Elevator(travelTimes[idx], initialFloor)
            self.floorsDict[idx] = []

    def setDesiredFloors(self, elevatorNum: int = 0, floorsToVisit: list = []) -> None:
        """
        This function sets the desired floors to visit for the specified elevator, and sets the next floor for the
        elevator if it is None
        :param elevatorNum: The elevator to set
        :param floorsToVisit: List of floor for the elevator to travel to
        """
        self.floorsDict[elevatorNum] = floorsToVisit

        # If the elevator doesn't have a floor to visit, set it
        if self.elevators[elevatorNum].nextFloor == None:
            self.elevators[elevatorNum].changeFloor(self.floorsDict[elevatorNum][0])

    def haveFloorsToVisit(self) -> bool:
        """
        This function returns a bool indicating if any elevators still have floors to visit
        :return: bool
        """
        haveFloorsToVisit = False
        for elevatorIdx, floors in self.floorsDict.items():
            if len(floors) > 0:
                haveFloorsToVisit = True
        return haveFloorsToVisit

    def runElevators(self):
        """
        This function updates the elevators one time step. If an elevator has reached its next floor it is sent to the
        subsequent floor in the struct.
        """
        # Loop over elevators
        for idx, elevator in self.elevators.items():
            # Get the list of floors to visit for the elevator
            floorsToVisit = self.floorsDict[idx]

            # Update the elevator state
            elevator.updateElevatorState()

            # Check if the elevator should be sent to the next floor
            if elevator.atDesiredFloor():
                floorsToVisit.pop(0)
                if len(floorsToVisit) > 0:
                    elevator.changeFloor(floorsToVisit[0])

    def getFloorsVisited(self, elevatorNum: int =0) -> list:
        """
        This function returns the floors that the specified elevator has visited
        :param elevatorNum:
        :return:
        """
        return self.elevators[elevatorNum].floorsVisited
