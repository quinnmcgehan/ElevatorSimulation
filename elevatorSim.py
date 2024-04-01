# elevatorSim.py
# Description: This script runs a simulation of an elevator traveling between several different floors. This script
#    initializes inputs and objects, and runs the simulation loop. The simulation is set up so the elevator is
#    controlled by an elevator manager object. The elevator manager class is stubbed so that it could handle multiple
#    different elevators in the future (thinking of a building with several elevators or something). The elevator
#    ultimately just has to keep track of its initial, current, and next floors, the floors it has visited, its travel
#    rate, and a set of valid floors.
#
# Assumptions:
#
# i) This simulation uses a time based loop for the main sim. I went back and forth on whether I needed to
#    simulate the elevator moving between floors or not. The other option I considered was a simulation where changing
#    floors would be instantaneous and the time a simple computation of the number of floors traveled multiplied by the
#    travel time between floors. Ultimately I decided I preferred making the elevator actually "move" between floors.
#
# ii) The time step is fixed at 1 in the while loop. This could certainly be modified in the future to handle variable
#     time steps.
#
# iii) The simulation doesn't run for a set amount of time. It runs until there are no more floors to travel between.
#
# iv) For this simulation I set the valid floors to be [0, 100]. This was somewhat arbitrary as negative floors would
#     work fine with the logic, and it could be arbitrarily tall. In a more sophisticated sim these would be
#     configurable.

# imports
from elevatorManager import ElevatorManager

# Time to travel between floors
# Constant for this case, but could be variable for different sims and different elevators
singleFloorTravelTime = 10

# Define initial floor and subsequent floors to visit
startingFloor = 12
floorsToVisit = [2, 9, 11, 32]

# Instantiate an ElevatorManager to be the brains of moving the elevator
myElevatorManager = ElevatorManager(numberOfElevators=1, travelTimes=[singleFloorTravelTime], initialFloor=startingFloor)

# Set the floors for the elevator to visit.
myElevatorManager.setDesiredFloors(elevatorNum=0, floorsToVisit=floorsToVisit)

# Initialize time variable
t = 0
while(myElevatorManager.haveFloorsToVisit()):

    # Update time variable
    t += 1

    # Update Elevators
    myElevatorManager.runElevators()

# Collect outputs
outputs = (t, myElevatorManager.getFloorsVisited(elevatorNum=0))
print(outputs)


