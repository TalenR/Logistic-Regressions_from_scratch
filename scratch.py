import numpy as np
import matplotlib.pyplot as plt


np.random.seed(12)
num_observations = 5000

x1 = np.random.multivariate_normal([0,0],[[1,0.75],[0.75,1]],num_observations)
x2 = np.random.multivariate_normal([1,4],[[1,0.75],[0.75,1]],num_observations)

simulated_seperableish_features = np.vstack((x1,x2)).astype(np.float32)
simulated_labels = np.hstack((np.zeros(num_observations), np.ones(num_observations)))

plt.figure(figsize=(12,8))
plt.scatter(simulated_seperableish_features[:,0],simulated_seperableish_features[:,1],
            c = simulated_labels, alpha = 0.4)
plt.show()

def sigmoid(scores):
    return 1 / (1 + np.exp(-scores))

def log_likelihood(features, target, weights):
    scores = np.dot(features, weights)
    ll = np.sum( target*scores - np.log(1 + np.exp(scores)))

def logistic_regression(features,target,num_steps,learning_rate,add_intercept = False):
    if add_intercept:
        intercept = np.ones((features.shape[0],1))
        features = np.hstack((intercept, features))

    weights = np.zeros(features.shape[1])

    for step in range(num_steps):
        scores = np.dot(features,weights)
        predictions = sigmoid(scores)

        # Update weights with gradient
        output_error_signal = target - predictions
        gradient = np.dot(features.T, output_error_signal)
        weights += learning_rate * gradient

        # Print log-likelihood error every so often
        if step % 1000 == 0:
            print(log_likelihood(features,target,weights))

    return weights

weights = logistic_regression(simulated_seperableish_features, simulated_labels,
                              num_steps = 30, learning_rate = 5e-5, add_intercept = True)
