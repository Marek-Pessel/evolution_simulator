import numpy as np
from types import MethodType

#######################
class NEURON():

    def __init__(self, name, threshold=0.5):
        self.connect_in = []
        self.connect_out = []
        #self.input = np.array([])
        self.output = 0
        self.weight = np.array([])
        self.name = name
        self.th = threshold

    def calc_activation(self)->float:
        input = np.array([pre.output for pre in self.connect_in])
        activation = self.weight @ input
        return activation

    def calc_output(self):
        act = self.calc_activation()
        self.output = np.tanh(act)

    def connect_with(self, neuron, w):
        self.connect_in.append(neuron)
        self.weight = np.append(self.weight, w)

    def __str__(self):
        return self.name


#######################################
class InnerNeuron(NEURON):
    def __init__(self, name):
        super().__init__(name)


#######  PERCEPTION NEURONS AND FUNCTIONS  #################################
class PerceptionNeuron(NEURON):
    def __init__(self, name):
        super().__init__(name)
        self.input = 0

    def calc_activation(self):
        act = self.input % 2 * 10
        if act:
            print("Odd detected")
        return act


#######  ACTION NEURONS AND FUNCTIONS  #################################
class ActionNeuron(NEURON):
    def __init__(self, name):
        super().__init__(name)

    def ex_action(self,env, creat):
        pass

def mv_north(self, env, creat):
    motion = [-1,0] # [y,x]
    # is neuron firering?
    actived = self.calc_output() >= self.th
    # is goal loction occupied?
    occupied = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].blocked
    if actived and not occupied:
        # creature moves
        creat.location[0] += motion[0]
        creat.location[1] += motion[1]
        # block new location
        env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]] = True
        # unblock old location
        env.world_grid[creat.location[0]-motion[0]][creat.location[1]-motion[1]] = False
        
def mv_south(self, env, creat):
    motion = [1,0] # [y,x]
    # is neuron firering?
    actived = self.calc_output() >= self.th
    # is goal loction occupied?
    occupied = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].blocked
    if actived and not occupied:
        # creature moves
        creat.location[0] += motion[0]
        creat.location[1] += motion[1]
        # block new location
        env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]] = True
        # unblock old location
        env.world_grid[creat.location[0]-motion[0]][creat.location[1]-motion[1]] = False

def mv_east(self, env, creat):
    motion = [0,1] # [y,x]
    # is neuron firering?
    actived = self.calc_output() >= self.th
    # is goal loction occupied?
    occupied = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].blocked
    if actived and not occupied:
        # creature moves
        creat.location[0] += motion[0]
        creat.location[1] += motion[1]
        # block new location
        env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]] = True
        # unblock old location
        env.world_grid[creat.location[0]-motion[0]][creat.location[1]-motion[1]] = False

def mv_west(self, env, creat):
    motion = [0,-1] # [y,x]
    # is neuron firering?
    actived = self.calc_output() >= self.th
    # is goal loction occupied?
    occupied = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].blocked
    if actived and not occupied:
        # creature moves
        creat.location[0] += motion[0]
        creat.location[1] += motion[1]
        # block new location
        env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]] = True
        # unblock old location
        env.world_grid[creat.location[0]-motion[0]][creat.location[1]-motion[1]] = False


AN_DICT = {
    "mv_n":mv_north,
    "mv_s":mv_south,
    "mv_e":mv_east,
    "mv_w":mv_west
}
def create_neurons()->list[NEURON]:
    AN_list = []
    for key in list(AN_DICT.keys()):
        an_ = ActionNeuron(key)
        an_.ex_action = MethodType(AN_DICT.get(key), an_)
        AN_list.append(an_)

    return AN_list
