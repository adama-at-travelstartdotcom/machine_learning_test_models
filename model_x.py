

import math
import random


class linear_regression_model:

    #dataset must be list with each example in the list as list
    #step must be positive real number
    #epoch must be natural number
    #batch_size must be natural number
    
    def __init__(self, dataset = [], step = 0.1, epoch = 100, batch_size = 0):

        self.dataset = dataset

        self.step = step
        self.epoch = epoch
        self.weight = 0
        self.bias = 0
        self.sum_of_loss = 0
        self.root_mean_error = 0
        self.sum_of_loss_list = []
        self.root_mean_error_list = []
        self.step_list = []
        self.batch_size = batch_size
        self.batched_dataset = []

        if batch_size == 0:
            self.batch_size = len(dataset)


        self.matplotlib_dataset = []



        first_half = 0
        second_half = 0

        for example_index in range(len(self.dataset)):

            if example_index < len(self.dataset)//2:
                first_half += self.dataset[example_index][1]/(len(self.dataset)//2)

            if example_index > len(self.dataset)//2:
                second_half += self.dataset[example_index][1]/(len(self.dataset)//2)

    def test(self):
        print(self.dataset)

    def matplotlib_dataset(self):
        
        matplotlib_dataset_x = []
        matplotlib_dataset_y = []

        for example in self.dataset:
            matplotlib_dataset_x.append(example[0])
            matplotlib_dataset_y.append(example[1])

        matplotlib_dataset1 = [matplotlib_dataset_x, matplotlib_dataset_y]

        return


    def batched_dataset(self):
                
        all_examples_that_will_run = []

        for example_number in range(self.epoch * self.batch_size):
            all_examples_that_will_run.append(self.dataset[example_number % len(self.dataset)])

        for batch_index in range(self.epoch - 1):
            self.batched_dataset.append(all_examples_that_will_run[self.batch_size * batch_index : self.batch_size * (batch_index + 1)])

        
        return self.batched_dataset


    def root_mean_error(self, k = 0):


        for example in self.batched_dataset:
                
            self.sum_of_loss += (example[0] * self.weight + self.bias - example[1])**2
                
        self.root_mean_error = math.sqrt(self.sum_of_loss/len(example))
        self.sum_of_loss_list.append(self.sum_of_loss)
        self.sum_of_loss = 0
        self.root_mean_error_list.append(self.root_mean_error)
        self.root_mean_error = 0

        return


    def model(self):


        self.root_mean_error()

        self.weight += self.step
            
                
        for iter in range(2 * self.epoch):
            
            a = 0

            if a%2 == 0:
            
                if self.root_mean_error_list[-1] < self.root_mean_error_list[-2]:
                    self.weight += self.step

                elif self.root_mean_error_list[-1] > self.root_mean_error_list[-2]:
                    self.weight -= self.step

                elif self.root_mean_error_list[-1] == self.root_mean_error_list[-2]:
                    self.weight -= self.step * random.random()/100
                    

            if a%2 == 1:
            
                if self.root_mean_error_list[-1] < self.root_mean_error_list[-2]:
                    self.bias += self.step

                elif self.root_mean_error_list[-1] > self.root_mean_error_list[-2]:
                    self.bias -= self.step

                elif self.root_mean_error_list[-1] == self.root_mean_error_list[-2]:
                    self.weight -= self.step * random.random()/100


            self.root_mean_error(iter // 2)

        weight_final = self.weight
        bias_final = self.bias

        return















# try using logarithm for step_list




#print(linear_regression_model(dataset = [[1,2],[3,4],[5,6]]).matplotlib_dataset)





