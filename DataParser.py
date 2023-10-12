import numpy as np

class DataParser:
    def __init__(self, fileName, test_size=0.33):
        self.folderPath = "NN_HW1_DataSet/basic/"
        self.filepath = self.folderPath + fileName
        self.X = np.array([])
        self.Y = np.array([])
        self.X_train = np.array([])
        self.X_test = np.array([])
        self.Y_train = np.array([])
        self.Y_test = np.array([])
        self._parse_data()
        self._split_data(test_size)
        self.Y_set, counts = np.unique(self.Y, return_counts=True)

    def _parse_data(self):
        X_list = []
        Y_list = []
        with open(self.filepath, 'r') as f:
            for line in f.readlines():
                data = line.split()
                x_val = [float(data[0]), float(data[1])]
                y_val = int(data[2])
                X_list.append(x_val)
                Y_list.append(y_val)

        self.X = np.array(X_list)
        self.Y = np.array(Y_list)

    def _split_data(self, test_size):
        data_size = len(self.X)
        test_size = int(data_size * test_size)
        indices = np.arange(data_size)
        np.random.shuffle(indices)

        train_indices = indices[test_size:]
        test_indices = indices[:test_size]

        self.X_train = self.X[train_indices]
        self.Y_train = self.Y[train_indices]
        self.X_test = self.X[test_indices]
        self.Y_test = self.Y[test_indices]



# Example usage:
if __name__ == "__main__":
    parser = DataParser("2Ccircle1.txt")
    print("X_train:", parser.X_train)
    print("X_test:", parser.X_test)
    print("Y_train:", parser.Y_train)
    print("Y_test:", parser.Y_test)
