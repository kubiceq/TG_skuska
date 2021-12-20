import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import pydot
from networkx.drawing.nx_pydot import graphviz_layout



class Vrchol(object):
    cislo = 0
    stupen = 0
    farba = 0

    def __init__(self, cislo, stupen, farba):
        self.cislo = cislo
        self.stupen = stupen
        self.farba = farba
    def __str__(self):
        print("Vrchol  ", self.cislo)
        print("Stupen  ", self.stupen)
        print("Farba    ", self.farba)
        return self.farba

#Global(and needed) variables
COLOR = "tab:blue"
i=0


print('#*********************************************Prehladanie grafu *********************************************')


#definuj graf
Graf_z_ulohy_1 = nx.Graph()
#matica susednosti(zadanie):
#################################################################################################################
# #Test0
# matica_susednosti = np.array([[0,1,0,0,0,0,1,0,0,0],
#                               [1,0,1,0,1,1,1,0,0,0],
#                               [0,1,0,1,1,0,0,0,0,0],
#                               [0,0,1,0,0,0,0,0,1,1],
#                               [0,1,1,0,0,1,0,0,1,0],
#                               [0,1,0,0,1,0,1,1,0,0],
#                               [1,1,0,0,0,1,0,1,0,0],
#                               [0,0,0,0,0,1,1,0,1,0],
#                               [0,0,0,1,1,0,0,1,0,1],
#                               [0,0,0,1,0,0,0,0,1,0]])
matica_susednosti = np.array([[0,0,1,0,0,0],
                              [0,0,1,1,0,0],
                              [1,1,0,1,1,1],
                              [0,1,1,0,1,1],
                              [0,0,1,1,0,1],
                              [0,0,1,1,1,0]])
#####################################################################################################################

# naformatuj tabulku
table = tabulate(matica_susednosti, tablefmt="simple")
print('************************MATICA_SUSEDNOSTI****************************')
print(table)
#vytvorenie grafu z matice susednosti
Graf_z_ulohy_1 = nx.from_numpy_matrix(matica_susednosti,create_using=nx.DiGraph())

#prehladaj do hlbky
print("Stromy pri prehladani do hlbky")
for vrchol in range(Graf_z_ulohy_1.order()):
    Strom_hlbky = nx.dfs_tree(Graf_z_ulohy_1, source=vrchol)
    hrany_od_0 = nx.dfs_edges(Strom_hlbky)
    hrany_od_1 = []
    # kedze my cislujeme vrcholy od 1, nie od 0, tak kazdu hranu premenujem +1
    for hrana in list(hrany_od_0):
        hrana = list(hrana)
        hrana[0] += 1
        hrana[1] += 1
        hrany_od_1.append(hrana)
    print(hrany_od_1)

#prehladaj do sirky pre vsetky vrcholy
print("Stromy pri prehladani do sirky")
for vrchol in range(Graf_z_ulohy_1.order()):
    Strom_sirky = nx.bfs_tree(Graf_z_ulohy_1, source=vrchol)
    hrany_od_0 = nx.dfs_edges(Strom_sirky)
    hrany_od_1 = []
    #kedze my cislujeme vrcholy od 1, nie od 0, tak kazdu hranu premenujem +1
    for hrana in list(hrany_od_0):
        hrana = list(hrana)
        hrana[0] += 1
        hrana[1] += 1
        hrany_od_1.append(hrana)
    print(hrany_od_1)

print("********************************Farbenie grafu**************************************")
#############################################################################################################################################
matica_susednosti = np.array([[0,1,0,0,0,0,1,0,0,0],
                              [1,0,1,0,1,1,1,0,0,0],
                              [0,1,0,1,1,0,0,0,0,0],
                              [0,0,1,0,0,0,0,0,1,1],
                              [0,1,1,0,0,1,0,0,1,0],
                              [0,1,0,0,1,0,1,1,0,0],
                              [1,1,0,0,0,1,0,1,0,0],
                              [0,0,0,0,0,1,1,0,1,0],
                              [0,0,0,1,1,0,0,1,0,1],
                              [0,0,0,1,0,0,0,0,1,0]])
# matica_susednosti = np.array([[],
#                               [],
#                               [],
#                               [],
#                               [],
#                               [],
#                               [],
#                               []])
#############################################################################################################################################

print("Usporiadane podla VRCHOLU")
degrees = [val for (node, val) in Graf_z_ulohy_1.degree()]
farbenie = nx.coloring.greedy_color(Graf_z_ulohy_1, strategy="largest_first")
pole_vrcholov = []
for vrchol in list(Graf_z_ulohy_1.nodes):
    print("vrchol: ",vrchol+1,"  stupen: ",degrees[vrchol]/2,"  farba: ",farbenie[vrchol]+1)
    pole_vrcholov.append(Vrchol(vrchol+1,degrees[vrchol]/2,farbenie[vrchol]+1))


