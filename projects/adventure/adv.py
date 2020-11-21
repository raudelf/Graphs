from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def opposite_directions(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'e':
        return 'w'
    elif direction == 'w':
        return 'e'


travel_paths = Stack()
visited = set()

# While the visited set is less than the amount of rooms in our current room then keep going
while len(visited) < len(world.rooms):

    # grab all possible exits in the current room
    exits = player.current_room.get_exits()

    print(f'Current Room:\t{player.current_room}\nExits:\t{exits}')
    # List that contains the path we take from the current room
    path = []

    # Loop through all exits
    for x in exits:
        # Save the possible exits if we have not visited it.
        if x is not None and player.current_room.get_room_in_direction(x) not in visited:
            path.append(x)
    # Add room to visited
    visited.add(player.current_room)
    # If the path list contains directions keep moving
    if len(path) > 0:
        direction = random.randint(0, len(path) - 1)
        travel_paths.push(path[direction])
        player.travel(path[direction])
        traversal_path.append(path[direction])
        print('There are rooms still left to visit')
    # Else, go back and try again
    else:
        end = travel_paths.pop()
        player.travel(opposite_directions(end))
        traversal_path.append(opposite_directions(end))

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
