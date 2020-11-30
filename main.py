import networkx as nx

graph=nx.Graph()
columns=None
with open("result.csv", "r") as fic:
    for line in fic.readlines():
        content = line.split(",")
        if not columns:
            columns=content[1:]
        else:
            usr = content[0]
            for i in range(1, len(content)-1):
                if content[i] != "0":
                    graph.add_edge(usr, columns[i], weight=float(content[i]))


graph.remove_nodes_from(nx.isolates(graph))

pr  = nx.algorithms.link_analysis.pagerank_alg.pagerank(graph)
cent= nx.algorithms.centrality.degree_centrality(graph)

print(cent)
