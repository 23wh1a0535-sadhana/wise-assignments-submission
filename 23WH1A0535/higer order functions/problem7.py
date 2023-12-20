#7. A newly constructed jail has 100 cells, numbered 1 to 100.
#The newly appointed jailer arrives and decides to walk around as he is bored -- the inmates are yet to arrive. 
#He notices that all the cells are open. He proceeds to close them, going from cell number 1 to 100 in order. 
#He returns to the beginning and visits all even numbered cells: 2, 4, 6 ....100, opening the doors of the visited cells. 
#Again he returns to the beginning and this times visits cells 3, 6, 9 ... 99. 
#As he encounters both closed and open doors, he closes the open doors and opens the closed doors.
#He continues his rounds the same way visiting 4,8, ... 5, 10, ..., 6, 12 ... till he completes 100 rounds. 
#Which doors are open and which are closed? 
#Discussion A nested for loop will do the task with a list of 100 elements and adjusting the index or using the cell number as the index and using a list of 101 elements (ignoring index 0)

def jail_doors_simulation(num_cells):
    doors = [0] * (num_cells + 1)  # Initializing all doors as closed (0)

    # Iterate through rounds
    for i in range(1, num_cells + 1):
        # Iterate through cells
        for j in range(i, num_cells + 1, i):
            # Toggle the state of the door
            doors[j] = 1 - doors[j]

    # Print the result
    for k in range(1, num_cells + 1):
        if doors[k] == 1:
            print(f"Door {k} is open.")
        else:
            print(f"Door {k} is closed.")

# Run the simulation for 100 cells
jail_doors_simulation(100)
