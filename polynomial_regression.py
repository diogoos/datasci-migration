from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

import numpy as np
import matplotlib.pyplot as plt

def fit_polynomial_curve(x,y,degree, xlabel, ylabel, title):
    """
    Inputs:
        x - list - a list of x values for the model to train on
        y - list - a list of y values for the model to train on
        degree - integer - a degree for the polynomial
        xlabel - string - label for the x axis of the graph
        ylabel - string - label for the y axis of the graph
        title - string - title for the graph
    Outputs:
        none
    Purpose:
        plots a graph of a polynomial regression
    """
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline(
        [
            ("polynomial_features", polynomial_features),
            ("linear_regression", linear_regression),
        ]
    )
    numpy_x = x.to_numpy()
    pipeline.fit(numpy_x[:, np.newaxis], y)

    x_test = np.linspace(x.min(), x.max(), 100)
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(x_test, pipeline.predict(x_test[:, np.newaxis]),c='r', label="Model")

    ax.plot(x, y, 'b*', mec='b', mfc='w', ms=10, label='Original Data')
    
    plt.xlabel(xlabel, fontsize = 20)
    plt.ylabel(ylabel, fontsize = 20)
    plt.title(title, fontsize = 20)

    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)

    plt.show()