import numpy as np

#######################
class NEURON():

    def __init__(self):
        self.connect_in = []
        self.connect_out = []
        #self.input = np.array([])
        self.output = 0
        self.weight = np.array([])

    def calc_activation(self):
        input = np.array([pre.output for pre in self.connect_in])
        activation = self.weight @ input
        # test comment

        return activation

    def calc_output(self):
        act = self.calc_activation()
        self.output = np.tanh(act)

    def connect_with(self, neuron, w):
        self.connect_in.append(neuron)
        self.weight = np.append(self.weight, w)


#######################################
class InnerNeuron(NEURON):
    def __init__(self):
        super().__init__()


########################################
class PerceptionNeuron(NEURON):
    def __init__(self):
        super().__init__()
        self.input = 0

    def calc_activation(self):
        act = self.input % 2 * 10
        if act:
            print("Odd detected")
        return act


########################################
class ActionNeuron(NEURON):
    def __init__(self):
        super().__init__()


    def ex_action(self,env):
        self.calc_output()
        y=0
        x=0
        if self.output > 0.5:
            y = np.random.randint(-1,1)
            x = np.random.randint(-1,1)

        return [y,x]

    