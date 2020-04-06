# This solution doesn't work as we can not fit quadratic equation with linear regression

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Learn more: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

# Import points
points = pd.read_csv("https://bit.ly/2UBhrMG", names=['X','Y'])

# print(points)
x = np.array(points['X'])
y = np.array(points['Y'])

x = x.reshape(-1,1)

print(x.shape)

# Plain ordinary least squares
fit = LinearRegression().fit(x,y)

# Print "m" and "b" coefficients
print("m = {0}".format(fit.coef_.flatten()))
print("b = {0}".format(fit.intercept_.flatten()))