newlist = sorted(pole_vrcholov, key=lambda x: x.stupen, reverse=True)
print("Usporiadane podla STUPNA")
for vrchol in newlist:
    print("vrchol: ",vrchol.cislo,"  stupen: ",vrchol.stupen,"  farba: ",vrchol.farba)
newlist = sorted(pole_vrcholov, key=lambda x: x.farba, reverse=False)
print("Usporiadane podla FARBY")
for vrchol in newlist:
    print("vrchol: ",vrchol.cislo,"  stupen: ",vrchol.stupen,"  farba: ",vrchol.farba)








##########################################################################################################################################################################################################################################################################################
print('#*********************************************   Matica najkratsej cesty    **********************************************************************************')
#????????????????????????????????????????????????????????????????????
#INF je pre nas nekonecno. preto ak bude v maticiach nejake velke cislo(blizke nasej INF), bude to pravdepodobne nekonecno
INF = 9999
# Algorithm
def floyd(G):
    dist = list(map(lambda p: list(map(lambda q: q, p)), G))
    # Adding vertices individually
    for r in range(nV):
        print("Stupen(D)",r+1)
        for p in range(nV):
            for q in range(nV):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
        sol(dist)
        print('**********************************************************************')
# Printing the output
def sol(dist):
    table = tabulate(dist, tablefmt="simple")
    print(table)

#Cenova Matica
#????????????????????????????????????????????????????????????????????#????????????????????????????????????????????????????????????????????#????????????????????????????????????????????????????????????????????
G =      [[0,6,INF,4,5,1],
         [6,0,9,INF,INF,3],
         [INF,9,0,10,INF,4],
         [4,INF,10,0,11,INF],
         [5,INF,INF,11,0,7],
         [6,3,4,INF,7,0]]

# G =      [[],
#          [],
#          [],
#          [],
#          [],
#          []]
#????????????????????????????????????????????????????????????????????#????????????????????????????????????????????????????????????????????#????????????????????????????????????????????????????????????????????


nV = len(G)
print('Zadanie == Stupen 0')
dist = list(map(lambda p: list(map(lambda q: q, p)), G))
sol(dist)
floyd(G)


print('#*********************************************   Hladanie kostier   **********************************************************************************')

from networkx.algorithms import tree
from networkx.drawing.nx_pydot import graphviz_layout
Graf_z_ulohy_3 = nx.Graph()

#definuj hrany
#????????????????????????????????????????????????????????????????????#????????????????????????????????????????????????????????????????????#????????????????????????????????????????????????????????????????????

#Patrik
Graf_z_ulohy_3.add_edge("1","2", weight =10 )
Graf_z_ulohy_3.add_edge("1","4", weight =9 )
Graf_z_ulohy_3.add_edge("1","6", weight =20 )
Graf_z_ulohy_3.add_edge("1","8", weight =16 )
Graf_z_ulohy_3.add_edge("2","3", weight =8 )
Graf_z_ulohy_3.add_edge("2","7", weight =18 )
Graf_z_ulohy_3.add_edge("3","4", weight =18 )
Graf_z_ulohy_3.add_edge("3","5", weight =9 )
Graf_z_ulohy_3.add_edge("3","8", weight = 15)
Graf_z_ulohy_3.add_edge("4","6", weight =14 )
Graf_z_ulohy_3.add_edge("5","6", weight =8 )
Graf_z_ulohy_3.add_edge("5","7", weight =7 )
Graf_z_ulohy_3.add_edge("7","8", weight = 12)

#????????????????????????????????????????????????????????????????????#????????????????????????????????????????????????????????????????????#????????????????????????????????????????????????????????????????????

#nakresli graf 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# i+=1
# plt.figure(i)
# plt.title('Graf 3')
# pos=nx.shell_layout(Graf_z_ulohy_3)
# nx.draw_networkx(Graf_z_ulohy_3,pos)
# labels = nx.get_edge_attributes(Graf_z_ulohy_3,'weight')
# nx.draw_networkx_edge_labels(Graf_z_ulohy_3,pos,edge_labels=labels)
# plt.show()
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#najdi minimalny strom grafu 3
print("minimalna  kostra: ")
minst = tree.minimum_spanning_edges(Graf_z_ulohy_3, algorithm='kruskal', data=False)
edgelist = list(minst)
vahaStromu = 0
for hrana in edgelist:
    vahaStromu+= Graf_z_ulohy_3.get_edge_data(hrana[0],hrana[1])['weight']
