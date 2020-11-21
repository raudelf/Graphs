import random

from util import Stack, Queue
from collections import deque


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def fisher_yates_shuffle(self, l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def get_friends(self, curr_friend):
        return self.friendships[curr_friend]

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for u in range(0, num_users):
            self.add_user(f'User{u + 1}')
        # Create friendships
        # if 1 is a friend of 2, and 2 is a friend of 1, count this as 2 friendships
        total_friendships = avg_friendships * num_users

        # create a list with all possible friendship combinations,
        # friendship_combos = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        friendship_combos = []
        for user_id in range(1, num_users + 1):
            # You can avoid this by only creating friendships where user1 < user2
            for friend_id in range(user_id + 1, num_users + 1):
                friendship_combos.append((user_id, friend_id))
        # shuffle the list,
        self.fisher_yates_shuffle(friendship_combos)
    # then grab the first N elements from the list
        friendships_to_make = friendship_combos[:(total_friendships // 2)]
        for friendship in friendships_to_make:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        while q.size() > 0:

            # get the next person in line
            curr_path = q.dequeue()
            curr_person = curr_path[-1]

            # Check if we visited them yet
            if curr_person not in visited:
                # If not, mark as visited
                # Key: user_id, Value: path
                visited[curr_person] = curr_path
                # Get their friends (visited their edges)
                friends = self.get_friends(curr_person)

                # Enqueue them
                for friend in friends:
                    friend_path = list(curr_path)

                    friend_path.append(friend)

                    q.enqueue(friend_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
