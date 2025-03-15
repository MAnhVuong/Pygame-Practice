import pygame
import Vehicle
import KeyboardMover
import Map

def main():
    car1           = Vehicle.Vehicle("./Images/orange_truck.png")
    car2           = Vehicle.Vehicle("./Images/red_car.png", locy=200)
    tree           = Vehicle.Vehicle("./Images/tree.png", locx=1000)
    listOfVehicles = [car1, tree, car2]
    kbReader       = KeyboardMover.KeyboardMover(car1, "l")
    kbReader2      = KeyboardMover.KeyboardMover(car2, "d")
    myMap          = Map.Map(1240,820)
    keepRunning = True
    while (keepRunning):
        keepRunning = kbReader.processOneEvent() and kbReader2.processOneEvent()
        myMap.update(listOfVehicles)
            

if __name__ == "__main__":
    main()