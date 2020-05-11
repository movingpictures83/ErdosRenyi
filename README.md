# ErdosRenyi
# Language: Python
# Input: TXT
# Output: GML
# Tested with: PluMA 1.0, Python 3.6
# Dependency: Networkx 2.4

PluMA plugin that uses the Erdos-Renyi algorithm to compute a random network of a user-specified number of nodes and edges.

The node and edge count are entered into an input TXT file of tab-delineated keywords and values (the keywords are "nodes" and "edges", respectively).

Output will be the network, in the Graph Modeling Language (GML) format.
