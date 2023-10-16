import numpy as np
import matplotlib.pyplot as plt

from DataParser import DataParser


class Perceptron:
    def __init__(self, learning_rate=0.01, epochs=100, y_set = []):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.random.randn(3)  # 2 for inputs and 1 for bias
        self.accuracy_list = []
        self.y_set = y_set

        self.train_accuracy = 0
        self.test_accuracy = 0

    def fit(self, X_train, y_train):
        # Adding bias input (1) to each training sample
        X_train = np.append(X_train, - np.ones((X_train.shape[0], 1)), axis=1)
        for _ in range(self.epochs):
            for x, y in zip(X_train, y_train):
                v = np.dot(x, self.weights)
                if(y == self.y_set[0] and v < 0):
                    self.weights += self.learning_rate * x
                if(y == self.y_set[1] and v > 0):
                    self.weights -= self.learning_rate * x

            # After each epoch, evaluate the accuracy on training data
            y_preds = self._step(np.dot(X_train, self.weights))
            # print("y_pred", y_preds)
            # print("y_train", y_train)
            accuracy = np.mean(y_preds == y_train)
            self.accuracy_list.append(accuracy)

        self.train_accuracy = max(self.accuracy_list)

    def evaluate_accuracy(self, X_test, y_test):
        # Adding bias input (1) to each test sample
        X_test = np.append(X_test, - np.ones((X_test.shape[0], 1)), axis=1)
        y_preds = self._step(np.dot(X_test, self.weights))
        print(y_preds, y_test)
        accuracy = np.mean(y_preds == y_test)
        self.test_accuracy = accuracy
        return accuracy


    def _step(self, x):
        return np.where(x >= 0, self.y_set[0], self.y_set[1])

    def plot_decision_boundary(self, canvas, all_X, all_Y, x, y, title):
        ax = canvas.axes
        ax.clear()

        ax.scatter(x[:, 0], x[:, 1], c=y, cmap='jet', marker='o')

        # Compute decision boundary
        x_min, x_max = all_X[:, 0].min() - 1, all_X[:, 0].max() + 1
        y_min, y_max = (-(self.weights[0] * x_min - self.weights[2]) / self.weights[1],
                        -(self.weights[0] * x_max - self.weights[2]) / self.weights[1])

        ax.plot([x_min, x_max], [y_min, y_max], 'k-')

        # Set axis limits
        ax.set_xlim(all_X[:, 0].min() - 0.5, all_X[:, 0].max() + 0.5)
        ax.set_ylim(all_X[:, 1].min() - 0.5, all_X[:, 1].max() + 0.5)

        ax.set_title(title)

        canvas.draw()

        # return plt

    def plot_accuracy(self):
        plt.plot(self.accuracy_list)
        plt.xlabel("Epochs")
        plt.ylabel("Training Accuracy")
        plt.title("Training Accuracy vs. Epochs")
        plt.show()



# Example usage:
if __name__ == "__main__":
    parser = DataParser("perceptron1.txt")
    print("X_train:", parser.X_train)
    print("X_test:", parser.X_test)
    print("Y_train:", parser.Y_train)
    print("Y_test:", parser.Y_test)
    print("Y_Set:" , parser.Y_set)

    perceptron = Perceptron(learning_rate=0.1, epochs=100, y_set = parser.Y_set)

    perceptron.fit(parser.X_train, parser.Y_train)

    print(perceptron.weights)
    # Plot decision boundary
    perceptron.plot_decision_boundary(parser.X, parser.Y)

    # Plot test accuracy vs epochs
    perceptron.plot_accuracy()
