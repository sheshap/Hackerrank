############PERCEPTRON and LOGISTIC REGRESSION#############
import numpy as np
import random

class Perecptron(): #Perceptron class

    def __init__(self, data, n):
        self.weights = np.zeros(2) #initialize weights to 0
        self.n = n #is the number of input data samples
        self.iterations = n*100 #maximum number of iterations as recomended 
        self.data = data #input data

    def train(self):
        for iter in range(self.iterations): #update weights for n*100 iterations
            for i in range(self.n): #process n input data samples
                temp = self.data[i].split(",") #splitting input data strings
                x1=int(temp[0]) 
                x2=int(temp[1])
                activation = self.weights[0]*x1+self.weights[1]*x2 #activation = weights*f
                
                if activation >= 0:
                    y = '+1'    #if activation value greater than 0 then +1 class
                else:
                    y = '-1'   # if activation value is negative then -1 class

                if y == temp[2]: #check of predicted y and actual label in temp[2] are same
                    pass # if predicted and actual label both same then no update of weights
                else:
                    if y == '+1':  #case 2 as per notes 8: of mis-classifed negative as positive then subtract 
                        self.weights[0] = self.weights[0] - x1
                        self.weights[1] = self.weights[1] - x2
                    elif y == '-1': #case 1 as per notes 8: of mis-classifed positive as negative then add
                        self.weights[0] = self.weights[0] + x1
                        self.weights[1] = self.weights[1] + x2

        print(str(self.weights[0])+","+str(self.weights[1])) #print weights

class Logistic(): #Logistic Regression class

    def __init__(self, data,n):
        self.alpha = 0.1 #learning rate
        self.weights = np.zeros(2) #initial weights set to 0
        self.n = n #number of input data samples
        self.iterations = n*100 #maximum number of iterations to update the weights
        self.data = data #input data

    def train(self):
        probabilities = np.zeros(self.n) #initially all probabilities are set to 0
        for iter in range(self.iterations):
            for i in range(self.n):
                temp = self.data[i].split(",") #split to remove commas
                x1=int(temp[0]) #x1 value
                x2=int(temp[1]) #x2 value
                activation = self.weights[0]*x1 +self.weights[1]*x2 #summation
                sigmoid = 1/(1+np.exp(-activation)) 
                probabilities[i] = sigmoid #class probabilites 
                
                if temp[2] == '-1': #convert true labes -1 to 0 so that the probabilites be positive
                    actual_y = 0
                else:
                    actual_y = 1
                predicted_y = sigmoid
                self.weights[0] = self.weights[0] + self.alpha * x1 * (actual_y-predicted_y)
                self.weights[1] = self.weights[1] + self.alpha * x2 * (actual_y-predicted_y)
 
        print(np.round(probabilities,3))
            
if __name__ == "__main__":
    print("Please not no space(s) in the input string")
    in_put_list = input("Enter input as P/L followed by, series of (x1,x2,-1) or (x1,x2,+1) terms: ")
    input_length = in_put_list[1:].split(")(") #length of input
    actual_input = []
    n = len(input_length)
    #for loop to remove braces
    for i in range(len(input_length)):
        if i == 0:
            actual_input.append(input_length[i][1:])
        elif i == len(input_length)-1:
            actual_input.append(input_length[i][:-1])
        else:
            actual_input.append(input_length[i])
        # print(actual_input[i])

    
    if in_put_list[0] == 'P':
        P=Perecptron(actual_input,n) #call perceptron
        P.train()
    elif in_put_list[0] == 'L':
        L=Logistic(actual_input,n)
        L.train()
    else:
        print("invalid input")
    
