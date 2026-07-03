from creature import Creature
from world import World
import numpy as np
from plot_utils import *
import csv
import os

### Define Settings ###
SIZE = [128,128]  # World dimensions [y,x]
INDIVIDUALS = 30 # how many creatures to create
TIME = 300       # Simulation time for one generation  

# init world map
env = World(size=SIZE)

# init creatures and place in world
CREATURES = []
for i in range(INDIVIDUALS):
    c = Creature(Gene=8, N_inner=4)

    while True:
        y = np.random.randint(1,SIZE[0]-2)
        x = np.random.randint(1,SIZE[1]-2)
        if not env.world_grid[y][x].blocked:
            c.location = [y,x]
            env.world_grid[y][x].blocked = True
            break
        else:
            print(f"Cell ({y}|{x}) is blocked")
    CREATURES.append(c)
    print(c)

#exit()

############  testing  #######
world_states = []
time = 0
print(f"\n##### World at step {time} #####")
#print(env)
#fix(size=SIZE, creatures=CREATURES, iteration=time)

while time < TIME:
    world_state = []
    for c in CREATURES:
        # let creature do its thing
        c.live_step(env)
        # store individual state as string "Y_X_0xRRGGBB"
        c_state = f"{c.location[0]}_{c.location[1]}_{c.color}"
        # add string to world_state
        world_state.append(c_state)
    
    # store world_state
    world_states.append(world_state)

    time += 1
    print(f"\n##### World at step {time} #####")
    #print(env)
    #fix(size=SIZE, creatures=CREATURES, iteration=time)


# save world_states as .csv
with open("test_plots/WorldStates.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(world_states)

video_from_csv("test_plots/WorldStates.csv", "test_plots/simulation.mp4")
os.system(f'start "" "test_plots/simulation.mp4"')