import numpy as np


class WorldCell():
    def __init__(self):
        self.blocked = False
        self.isCreature = False
        self.isFood = False

#############

class World():
    def __init__(self, size = [10,10]):
        self.size = size
        self.world_grid = []

        for y in range(size[0]):
            row_y = []
            for x in range(size[1]):
                cell_ = WorldCell()
                # is cell an edge cell?
                if y == 0 or y == size[0]-1 or x == 0 or x == size[1]-1:
                    cell_.blocked = True
                row_y.append(cell_) # add current cell to row

            self.world_grid.append(row_y) # add current row to grid

    def __str__(self):
        ret = "\n"
        for row in self.world_grid:
            row_ = []
            for cell_ in row:
                marker = 0
                if cell_.blocked:
                    marker = 1
                elif cell_.isFood:
                    marker = 2
                
                row_.append(marker)
            ret += f"{row_}\n"
        
        return ret
            