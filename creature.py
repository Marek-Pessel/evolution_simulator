import numpy as np
from neurons import InnerNeuron as IN, PerceptionNeuron as PN, ActionNeuron as AN


inner1 = IN()
perc1 = PN()
act1 = AN()

inner1.connect_with(perc1)
act1.connect_with(inner1)


class Creature():
    def __init__(self, Gen:int|list=4, N_inner=4):
        self.inner_neurons  = [IN() for i in range(N_inner)]
        self.perc_neurons   = [perc1]
        self.act_neurouns   = [act1]
        self.location       = []    # [y,x]
        self.ID             = str(np.random.randint(100,999))
        self.Gen            = Gen   # int or list[0x]

        self.init_brain()

    def init_brain(self):
        if isinstance(self.Gen, int):
            #TODO: random gen genrator
            pass
        
        #TODO: use gen code


        
    def __str__(self):
        return self.ID

    def live_step(self, env):
        print(f"---- Creature {self} acts ----")
        self.perc_neurons[0].input = np.random.randint(-10,10)

        for perc in self.perc_neurons:
            perc.calc_output()

        for inner in self.inner_neurons:
            inner.calc_output()

        for act in self.act_neurouns:
            motion = act.ex_action(env)
            if motion[0] == 0 and motion[1] == 0:
                print(f"No motion commands")
                continue
            new_y = self.location[0] + motion[0]
            new_x = self.location[1] + motion[1]

            if not env.world_grid[new_y][new_x].blocked:
                # free up old cell
                env.world_grid[self.location[0]][self.location[1]].blocked = False
                # block new cell
                env.world_grid[new_y][new_x].blocked = True
                # update location
                self.location = [new_y,new_x]
                print(f"moved to new cell {self.location}")
            else:
                print(f"cell [{new_y},{new_x}] was blocked")
            


        