import networkx
import random
random.seed(1234)

class ErdosRenyiPlugin:
	def input(self, filename):
                inputfile = open(filename, 'r')
                self.parameters = dict()
                for line in inputfile:
                   contents = line.split('\t')
                   self.parameters[contents[0]] = int(contents[1])


	def run(self):
                self.G = networkx.gnm_random_graph(self.parameters['nodes'],
                                                   self.parameters['edges'])

	def output(self, filename):
		networkx.write_gml(self.G, filename)
