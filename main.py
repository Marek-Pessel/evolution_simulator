from creature import Creature
from world import World
import numpy as np
from plot_utils import fix_sim_step as fix

### Define Settings ###
SIZE = [128,128]  # World dimensions [y,x]
INDIVIDUALS = 10 # how many creatures to create
TIME = 10       # Simulation time for one generation  

# init world map
env = World(size=SIZE)

# init creatures and place in world
CREATURES = []
for i in range(INDIVIDUALS):
    c = Creature(N_inner=2)

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

time = 0
print(f"\n##### World at step {time} #####")
print(env)

while time < TIME:

    for c in CREATURES:
        c.live_step(env)

    time += 1
    print(f"\n##### World at step {time} #####")
    print(env)
    fix(size=SIZE, creatures=CREATURES)