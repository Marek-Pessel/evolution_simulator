import numpy as np
from neurons import InnerNeuron as IN, PerceptionNeuron as PN, ActionNeuron as AN
from neurons import create_neurons


perc1 = PN(name="perc1")
perc2 = PN(name="perc2")
perc3 = PN(name="perc3")
perc4 = PN(name="perc4")
act1 = AN(name="act1")
act2 = AN(name="act2")
act3 = AN(name="act3")
act4 = AN(name="act4")


class Creature():
    def __init__(self, Gene=4, N_inner=4):
        self.inner_neurons  = [IN(f"inner{i+1}") for i in range(N_inner)]
        self.perc_neurons   = [PN(f"perc{i+1}") for i in range(4)]
        self.act_neurouns   = create_neurons()
        self.location       = []    # [y,x]
        self.ID             = str(np.random.randint(100,999))
        self.Gene           = Gene   # int or list[0x]
        self.init_brain()
        self.color          = self.color_from_gene()

    def init_brain(self):
        if isinstance(self.Gene, int):
            print("## Gene is INTEGER")
            self.Gene = self.random_genes()
            print(f"-- Gene was generated:\n {self.Gene}")
        
        for gene in self.Gene:
            print(f"-- Use gene: {gene}")
            # hex to bin
            binary = bin(int(gene, 16))
            # cut off 0b prefix
            binary = binary[2:] # 24-digit binary
            # slice binary to meaningfull peaces
            post = int(binary[:4],2)        # neuron type
            post_spec = int(binary[4:9],2)  # which of those?
            pre = int(binary[9:13],2)       # neuron type
            pre_spec = int(binary[13:18],2) # which of those
            sign = int(binary[18],2)        # +/- aka 0/1
            weight = int(binary[19:],2) / 8    # abs of the connection weight [0,4]

            ### connect neurons following genetic information
            # choose presynaptic neuron
            pre_neuron = self.choose_neuron(pre, pre_spec)
            # choose postsynaptic neuron
            post_neuron = self.choose_neuron(post, post_spec)
            # calc weight for connection
            if sign:
                weight *= -1
            
            # connect neurons
            post_neuron.connect_with(pre_neuron, weight)
            print(f"-- connected {pre_neuron} --[{weight}]--> {post_neuron}")

    def color_from_gene(self):
        
        summed = sum([int(gene,16) for gene in self.Gene])
        normed = int(summed / len(self.Gene))

        return hex(normed)

    def random_genes(self) -> list[str]:
        """
        Just call in times self.Gene is an integer (Genecode has to be generated).
        Returns a list with n-time random hex strings between 0x100000 and 0xffffff.
        """

        min_gene_code = int('100000', 16)    # lowest 6-digit Hex as low bound
        max_gene_code = int('ffffff', 16)    # highest 6-digit Hex as high bound

        # generate random genes
        _Gene = []
        print(f"-- create {self.Gene} random genes")
        for i in range(self.Gene):
            _gene = np.random.randint(min_gene_code, max_gene_code) # int
            _gene = hex(_gene)    # hexadecimal string
            _Gene.append(_gene)
        
        return _Gene

    def choose_neuron(self, type_, spec):
        if type_ < 5:
            choose_from = self.perc_neurons
        elif type_ < 10:
            choose_from = self.inner_neurons
        else:
            choose_from = self.act_neurouns

        idx = int(len(choose_from)/32 * spec)

        return choose_from[idx]
        
    def __str__(self):
        ret = f"\n########  Creature-{self.ID}   ########\n"
        ret += f"at location {self.location}\nBrain is:\n"
        neur = self.perc_neurons + self.inner_neurons + self.act_neurouns
        for n in neur:
            for i, each in enumerate(n.connect_in):
                ret += f"{each} --[{n.weight[i]}]--> {n}\n"

        return ret

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
            


        