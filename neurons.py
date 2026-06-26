import numpy as np

#######################
class NEURON():

    def __init__(self, name):
        self.connect_in = []
        self.connect_out = []
        #self.input = np.array([])
        self.output = 0
        self.weight = np.array([])
        self.name = name

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

    def __str__(self):
        return self.name


#######################################
class InnerNeuron(NEURON):
    def __init__(self, name):
        super().__init__(name)


########################################
class PerceptionNeuron(NEURON):
    def __init__(self, name):
        super().__init__(name)
        self.input = 0

    def calc_activation(self):
        act = self.input % 2 * 10
        if act:
            print("Odd detected")
        return act


########################################
class ActionNeuron(NEURON):
    def __init__(self, name):
        super().__init__(name)


    def ex_action(self,env):
        self.calc_output()
        y=0
        x=0
        if self.output > 0.5:
            y = np.random.randint(-1,1)
            x = np.random.randint(-1,1)

        return [y,x]

    