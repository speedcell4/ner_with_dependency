import dgl

def build_karate_club_graph(num_nodes, max_len):
    g = dgl.DGLGraph()
    # add 34 nodes into the graph; nodes are labeled from 0~33
    g.add_nodes(max_len)
    # all 78 edges as a list of tuples
    edge_list = []
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            edge_list.append((i,j))
    # edge_list = [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2),
    #     (4, 0), (5, 0), (6, 0), (6, 4), (6, 5), (7, 0), (7, 1),
    #     (7, 2), (7, 3), (8, 0), (8, 2), (9, 2), (10, 0), (10, 4),
    #     (10, 5), (11, 0), (12, 0), (12, 3), (13, 0), (13, 1), (13, 2),
    #     (13, 3), (16, 5), (16, 6), (17, 0), (17, 1), (19, 0), (19, 1),
    #     (21, 0), (21, 1), (25, 23), (25, 24), (27, 2), (27, 23),
    #     (27, 24), (28, 2), (29, 23), (29, 26), (30, 1), (30, 8),
    #     (31, 0), (31, 24), (31, 25), (31, 28), (32, 2), (32, 8),
    #     (32, 14), (32, 15), (32, 18), (32, 20), (32, 22), (32, 23),
    #     (32, 29), (32, 30), (32, 31), (33, 8), (33, 9), (33, 13),
    #     (33, 14), (33, 15), (33, 18), (33, 19), (33, 20), (33, 22),
    #     (33, 23), (33, 26), (33, 27), (33, 28), (33, 29), (33, 30),
    #     (33, 31), (33, 32)]
    # add edges two lists of nodes: src and dst
    src, dst = tuple(zip(*edge_list))
    g.add_edges(src, dst)
    # edges are directional in DGL; make them bi-directional
    g.add_edges(dst, src)

    return g


max_num_nodes = 5
G1 = build_karate_club_graph(4, max_num_nodes)
G2 = build_karate_club_graph(5, max_num_nodes)
G = dgl.batch([G1, G2])
print('We have %d nodes.' % G.number_of_nodes())
print('We have %d edges.' % G.number_of_edges())


import torch
#
G.ndata['feat'] = torch.randn(max_num_nodes * 2, 10)  ## N x h
# G.nodes[2].data['feat'] = torch.randn(1, 34)
# # print out node 2's input feature
# print(G.nodes[2].data['feat'])
#
# # print out node 10 and 11's input features
# print(G.nodes[[10, 11]].data['feat'])