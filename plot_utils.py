import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb



def fix_sim_step(size, creatures):
    
    # Hintergrund = weiß
    grid = np.ones((size[0], size[1], 3), dtype=float)
    creats = []
    for creature in creatures:
        row = creature.location[0]
        col = creature.location[1]
        color = creature.color[2:]
        color = f"#{color}"

        grid[row, col] = to_rgb(color)

    #fig, ax = plt.subplots(figsize=(size[0], size[1]))
    #ax.imshow(grid, interpolation="none")
    for creature in creatures:
        color = creature.color[2:]
        color = f"#{color}"
        plt.scatter(
        creature.location[1],
        creature.location[0],
        s=10,                 # Größe
        c=color,                # Hex-Farbe
        marker="o",            # Kreis
        edgecolors="grey",
        #figsize=(size[0], size[1])
    )

    # Always show the complete environment
    plt.xlim(-0.5, size[1] - 0.5)
    plt.ylim(size[0] - 0.5, -0.5)
    plt.gca().set_aspect("equal")
    plt.xticks([])
    plt.yticks([])
    #plt.set_aspect("equal")
    #ax.grid(True, color="grey", linewidth=0.5)
    
    plt.show()