print(sorted(edgelist))
print("Vaha Minimalnej Kostry = ",vahaStromu)



#vykresli minimalny strom grafu 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tmin = nx.Graph();
# Tmin.add_edges_from(edgelist)
# i+=1
# plt.figure(i)
# plt.title('Minimalna kostra grafu 3')
# nx.draw(Tmin, with_labels=True)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#vykresli minimalny strom V grafe 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# i+=1
# plt.figure(i)
# plt.title('Minimalny strom v Grafe 3')
# pos=nx.shell_layout(Graf_z_ulohy_3)
# nx.draw_networkx(Graf_z_ulohy_3,pos)
# labels = nx.get_edge_attributes(Graf_z_ulohy_3,'weight')
# nx.draw_networkx_edges(Graf_z_ulohy_3,pos,edgelist=edgelist,edge_color= COLOR,width=4)
# nx.draw_networkx_edge_labels(Graf_z_ulohy_3,pos,edge_labels=labels)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#najdi maximalny strom
print("maximalny strom / kostra: ")
maxst = tree.maximum_spanning_edges(Graf_z_ulohy_3, algorithm='kruskal', data=False)
edgelist = list(maxst)
vahaStromu = 0
for hrana in edgelist:
    vahaStromu+= Graf_z_ulohy_3.get_edge_data(hrana[0],hrana[1])['weight']
print(sorted(edgelist))
print("Vaha Maximalneho Stromu = ",vahaStromu)

#vykresli maximalny strom
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tmax = nx.Graph();
# Tmax.add_edges_from(edgelist)
# i+=1
# plt.figure(i)
# plt.title('Maximalna kostra grafu 3')
# nx.draw(Tmax, with_labels=True)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#vykresli maximalny strom V grafe 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# i+=1
# plt.figure(i)
# plt.title('Maximalny strom v grafe 3')
# pos=nx.shell_layout(Graf_z_ulohy_3)
# nx.draw_networkx(Graf_z_ulohy_3,pos)
# labels = nx.get_edge_attributes(Graf_z_ulohy_3,'weight')
# nx.draw_networkx_edges(Graf_z_ulohy_3,pos,edgelist=edgelist,edge_color= COLOR,width=4)
# nx.draw_networkx_edge_labels(Graf_z_ulohy_3,pos,edge_labels=labels)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




print('#*********************************************   Djikstra   **********************************************************************************')

Graf_Djikstra = nx.Graph()
Graf_Djikstra.add_edge("1","2", weight =10 )
Graf_Djikstra.add_edge("1","4", weight =9 )
Graf_Djikstra.add_edge("1","6", weight =20 )
Graf_Djikstra.add_edge("1","8", weight =16 )
Graf_Djikstra.add_edge("2","3", weight =8 )
Graf_Djikstra.add_edge("2","7", weight =18 )
Graf_Djikstra.add_edge("3","4", weight =18 )
Graf_Djikstra.add_edge("3","5", weight =9 )
Graf_Djikstra.add_edge("3","8", weight = 15)
Graf_Djikstra.add_edge("4","6", weight =14 )
Graf_Djikstra.add_edge("5","6", weight =8 )
Graf_Djikstra.add_edge("5","7", weight =7 )
Graf_Djikstra.add_edge("7","8", weight = 12)

for x in range (len(Graf_Djikstra.nodes())):
    for y in range(len(Graf_Djikstra.nodes())):
        cesta = nx.dijkstra_path(Graf_Djikstra, str(x+1), str(y+1))
        print(x + 1, " -> ", y + 1, " -> ", cesta)


print('#*********************************************   Euler   **********************************************************************************')

Graf_Euler = nx.Graph()
#Test 0
# Graf_Euler.add_edge("1","2")
# Graf_Euler.add_edge("2","3")
# Graf_Euler.add_edge("3","4")
# Graf_Euler.add_edge("4","5")
# Graf_Euler.add_edge("5","6")
# Graf_Euler.add_edge("6","7")
# Graf_Euler.add_edge("7","8")
# Graf_Euler.add_edge("8","9")
# Graf_Euler.add_edge("8","3")
# Graf_Euler.add_edge("3","7")
# Graf_Euler.add_edge("7","9")

Graf_Euler.add_edge("1","2")
Graf_Euler.add_edge("2","3")
Graf_Euler.add_edge("3","4")
Graf_Euler.add_edge("4","1")


print ("Stupne vrcholov:",list(Graf_Euler.degree()))
if nx.is_eulerian(Graf_Euler):
    print("Ma eulerovsku kruznicu")
    print(list(nx.eulerian_circuit(Graf_Euler)))
else:
    print("Nema eulerovsku kruznicu")

