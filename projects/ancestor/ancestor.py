from util import Stack, Queue
# def dft(ancestors, starting_node, distance):

#     parents = getNeighbors(node)

#     if len(parents) == 0:
#         return (node, distance)

#     ancient_one = (node, distance)
#     for parent in parents:
#         node_pair = dft(ancestors, parent, distance + 1)

#         if node_pair[1] > distance:
#             ancient_one = node_pair


def getNeighbors(ancestors, curr_node):
    neighbors = []

    for neighbor in ancestors:
        if neighbor[1] == curr_node:
            neighbors.append(neighbor)

        if len(neighbors) > 1:
            return neighbors
        else:
            return neighbors


def earliest_ancestor(ancestors, starting_node, distance=0):
    pass
