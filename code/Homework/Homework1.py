import numpy as np
import pandas as pd
import time

start = time.time()

df = pd.read_csv("https://bit.ly/2UBhrMG", names=['X','Y'])
print(df.columns)

X = df['X']
Y = df['Y']

# points = [(Point(row[0], row[1])) for index, row in pd.read_csv("https://bit.ly/2UBhrMG").iterrows()]

# Building the model
a = 0.0
b = 0.0
#
epochs = 150000  # The number of iterations to perform
#
n = float(len(df))  # Number of points
#
best_loss = 10000000000000.0  # Initialize with a really large value
#
for i in range(epochs):

    # Randomly adjust "m" or "b"

    a_adjust = np.random.normal()
    b_adjust = np.random.normal()

    a += a_adjust
    b += b_adjust

    # Calculate loss, which is total mean squared error
    new_loss = sum((Y - (a * X**2 + b))**2) / n
    # for p in points:
    #     new_loss += (p.y - (a * p.x * p.x + b)) ** 2

    # If loss has improved, keep new values. Otherwise revert.
    if new_loss < best_loss:
        # print("y = {0}x**2 + {1}".format(a, b))
        best_loss = new_loss
    else:
        a -= a_adjust
        b -= b_adjust

print(f"y = {a}x**2 + {b}")
print(f"Time: {time.time() - start}")
