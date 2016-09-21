"""
URL: https://www.codeeval.com/open_challenges/165/

Date Started: 21-12-2014
Date Finished: 21-12-2014
    
Author: Samarth Bhargav
"""

import sys

def suggest(peeps):
    solutions = []    
    for name, user in peeps.items():
        num_friends = len(user.friend_list)
        gr = {}
        for friend in user.friend_list:
            friend_groups = peeps[friend].groups
            for group in friend_groups:
                if group not in gr:
                    gr[group] = 0
                gr[group] += 1
        sol = []
        for group, num in gr.items():
            if num >= (num_friends/2.0):
                if group not in user.groups:
                    sol.append(group)
        sol.sort()
        solutions.append((name, sol))
        
    return solutions

class User(object):
    def __init__(self, name, friend_list, groups):
        self.name = name
        self.friend_list = friend_list
        self.groups = groups
        
        

if len(sys.argv) == 2:
    with open(sys.argv[1]) as reader:
        peeps = {}
        for line in reader:
            name, friends, groups = line.strip().split(":")
            peeps[name] = User(name, friends.split(","), groups.split(","))
        
        ll = suggest(peeps)
        ll = sorted(ll, key=lambda k: k[0])
        
        for val in ll:
            if len(val[1]) == 0:
                continue
            print "{}:{}".format(val[0], ",".join(val[1]))


if __name__ == "__main__":
    f = """Amira:Isaura,Lizzie,Madalyn,Margarito,Shakira,Un:Driving,Mineral collecting
Elliot:Isaura,Madalyn,Margarito,Shakira:Juggling,Mineral collecting
Isaura:Amira,Elliot,Lizzie,Margarito,Verla,Wilford:Juggling
Lizzie:Amira,Isaura,Verla:Driving,Mineral collecting,Rugby
Madalyn:Amira,Elliot,Margarito,Verla:Driving,Mineral collecting,Rugby
Margarito:Amira,Elliot,Isaura,Madalyn,Un,Verla:Mineral collecting
Shakira:Amira,Elliot,Verla,Wilford:Mineral collecting
Un:Amira,Margarito,Wilford:
Verla:Isaura,Lizzie,Madalyn,Margarito,Shakira:Driving,Juggling,Mineral collecting
Wilford:Isaura,Shakira,Un:Driving"""
    peeps = {}
    for line in f.split("\n"):
        name, friends, groups = line.split(":")
        peeps[name] = User(name, friends.split(","), groups.split(","))
        
    ll = suggest(peeps)
    ll = sorted(ll, key=lambda k: k[0])
    for val in ll:
            if len(val[1]) == 0:
                continue
            print "{}:{}".format(val[0], ",".join(val[1]))