import networkx as nx
from database.DAO import DAO
class Model:
    def __init__(self):
        self._listChromosomes = None
        self._graph = nx.DiGraph()
        self._listGenes = []
        self._idMap = {}

    def buildGraph(self):
        self._listChromosomes = DAO.get_all_chromosomes()
        self._graph.add_nodes_from(self._listChromosomes)
        self._listGenes = DAO.get_all_genes()
        for g in self._listGenes:
            self._idMap[g.GeneID] = g

        self._archi = DAO.get_all_edges()
        for a in self._archi:
            cr1 = a[0]
            cr2 = a[1]
            corr = a[4]
            if cr1 in self._graph.nodes and cr2 in self._graph.nodes:
                if self._graph.has_edge(cr1, cr2):
                    self._graph[cr1][cr2]['weight'] += corr
                else:
                    self._graph.add_edge(cr1, cr2, weight=corr)

    def calcolaMin(self):
        pesoMin = 100000
        for a in self._graph.edges():
            peso = self._graph[a[0]][a[1]]['weight']
            if peso < pesoMin:
                pesoMin = peso
        return pesoMin
    def calcolaMax(self):
        pesoMax = 0
        for a in self._graph.edges():
            peso = self._graph[a[0]][a[1]]['weight']
            if peso > pesoMax:
                pesoMax = peso
        return pesoMax

    def getNumNodi(self):
        return len(self._graph.nodes)
    def getNumArchi(self):
        return len(self._graph.edges)

    def contaValoriSoglia(self, soglia):
        numMaggiori = 0
        numMinori = 0
        for a in self._graph.edges:
            peso = self._graph[a[0]][a[1]]['weight']
            if peso > soglia:
                numMaggiori += 1
            else:
                numMinori += 1
        return numMaggiori, numMinori




