# Models Used

## AdaBoost Classifier

Adaboost is an ensemble classifier that tries to iteratively adjust the weights of incorrectly classified examples and focuses on the more difficult cases.
Its hyperparameters include:
- **Base_estimator** - in this case a Decision Tree Classifier was used
- **n_estimator** - the number of estimators at which boosting stops
- **algorithm** - the boosting algorithm either 'SAMME' or 'SAMME.R'
- **learning_rate** - the rate by which the contribution of each classifier is shrunk

## Multi-Layer Perceptron (MLP) Classifier

MLP Classifier is a neural network classifier. It's hyperparameters include:
- **hidden_layer_sizes** - this determines the depth of the neural network and the number of units in each layer. We sticked to using a depth of 2 in order to avoid overfitting and tuned the number of units in each layer.
- **activation** - the activation function used in the hidden layer. 
- **solver** - the algorithm used for weight optimization. 
