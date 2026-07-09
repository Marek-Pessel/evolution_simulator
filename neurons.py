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
    
    def calc_output(self, env, creat):
        # is anyone inhibitate this neuron?
        act = self.calc_activation()
        if act >= 0:
            self.output = self.percept(env, creat) + act
        else:
            self.output = 0

    def percept(self, env, creat):
        pass

def dst_north(self, env, creat)->float:
    #print("-- dst_north was called")

    dst = 0
    while True:
        # check cells northern from the creature
        if env.world_grid[creat.location[0]-(dst+1)][creat.location[1]].blocked:
            break
        else:
            dst += 1
    
    if dst == 0:
        return 1.5
    else:
        return 1/dst

def dst_south(self, env, creat)->float:
    #print("-- dst_south was called")
    dst = 0
    while True:
        # check cells northern from the creature
        if env.world_grid[creat.location[0]+(dst+1)][creat.location[1]].blocked:
            break
        else:
            dst += 1
    
    if dst == 0:
        return 1.5
    else:
        return 1/dst

def dst_east(self, env, creat)->float:
    #print("-- dst_east was called")
    dst = 0
    while True:
        # check cells northern from the creature
        if env.world_grid[creat.location[0]][creat.location[1]+(dst+1)].blocked:
            break
        else:
            dst += 1
    
    if dst == 0:
        return 1.5
    else:
        return 1/dst

def dst_west(self, env, creat)->float:
    #print("-- dst_west was called")
    dst = 0
    while True:
        # check cells northern from the creature
        if env.world_grid[creat.location[0]][creat.location[1]-(dst+1)].blocked:
            break
        else:
            dst += 1
    
    if dst == 0:
        return 1.5
    else:
        return 1/dst

PN_DICT = {
    "dst_n":dst_north,
    "dst_s":dst_south,
    "dst_e":dst_east,
    "dst_w":dst_west
}

#######  ACTION NEURONS AND FUNCTIONS  #################################
class ActionNeuron(NEURON):
    def __init__(self, name, threshold=0.4):
        super().__init__(name, threshold)

    def ex_action(self,env, creat):
        pass

def mv_north(self, env, creat):
    #print("-- mv_north was called")
    motion = [-1,0] # [y,x]
    # is neuron firering?
    self.calc_output()
    activated = self.output >= self.th
    # is goal loction occupied or end of the map?
    occupied = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].isCreature
    blocked = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].blocked
    if activated and not (occupied or blocked):
        # creature moves
        creat.location[0] += motion[0]
        creat.location[1] += motion[1]
        print(f"creature-{creat.ID} moved to {creat.location}")
        # block new location
        env.world_grid[creat.location[0]][creat.location[1]].isCreature = True
        #print(f"Cell [{creat.location[0]},{creat.location[1]}] blocked")
        # unblock old location
        env.world_grid[creat.location[0]-motion[0]][creat.location[1]-motion[1]].isCreature = False
        #print(f"Cell [{creat.location[0]-motion[0]},{creat.location[1]-motion[1]}]")
        
def mv_south(self, env, creat):
    #print("-- mv_south was called")
    motion = [1,0] # [y,x]
    # is neuron firering?
    self.calc_output()
    activated = self.output >= self.th
    # is goal loction occupied or end of the map?
    occupied = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].isCreature
    blocked = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].blocked
    if activated and not (occupied or blocked):
        # creature moves
        creat.location[0] += motion[0]
        creat.location[1] += motion[1]
        print(f"creature-{creat.ID} moved to {creat.location}")
        # block new location
        env.world_grid[creat.location[0]][creat.location[1]].isCreature = True
        #print(f"Cell [{creat.location[0]},{creat.location[1]}] blocked")
        # unblock old location
        env.world_grid[creat.location[0]-motion[0]][creat.location[1]-motion[1]].isCreature = False
        #print(f"Cell [{creat.location[0]-motion[0]},{creat.location[1]-motion[1]}]")

def mv_east(self, env, creat):
    #print("-- mv_east was called")
    motion = [0,1] # [y,x]
    # is neuron firering?
    self.calc_output()
    activated = self.output >= self.th
    # is goal loction occupied or end of the map?
    occupied = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].isCreature
    blocked = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].blocked
    if activated and not (occupied or blocked):
        # creature moves
        creat.location[0] += motion[0]
        creat.location[1] += motion[1]
        print(f"creature-{creat.ID} moved to {creat.location}")
        # block new location
        env.world_grid[creat.location[0]][creat.location[1]].isCreature = True
        #print(f"Cell [{creat.location[0]},{creat.location[1]}] blocked")
        # unblock old location
        env.world_grid[creat.location[0]-motion[0]][creat.location[1]-motion[1]].isCreature = False
        #print(f"Cell [{creat.location[0]-motion[0]},{creat.location[1]-motion[1]}]")

def mv_west(self, env, creat):
    #print("-- mv_west was called")
    motion = [0,-1] # [y,x]
    # is neuron firering?
    self.calc_output()
    activated = self.output >= self.th
    # is goal loction occupied or end of the map?
    occupied = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].isCreature
    blocked = env.world_grid[creat.location[0]+motion[0]][creat.location[1]+motion[1]].blocked
    if activated and not (occupied or blocked):
        # creature moves
        creat.location[0] += motion[0]
        creat.location[1] += motion[1]
        print(f"creature-{creat.ID} moved to {creat.location}")
        # block new location
        env.world_grid[creat.location[0]][creat.location[1]].isCreature = True
        #print(f"Cell [{creat.location[0]},{creat.location[1]}] is blocked")
        # unblock old location
        env.world_grid[creat.location[0]-motion[0]][creat.location[1]-motion[1]].isCreature = False
        #print(f"Cell [{creat.location[0]-motion[0]},{creat.location[1]-motion[1]}] is free")


AN_DICT = {
    "mv_n":mv_north,
    "mv_s":mv_south,
    "mv_e":mv_east,
    "mv_w":mv_west
}

def create_neurons()->list[NEURON]:
    AN_list = []
    for key in list(AN_DICT.keys()):
        an_ = ActionNeuron(key, threshold=0.3)
        an_.ex_action = MethodType(AN_DICT.get(key), an_)
        AN_list.append(an_)
    
    PN_list = []
    for key in list(PN_DICT.keys()):
        pn_ = PerceptionNeuron(key)
        pn_.percept = MethodType(PN_DICT.get(key), pn_)
        PN_list.append(pn_)

    return AN_list, PN_list
