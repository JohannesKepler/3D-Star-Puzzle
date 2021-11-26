# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import itertools

correct = [set(["SatA","SatB"]),set(["JupA","JupB"]),set(["EarA","EarB"]),set(["Sun","Sun"])]
checklist=[(1,7),(5,11),(2,12),(6,16),(10,20),(13,19),(17,23),(14,24),(18,28),(22,32),(25,31),(29,35)]


class Tile():
    def __init__(self, sides):
        self.sides = sides
        
    def sayhi(self):
        print(self.sides,self.pos,self.rot)
        print(self.edge0,self.edge1,self.edge2,self.edge3)
        
    def assign_pos(self,pos,rot):
        self.rot = rot
        
        self.pos = pos
        self.edge0=(0+self.rot)%4+self.pos*4
        self.edge1=(1+self.rot)%4+self.pos*4
        self.edge2=(2+self.rot)%4+self.pos*4
        self.edge3=(3+self.rot)%4+self.pos*4
        
    def add_to_board(self,NewBoard):
        NewBoard.nodes[self.edge0]=self.sides[0]
        NewBoard.nodes[self.edge1]=self.sides[1]
        NewBoard.nodes[self.edge2]=self.sides[2]
        NewBoard.nodes[self.edge3]=self.sides[3]
    
    def rotate(self):
        self.rot += 1%4
        self.assign_pos(self.pos,self.rot)
        
        
    
class Board():
    def __init__(self,nodes):
        self.nodes = nodes
    def sayhi(self):
        print(self.nodes)
    def check_valid(self):
        for pair in checklist:
            if not set([self.nodes[pair[0]],self.nodes[pair[1]]]) in checklist:
                return False
        return True
        

def play_game():
    sides_0=['Sun','EarA','SatA','SatB']
    sides_1=['Sun','SatA','JupA','EarB']
    sides_2=['JupA','EarA','Sun','SatA']
    sides_3=['SatB','Sun','EarA','JupB']
    sides_4=['JupB','SatA','JupA','Sun']
    sides_5=['Sun','EarB','JupA','SatA']
    sides_6=['EarB','Sun','JupA','EarA']
    sides_7=['JupB','SatB','EarB','Sun']
    sides_8=['JupB','EarA','Sun','SatA']
    NewBoard = Board(['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''])
    #NewBoard.sayhi()
    Tile0 = Tile(sides_0)
    Tile1 = Tile(sides_1)
    Tile2 = Tile(sides_2)
    Tile3 = Tile(sides_3)
    Tile4 = Tile(sides_4)
    Tile5 = Tile(sides_5)
    Tile6 = Tile(sides_6)
    Tile7 = Tile(sides_7)
    Tile8 = Tile(sides_8)
    
    tile_list=[Tile0,Tile1,Tile2,Tile3,Tile4,Tile5,Tile6,Tile7,Tile8]
    tile_list_permutations=list(itertools.permutations(tile_list))
    for solution in tile_list_permutations:
        for idx,tile in enumerate(solution):
            tile.assign_pos(idx,0)
            tile.add_to_board(NewBoard)
        if NewBoard.check_valid():
            NewBoard.sayhi()
        
#    Tile0.assign_pos(1,3)
#    Tile0.add_to_board(NewBoard)
    #Tile0.sayhi()
    #NewBoard.sayhi()

#    Tile1.assign_pos(2,2)
#    Tile1.add_to_board(NewBoard)
#    #Tile1.sayhi()
#    NewBoard.sayhi()

play_game()
#
#add tile to board
#node[1] = set(["JupA"])
#add another tile to board
#node[1] = set(["JupA","JupB"])
#
#check if correct
#if node[1] in correct:
#    return True
#

    