if nx.has_eulerian_path(Graf_Euler):
    print("Ma eulerovsky tah ")
    print(list(nx.eulerian_path(Graf_Euler)))
else:
    print("Nema eulerovsky tah")









print('#*********************************************   Toky   **********************************************************************************')
Graf_z_ulohy_4 = nx.DiGraph()

#Patrik

Graf_z_ulohy_4.add_edge("z","1", capacity = 8 )
Graf_z_ulohy_4.add_edge("z","3", capacity = 7 )
Graf_z_ulohy_4.add_edge("z","2", capacity = 10 )
Graf_z_ulohy_4.add_edge("1","u", capacity = 5 )
Graf_z_ulohy_4.add_edge("1","3", capacity = 5 )
Graf_z_ulohy_4.add_edge("1","4", capacity = 7 )
Graf_z_ulohy_4.add_edge("2","1", capacity = 3 )
Graf_z_ulohy_4.add_edge("2","3", capacity = 4 )
Graf_z_ulohy_4.add_edge("2","4", capacity = 3 )
Graf_z_ulohy_4.add_edge("3","u", capacity = 8 )
Graf_z_ulohy_4.add_edge("3","4", capacity = 3 )
Graf_z_ulohy_4.add_edge("4","u", capacity = 11 )


#????????????????????????????????????????????????????????????????????

#vykresli Graf 4
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# i+=1
# plt.figure(i)
# plt.title('Graf 4')
# pos=nx.shell_layout(Graf_z_ulohy_4) # pos = nx.nx_agraph.graphviz_layout(G)
# nx.draw_networkx(Graf_z_ulohy_4,pos)
# labels = nx.get_edge_attributes(Graf_z_ulohy_4,'capacity')
# nx.draw_networkx_edge_labels(Graf_z_ulohy_4,pos,edge_labels=labels)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
kapacita, flow_dict = nx.maximum_flow(Graf_z_ulohy_4,"z","u")
print("Maximalny tok:",flow_dict)
print('Kapacita maximalneho toku: ',kapacita)

#vykresli maximalny tok v grafe 4
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# edgelist = []
# edgeLabels = {}
# for vrchol in flow_dict:
#     for protiVrchol in flow_dict[vrchol]:
#         edgelist.append([vrchol,protiVrchol])
#         edgeLabels[(vrchol,protiVrchol)] = flow_dict[vrchol][protiVrchol]
# i+=1
# plt.figure(i)
# plt.title('Graf 4')
# pos=nx.shell_layout(Graf_z_ulohy_4) # pos = nx.nx_agraph.graphviz_layout(G)
# nx.draw_networkx(Graf_z_ulohy_4,pos)
# labels = nx.get_edge_attributes(Graf_z_ulohy_4,'capacity')
# nx.draw_networkx_edge_labels(Graf_z_ulohy_4,pos,edge_labels=labels)
#
# i+=1
# plt.figure(i)
# plt.title('Graf 4 s maximalnou kapacitou toku')
# nx.draw_networkx(Graf_z_ulohy_4,pos)
# labels = edgeLabels
# nx.draw_networkx_edges(Graf_z_ulohy_4,pos,edgelist=edgelist,edge_color= COLOR,width=2)
# nx.draw_networkx_edge_labels(Graf_z_ulohy_4,pos,edge_labels=labels)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

kapacita, flow_dict = nx.minimum_cut(Graf_z_ulohy_4,"z","u")
print("Minimalmy rez:",flow_dict)
print('Kapacita minimalneho rezu: ',kapacita)

#vykresli rozdelenie vrcholov
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# color_map = list(Graf_z_ulohy_4)
# edgelist = []
# pom = 0
# for skupina in flow_dict:
#     pom+=1
#     if pom == 1:
#         for vrchol in skupina:
#             index = list(Graf_z_ulohy_4).index(vrchol)
#             color_map[index] = 'blue'
#             #print(index)
#     if pom == 2:
#         for vrchol in skupina:
#             index = list(Graf_z_ulohy_4).index(vrchol)
#             color_map[index] = 'red'
#             #print(index)
# plt.title('Rozdelenie grafu pre minimalny rez')
# pos=nx.planar_layout(Graf_z_ulohy_4)
# labels = nx.get_edge_attributes(Graf_z_ulohy_4,'capacity')
# nx.draw_networkx_edges(Graf_z_ulohy_4,pos,edgelist=edgelist,edge_color= COLOR,width=4)
# nx.draw_networkx_edge_labels(Graf_z_ulohy_4,pos,edge_labels=labels)
# nx.draw_networkx(Graf_z_ulohy_4,pos, node_color = color_map)
# plt.show()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#by kubqo, FLO, LJ