


import model_x
import model_xi

import numpy as np 


linear_regression_x = model_x.linear_regression_model(dataset = [[1,2],[3,4],[5,6],[7,8],[9,10]])

linear_regression_xi = model_xi.linear_regression_model(dataset = [[1,2],[3,4],[5,6],[7,8],[9,10]])

print(linear_regression_x.batched_dataset)
print(linear_regression_x.test)

linear_regression_xi.execute


#create data

#x = np.array([1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9])
#y = np.array([13, 14, 17, 12, 23, 24, 25, 25, 24, 28, 32, 33])


'''
import matplotlib.pyplot as plt



#create basic scatterplot
plt.plot(x, y, 'o')

#obtain m (slope) and b(intercept) of linear regression line
m, b = np.polyfit(x, y, 1)

#add linear regression line to scatterplot 
plt.plot(x, m*x+b)

plt.show()



'''
