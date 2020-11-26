import queue 
import sys
import math

pos_inf = math.inf #positive infinity
neg_inf = -1*pos_inf #negative infinity

childindex = 0 #global variable to represent index value for each leaf node
cidx = [] #global list to store indices of pruned leaf node(due to pruning of an internal node or leaf node)

#below class represents a tree node after depth 1 including the leaf nodes 
class TreeNode:
    #init is the constructor for TreeNode
    def __init__(self, state, children, depth, parent):
        self.state = state
        self.depth = depth
        self.parent = parent
        #state split into two child nodes with equal number of values
        self.children = [TreeNode(state[0:len(state)//2],None,self.depth+1,self),TreeNode(state[len(state)//2:],None,self.depth+1,self)] if len(state)//2 >= 1 else None
        
        if self.children is None:
            self.value = state[0]
            global childindex
            self.index = childindex #each leaf node which carries a value is assigned index
            childindex = childindex + 1 
        else:
            if self.depth % 2 == 0: #if node is at max level then its value initialized to negative infinity
                self.value = neg_inf
            else: #if a node is at min leavel then its value is initialized to positive infinity
                self.value = pos_inf

class RootNode: 
    
    def __init__(self, state):
        self.state = state
        self.parent = self   
        self.depth = 0     
        #Root node has 3 children so each child is assigned with 4 values
        self.children = [TreeNode(self.state[0:4],None, 1, self), TreeNode(self.state[4:8],None,1, self), TreeNode(self.state[8:12],None,1, self)]
        if self.depth % 2 == 0: #root node is max node in this case can be changed to min node also
            self.value = neg_inf
        else: 
            self.value = pos_inf

#max_value implementation for alpha beta pruning
def max_value(state, alpha, beta):
    if state.children is not None:
        state.value = neg_inf
        for i in state.children:
            state.value = max(state.value, min_value(i, alpha, beta))
            if state.value >= beta:              
                return int(state.value)
            alpha = max(alpha, state.value)
    else:
        cidx.append(state.index) #store indices of leaf nodes which are not pruned
    return int(state.value)

#min_value implementation for alpha beta pruning
def min_value(state, alpha, beta):
    if state.children is not None:
        state.value = pos_inf
        for i in state.children:
            state.value = min(state.value, max_value(i, alpha, beta))
            if state.value <= alpha:
                return int(state.value)
            beta = min(beta, state.value)
    else:
        cidx.append(state.index) #store indices of leaf nodes which are not pruned
    return int(state.value)

if __name__ == "__main__":
    in_put = input("Enter input of 12 digits separated by space(Sample input 4 6 7 9 1 2 0 1 8 1 9 2)\n")
    in_put_list = in_put.split(" ") #12 input digits separated by space
    input_length = len(in_put_list) #length of input
    if input_length != 12: #if number of digits in input not equal to 12 then invalid input
        print("input doesn't have 12 values. TRY AGAIN")
    tree = RootNode(in_put_list) #create a tree 
    max_value(tree, neg_inf, pos_inf) #this is where the alpha-beta pruning algorithm starts, root node is max_value, can be changed to min_value
    res = [str(ele) for ele in range(len(in_put_list)) if ele not in cidx] #
    print("\""+" ".join(res)+"\"")
